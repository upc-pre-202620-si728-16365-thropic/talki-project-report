#!/usr/bin/env python3
"""Run the analysis, scoring and progress journey on real services and record what happens.

Scope: live-coach, filler-detection, scoring, progress and gamification with one RabbitMQ
and disposable H2 databases. The closing event is sent as POST /v1/coach/{id}/finalize with a
written transcript: no microphone, no Gemini call and no session-service state transition.

Prerequisites (Linux or WSL): JDK 17, Maven, Docker. Run it from the report repository:
    python3 scripts/capture-sb1-04-evidence.py --root .. --hold 0
Only the container and child processes created by this command are stopped.
"""
import argparse
import datetime as dt
import glob
import json
import os
from pathlib import Path
import secrets
import shutil
import socket
import subprocess
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request

SERVICES = {
    'live-coach-service': ('talki-session-services', 18083),
    'filler-detection-service': ('talki-analysis-services', 18087),
    'scoring-service': ('talki-analysis-services', 18088),
    'progress-service': ('talki-engagement-services', 18089),
    'gamification-service': ('talki-engagement-services', 18090),
}
BROKER_PORT = 25673
TRANSCRIPT = ('Este es mi proyecto, eh, sobre comunicación oral y o sea practico cada semana '
              'con mi equipo de la universidad para mejorar mi exposición final')


def git(repo, *args):
    return subprocess.run(['git', '-C', str(repo), *args], check=True,
                          capture_output=True, text=True).stdout.strip()


