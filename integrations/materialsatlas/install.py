#!/usr/bin/env python3
"""Apply the MatVerse integration to an explicitly selected MaterialsAtlas checkout."""
import argparse
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]


def replace_once(text, old, new):
    if new in text:
        return text
    if text.count(old) != 1:
        raise ValueError(f'Expected one integration anchor: {old[:100]!r}')
    return text.replace(old, new, 1)


def prepare(target):
    frontend = target / 'frontend_v2'
    app_path = frontend / 'src/App.vue'
    catalog_path = target / 'backend_v2/app/catalog.py'
    app = app_path.read_text()
    app = replace_once(app,
        "const AppRunner = defineAsyncComponent(() => import('./components/AppRunner.vue'))",
        "const AppRunner = defineAsyncComponent(() => import('./components/AppRunner.vue'))\nconst MatVerseApp = defineAsyncComponent(() => import('./components/MatVerseApp.vue'))")
    app = replace_once(app, 'const iconBySlug: Record<string, string> = {',
        "const iconBySlug: Record<string, string> = {\n  matverse: asset('matverse.png'),")
    app = replace_once(app,
        '          <AppRunner\n            v-if="selectedApp"',
        '          <MatVerseApp v-if="selectedApp?.slug === \'matverse\'" />\n          <AppRunner\n            v-else-if="selectedApp"')
    catalog = catalog_path.read_text()
    addition = '''APPS = [
    AppDefinition(
        slug="matverse",
        title="MatVerse — Materials Dataset Atlas",
        navbar_title="MatVerse Dataset Search",
        category=TOOLS_CATEGORY,
        description="Search crystal materials datasets, property tables, API access routes and original source collections.",
        fields=[],
        example={},
        result_kind="table",
        implemented=True,
        backend_kind="database",
        backend_note="Interactive dataset discovery runs in the browser; no compute job is required. Dataset-specific access and license terms apply.",
        access_mode="public",
        is_visible=True,
    ),'''
    catalog = replace_once(catalog, 'APPS = [', addition)
    return {app_path: app.encode(), catalog_path: catalog.encode(),
        frontend / 'src/components/MatVerseApp.vue': (HERE / 'MatVerseApp.vue').read_bytes(),
        frontend / 'src/assets/images/matverse.png': (REPO / 'assets/matverse-logo.png').read_bytes(),
        frontend / 'public/matverse/index.html': (REPO / 'index.html').read_bytes()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--target', type=Path, required=True)
    parser.add_argument('--check', action='store_true', help='Check integration anchors without writing')
    args = parser.parse_args()
    target = args.target.resolve()
    manifest = json.loads((REPO / 'data/ui_manifest.json').read_text())
    current_hash = hashlib.sha256((REPO / 'index.html').read_bytes()).hexdigest()
    if current_hash != manifest['index_sha256']:
        raise ValueError('Build the MatVerse site before installing: UI manifest does not match index.html')
    outputs = prepare(target)  # Validate every anchor before any writes.
    receipt = {'target': str(target), 'check_only': args.check, 'outputs': {}}
    for path, data in outputs.items():
        receipt['outputs'][str(path.relative_to(target))] = hashlib.sha256(data).hexdigest()
        if not args.check:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    main()
