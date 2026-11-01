#!/usr/bin/env python3
"""Render the complete, deduplicated public source-link index."""
import argparse
import json
from pathlib import Path
from urllib.parse import urlparse
from build_catalog import CATEGORIES, DATE, url_ok
from collection_inventory import load_inventory

ROOT = Path(__file__).resolve().parents[1]

def text(s):
    return str(s).replace('|', '\\|').replace('\n', ' ').replace('[','(').replace(']',')')

def link(label,url):
    return f'[{text(label)}](<{url}>)'

def render():
    datasets=json.loads((ROOT/'data/datasets.json').read_text())
    resources=json.loads((ROOT/'data/resources.json').read_text())
    all_urls={}
    def register(url,label,origin):
        if not isinstance(url,str) or urlparse(url).scheme not in {'http','https'}: return
        if not url_ok(url): raise ValueError('Source URL contains credentials or an ephemeral access query; use its stable public entrypoint.')
        entry=all_urls.setdefault(url,{'labels':set(),'origins':set()})
        entry['labels'].add(label);entry['origins'].add(origin)
    collection_inventory=load_inventory(ROOT)
    lines=['# MatVerse source links','',f'Link inventory checked {DATE}. This file combines every official route and evidence URL in the maintained catalog, navigation-resource sources, all {len(collection_inventory["collections"])} inspected resource collections, and supporting perspective references.','',
           'Collection-listed links are discovery leads. Their presence here does not mean every destination is still accessible, every resource supplies crystal coordinates, or every count/license has been verified. Crystal-related additions enter the ranked catalog only with their own evidence; adjacent molecular, polymer, engineering and handbook resources remain labeled in the collection inventories.','',
           f'**All {collection_inventory["entry_count"]} imported link occurrences are searchable** in the [Source entries view](https://usccolumbia.github.io/matverse/?view=sources). See the [collection coverage audit](docs/collection-coverage.md) and [complete entry JSON](data/collection_entries.json). Both requested GitHub lists are included in full within the documented extraction boundaries.','',
           '## Source collections supplied by the user','']
    collections=[]
    for path in sorted((ROOT/'research').glob('collection_*.json')):
        if path.stem.endswith('_additions'):continue
        c=json.loads(path.read_text())
        if 'links' not in c:continue
        collections.append(c)
        url=c.get('url') or c.get('repository_url');name=c.get('repository') or c.get('name') or path.stem
        if url:
            register(url,name,'Requested collection')
            lines += [f'### {link(name,url)}','']
        else:lines += [f'### {text(name)}','']
        if c.get('readme_url'):register(c['readme_url'],name+' README','Collection provenance')
        rev=c.get('revision') or c.get('commit_sha') or c.get('commit')
        if rev:lines += [f'Inspected revision: `{rev}`.','']
        if c.get('coverage_notes'):
            lines += ['Inspection boundary and caveats:', ''] + ['- '+text(note) for note in c['coverage_notes']] + ['']
        for receipt in c.get('response_receipts',[]):
            if receipt.get('url'):register(receipt['url'],name+' inspected document','Collection evidence')
        for source in c.get('sources',[]):
            if isinstance(source,dict) and source.get('url'):register(source['url'],source.get('title',name+' provenance'),'Collection evidence')
        entries=c['links']
        lines += [f'{len(entries)} labeled link occurrences; {len({e["url"] for e in entries})} distinct URLs. Section and scope labels preserve the collection context.','', '| Linked source | Original section | Scope |','|---|---|---|']
        seen=set()
        for e in entries:
            url=e['url'];label=e.get('label') or urlparse(url).netloc;section=e.get('section','Not recorded');scope=e.get('scope','uncertain')
            if isinstance(section,list):section=' / '.join(section)
            register(url,label,name)
            key=(url,label,section)
            if key in seen:continue
            seen.add(key)
            lines.append(f'| {link(label,url)} | {text(section)} | {text(scope)} |')
        lines += ['']
    lines += ['## Ranked catalog: official routes and evidence','']
    for category,title in CATEGORIES.items():
        lines += [f'### {title}','']
        for d in [d for d in datasets if d['category']==category]:
            lines += [f'#### {text(d["name"])}', '',f'Release: {d["version"]}.','']
            for role,url in d['links'].items():
                register(url,d['name']+' — '+role,'Catalog official route')
                lines += [f'- {role.capitalize()}: {link(d["name"],url)}']
            for s in d['sources']:
                register(s['url'],s['title'],'Catalog evidence')
                lines += [f'- Evidence ({s["verified_date"]}): {link(s["title"],s["url"])}']
            lines += ['']
    lines += ['## Repository, portal and adjacent-resource evidence','']
    for r in resources:
        register(r['url'],r['name'],'Navigation resource')
        lines += [f'### {link(r["name"],r["url"])}', '',f'Role: {r["kind"]}.','']
        for s in r['sources']:
            register(s['url'],s['title'],'Resource evidence')
            lines += [f'- {link(s["title"],s["url"])} (checked {s["verified_date"]})']
        lines += ['']
    references=[('Materials Databases: Foundations of Modern Digital Materials','https://doi.org/10.1021/prechem.5c00449'),('The rise of the digital materials ecosystem','https://doi.org/10.20517/aiagent.2026.08'),('Accelerating Catalyst Materials Discovery With Large Artificial Intelligence Models','https://doi.org/10.1002/anie.202526150'),('Roadmap for transforming heterogeneous catalysis with artificial intelligence','https://doi.org/10.1038/s41929-026-01479-x'),('Superconductor Discovery in the Emerging Paradigm of Materials Informatics','https://doi.org/10.1021/acs.chemmater.4c01757')]
    lines += ['## Supporting perspective papers','']
    for label,url in references:
        register(url,label,'Supporting perspective');lines += ['- '+link(label,url)]
    lines += ['', 'The [ACS crosswalk](docs/review-crosswalk.md), [related-paper notes](docs/related-perspectives.md), and [superconductivity supplement](docs/superconductivity.md) describe how these references were used and which full texts or previews were available. The [requested-resource crosswalk](docs/requested-resources.md) maps the additional supplied URLs.','', '## All distinct source URLs','',f'**{len(all_urls)} distinct public URLs** across the sections above. This index deduplicates exact URL strings; redirects, mirrors and release variants may point to overlapping content.','', '| Source link | Included as |','|---|---|']
    for url,e in sorted(all_urls.items(),key=lambda v:(urlparse(v[0]).netloc,v[0])):
        label=sorted(e['labels'],key=lambda x:(len(x),x))[0]
        lines += [f'| {link(label,url)} | {text("; ".join(sorted(e["origins"])))} |']
    lines += ['', '[Back to the catalog](README.md) · [Search the HTML directory](https://usccolumbia.github.io/matverse/)','']
    inventory={'checked_date':DATE,'unique_urls':len(all_urls),'collection_repositories':[c.get('repository') for c in collections],'sources':[{'url':u,'labels':sorted(e['labels']),'origins':sorted(e['origins'])} for u,e in sorted(all_urls.items())]}
    coverage=['# Source collection coverage','',f'Checked {DATE}. The source-entry directory preserves every labeled public HTTP(S) link occurrence in the inspected inventories. Entries include datasets, papers, portals, software, handbooks and adjacent domains; they are not counts of independent crystal datasets.','',
              '| Collection | Imported / inventoried entries | Distinct entry URLs | Missing from sources.md | Search |','|---|---:|---:|---:|---|']
    for c in collection_inventory['collections']:
        own=[e for e in collection_inventory['entries'] if e['collection']==c['id']]
        missing={e['url'] for e in own}-all_urls.keys()
        if missing:raise ValueError(f'Collection URLs missing from source index: {c["id"]}')
        c['source_index_missing_url_count']=len(missing)
        coverage += [f'| {link(c["name"],c["url"])} | {len(own)} / {c["entry_count"]} | {c["unique_url_count"]} | 0 | [Browse entries](https://usccolumbia.github.io/matverse/?view=sources&collection={c["id"]}) |']
    coverage += ['',f'**{collection_inventory["entry_count"]} entries; {collection_inventory["unique_url_count"]} distinct entry URLs across all {len(collection_inventory["collections"])} collections.** Repeated entries and links shared between lists are retained with their original context unless the collection boundary explicitly documents exact-URL deduplication. Blaiszik and Seda Oturak together contribute 364 occurrences and 296 distinct URLs at the inspected revisions.','',
                 '## What complete coverage means','',
                 'Every entry in each checked inventory is included in sources.md, the downloadable JSON, and the searchable Source entries view. The inventory preserves the source label, URL, original section, scope classification and source collection. Internal page anchors and non-URL placeholders are outside the extraction boundary. Linked external websites are not recursively crawled.','',
                 'The collection revisions, extraction boundaries and inventory hashes below make this claim reproducible. Live GitHub HEAD matched both requested list revisions when rechecked on 2026-11-01. This is an inventory-completeness check, not independent validation of each destination, dataset size or license. A crystal-related scope label is a triage aid; it does not certify atomic-coordinate availability. The ranked catalog maintains its separate evidence requirements.','',
                 '## Revisions and extraction boundaries','']
    for c in collection_inventory['collections']:
        coverage += [f'### {text(c["name"])}','',f'- Inventory: [{c["inventory_file"]}](../{c["inventory_file"]})',f'- Revision: `{c["revision"]}`',f'- Inventory SHA-256: `{c["inventory_sha256"]}`',f'- Scope counts: {text(json.dumps(c["scope_counts"],sort_keys=True))}','']
        coverage += ['- '+text(note) for note in c['coverage_notes']]+['']
    coverage += ['[All source links](../sources.md) · [Complete entry JSON](../data/collection_entries.json) · [Back to catalog](../README.md)','']
    collection_inventory['checked_date']=DATE
    collection_inventory['note']='Complete imported link inventory within the documented extraction boundaries; not a list of independently verified crystal datasets.'
    outputs={'sources.md':'\n'.join(lines),'data/source_links.json':json.dumps(inventory,indent=2,ensure_ascii=False)+'\n',
             'data/collection_entries.json':json.dumps(collection_inventory,indent=2,ensure_ascii=False)+'\n','docs/collection-coverage.md':'\n'.join(coverage)}
    requested=next((c for c in collections if c.get('id')=='user_resources_20261101'),None)
    if requested:
        by_id={d['id']:d for d in datasets};by_url={r['url']:r for r in resources}
        crosswalk=['# Requested materials-data resources: coverage and current routes','',f'Checked {DATE}. Every one of the {len(requested["links"])} distinct supplied URLs is preserved in [sources.md](../sources.md) and the [searchable supplied-list collection](https://usccolumbia.github.io/matverse/?view=sources&collection=user_resources_20261101). Exact duplicate CDCS and UCSD SRD mentions are documented in the [input inventory](../research/collection_user_resources_20261101.json) and counted once here.','',
                   'Historical numbers in the supplied descriptions are discovery context. The dataset cards retain verified release-specific counts, units, access and evidence. Registries, curation software, model archives and adjacent polymer resources remain identifiable as resources rather than being counted as additional crystal corpora.','',
                   '| Supplied source | Treatment | MatVerse coverage / current routes | Audit note |','|---|---|---|---|']
        for e in requested['links']:
            assert e['url'] in all_urls,e['url']
            destinations=[]
            for ident in e.get('catalog_ids',[]):
                d=by_id[ident];destinations.append(link(d['name'],f'catalog/{d["category"]}.md#{ident}'))
            for url in e.get('resource_urls',[]):
                r=by_url[url];destinations.append(link(r['name'],url))
            assert destinations,e['label']
            crosswalk.append(f'| {link(e["label"],e["url"])} | {text(e["treatment"])} | {" · ".join(destinations)} | {text(e["note"])} |')
        crosswalk += ['', '## Interpretation and attribution corrections','',
                      'The ADS bibcode resolves to the Clark University Organic Superconductor Database presentation. UCSD SRD is documented independently by the owning Schuller group; its current counts, test-status definitions, coordinate payload and data license were not established during the server-error checks. NIST 62 Version 2.0 documents the existing WebHTS / SRD 62 family. These three identities are kept separate.','',
                      'The linked 2024 Chemistry of Materials review led to the corrected CompSC release: 586 structures, 583 numeric lambda values and 566 numeric omega_log values. Its older 587-structure description is retained as historical context. The full author-posted review was available even though direct publisher requests failed.','',
                      'A separate source audit found that JARVIS supercon_chem and the Stanev author CSV contain exactly the same 16,414 formula/Tc pairs. They are represented once. The author assigns zero to unreported Tc; 3,966 zero-coded rows therefore do not automatically establish confirmed negative experiments. This also qualifies inherited 3DSC zero-label interpretation.','',
                      '## Primary-source audit notes','',
                      '- [Crystal platforms, legacy routes and access](../research/resource_supplement_crystal_notes.md)',
                      '- [Registries, polymers, models and curation infrastructure](../research/resource_supplement_infrastructure_notes.md)',
                      '- [UCSD, OSD abstract, ACS review, CompSC and label provenance](../research/resource_supplement_superconductivity_notes.md)','',
                      '[Back to MatVerse](../README.md) · [Superconductivity comparison](superconductivity.md)','']
        outputs['docs/requested-resources.md']='\n'.join(crosswalk)
    return outputs

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args()
    for name,content in render().items():
        path=ROOT/name
        if args.check:
            if not path.exists() or path.read_bytes()!=content.encode():raise SystemExit(f'Stale source index: {name}')
        else:path.write_text(content,encoding='utf-8')
    print('Source-link index is current.' if args.check else 'Built sources.md and machine-readable source URL inventory.')

if __name__=='__main__':main()