class Journey:
    def __init__(self):
        self.calls = []

    def call(self, service, method, path, label=None, query=None):
        url = f'http://127.0.0.1:{SERVICES[service][1]}{path}'
        if query:
            url += '?' + urllib.parse.urlencode(query)
        request = urllib.request.Request(url, method=method)
        try:
            with urllib.request.urlopen(request, timeout=15) as response:
                status, body = response.status, response.read()
        except urllib.error.HTTPError as error:
            status, body = error.code, error.read()
        try:
            document = json.loads(body)
        except ValueError:
            document = body.decode(errors='replace')[:500]
        if label:
            shown = dict(query or {})
            if 'transcriptGemini' in shown:
                shown['transcriptGemini'] = f"[{len(shown['transcriptGemini'].split())} palabras]"
            self.calls.append({'step': label, 'service': service, 'method': method, 'path': path,
                               'query': shown, 'httpStatus': status, 'response': document})
            print(f'{status} {label}', flush=True)
        return status, document

    def poll(self, service, path, query, wanted, label, attempts=60):
        seen = []
        for _ in range(attempts):
            status, document = self.call(service, 'GET', path, query=query)
            if not seen or seen[-1] != status:
                seen.append(status)
            if status == wanted:
                break
            time.sleep(0.25)
        final_status, document = self.call(service, 'GET', path, label=label, query=query)
        self.calls[-1]['statusesObservedWhilePolling'] = seen
        return final_status, document


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', type=Path, required=True, help='folder holding the talki-* repositories')
    parser.add_argument('--output', type=Path, default=Path('assets/evidence/tb2/sb1-04'))
    parser.add_argument('--hold', type=int, default=0, help='seconds to keep services up for Swagger captures')
    args = parser.parse_args()
    root = args.root.resolve()
    args.output.mkdir(parents=True, exist_ok=True)

    sources = {}
    for repo in sorted({repo for repo, _ in SERVICES.values()}):
        sources[repo] = {'branch': git(root / repo, 'branch', '--show-current'),
                         'commit': git(root / repo, 'rev-parse', 'HEAD'),
                         'cleanWorkingTree': git(root / repo, '-c', 'core.autocrlf=true', 'status', '--porcelain') == ''}

    for service, (repo, _) in SERVICES.items():
        print('Building', service, flush=True)
        subprocess.run(['mvn', '-B', '-ntp', '-q', 'clean', 'package', '-DskipTests'],
                       cwd=root / repo / service, check=True)

    workdir = Path(tempfile.mkdtemp(prefix='talki-sb1-04-'))
    jars = {}
    for service, (repo, _) in SERVICES.items():
        built = [j for j in glob.glob(str(root / repo / service / 'target' / '*.jar'))]
        jars[service] = shutil.copy(built[0], workdir)

    container = 'talki-sb1-04-' + secrets.token_hex(4)
    password = secrets.token_hex(16)
    processes, logs = [], {}
    journey = Journey()
    try:
        subprocess.run(['docker', 'run', '-d', '--rm', '--name', container,
                        '-e', 'RABBITMQ_DEFAULT_USER=sb1fixture', '-e', 'RABBITMQ_DEFAULT_PASS=' + password,
                        '-p', f'127.0.0.1:{BROKER_PORT}:5672', 'rabbitmq:3.12-management'],
                       check=True, stdout=subprocess.DEVNULL)
        # Solo se leen los logs: un rabbitmq-diagnostics durante el arranque hace caer al broker.
        for _ in range(60):
            startup = subprocess.run(['docker', 'logs', container], capture_output=True, text=True)
            if 'Server startup complete' in startup.stdout + startup.stderr:
                break
            time.sleep(2)
        else:
            raise RuntimeError('RabbitMQ did not become ready: ' + (startup.stdout + startup.stderr)[-600:])

        environment = dict(os.environ, RABBITMQ_HOST='127.0.0.1', RABBITMQ_PORT=str(BROKER_PORT),
                           RABBITMQ_USERNAME='sb1fixture', RABBITMQ_PASSWORD=password,
                           RABBITMQ_VHOST='/', GEMINI_API_KEY='')
        for service, (_, port) in SERVICES.items():
            logs[service] = workdir / f'{service}.log'
            processes.append(subprocess.Popen(
                ['java', '-jar', jars[service]],
                env=dict(environment, PORT=str(port), SERVER_PORT=str(port)),
                stdout=open(logs[service], 'w'), stderr=subprocess.STDOUT))
        for service, (_, port) in SERVICES.items():
            for _ in range(120):
                try:
                    with urllib.request.urlopen(f'http://127.0.0.1:{port}/actuator/health', timeout=2) as r:
                        if r.status == 200:
                            break
                except OSError:
                    pass
                time.sleep(1)
            else:
                raise RuntimeError(f'{service} did not become healthy')
            print('Healthy', service, flush=True)

        run = secrets.token_hex(3)
        owner, intruder = f'sb1-owner-{run}', f'sb1-intruder-{run}'
        session, empty = f'sb1-session-{run}', f'sb1-empty-{run}'
        report = f'/v1/reports/{session}'
        closing = {'userId': owner, 'mode': 'quick_practice', 'transcriptGemini': TRANSCRIPT,
                   'wordsPerMinute': 130, 'silenceRatio': 0.08, 'volumeRmsAvg': 0.6, 'durationSeconds': 300}
        dashboard = '/v1/progress/dashboard'

        _, before = journey.call('progress-service', 'GET', dashboard, 'Progreso antes de practicar', {'userId': owner})
        journey.call('scoring-service', 'GET', report, 'Reporte antes del cierre', {'userId': owner})
        journey.call('live-coach-service', 'POST', f'/v1/coach/{session}/finalize', 'Cierre de la práctica', closing)
        status_report, first = journey.poll('scoring-service', report, {'userId': owner}, 200, 'Reporte del propietario')
        time.sleep(1)
        _, after = journey.call('progress-service', 'GET', dashboard, 'Progreso después de la evaluación', {'userId': owner})

        journey.call('live-coach-service', 'POST', f'/v1/coach/{session}/finalize', 'Cierre repetido de la misma práctica', closing)
        time.sleep(6)
        _, second = journey.call('scoring-service', 'GET', report, 'Reporte tras el cierre repetido', {'userId': owner})
        _, repeated = journey.call('progress-service', 'GET', dashboard, 'Progreso tras el cierre repetido', {'userId': owner})

        status_other, _ = journey.call('scoring-service', 'GET', report, 'Reporte consultado por otro usuario', {'userId': intruder})
        status_missing, _ = journey.call('scoring-service', 'GET', report, 'Reporte sin userId')

        journey.call('live-coach-service', 'POST', f'/v1/coach/{empty}/finalize', 'Cierre de una práctica sin palabras',
                     {'userId': owner, 'mode': 'quick_practice', 'durationSeconds': 30})
        status_empty, insufficient = journey.poll('scoring-service', f'/v1/reports/{empty}', {'userId': owner}, 200,
                                                  'Reporte de la práctica sin palabras')
        time.sleep(1)
        _, final = journey.call('progress-service', 'GET', dashboard, 'Progreso tras la práctica sin palabras', {'userId': owner})

        status_gamification, _ = journey.call('gamification-service', 'GET', f'/v1/gamification/streaks/{owner}',
                                              'Racha del usuario, observación para SB1-05-B')

        queues = subprocess.run(['docker', 'exec', container, 'rabbitmqctl', '-q', 'list_queues', 'name', 'messages'],
                                capture_output=True, text=True, check=True).stdout
        depth = {}
        for line in queues.splitlines():
            parts = line.split()
            if len(parts) == 2 and parts[1].isdigit():
                depth[parts[0]] = int(parts[1])

        rejected = {service: logs[service].read_text(errors='replace').count('UnrecognizedPropertyException')
                    for service in SERVICES}

        checks = {
            'reportAvailableToOwner': status_report == 200 and first.get('analysisState') == 'COMPLETED',
            'sameSessionThroughThePipeline': first.get('sessionId') == session,
            'fillersDetected': first.get('evidence', {}).get('totalFillers', 0) > 0,
            'progressUpdatedOnce': before.get('totalSessions') == 0 and after.get('totalSessions') == 1,
            'minutesFromEventDuration': after.get('totalMinutes') == 5,
            'repeatedClosingKeepsReport': second.get('computedAt') == first.get('computedAt'),
            'repeatedClosingKeepsProgress': repeated == after,
            'otherUserGets404': status_other == 404,
            'missingUserIdGets400': status_missing == 400,
            'emptyPracticeHasNoScore': status_empty == 200
                and insufficient.get('analysisState') == 'INSUFFICIENT_EVIDENCE'
                and 'overallScore' not in insufficient,
            'emptyPracticeDoesNotChangeProgress': final == repeated,
            'deadLetterQueuesEmpty': all(v == 0 for k, v in depth.items() if k.endswith('.dlq')),
        }

        for service in ('filler-detection-service', 'scoring-service', 'progress-service'):
            with urllib.request.urlopen(f'http://127.0.0.1:{SERVICES[service][1]}/v3/api-docs', timeout=15) as r:
                (args.output / f'openapi-{service}.json').write_text(
                    json.dumps(json.loads(r.read()), indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

        result = {
            'checkedAt': dt.datetime.now(dt.timezone.utc).isoformat(),
            'scope': 'Real services, one RabbitMQ, disposable H2 and fixture data. The closing event uses a '
                     'written transcript: no microphone, Gemini call, session-service transition or public deployment.',
            'sources': sources,
            'allChecksPassed': all(checks.values()),
            'checks': checks,
            'observations': {
                'unrecognizedPropertyErrorsByServiceLog': rejected,
                'gamificationStreakHttpStatus': status_gamification,
                'queueDepthAtEnd': depth,
            },
            'calls': journey.calls,
        }
        (args.output / 'e2e-execution.json').write_text(
            json.dumps(result, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
        print(json.dumps({'allChecksPassed': result['allChecksPassed'], 'checks': checks,
                          'observations': result['observations']}, indent=2), flush=True)
        if args.hold:
            print(f'Holding services for {args.hold}s', flush=True)
            time.sleep(args.hold)
    finally:
        for process in processes:
            process.terminate()
        for process in processes:
            try:
                process.wait(timeout=20)
            except subprocess.TimeoutExpired:
                process.kill()
        subprocess.run(['docker', 'rm', '-f', container], capture_output=True)
        shutil.rmtree(workdir, ignore_errors=True)


if __name__ == '__main__':
    main()
