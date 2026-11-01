"""Normalize Scientific Data identifiers and render the bounded journal survey."""
import json
import re
from collections import Counter
from urllib.parse import unquote


def descriptor_dois(url):
    """Accept current DOIs and both dotted and compact legacy Nature article IDs."""
    text = unquote(url).lower()
    identifiers = set(re.findall(r's41597-\d{3}-[0-9a-z]+-[0-9a-z]+', text))
    identifiers.update(re.findall(r'sdata\.20\d{2}\.\d+', text))
    identifiers.update(f'sdata.{year}.{number}' for year, number in
                       re.findall(r'sdata(20\d{2})(\d+)', text))
    return {'10.1038/' + value for value in identifiers}


def dataset_descriptors(dataset):
    urls = list(dataset['links'].values()) + [s['url'] for s in dataset['sources']]
    return sorted(set().union(*(descriptor_dois(url) for url in urls)))


def render_scientific_data(root, datasets, categories, date, cell, size, order):
    folder = root / 'research/sdata_20261101'
    receipt = json.loads((folder / 'journal_harvest_receipts.json').read_text())
    works = {w['doi']: w for w in json.loads((folder / 'journal_works.json').read_text())}
    by_doi = {}
    selected = []
    added = []
    for d in datasets:
        dois = dataset_descriptors(d)
        if not dois:
            continue
        selected.append(d)
        if 'Scientific-Data-survey-20261101' in d['tags']:
            added.append(d)
        for doi in dois:
            by_doi.setdefault(doi, []).append(d['id'])
    index = []
    for doi, ids in sorted(by_doi.items()):
        w = works.get(doi, {})
        index.append(dict(doi=doi, title=w.get('title'),
                          publication_date=w.get('publication_date'),
                          catalog_ids=sorted(ids), journal_metadata_match=bool(w),
                          url='https://doi.org/' + doi))
    lines = ['# Materials datasets in Scientific Data', '',
             '[Back to MatVerse](../README.md) · [Journal](https://www.nature.com/sdata/) · [Search catalog additions](https://usccolumbia.github.io/matverse/?q=%22Scientific-Data-survey-20261101%22)', '',
             f'Checked {date}. This pass adds **{len(added)} dataset/release records**. The catalog now links **{len(selected)} records to {len(index)} distinct Scientific Data descriptors**. A descriptor can cover several releases or subsets; these are not independent material totals.', '',
             '## Search scope and audit trail', '',
             f'The [Crossref journal endpoint](https://api.crossref.org/journals/2052-4463/works) was paginated to its reported total: **{receipt["unique_works"]:,} indexed records** for ISSN 2052-4463 through {receipt["cutoff"]}. A broad, preserved title-keyword screen flagged **{receipt["title_candidates"]:,} candidates**. Searches of publisher pages, linked references and dataset repositories supplemented that screen. Three independent topical passes covered structures/computation, physical properties/synthesis, and characterization/processing.', '',
             'Complete API pagination means complete retrieval of this indexed response, not complete publisher indexing or full-text review of every article. Title matches include unrelated biomedical and environmental papers. Most candidates remain unreviewed discovery leads. Only primary-source-verified releases enter the ranked catalog. This is a broad journal search with a documented verification boundary, not an exhaustive census of all materials data published by Scientific Data.', '',
             '[Full journal metadata](../research/sdata_20261101/journal_works.json) · [Title candidates](../research/sdata_20261101/journal_candidates.json) · [Query/page receipts and hashes](../research/sdata_20261101/journal_harvest_receipts.json) · [Reproducible harvest script](../research/sdata_20261101/harvest_journal.py) · [Source-entry dispositions](../research/collection_sdata_20261101.json) · [Descriptor-to-catalog index](../data/scientific_data_index.json) · [Frozen research brief](../research/sdata_20261101/BRIEF.md) · [Integration receipt](../research/sdata_20261101/integration_receipt.json)', '',
             'The source-entry inventory retains every title candidate, its DOI and its review treatment, plus verified descriptor matches missed by title keywords. Existing catalog matches and verified new additions are distinguished from unresolved leads and corrections. Local research notes and compact repository receipts are retained in the three topical folders under [the audit directory](../research/sdata_20261101/README.md). Large retrieved article bodies and payloads remain in ignored local caches.', '',
             '## What the collections enable', '',
             'Crystal/DFT collections provide coordinates and calculated labels, but often share parent structures with Materials Project, COD, CoRE MOF or PhononDB. Property tables capture measurements or calculations under specific temperatures, processing histories, functionals or pressure ranges. Images, spectra, simulated diffraction patterns and atomistic trajectories add other observations of materials; they are not interchangeable with unique equilibrium crystals.', '',
             'For training, split related structures, source papers, specimens and trajectories together where appropriate. Literature-extracted values can repeat observations from parent databases. Simulation grids over functionals or charge models expand label coverage without creating the same number of independent structures. Report the release, counted unit, conditions and lineage used for each experiment.', '',
             'Dataset rights were checked separately from article rights. A CC BY article does not automatically license a linked archive. Missing rights or sizes remain explicit; unknown sizes are unranked. Selected small-file recounts and repository metadata inspections are documented in the cards. Full bulk transfers, numerical replication and comprehensive row-level quality audits were not performed.', '',
             '## Verified catalog coverage', '',
             'Sizes descend within each category; unknown sizes appear last. “New” identifies this search pass. Counts are not summed across units, parents, derivatives or releases.', '']
    for cat, title in categories.items():
        rows = sorted([d for d in selected if d['category'] == cat], key=order)
        if not rows:
            continue
        lines += [f'### {title}', '', '| Dataset / release | Reported volume | Structure level | Descriptor | Pass |', '|---|---:|---|---|---|']
        for d in rows:
            links = ' · '.join(f'[paper {i + 1}](https://doi.org/{doi})' for i, doi in enumerate(dataset_descriptors(d)))
            status = 'New' if d in added else 'Existing'
            lines.append(f'| [{cell(d["name"])}](catalog/{cat}.md#{d["id"]}) | {size(d)} {cell(d["count_unit"])} | `{d["structure_level"]}` | {links} | {status} |')
        lines += ['']
    counts = Counter('new' if 'Scientific-Data-survey-20261101' in d['tags'] else 'existing' for d in selected)
    machine = dict(checked_date=date, journal='Scientific Data', issn='2052-4463',
                   search_metadata_records=receipt['unique_works'], title_candidates=receipt['title_candidates'],
                   catalog_records=len(selected), new_catalog_records=counts['new'],
                   existing_catalog_records=counts['existing'], distinct_descriptors=len(index),
                   completeness_note='Indexed metadata retrieval completed; title candidates and primary-source verification are not exhaustive journal coverage.',
                   descriptors=index)
    return {'docs/scientific-data.md': '\n'.join(lines),
            'data/scientific_data_index.json': json.dumps(machine, ensure_ascii=False, indent=2) + '\n'}
