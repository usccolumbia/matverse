"""Render every row of the inspected Matbench Discovery data-set directory."""
import json


def render_matbench_coverage(root, datasets, cell):
    audit=json.loads((root/'research/matbench_coverage_20261101/audit.json').read_text())
    receipt=json.loads((root/'research/matbench_coverage_20261101/integration_receipt.json').read_text())
    by_id={d['id']:d for d in datasets}
    labels={'existing_dataset':'Existing family / release mapping','new_dataset':'New named dataset / release','existing_resource':'Existing resource','new_resource':'New adjacent or unavailable resource'}
    lines=['# Matbench Discovery data-set directory coverage', '',
           '[Back to MatVerse](../README.md) · [Original directory](https://matbench-discovery.materialsproject.org/data/sets) · [Search all 46 entries](https://usccolumbia.github.io/matverse/?view=sources&collection=matbench_discovery_20261101)', '',
           f'Checked {audit["checked_date"]}. **All 46 displayed rows** agree with the maintained dataset registry at revision `{audit["revision"]}` and are preserved as searchable source entries. All 126 distinct outgoing primary routes are included in the source inventory. The audit adds **{len(receipt["new_dataset_ids"])} named datasets/releases** and **{len(receipt["new_resource_urls"])} resources**.', '',
           'Before this audit, coverage included many major families but was incomplete at the named-release and subset level. The initial crosswalk found 23 rows with existing dataset-family mappings, two existing resources, thirteen missing named releases and eight missing adjacent/unreleased resources. A family match is not proof of an identical dated corpus or counting denominator.', '',
           '## Coverage and counting boundaries', '',
           'MP v2022.10.28 is a frozen historical release with 154,718 entries; it does not replace the current Materials Project card’s 271,325 structures. MatPES PBE and r2SCAN are separate 2025.1 releases. sAlex validation is a 553,218-frame subset that overlaps the existing train-plus-validation card. COSMOS aggregates many existing parents and cannot be added to them as a new population.', '',
           'The page includes isolated molecules, molecular dynamics benchmarks, polymer data, software aggregators and unavailable full training corpora. These remain labeled resources or source leads. Public near-stable GNoME structures and the unavailable full GNoME training corpus have different scopes, as do public ELEMENTA partitions and the full training count.', '',
           'Alexandria is an existing family match, not a verified exact match to the page’s 30,497,628-frame training corpus. The provider separates dated optimized-geometry and optimization-path downloads; the registry does not tie that count to one frozen path. Its page-reported count and links are retained below without overwriting the equilibrium-structure card or inventing a release boundary.', '',
           'MDR-PBE has a documented 9,959-material reference claim but an independently counted current directory contains 9,958 mp-named files. The new card ranks the counted file population and preserves the discrepancy. PFT’s 8,510 training materials form an overlapping subset. None of these configuration, file, material and graph counts are interchangeable.', '',
           '## Complete entry crosswalk', '',
           'Sizes in this table preserve the directory’s reported columns, including its use of “structures” for many configuration/frame populations. Catalog cards state the actual counted units and any release mismatch.', '',
           '| Directory entry | Page structures / materials | Treatment | Catalog / resource route | Scope notes |', '|---|---:|---|---|---|']
    for e in audit['entries']:
        targets=' · '.join(f'[{cell(by_id[i]["name"])}](catalog/{by_id[i]["category"]}.md#{i})' for i in e['catalog_ids'])
        if e.get('resource_url'): targets+=(' · ' if targets else '')+f'[Resource]({e["resource_url"]})'
        fmt=lambda v: f'{v:,}' if isinstance(v,int) else 'not reported' if v is None else cell(v)
        lines.append(f'| [{cell(e["key"])} — {cell(e["name"])}]({e["detail_url"]}) | {fmt(e["listed_structures"])} / {fmt(e["listed_materials"])} | {labels[e["status"]]} | {targets} | {cell(e["note"])} |')
    lines += ['', '## Remaining release-level limits', '']
    for key,note in audit['important_scope_notes'].items(): lines.append(f'- **{key}:** {note}')
    lines += ['', '## Evidence', '',
              '[Complete audit JSON](../research/matbench_coverage_20261101/audit.json) · [Integration receipt](../research/matbench_coverage_20261101/integration_receipt.json) · [Source-entry inventory](../research/collection_matbench_discovery_20261101.json) · [Primary-source notes](../research/matbench_coverage_20261101/notes.md) · [Request receipts](../research/matbench_coverage_20261101/receipts.json)', '',
              'The directory and registry were inspected and selected release metadata were checked. This does not establish that every large payload was downloaded, every release independently recounted, or every provider-declared license independently assessed.', '']
    return '\n'.join(lines)
