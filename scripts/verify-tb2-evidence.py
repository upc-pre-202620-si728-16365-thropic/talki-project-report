#!/usr/bin/env python3
"""Read-only verification of the public Talki baseline reused for TB2."""
import argparse
import concurrent.futures
import datetime as dt
import json
from pathlib import Path
import subprocess
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET

SERVICES = {
    'identity-service': ('talki-user-services', 'https://talki-user-services-production.up.railway.app'),
    'notification-service': ('talki-user-services', 'https://notification-service-production-a277.up.railway.app'),
    'session-service': ('talki-session-services', 'https://session-service-production-c267.up.railway.app'),
    'live-coach-service': ('talki-session-services', 'https://live-coach-service-production.up.railway.app'),
    'filler-detection-service': ('talki-analysis-services', 'https://filler-detection-service-production.up.railway.app'),
    'scoring-service': ('talki-analysis-services', 'https://scoring-service-production-9702.up.railway.app'),
    'progress-service': ('talki-engagement-services', 'https://progress-service-production-cd14.up.railway.app'),
    'gamification-service': ('talki-engagement-services', 'https://gamification-service-production-3c2c.up.railway.app'),
}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--sources', type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    output = root / 'assets/evidence/tb2'
    output.mkdir(parents=True, exist_ok=True)
    repos = {}
    for repo in sorted({r for r, _ in SERVICES.values()} | {'talki-frontend'}):
        folder = args.sources / repo
        sha = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=folder, text=True).strip()
        committed = subprocess.check_output(['git', 'show', '-s', '--format=%cI', 'HEAD'], cwd=folder, text=True).strip()
        repos[repo] = {'sha': sha, 'committedAt': committed,
                       'url': 'https://github.com/upc-pre-202601-si657-7940-thropic/' + repo}
    cases = []
    for service, (_, origin) in SERVICES.items():
        cases.extend([(service, 'health', origin + '/actuator/health'),
                      (service, 'openapi', origin + '/v3/api-docs')])
    cases.extend([
        ('frontend', 'page', 'https://talki-frontend.vercel.app'),
        ('prototype', 'page', 'https://upc-pre-202620-si728-16365-thropic.github.io/talki-project-report/assets/ux/prototype/'),
        ('gallery', 'page', 'https://upc-pre-202620-si728-16365-thropic.github.io/talki-project-report/'),
    ])

    def probe(case):
        name, kind, url = case
        record = {'name': name, 'kind': kind, 'url': url}
        try:
            request = urllib.request.Request(url, headers={'User-Agent': 'Talki-TB2-Evidence-ReadOnly/1.0'})
            with urllib.request.urlopen(request, timeout=20) as response:
                body = response.read(2_000_001)
                record.update(httpStatus=response.status, finalUrl=response.url,
                              contentType=response.headers.get('Content-Type', ''))
                if kind in ('health', 'openapi') and len(body) <= 2_000_000:
                    try:
                        document = json.loads(body)
                        if kind == 'health':
                            record['healthStatus'] = document.get('status')
                        elif document.get('openapi'):
                            path = output / 'openapi' / (name + '.json')
                            path.parent.mkdir(exist_ok=True)
                            path.write_text(json.dumps(document, ensure_ascii=False, indent=2) + '\n')
                            record.update(openapiVersion=document['openapi'],
                                          paths=len(document.get('paths', {})),
                                          evidenceFile=str(path.relative_to(root)))
                    except (ValueError, AttributeError):
                        record['jsonStatus'] = 'not_json'
                if len(body) > 2_000_000:
                    record['bodyTruncated'] = True
        except urllib.error.HTTPError as error:
            record['httpStatus'] = error.code
        except (urllib.error.URLError, TimeoutError, OSError) as error:
            record['error'] = str(getattr(error, 'reason', error))[:200]
        return record

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
        probes = list(pool.map(probe, cases))
    tests = []
    for service, (repo, _) in SERVICES.items():
        reports = sorted((args.sources / repo / service / 'target/surefire-reports').glob('TEST-*.xml'))
        record = {'service': service, 'repository': repo, 'tests': 0, 'failures': 0,
                  'errors': 0, 'skipped': 0, 'suites': [], 'reportFound': bool(reports)}
        for report in reports:
            suite = ET.parse(report).getroot()
            for field in ('tests', 'failures', 'errors', 'skipped'):
                record[field] += int(suite.get(field, '0'))
            record['suites'].append({'name': suite.get('name'),
                                    'tests': int(suite.get('tests', '0')),
                                    'javaVersion': next((p.get('value') for p in suite.findall('properties/property')
                                                         if p.get('name') == 'java.version'), None)})
        tests.append(record)
    result = {
        'checkedAt': dt.datetime.now(dt.timezone.utc).isoformat(),
        'scope': 'Read-only checks of reused 202601 sources; not proof of new implementation or user validation in 202620.',
        'repositories': repos, 'publicProbes': probes, 'unitTests': tests,
        'acceptanceFeatureFilesFound': [str(p.relative_to(args.sources)) for p in args.sources.rglob('*.feature')],
    }
    (output / 'verification.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    for r in probes:
        print(r['name'], r['kind'], r.get('httpStatus', r.get('error')), r.get('healthStatus', ''))
    print('Unit tests:', sum(t['tests'] for t in tests), 'errors:', sum(t['errors'] + t['failures'] for t in tests))

if __name__ == '__main__':
    main()
