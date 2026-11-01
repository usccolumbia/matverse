#!/usr/bin/env python3
"""Validate MatVerse JSON and deterministically render Markdown and CSV (stdlib)."""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse, parse_qsl

ROOT = Path(__file__).resolve().parents[1]
DATE = '2026-11-01'
CATEGORIES = {
    'aggregated_crystals': 'Aggregated and deduplicated crystal collections',
    'bulk_computed': 'Computed bulk inorganic crystals',
    'experimental_crystallography': 'Experimental crystallography and reference collections',
    'mlip_configurations': 'Bulk and mixed-domain MLIP configurations',
    'two_dimensional': 'Two-dimensional and layered materials',
    'porous_frameworks': 'MOFs, COFs and zeolites',
    'molecular_crystals': 'Molecular crystals and ice',
    'surfaces_catalysis': 'Surfaces, interfaces and catalysis',
    'property_benchmarks': 'Computed properties and prediction benchmarks',
    'generation_benchmarks': 'Crystal generation and discovery benchmarks',
    'experimental_properties': 'Experimental properties and literature extraction',
    'diffraction_spectroscopy': 'Diffraction, spectroscopy and characterization',
}
FIELDS = ['id', 'name', 'category', 'description', 'version', 'year', 'count',
          'count_display', 'count_unit', 'count_scope', 'count_precision',
          'structure_level', 'provenance', 'properties', 'access', 'license',
          'links', 'sources', 'caveats', 'tags']


def order(d):
    return (d['count'] is None, -(d['count'] or 0), d['name'].casefold(), d['id'])


def url_ok(s):
    p = urlparse(s)
    sensitive = any(k.lower().startswith('x-amz-') or k.lower() in {'access_token', 'token', 'api_key', 'apikey', 'password', 'authorization', 'signature'} for k, v in parse_qsl(p.query))
    return p.scheme in {'https', 'http'} and bool(p.netloc) and not p.username and not p.password and not sensitive


def validate(data, resources):
    ids = set()
    for d in data:
        missing = set(FIELDS) - d.keys()
        assert not missing, f"{d.get('id')}: missing {missing}"
        assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', d['id']), d['id']
        assert d['id'] not in ids, f"Duplicate id: {d['id']}"
        ids.add(d['id'])
        assert d['category'] in CATEGORIES, f"Unknown category {d['category']}"
        assert d['count'] is None or (type(d['count']) is int and d['count'] > 0), d['id']
        assert d['count_precision'] in {'exact', 'approximate', 'lower_bound', 'unknown'}, d['id']
        assert (d['count'] is None) == (d['count_precision'] == 'unknown'), d['id']
        assert d['year'] is None or type(d['year']) is int, d['id']
        assert d['structure_level'] in {'periodic_atomic', 'structure_linked', 'composition_only', 'mixed'}, d['id']
        assert d['access'] in {'open', 'registration', 'restricted', 'commercial', 'mixed'}, d['id']
        for f in ['name', 'description', 'version', 'count_unit', 'count_scope', 'license']:
            assert isinstance(d[f], str) and d[f].strip(), (d['id'], f)
        for f in ['properties', 'caveats', 'tags']:
            assert isinstance(d[f], list) and all(isinstance(v, str) for v in d[f]), (d['id'], f)
        assert d['links'] and all(url_ok(v) for v in d['links'].values()), d['id']
        assert d['sources'], f"No evidence for {d['id']}"
        for s in d['sources']:
            assert url_ok(s['url']) and s['title'] and s['evidence'], (d['id'], s)
            assert re.fullmatch(r'\d{4}-\d{2}-\d{2}', s['verified_date']), (d['id'], s)
        if 'count_derivation' in d:
            assert sum(d['count_derivation']['values']) == d['count'], d['id']
    for r in resources:
        assert all(r.get(k) for k in ['name', 'url', 'kind', 'description', 'sources']), r
        assert url_ok(r['url']), r
        assert all(url_ok(s['url']) and s['title'] and s['evidence'] for s in r['sources']), r['name']
    return ids


def cell(value):
    return str(value).replace('|', '\\|').replace('\n', ' ')


def size(d):
    if d['count'] is None:
        return 'Unranked'
    prefix = {'exact': '', 'approximate': '~', 'lower_bound': '≥'}[d['count_precision']]
    return prefix + f"{d['count']:,}"


