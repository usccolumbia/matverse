"""Render the bounded additional-materials discovery pass."""
import json


def render_additional_survey(root, datasets, categories, cell, size, order):
    receipt = json.loads((root / 'research/additional_20261101/integration_receipt.json').read_text())
    by_id = {d['id']: d for d in datasets}
    rows = [by_id[ident] for ident in receipt['new_dataset_ids']]
    lines = ['# Additional materials dataset discoveries', '',
             '[Back to MatVerse](../README.md) · [Search these additions](https://usccolumbia.github.io/matverse/?q=%22additional-materials-20261101%22) · [All source links](../sources.md)', '',
             f'Checked {receipt["checked_date"]}. This targeted extension adds **{len(rows)} dataset/release records** beyond the {receipt["initial_catalog_records"]}-record baseline. The maintained catalog now contains **{len(datasets)} records**. New records include independently useful property layers and named derived releases; they are not all disjoint material populations.', '',
             '## Questions and search method', '',
             'The search asked which relevant releases remained absent after the journal/property surveys, what their independent counting units and parent lineages were, and which primary sources established scope, access and rights. Independent passes covered defects/disorder, porous materials/adsorption and specialized functional/low-dimensional materials. A coordinating pass examined atomistic reference sets and experimental transport/alloy properties.', '',
             'Searches followed papers to provider pages, author repositories, release APIs and selected payloads. A title hit or downloadable model alone was insufficient. This is a targeted extension across missing domains, not a census of every materials dataset online. Failed requests, deferred leads and alternative versions remain in the research trail.', '',
             '[Frozen brief](../research/additional_20261101/BRIEF.md) · [Research package](../research/additional_20261101/README.md) · [Integration receipt and source hashes](../research/additional_20261101/integration_receipt.json) · [Source-entry dispositions](../research/collection_additional_20261101.json)', '',
             '## What is newly covered', '',
             'The structural additions extend dimensionality and order: C1DB covers one-dimensional systems, SACADA indexes carbon allotropes, and defect/grain-boundary/irradiation releases describe departures from perfect bulk crystals. Porous collections supply hypothetical coordinates, adsorption data and thermal or diffusion labels. Specialized functional releases add Heusler, altermagnetic, spin-Hall, optical and ferroelectric-search data.', '',
             'These objects require different reuse strategies. A grain-boundary minimum is distinct from every candidate searched to obtain it; a defect-site calculation is distinct from its host crystal. A generated ferroelectric-search CIF is a model proposal, while measured thermoelectric observations and DFT-derived transport targets have different provenance. The DXMag ternary CSV counts calculation rows, whereas the other two Heusler releases report compound populations with ML-derived ground-state/property labels.', '',
             'For atomistic learning, SoLiD26 adds explicit solid–liquid environments and SevenNet DBS adds harmonized single-point labels over existing parent geometries. The smaller GAP/MACE/ACE reference cohorts span particular chemistries and sampling schemes. SiOx reuses Si and silica references; original and revised carbon datasets overlap. Synthetic a-Si and amorphous-graphene labels come from trained potentials and must not be treated as fresh DFT observations.', '',
             '## Verified release table', '',
             'Reported sizes descend within each category. Units, access, licenses and caveats remain explicit in the linked cards. Unknown sizes are unranked; counts are not added across parents, derivatives, frames, specimens or property observations.', '']
    for category, title in categories.items():
        selected = sorted([d for d in rows if d['category'] == category], key=order)
        if not selected:
            continue
        lines += [f'### {title}', '', '| Release | Reported volume | Label provenance | Access |', '|---|---:|---|---|']
        for d in selected:
            lines.append(f'| [{cell(d["name"])}](catalog/{category}.md#{d["id"]}) | {size(d)} {cell(d["count_unit"])} | {cell(d["provenance"])} | {d["access"]} |')
        lines += ['']
    lines += ['## Release and denominator findings', '',
              'SoLiD26’s September preprint described access by request. Its October revision and actual Materials Cloud deposit establish an open CC BY 4.0 release. The 15,379,823-frame count is source-reported; the 63.8 GiB compressed payload was not downloaded. The public README warns that ASE constraints can alter returned forces, so raw force labels must be read appropriately.', '',
              'SACADA’s live read-only response contains 1,661 unique IDs, even though its HTML displays an older update label. A sample ZIP contains ideal-net and optimized CIFs for one entry; these are not two new allotropes. Complete coordinate/property coverage and redistribution rights remain unverified.', '',
              'The MACE-MP-MOF0 downloadable v2 archive contains 4,311 complete frames across train/validation/test files, differing from the article’s 4,764 DFT points. PhononMOFdb’s inspected thermal archive contains 11,900 records. The Heusler ternary table has 106,235 UUID-distinct calculation rows; the provider’s 27,864-compound figure is a different unreconciled denominator. The ranked altermagnet table has 171 rows, compared with 180 discussed by the paper/current application. Each discrepancy is qualified in its card.', '',
              'The current sysTEm workbook contains 8,650 observations and 1,437 standardized composition strings, spanning 10–1275 K. It overlaps ESTM and extended MRL. The complex-oxide thermal-expansion table supplies 204 composition/temperature-range records. ULTERA’s May 2025 metadata reports 12,540+ HEA/MEA property points, but its files remain restricted and no data license was established.', '',
              '## Limits and follow-up', '',
              'Public metadata, downloadable coordinates, a declared license and a documentation check are separate signals. Some CMR pages have conflicting license statements; MINT’s client-code license does not establish its data rights; some defect archives have unverified rights. NIST adsorption’s historical count is explicitly dated and not presented as a live counter. Dataset cards preserve these distinctions.', '',
              'Selected small/medium payloads were independently counted or sampled. Larger corpora retain provider-reported counts. No blanket claim of numerical accuracy, unbiased sampling, deduplicated material identities or complete bulk-transfer success follows. Split related source papers, trajectories, hosts and parent structures together where needed to reduce leakage.', '',
              f'The local preview exposed a previous source-year parsing error: **{len(receipt["year_corrections"])} records** had been assigned 2002. Those values were corrected to the journal publication years using the retained DOI/date metadata. The integration receipt preserves each before/after value and source; historical staging files remain unchanged.', '',
              'The search answers the first question with the verified additions above, the second through the category/unit/provenance crosswalk, and the third through release-specific sources and access/rights fields. Deferred candidates remain discoverable without being promoted into the ranked catalog. All changes remain local pending the user’s publication instruction.', '']
    return '\n'.join(lines)
