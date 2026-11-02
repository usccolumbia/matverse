#!/usr/bin/env python3
"""Emit operational JSON and fail on actionable service problems (for systemd)."""
import json
from pathlib import Path
import shutil
import sys
import time
import urllib.request
root = Path('/data/materialsatlas-data')
errors = []
report = {'checked_at': time.time(), 'disk_free_bytes': shutil.disk_usage(root).free}
report['service_bytes'] = sum(p.stat().st_size for p in root.rglob('*') if p.is_file())
for name in ('health', 'metrics'):
    try:
        with urllib.request.urlopen('http://127.0.0.1:8094/api/data/v1/' + name, timeout=30) as response:
            report[name] = json.load(response)
    except Exception as exc:
        errors.append(f'{name}: {exc}')
if report['disk_free_bytes'] < 10_000_000_000:
    errors.append('Less than 10 GB filesystem headroom')
if report['service_bytes'] > 90_000_000_000:
    errors.append('More than 90% of the 100 GB service budget used')
if report.get('metrics', {}).get('stale_workers', 0):
    errors.append('Stale export workers detected')
report['errors'] = errors
report['status'] = 'failed' if errors else 'healthy'
path = root / 'state/monitor.json'
path.with_suffix('.tmp').write_text(json.dumps(report, indent=2))
path.with_suffix('.tmp').replace(path)
print(json.dumps(report))
sys.exit(bool(errors))