def table(rows, prefix=''):
    lines = ['| Dataset / release | Reported size | Counted unit | Access | Data license |',
             '|---|---:|---|---|---|']
    for d in sorted(rows, key=order):
        card = f"{prefix}docs/catalog/{d['category']}.md#{d['id']}"
        name = f"[{cell(d['name'])}]({card})"
        lines.append('| ' + ' | '.join([name, size(d), cell(d['count_unit']), cell(d['access']), cell(d['license'])]) + ' |')
    return '\n'.join(lines)


def render(data, resources):
    counts = Counter(d['category'] for d in data)
    unknown = sum(d['count'] is None for d in data)
    source_count = len({s['url'] for d in data for s in d['sources']})
    header = (ROOT / 'templates/README_intro.md.txt').read_text().replace('{{DATASETS}}', str(len(data))).replace('{{CATEGORIES}}', str(len(counts))).replace('{{SOURCES}}', str(source_count)).replace('{{UNRANKED}}', str(unknown))
    lines = [header.rstrip(), '', '## Browse by category', '']
    for cat, title in CATEGORIES.items():
        if counts[cat]:
            lines.append(f"- [{title}](#{cat.replace('_', '-')}) ({counts[cat]})")
    lines += ['', '## Ranked catalog', '', 'Sizes descend **within each category**. Approximate figures use `~`, source lower bounds use `≥`, and unverified sizes appear last. Units remain explicit: these are volume rankings, not quality rankings. Click a dataset for its release, official download links, evidence and caveats.', '']
    for cat, title in CATEGORIES.items():
        rows = [d for d in data if d['category'] == cat]
        if not rows:
            continue
        lines += [f'<a id="{cat.replace("_", "-")}"></a>', f'### {title}', '', table(rows), '']
    lines += ['## Maintain and cite', '', 'Edit [data/datasets.json](data/datasets.json), then run `python3 scripts/build_catalog.py`. Run `python3 scripts/build_catalog.py --check` before opening a pull request. See [CONTRIBUTING.md](CONTRIBUTING.md) for count and source requirements.', '', 'Please cite each original dataset when reusing it. Use [CITATION.cff](CITATION.cff) to cite this catalog. Catalog text and metadata are CC BY 4.0; scripts are MIT. Listed datasets retain their own terms. MatVerse hosts catalog metadata and links; it does not mirror the dataset payloads.', '']
    outputs = {'README.md': '\n'.join(lines)}
    for cat, title in CATEGORIES.items():
        rows = sorted([d for d in data if d['category'] == cat], key=order)
        if not rows:
            continue
        lines = [f'# {title}', '', '[Back to MatVerse](../../README.md)', '', f'Checked {DATE}. Counts are source-reported or explicitly derived from release metadata; full datasets were not independently deduplicated.', '']
        for d in rows:
            lines += [f'<a id="{d["id"]}"></a>', f'## {d["name"]}', '', d['description'], '', f"**Size:** {size(d)} {d['count_unit']} (source wording: {d['count_display']}).", '', f"**Scope:** {d['count_scope']}", '', f"**Release:** {d['version']}. **Year:** {d['year'] if d['year'] else 'Not verified'}.", '', f"**Provenance:** {d['provenance']}. **Structure availability:** `{d['structure_level']}`.", '', '**Labels/content:** ' + '; '.join(d['properties']) + '.', '', f"**Access:** {d['access']}. **Dataset license:** {d['license']}.", '', '**Official routes:** ' + ' · '.join(f'[{k}]({v})' for k, v in d['links'].items()), '']
            if d.get('additional_counts'):
                lines += ['Other denominators (not added to the ranking):', '']
                lines += [f"- {v['value']:,} {v['unit']}: {v['scope']}" for v in d['additional_counts']]
                lines += ['']
            if d.get('count_derivation'):
                v = d['count_derivation']
                lines += [f"**Count derivation:** {v['method']}; " + ' + '.join(f'{x:,}' for x in v['values']) + f" = {d['count']:,}.", '']
            lines += ['**Evidence:**', '']
            for s in d['sources']:
                lines += [f"- [{s['title']}]({s['url']}) (checked {s['verified_date']}): {s['evidence']}"]
            if d['caveats']:
                lines += ['', '**Reuse and interpretation notes:**', ''] + [f'- {c}' for c in d['caveats']]
            lines += ['', '**Tags:** ' + (', '.join(d['tags']) if d['tags'] else 'None assigned') + '.', '']
        outputs[f'docs/catalog/{cat}.md'] = '\n'.join(lines)
    cols = FIELDS[:]
    stream = io.StringIO(newline='')
    writer = csv.DictWriter(stream, fieldnames=cols, lineterminator='\n')
    writer.writeheader()
    for cat in CATEGORIES:
        for d in sorted([d for d in data if d['category'] == cat], key=order):
            writer.writerow({k: json.dumps(d[k], ensure_ascii=False, separators=(',', ':')) if isinstance(d[k], (dict, list)) else '' if d[k] is None else d[k] for k in cols})
    outputs['data/datasets.csv'] = stream.getvalue()
    lines = ['# Dataset repositories, discovery tools and adjacent resources', '', '[Back to MatVerse](../README.md)', '', 'These resources are navigation layers, collections, APIs, format mirrors or adjacent data. They are not additional independent crystal datasets and are not included in size rankings.', '', '| Resource | Role | Description |', '|---|---|---|']
    for r in sorted(resources, key=lambda r: (r['kind'], r['name'].casefold())):
        lines.append(f"| [{cell(r['name'])}]({r['url']}) | {cell(r['kind'])} | {cell(r['description'])} |")
    lines += ['', '## Evidence', '']
    for r in sorted(resources, key=lambda r: r['name'].casefold()):
        lines += [f"### {r['name']}", '']
        lines += [f"- [{s['title']}]({s['url']}) ({s['verified_date']}): {s['evidence']}" for s in r['sources']]
        lines += ['']
    outputs['docs/resources.md'] = '\n'.join(lines)
    lines = ['# Scientific Data journal index', '', '[Back to MatVerse](../README.md)', '', 'Dataset records with a verified Scientific Data descriptor among their evidence sources. This is an index into the catalog, not a census of everything published by the journal. Counts refer to the release selected in each card; a descriptor can describe an older release.', '', '| Dataset | Category | Reported volume | Descriptor evidence |', '|---|---|---:|---|']
    for d in sorted(data, key=lambda d: (d['category'], order(d))):
        sources = [s for s in d['sources'] if re.search(r's41597|sdata\.', s['url']) or 'scientific data' in s['title'].casefold()]
        if not sources:
            continue
        links = ' · '.join(f"[descriptor {i+1}]({s['url']})" for i, s in enumerate(sources))
        lines.append(f"| [{cell(d['name'])}](catalog/{d['category']}.md#{d['id']}) | {CATEGORIES[d['category']]} | {size(d)} {cell(d['count_unit'])} | {links} |")
    lines += ['', 'Further journal searching should consider perovskites, high-entropy materials, defects, diffraction, battery and magnetic materials, and phonon/electron-phonon datasets. Inclusion requires a verified primary descriptor and an explicit scope; a journal article license alone does not establish the accompanying data license.', '']
    outputs['docs/scientific-data.md'] = '\n'.join(lines)
    summary = dict(checked_date=DATE, dataset_records=len(data), categories=dict(counts), unranked_records=unknown, distinct_dataset_source_urls=source_count, navigation_resources=len(resources), count_total=None, count_total_note='Intentionally omitted: units, overlapping datasets and releases are not additive.')
    outputs['data/summary.json'] = json.dumps(summary, indent=2, ensure_ascii=False) + '\n'
    input_paths = ['data/datasets.json', 'data/resources.json', 'data/dataset.schema.json',
                   'templates/README_intro.md.txt', 'scripts/build_catalog.py',
                   'docs/SURVEY.md', 'docs/METHODOLOGY.md', 'docs/review-crosswalk.md']
    manifest = {
        'checked_date': DATE,
        'algorithm': 'sha256',
        'inputs': {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in input_paths},
        'generated_views': {p: hashlib.sha256(v.encode()).hexdigest() for p, v in outputs.items()},
        'scope': 'Catalog source files and generated views; excludes upstream dataset payloads and local research caches.',
    }
    outputs['data/catalog_manifest.json'] = json.dumps(manifest, indent=2) + '\n'
    return outputs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Validate inputs and fail if committed views are stale')
    args = parser.parse_args()
    data = json.loads((ROOT / 'data/datasets.json').read_text())
    resources = json.loads((ROOT / 'data/resources.json').read_text())
    validate(data, resources)
    outputs = render(data, resources)
    stale = []
    for path, content in outputs.items():
        target = ROOT / path
        if args.check:
            if not target.exists() or target.read_bytes() != content.encode():
                stale.append(path)
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding='utf-8')
    if stale:
        raise SystemExit('Stale generated views: ' + ', '.join(stale))
    print(f"Validated {len(data)} dataset records, {len(resources)} resources; " + ('generated views match.' if args.check else f'wrote {len(outputs)} views.'))


if __name__ == '__main__':
    main()
