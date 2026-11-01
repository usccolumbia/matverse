#!/usr/bin/env python3
"""Import pinned MateriaViva property-table metadata, never the full payloads."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / 'research/materiaviva_properties_20261101'
REVISION = '6010a086ade47c2c99d1b2dca3a944c3996959a4'
BASE = 'https://huggingface.co/datasets/AI4QC/MateriaViva-Open'
DATE = '2026-11-01'


def read(path):
    return json.loads(path.read_text())


def records():
    manifest = read(RESEARCH / 'property_manifest.json')
    labels = read(RESEARCH / 'property_labels.json')
    providers = read(RESEARCH / 'upstream_sources.json')
    files = {r['path']: r for r in read(RESEARCH / 'file_inventory.json')}
    assert len(manifest['per_property']) == manifest['properties'] == 148
    assert set(labels) == set(manifest['per_property'])
    assert sum(p['rows'] for p in manifest['per_property'].values()) == manifest['rows']
    rows = []
    manifest_url = f'{BASE}/blob/{REVISION}/properties/MANIFEST.json'
    registry_url = f'{BASE}/blob/{REVISION}/licences.json'
    for key, prop in manifest['per_property'].items():
        label = labels[key]
        assert sum(prop['sources'].values()) == prop['rows']
        path = f'properties/{key}.parquet'
        file = files[path]
        original_sources = [dict(source_id=source_id, values=count, **providers[source_id]) for source_id, count in sorted(prop['sources'].items(), key=lambda item: (-item[1], item[0]))]
        unit = prop['unit']
        kind = {'num': 'numeric', 'text': 'text descriptor', 'bool': 'boolean (0/1)'}[prop['kind']]
        source_count = len(original_sources)
        evidence = [dict(url=manifest_url, title='MateriaViva pinned property manifest', evidence=f'{key}: {prop["rows"]:,} value rows; {prop["structures"]:,} distinct structure references; unit {unit if unit else "not specified / unitless"}; kind {prop["kind"]}; full source-row counts retained.', verified_date=DATE), dict(url=f'{BASE}/blob/{REVISION}/README.md', title='MateriaViva property schema and provenance', evidence='One row per source/method value; material_id joins the structure release. Original source_native_id, method, licence and licence_class are retained; values are not averaged.', verified_date=DATE), dict(url=registry_url, title='MateriaViva upstream source declarations', evidence='Provider-declared upstream identities, rights classes and evidence links; these declarations are not independent verification of each original row or access path.', verified_date=DATE)]
        evidence += [dict(url=s['url'], title='Original source: '+s['name'], evidence=f'MateriaViva source ID {s["source_id"]}: {s["values"]:,} rows in this property table. Original access route mapped from pinned source registry and catalog provenance; it may require an account or have changed. '+s.get('notes',''), verified_date=DATE) for s in original_sources]
        for source in evidence:
            source['evidence'] = source['evidence'].rstrip()
        classes = {s['license_class'] for s in original_sources}
        licence = 'Per-row upstream terms; retain licence and licence_class.'
        if 'unclear' in classes: licence += ' Some upstream rights are not verified.'
        if classes & {'noncommercial', 'restricted'}: licence += ' Includes provider-declared noncommercial or restricted sources.'
        caveats = ['A property-specific discovery entry within MateriaViva, overlapping the parent aggregate and original databases; counts are value rows, not independent materials.', 'Several source/method values may refer to the same structure. Join material_id to parent structures and retain source_native_id, method and conditions; do not average or pool unlike methods by default.', 'Public download access does not override per-row original-source terms. Global manifest license-class totals do not establish per-property class distributions.', 'Original source links identify upstream providers, not necessarily an exact current row-level reconstruction. Grouped source aliases retain their mapping limits.']
        if not unit: caveats.append('The manifest gives no unit. This can mean dimensionless, boolean, categorical, or an unspecified unit; consult the original property definition.')
        if label.get('notes'): caveats += label['notes'] if isinstance(label['notes'],list) else [label['notes']]
        if key == 'easy_axis': caveats.append('Manifest flags 1,521 easy_axis values in an unexpected upstream column. The downloaded export was checked: its value column is string-typed, populated in all 1,521 rows, with 1,489 distinct material IDs. This diagnostic is not evidence of missing exported values.')
        rows.append(dict(id='materiaviva-property-'+key.replace('_','-'), name='MateriaViva — '+label['name'], category='materials_properties', description=f'{label["description"]} Direct access through MateriaViva; {prop["structures"]:,} linked structures and {source_count} original source'+('s.' if source_count != 1 else '.'), version='MateriaViva Open property export; revision '+REVISION, year=2026, count=prop['rows'], count_display=f'{prop["rows"]:,}', count_unit='property values', count_scope=f'{key}.parquet: {kind}; {prop["structures"]:,} distinct material_id references; source/method values retained separately. Count is reported by the pinned manifest.', count_precision='exact', structure_level='structure_linked', provenance='source- and method-labeled aggregate; original measurement, computation or descriptor provenance retained per row', properties=[label['name'], unit or 'unit not specified / unitless', label['family'], key, kind], access='open', license=licence, links=dict(homepage=f'{BASE}/blob/{REVISION}/{path}', data=f'{BASE}/resolve/{REVISION}/{path}', parent=BASE, manifest=manifest_url), sources=evidence, caveats=caveats, tags=list(dict.fromkeys(['MateriaViva','MaterialViva','Matvina','MateriaViva-property-subset', 'materiaviva-properties-20261101',label['family'],key]+label['aliases'])), additional_counts=[dict(value=prop['structures'],unit='linked structures',scope='Distinct material_id references in this property table; overlaps other properties.')], property_dataset=dict(provider='MateriaViva Open',property_key=key,unit=unit,value_kind=prop['kind'],revision=REVISION,parent_id='materiaviva-open',structures=prop['structures'],file_bytes=file['size'],file_sha256=file['lfs']['oid'],direct_access=f'{BASE}/blob/{REVISION}/{path}',direct_download=f'{BASE}/resolve/{REVISION}/{path}',upstream_sources=original_sources)))
    return rows


def main():
    data = read(ROOT / 'data/datasets.json')
    rows = records()
    data = [d for d in data if not d.get('property_dataset') or d['property_dataset'].get('provider') != 'MateriaViva Open'] + rows
    parent = next(d for d in data if d['id'] == 'materiaviva-open')
    parent['tags'] = list(dict.fromkeys(parent.get('tags', []) + ['MateriaViva','MaterialViva','Matvina','148 property tables']))
    note = 'Structure-release licensing is separate from property-row terms: the property manifest reports 97,837,513 open, 15,215,145 unclear, 313,041 noncommercial and 93,603 restricted value rows. Preserve each row’s licence and licence_class; these global totals do not determine each property’s class distribution.'
    if note not in parent['caveats']: parent['caveats'].append(note)
    (ROOT / 'data/datasets.json').write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
    receipt = dict(checked_date=DATE,revision=REVISION,property_tables=len(rows),values=sum(d['count'] for d in rows),upstream_source_ids=sorted({s['source_id'] for d in rows for s in d['property_dataset']['upstream_sources']}),new_dataset_ids=[d['id'] for d in rows],counts_source='Pinned properties/MANIFEST.json; selected small payloads independently checked. Full corpus not downloaded.',rows_by_licence_class=read(RESEARCH/'property_manifest.json')['rows_by_licence_class'])
    (RESEARCH/'integration_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(f'Imported {len(rows)} property tables; catalog now {len(data)} entries')


if __name__ == '__main__': main()
