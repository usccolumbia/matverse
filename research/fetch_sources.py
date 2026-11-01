"""Fetch small public source documents for research; cache payloads locally only."""
import concurrent.futures
import datetime
import hashlib
import json
from pathlib import Path
import urllib.request

ROOT = Path(__file__).resolve().parent
CACHE = ROOT / 'cache'
CACHE.mkdir(exist_ok=True)

def fetch(item):
    key, url = item
    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'MatVerse-research/0.1 (public dataset documentation)'})
        with urllib.request.urlopen(req, timeout=35) as response:
            data = response.read(4_000_001)
            if len(data) > 4_000_000:
                raise ValueError('Document exceeds 4 MB metadata limit')
            (CACHE / (key + '.txt')).write_bytes(data)
            return {'id':key, 'url':url, 'retrieved_at':now, 'status':response.status, 'bytes':len(data), 'sha256':hashlib.sha256(data).hexdigest()}
    except Exception as exc:
        return {'id':key, 'url':url, 'retrieved_at':now, 'error':str(exc)}

if __name__ == '__main__':
    import sys
    inputs = json.loads(Path(sys.argv[1]).read_text())
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(fetch, inputs.items()))
    target = ROOT / 'source_fetch_manifest.json'
    previous = json.loads(target.read_text()) if target.exists() else []
    combined = {r['id']:r for r in previous}
    combined.update({r['id']:r for r in results})
    target.write_text(json.dumps(list(combined.values()), indent=2) + '\n')
    for r in results:
        print(r['id'], r.get('status', r.get('error')), r.get('bytes',''))
