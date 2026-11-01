"""Render provenance-aware discovery of all pinned MateriaViva property tables."""
import json


def render_materiaviva(root, datasets, cell, size, order):
    receipt = json.loads((root/'research/materiaviva_properties_20261101/integration_receipt.json').read_text())
    by_id = {d['id']:d for d in datasets}
    rows = sorted([by_id[i] for i in receipt['new_dataset_ids']],key=order)
    lines = ['# MateriaViva materials property datasets', '',
             '[Back to MatVerse](../README.md) · [Search all property tables](https://usccolumbia.github.io/matverse/?category=materials_properties) · [Direct provider](https://huggingface.co/datasets/AI4QC/MateriaViva-Open)', '',
             f'Checked {receipt["checked_date"]}. **All 148 property tables** are separate searchable entries in **Materials properties**. Together the manifest reports **113,459,302 value rows**, contributed by **56 original source IDs**. These are overlapping property subsets, not 148 independent material populations. Values from multiple methods or databases remain separate.', '',
             f'Pinned provider revision: `{receipt["revision"]}`. Counts, units, kinds, source-row counts and file identities are retained in the [metadata package](../research/materiaviva_properties_20261101/integration_receipt.json).', '',
             '## Access and interpretation', '',
             '**Direct access** opens the specific MateriaViva Parquet file and a pinned download. **Original sources / indirect access** lists every contributing upstream provider with its row count; no source list is shortened to an ellipsis. The aggregate source key and native record identifiers retain the path back to original data. Some aliases cover multiple releases, so a provider link is not a claim that the exact original row can be reconstructed there today.', '',
             'Search uses plain property names and aliases, for example superconducting critical temperature / Tc, ionic conductivity, Seebeck coefficient, band gap, lattice thermal conductivity and SHG. Numeric physical properties, boolean indicators and text descriptors remain distinguishable. A missing manifest unit is shown as unspecified / unitless, without assuming a unit.', '',
             'Each Parquet row contains material_id, value, method, source, source_native_id, licence and licence_class. Join material_id to the parent structure release; the property file does not itself contain all crystal coordinates. Counts below separate value rows from distinct referenced structures. Temperatures, functionals, conventions and experimental versus calculated targets require original-source context.', '',
             '## Property tables, descending by value rows', '',
             '| Property dataset | Value rows | Linked structures | Unit / kind | Original sources / indirect access (value rows) |', '|---|---:|---:|---|---|']
    for d in rows:
        p=d['property_dataset']
        upstream=' · '.join(f'[{cell(s["name"])}]({s["url"]}) ({s["values"]:,}; `{s["source_id"]}`)' for s in p['upstream_sources'])
        unit=cell(p['unit']) if p['unit'] else 'unspecified / unitless'
        lines.append(f'| [{cell(d["name"])}](catalog/materials_properties.md#{d["id"]}) · [MateriaViva file]({p["direct_access"]}) · [download]({p["direct_download"]}) | {size(d)} | {p["structures"]:,} | {unit} / {p["value_kind"]} | {upstream} |')
    lines += ['', '## Licensing and scope', '',
              'Property-row terms are separate from eligibility for the Open structure release. The global manifest classifies 97,837,513 property rows as open, 15,215,145 as unclear, 313,041 as noncommercial and 93,603 as restricted. These are provider declarations and global totals; they are not per-property distributions or an independent legal assessment. Preserve each row’s licence and licence_class and cite the original provider.', '',
              'Model predictions and curve/spectrum tables are separate release components and are not silently counted among these 148 source/method property tables. A source-derived value can nevertheless be calculated or predicted; retain the row method.', '',
              'The manifest flags 1,521 easy_axis values in an unexpected upstream column. The exported file was independently checked: all 1,521 value fields are populated strings and reference 1,489 material IDs. This is an upstream diagnostic, not a finding of missing exported values.', '',
              '## Verification', '',
              'All 148 keys match the pinned manifest and property-file listing. Per-source row counts sum to each property total; the property totals sum to 113,459,302. All 56 source IDs map to original provider routes, with grouped-source limitations retained. Full property payloads were not all downloaded or independently deduplicated.', '',
              'Four small files were downloaded and checked against provider SHA-256 identities: ionic conductivity (5 values), Curie temperature (6), magnetic easy axis (1,521), and superconducting critical temperature (26,613). Their schemas, row counts, source populations and license classes matched the pinned metadata. This verifies these examples, not every value in the corpus.', '',
              '[Pinned manifest](../research/materiaviva_properties_20261101/property_manifest.json) · [File identities](../research/materiaviva_properties_20261101/file_inventory.json) · [Payload checks](../research/materiaviva_properties_20261101/sample_verification.json) · [Original-source mapping](../research/materiaviva_properties_20261101/upstream_sources.json) · [Mapping limits](../research/materiaviva_properties_20261101/source_mapping_notes.md)', '']
    return '\n'.join(lines)
