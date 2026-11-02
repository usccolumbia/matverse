#!/usr/bin/env python3
"""Retain versioned data and code; regenerate cache instead of backing it up."""
import datetime
import json
from pathlib import Path
import sqlite3
import subprocess
import time
root = Path('/data/materialsatlas-data')
disk = Path('/run/media/jianjunh/MaterialsAtlas1')
if not disk.is_mount():
    raise RuntimeError('Separate backup disk is not mounted')
revision = (root / 'current').read_text().strip()
release = root / 'releases' / revision
if not (release / 'OPTIMADE_READY.json').exists():
    raise RuntimeError('Wait for normalized release before taking the complete backup')
dest = disk / 'materialsatlas-data-api-backup'
dest.mkdir(exist_ok=True)
subprocess.run(['rsync','-a',str(release),str(dest / 'releases') + '/'],check=True)
subprocess.run(['rsync','-a','--exclude=__pycache__','/home/jianjunh/materialsatlas-data-api/',str(dest / 'service') + '/'],check=True)
state = dest / 'state'
state.mkdir(exist_ok=True)
stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ')
with sqlite3.connect(root / 'state/jobs.sqlite3') as source, sqlite3.connect(state / f'jobs-{stamp}.sqlite3') as target:
    source.backup(target)
(dest / 'current').write_text(revision + '\n')
receipt = {'revision': revision, 'completed_at': time.time(), 'destination': str(dest),
           'cache_policy': 'exports/tmp omitted; resubmit expired jobs after recovery'}
(dest / 'latest-backup.json').write_text(json.dumps(receipt,indent=2))
(root / 'state/latest-backup.json').write_text(json.dumps(receipt,indent=2))
print(json.dumps(receipt))
