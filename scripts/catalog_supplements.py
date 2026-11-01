"""Validate and render API routes and the bounded JARVIS coverage audit."""
import json

KINDS = {'optimade': 'OPTIMADE', 'native_api': 'Native API', 'bulk_sdk': 'Bulk SDK', 'bulk_files': 'Bulk files'}
AUTH = {'none': 'Anonymous public route', 'api_key': 'API key', 'account': 'Account / authorization', 'mixed': 'Depends on operation or dataset'}
STATUS = {'sample_verified': 'Small record sample verified', 'metadata_verified': 'Metadata response verified', 'empty_response': 'JSON response; empty sample', 'auth_required': 'Authentication required', 'unavailable': 'Probe unsuccessful', 'documented': 'Documented; not queried'}


def load_apis(root, datasets, url_ok):
    rows = json.loads((root / 'data/api_sources.json').read_text())
    ids, dataset_ids = set(), {d['id'] for d in datasets}
    for r in rows:
        assert r['id'] not in ids, r['id']
        ids.add(r['id'])
        assert r['kind'] in KINDS and r['auth'] in AUTH, r['id']
        assert all(r.get(k) for k in ['name', 'entrypoint', 'description', 'auth_notes', 'formats', 'sources', 'limitations']), r['id']
        assert url_ok(r['entrypoint']), r['id']
        assert set(r['catalog_ids']) <= dataset_ids, r['id']
        assert r['verification']['status'] in STATUS, r['id']
        if r['verification'].get('probe_url'):
            assert url_ok(r['verification']['probe_url']), r['id']
        assert all(url_ok(s['url']) and s['title'] and s['evidence'] and s['verified_date'] for s in r['sources']), r['id']
    return rows


