#!/usr/bin/env python3
"""Build the self-contained MatVerse directory from the maintained catalog."""
import argparse
import hashlib
import json
from pathlib import Path
from build_catalog import CATEGORIES, DATE, validate
from collection_inventory import load_inventory

ROOT = Path(__file__).resolve().parents[1]

def render():
    datasets = json.loads((ROOT / 'data/datasets.json').read_text())
    resources = json.loads((ROOT / 'data/resources.json').read_text())
    validate(datasets, resources)
    inventory = load_inventory(ROOT)
    payload = {'datasets': datasets, 'resources': resources, 'categories': CATEGORIES, 'checkedDate': DATE,
               'collections': inventory['collections'], 'sourceEntries': inventory['entries']}
    encoded = json.dumps(payload, ensure_ascii=False, separators=(',', ':')).replace('<', '\\u003c').replace('\u2028', '\\u2028').replace('\u2029', '\\u2029')
    template = (ROOT / 'web/index.template.html').read_text()
    for token, value in {'__DATASET_COUNT__': len(datasets), '__RESOURCE_COUNT__': len(resources), '__ENTRY_COUNT__': len(inventory['entries']), '__COLLECTION_COUNT__': len(inventory['collections']), '__CATEGORY_COUNT__': len(CATEGORIES), '__SOURCE_COUNT__': len({s['url'] for d in datasets for s in d['sources']})}.items():
        template = template.replace(token, str(value))
    assert all(template.count(token) == 1 for token in ['__STYLE__', '__CATALOG__', '__APP__'])
    html = template.replace('__STYLE__', (ROOT / 'web/styles.css').read_text()).replace('__CATALOG__', encoded).replace('__APP__', (ROOT / 'web/app.js').read_text())
    inputs = ['data/datasets.json', 'data/resources.json', 'web/index.template.html', 'web/styles.css', 'web/app.js', 'scripts/collection_inventory.py'] + [c['inventory_file'] for c in inventory['collections']]
    manifest = {'catalog_date': DATE, 'dataset_records': len(datasets), 'resources': len(resources), 'source_entries': len(inventory['entries']), 'source_collections': len(inventory['collections']), 'sha256': {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in inputs}, 'index_sha256': hashlib.sha256(html.encode()).hexdigest(), 'note': 'One standalone HTML file; no network requests are needed to search or export the embedded catalog.'}
    return {'index.html': html, 'data/ui_manifest.json': json.dumps(manifest, indent=2) + '\n', '.nojekyll': ''}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    for name, content in render().items():
        path = ROOT / name
        if args.check:
            if not path.exists() or path.read_bytes() != content.encode():
                raise SystemExit(f'Stale UI output: {name}; run python3 scripts/build_site.py')
        else:
            path.write_text(content, encoding='utf-8')
    print('MatVerse UI is current.' if args.check else 'Built standalone index.html and UI provenance manifest.')

if __name__ == '__main__':
    main()
