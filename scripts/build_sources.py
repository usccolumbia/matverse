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
    lines=['# MatVerse source links','',f'Link inventory checked {DATE}. This file combines every official route and evidence URL in the maintained catalog, navigation-resource sources, all six requested source collections, and supporting perspective references.','',
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
    references=[('Materials Databases: Foundations of Modern Digital Materials','https://doi.org/10.1021/prechem.5c00449'),('The rise of the digital materials ecosystem','https://doi.org/10.20517/aiagent.2026.08'),('Accelerating Catalyst Materials Discovery With Large Artificial Intelligence Models','https://doi.org/10.1002/anie.202526150'),('Roadmap for transforming heterogeneous catalysis with artificial intelligence','https://doi.org/10.1038/s41929-026-01479-x')]
    lines += ['## Supporting perspective papers','']
    for label,url in references:
        register(url,label,'Supporting perspective');lines += ['- '+link(label,url)]
    lines += ['', 'The [ACS crosswalk](docs/review-crosswalk.md) and [related-paper notes](docs/related-perspectives.md) describe how these references were used and which full texts or previews were available.','', '## All distinct source URLs','',f'**{len(all_urls)} distinct public URLs** across the sections above. This index deduplicates exact URL strings; redirects, mirrors and release variants may point to overlapping content.','', '| Source link | Included as |','|---|---|']
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
    coverage += ['',f'**{collection_inventory["entry_count"]} occurrences; {collection_inventory["unique_url_count"]} distinct entry URLs across all six collections.** Repeated entries and links shared between lists are retained with their original context. Blaiszik and Seda Oturak together contribute 364 occurrences and 296 distinct URLs at the inspected revisions.','',
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
    return {'sources.md':'\n'.join(lines),'data/source_links.json':json.dumps(inventory,indent=2,ensure_ascii=False)+'\n',
            'data/collection_entries.json':json.dumps(collection_inventory,indent=2,ensure_ascii=False)+'\n','docs/collection-coverage.md':'\n'.join(coverage)}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args()
    for name,content in render().items():
        path=ROOT/name
        if args.check:
            if not path.exists() or path.read_bytes()!=content.encode():raise SystemExit(f'Stale source index: {name}')
        else:path.write_text(content,encoding='utf-8')
    print('Source-link index is current.' if args.check else 'Built sources.md and machine-readable source URL inventory.')

if __name__=='__main__':main()
