#!/usr/bin/env python3
"""Render the complete, deduplicated public source-link index."""
import argparse
import json
from pathlib import Path
from urllib.parse import urlparse
from build_catalog import CATEGORIES, DATE, url_ok

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
    lines=['# MatVerse source links','',f'Link inventory checked {DATE}. This file combines every official route and evidence URL in the maintained catalog, navigation-resource sources, the two requested source collections, and supporting perspective references.','',
           'Collection-listed links are discovery leads. Their presence here does not mean every destination is still accessible, every resource supplies crystal coordinates, or every count/license has been verified. Crystal-related additions enter the ranked catalog only with their own evidence; adjacent molecular, polymer, engineering and handbook resources remain labeled in the collection inventories.','',
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
    return {'sources.md':'\n'.join(lines),'data/source_links.json':json.dumps(inventory,indent=2,ensure_ascii=False)+'\n'}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args()
    for name,content in render().items():
        path=ROOT/name
        if args.check:
            if not path.exists() or path.read_bytes()!=content.encode():raise SystemExit(f'Stale source index: {name}')
        else:path.write_text(content,encoding='utf-8')
    print('Source-link index is current.' if args.check else 'Built sources.md and machine-readable source URL inventory.')

if __name__=='__main__':main()
