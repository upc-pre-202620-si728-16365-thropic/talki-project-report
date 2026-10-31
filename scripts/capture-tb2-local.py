#!/usr/bin/env python3
"""Capture a bounded local smoke test of the archived baseline, without paid AI calls.

Prerequisites: package all eight services with JDK 17 and Maven; Docker running;
docker pull rabbitmq:3.12-management. Sources must match verification.json.
Only the container and child processes created by this command are stopped.
"""
import argparse
import concurrent.futures
import datetime as dt
import json
import os
from pathlib import Path
import secrets
import socket
import subprocess
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request

from importlib.machinery import SourceFileLoader

ROOT = Path(__file__).resolve().parents[1]
SERVICES = SourceFileLoader('evidence', str(ROOT / 'scripts/verify-tb2-evidence.py')).load_module().SERVICES

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--sources', type=Path, required=True)
    parser.add_argument('--java-home', type=Path, required=True)
    args = parser.parse_args()
    output = ROOT / 'assets/evidence/tb2'
    output.mkdir(parents=True, exist_ok=True)
    processes, logs, results = [], [], []
    ports = dict(zip(SERVICES, [18081, 18091, 18082, 18083, 18087, 18088, 18089, 18090]))
    container = 'talki-tb2-evidence-' + secrets.token_hex(4)
    broker_password = secrets.token_urlsafe(24)

    def call(service, method, path, payload=None, label=None):
        url = f'http://127.0.0.1:{ports[service]}' + path
        data = None if payload is None else json.dumps(payload).encode()
        req = urllib.request.Request(url, data=data, method=method,
                                     headers={'Content-Type': 'application/json'})
        try:
            with urllib.request.urlopen(req, timeout=15) as response:
                status, body = response.status, response.read()
        except urllib.error.HTTPError as error:
            status, body = error.code, error.read()
        try:
            document = json.loads(body)
        except ValueError:
            document = body.decode(errors='replace')[:500]
        if label:
            # Do not persist passwords or JWTs, even from a disposable local run.
            safe = dict(document) if isinstance(document, dict) else document
            if isinstance(safe, dict) and 'token' in safe:
                safe['token'] = '[redacted ephemeral local JWT]'
            results.append({'label': label, 'service': service, 'method': method,
                            'path': path, 'httpStatus': status, 'response': safe})
            print(label, status, flush=True)
        return status, document

    try:
        subprocess.run(['docker', 'run', '-d', '--rm', '--name', container,
                        '-e', 'RABBITMQ_SERVER_ADDITIONAL_ERL_ARGS=+S 2:2',
                        '-e', 'RABBITMQ_DEFAULT_USER=tb2fixture',
                        '-e', 'RABBITMQ_DEFAULT_PASS=' + broker_password,
                        '-p', '127.0.0.1:25672:5672', 'rabbitmq:3.12-management'],
                       check=True, stdout=subprocess.DEVNULL)
        for _ in range(40):
            try:
                with socket.create_connection(('127.0.0.1', 25672), timeout=2):
                    break
            except OSError:
                pass
            time.sleep(2)
        else:
            raise RuntimeError('The isolated local RabbitMQ did not become ready')
        for service, (repo, _) in SERVICES.items():
            jars = [p for p in (args.sources / repo / service / 'target').glob('*.jar')
                    if not p.name.endswith('.original')]
            if len(jars) != 1:
                raise RuntimeError(f'Expected one packaged JAR for {service}')
            env = os.environ.copy()
            env.update(PORT=str(ports[service]), SERVER_ADDRESS='127.0.0.1',
                       RABBITMQ_HOST='127.0.0.1', RABBITMQ_PORT='25672',
                       RABBITMQ_USERNAME='tb2fixture', RABBITMQ_PASSWORD=broker_password,
                       GEMINI_API_KEY='', JWT_SECRET=secrets.token_urlsafe(48))
            log = tempfile.TemporaryFile()
            logs.append(log)
            processes.append(subprocess.Popen([str(args.java_home / 'bin/java'), '-Xmx192m',
                                               '-jar', str(jars[0])], env=env,
                                              stdout=log, stderr=subprocess.STDOUT))
        def docs(service):
            for _ in range(45):
                try:
                    status, spec = call(service, 'GET', '/v3/api-docs')
                    if status == 200 and spec.get('openapi'):
                        folder = output / 'openapi-local'; folder.mkdir(exist_ok=True)
                        (folder / (service + '.json')).write_text(json.dumps(spec, ensure_ascii=False, indent=2)+'\n')
                        return {'service': service, 'httpStatus': status,
                                'paths': len(spec.get('paths', {})),
                                'file': str((folder / (service + '.json')).relative_to(ROOT))}
                except (OSError, ValueError):
                    pass
                time.sleep(2)
            raise RuntimeError(f'No local OpenAPI document from {service}')
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
            documents = list(pool.map(docs, SERVICES))
        email = 'tb2-local-fixture@example.invalid'
        password = secrets.token_urlsafe(24)
        status, user = call('identity-service', 'POST', '/v1/auth/register',
                            {'email': email, 'password': password, 'username': 'TB2 local fixture',
                             'academicSegment': 'ciclos_1_5'}, 'register fixture')
        registered = status == 201
        flow_completed = False
        if registered:
            status, _ = call('identity-service', 'POST', '/v1/auth/login',
                             {'email': email, 'password': password}, 'login fixture')
            if status == 200:
                status, session = call('session-service', 'POST', '/v1/sessions',
                                       {'title': 'TB2 local fixture', 'sessionType': 'quick_practice',
                                        'userId': user['userId']}, 'create fixture session')
                if status == 201:
                    sid = session['id']
                    call('session-service', 'GET', f'/v1/sessions/{sid}', label='read fixture session')
                    call('session-service', 'GET', '/v1/sessions?userId='+str(user['userId']), label='list fixture sessions')
                    status, _ = call('session-service', 'POST', f'/v1/sessions/{sid}/finalize', label='finalize fixture session')
                    flow_completed = status == 202
            for service, path in [('progress-service', '/v1/progress/dashboard?userId='+str(user['userId'])),
                                  ('gamification-service', '/v1/gamification/streaks/'+str(user['userId']))]:
                call(service, 'GET', path, label='read '+service)
        call('live-coach-service', 'GET', '/v1/coach/modes', label='available modes')
        call('live-coach-service', 'POST', '/v1/coach/live-token?mode=quick_practice', label='AI unavailable without configured key')
        result = {'checkedAt': dt.datetime.now(dt.timezone.utc).isoformat(),
                  'scope': 'Local integration smoke with disposable fixture data and H2. No microphone, paid Gemini call, production deployment, or participant validation.',
                  'flowCompleted': flow_completed,
                  'openapiDocuments': documents, 'checks': results}
        (output / 'local-execution.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    finally:
        for process in processes:
            process.terminate()
        for process in processes:
            try:
                process.wait(timeout=10)
            except subprocess.TimeoutExpired:
                process.kill(); process.wait()
        for log in logs:
            log.close()
        subprocess.run(['docker', 'rm', '-f', container], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

if __name__ == '__main__':
    main()