def render_supplements(root, datasets, resources, apis, date, cell):
    by_id = {d['id']: d for d in datasets}
    def cards(ids):
        return ' · '.join(f'[{cell(by_id[i]["name"])}](catalog/{by_id[i]["category"]}.md#{i})' for i in ids)
    lines = ['| Source / interface | Interface type | Authentication | Verification on '+date+' |', '|---|---|---|---|']
    for r in apis:
        lines.append(f'| [{cell(r["name"])}](#{r["id"]}) | {KINDS[r["kind"]]} | {AUTH[r["auth"]]} | {STATUS[r["verification"]["status"]]} |')
    details = []
    for r in apis:
        v = r['verification']
        details += [f'<a id="{r["id"]}"></a>', '## '+r['name'], '', r['description'], '',
                    f'**Interface:** {KINDS[r["kind"]]}. **Entrypoint:** [{r["entrypoint"]}]({r["entrypoint"]}).', '',
                    '**Authentication:** '+r['auth_notes'], '', '**Formats:** '+', '.join(r['formats'])+'.', '',
                    '**Verification:** '+STATUS[v['status']]+' ('+v['checked_date']+'). '+v['note']+'.', '']
        if v.get('probe_url'):
            details += [f'Probe: [{cell(v["probe_url"])}](<{v["probe_url"]}>)'+(f'; HTTP {v["http_status"]}.' if v.get('http_status') else '; no HTTP response recorded.'), '']
        if r['catalog_ids']:
            details += ['**Catalog coverage:** '+cards(r['catalog_ids']), '']
        details += ['**Limits and interpretation:**', '']+['- '+s for s in r['limitations']]+['', '**Official evidence:**', '']
        details += [f'- [{s["title"]}]({s["url"]}) (checked {s["verified_date"]}): {s["evidence"]}' for s in r['sources']]+['']
    template = (root / 'templates/api-access.md.txt').read_text()
    client_inventory = json.loads((root / 'research/collection_optimade_clients.json').read_text())
    provider_lines = ['| Provider ID | Database / provider index |', '|---|---|']
    for e in client_inventory['links']:
        if e.get('provider_id'):
            provider_lines.append(f'| `{e["provider_id"]}` | [{cell(e["label"].split(": ", 1)[1])}]({e["url"]}) |')
    template = template.replace('{{OPTIMADE_PROVIDERS}}', '\n'.join(provider_lines))
    api_doc = template.replace('{{DATE}}', date).replace('{{API_COUNT}}', str(len(apis))).replace('{{API_TABLE}}', '\n'.join(lines)).replace('{{API_DETAILS}}', '\n'.join(details))

    c = json.loads((root / 'research/collection_jarvis_databases.json').read_text())
    top = [e for e in c['links'] if e['section'] == 'JARVIS homepage / Databases']
    named = [e for e in c['links'] if e['section'] == 'JARVIS-Tools / Figshare based databases']
    extra = [e for e in c['links'] if e['section'].startswith('Pinned downloader')]
    assert len(top) == c['homepage_database_rows'] == 13
    assert len(named) == c['documented_dataset_rows'] == 65
    assert len({e['registry_key'] for e in named + extra if e.get('registry_key')}) == c['downloader_registry_keys'] == 66
    urls = {r['url'] for r in resources}
    jarvis = ['# JARVIS database coverage audit', '', f'Checked {date}. **All {len(top)} homepage database rows, all {len(named)} linked Figshare table entries and all 66 current downloader names are included.** The homepage numbers its rows 1–7 and 9–14; there is no row 8.', '',
              'Before this audit, MatVerse covered selected JARVIS releases and the notebook collection, but not the complete database directory. The current inventory preserves every requested row and the linked download inventory. Seven additional ranked dataset releases fill major gaps; search tools, APIs, literature portals and alternate front ends remain resources.', '',
              '[Search all JARVIS source entries](https://usccolumbia.github.io/matverse/?view=sources&collection=jarvis_databases) · [Inventory JSON](../research/collection_jarvis_databases.json) · [API access guide](api-access.md)', '',
              '## Homepage Databases: complete crosswalk', '', '| Original database row | Catalog / resource representation | Note |', '|---|---|---|']
    for e in top:
        assert e.get('catalog_ids') or e.get('resource_urls'), e['label']
        assert set(e.get('resource_urls', [])) <= urls
        targets = cards(e.get('catalog_ids', []))
        targets += (' · ' if targets and e.get('resource_urls') else '')+' · '.join(f'[Resource]({u})' for u in e.get('resource_urls', []))
        jarvis += [f'| [{cell(e["label"])}]({e["url"]}) | {targets} | {cell(e["note"])} |']
    jarvis += ['', '## Figshare documentation: every named entry', '',
               'The numbers below preserve documentation wording. They mix materials, configurations, property records, papers, files and Hamiltonians; they are not a size ranking or an additive crystal total. Third-party mirrors retain their source identities. “Inventory only” means the route is searchable and sourced, while that specific release has not been promoted to an independently checked ranked dataset card.', '',
               '| Original name / download route | Documented data points | Catalog treatment |', '|---|---:|---|']
    for e in named:
        jarvis += [f'| [{cell(e["label"])}]({e["url"]}) | {cell(e["documented_count"])} | {cards(e.get("catalog_ids", [])) or "Inventory only; mirror / adjacent / release lead"} |']
    jarvis += ['', '## Registry-only entries', '', 'These names occur in pinned `get_db_info()` but not in the documentation table. Progress-message numbers are not promoted to exact dataset counts.', '']
    jarvis += [f'- [{e["label"]}]({e["url"]})' for e in extra]
    jarvis += ['', '## Access, versions and checks', '',
               '- `stm`, `wtbh_electron` and `wtbh_phonon` have dedicated helpers. They are documentation entries but not current `data(name)` keys. Wannier helpers use `WANN` and `FD-ELAST` groups in `raw_files`.',
               '- The selected `dft_3d` mirror is the December 2022 release with 75,993 documented entries. The homepage statistics show 77,096, descriptive text says 80,000+, and Figshare lists a newer September 2025 file. These sources do not identify one interchangeable release.',
               '- The parsed interface archive contains 593 records; the selected vacancy archive contains 464. Other sizes are documentation-reported unless a dataset card states otherwise. Deposit metadata confirms CC BY 4.0 for QETB, FF, interface/surface and vacancy deposits. Hamiltonian payload rights remain unverified.',
               '- JARVIS-DFT2 is an alternate route to the DFT family. Universal Search, ChemNLP, Leaderboard, Notebooks and OPTIMADE do not add independent crystal structure counts.',
               '- Portal login requirements are distinct from public Figshare downloads. The JARVIS OPTIMADE probe returned JSON with an empty sample; this does not establish working structure retrieval.', '',
               '## Source provenance', '',
               f'- [JARVIS homepage]({c["url"]}) and [Figshare documentation](https://pages.nist.gov/jarvis/databases/).',
               f'- [Pinned downloader](https://github.com/usnistgov/jarvis/blob/{c["revision"]}/jarvis/db/figshare.py), revision `{c["revision"]}`. Parsed as syntax; not executed.',
               '- [Document response hashes](../research/provenance/jarvis_api_inputs_20261101.json)',
               '- [Deposit metadata and file identities](../research/provenance/jarvis_release_metadata_20261101.json)',
               '- [Provider discovery and bounded archive checks](../research/provenance/optimade_discovery_20261101.json)',
               '- [Small API probe receipts](../research/provenance/api_probes_20261101.json)', '', '[Back to MatVerse](../README.md)', '']
    return {'docs/api-access.md': api_doc, 'docs/jarvis-coverage.md': '\n'.join(jarvis)}
