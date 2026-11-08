#!/usr/bin/env python3
"""Summarize the Surefire and Failsafe XML left by `mvn -B -ntp clean verify` in each service.

Run after verifying the services, from the report repository:
    python3 scripts/collect-sb1-04-test-results.py --root ..
"""
import argparse
import datetime as dt
import json
from pathlib import Path
import shutil
import subprocess
import xml.etree.ElementTree as ET

SERVICES = {
    'filler-detection-service': 'talki-analysis-services',
    'scoring-service': 'talki-analysis-services',
    'progress-service': 'talki-engagement-services',
}


def suites(folder):
    rows = []
    for path in sorted(folder.glob('TEST-*.xml')):
        suite = ET.parse(path).getroot()
        rows.append({
            'class': suite.get('name'),
            'tests': int(suite.get('tests')),
            'failures': int(suite.get('failures')),
            'errors': int(suite.get('errors')),
            'skipped': int(suite.get('skipped')),
        })
    return rows


def total(rows):
    return {key: sum(row[key] for row in rows) for key in ('tests', 'failures', 'errors', 'skipped')}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', type=Path, required=True)
    parser.add_argument('--output', type=Path, default=Path('assets/evidence/tb2/sb1-04'))
    args = parser.parse_args()
    root = args.root.resolve()
    args.output.mkdir(parents=True, exist_ok=True)

    services = {}
    for service, repo in SERVICES.items():
        git = lambda *a: subprocess.run(['git', '-C', str(root / repo), *a], check=True,
                                        capture_output=True, text=True).stdout.strip()
        target = root / repo / service / 'target'
        unit, integration = suites(target / 'surefire-reports'), suites(target / 'failsafe-reports')
        if not unit or not integration:
            raise SystemExit(f'{service}: run mvn verify first; no test reports in {target}')
        services[service] = {
            'repository': repo,
            'branch': git('branch', '--show-current'),
            'commit': git('rev-parse', 'HEAD'),
            'unit': {'total': total(unit), 'classes': unit},
            'integrationAndBdd': {'total': total(integration), 'classes': integration},
        }

    java = subprocess.run(['java', '-version'], capture_output=True, text=True).stderr.splitlines()[0]
    (args.output / 'test-results.json').write_text(json.dumps({
        'collectedAt': dt.datetime.now(dt.timezone.utc).isoformat(),
        'command': 'mvn -B -ntp clean verify',
        'java': java,
        'scope': 'Unit tests with test doubles; *IT and Cucumber use real RabbitMQ (Testcontainers '
                 'rabbitmq:3.12-management) and disposable H2. No percentage coverage is measured.',
        'services': services,
    }, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

    cucumber = root / 'talki-analysis-services/scoring-service/target/cucumber-report.json'
    scenarios = json.loads(cucumber.read_text(encoding='utf-8'))
    shutil.copy(cucumber, args.output / 'cucumber-report.json')
    for feature in scenarios:
        for scenario in feature['elements']:
            statuses = {step['result']['status'] for step in scenario['steps']}
            print(scenario['name'], statuses)


if __name__ == '__main__':
    main()
