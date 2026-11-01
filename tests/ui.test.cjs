const test=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const ui=require('../web/app.js');
const datasets=JSON.parse(fs.readFileSync('data/datasets.json','utf8'));
const resources=JSON.parse(fs.readFileSync('data/resources.json','utf8'));
const categories=JSON.parse(fs.readFileSync('data/summary.json','utf8')).categories;
const filter=patch=>ui.filterDatasets(datasets,{...ui.DEFAULT_STATE,...patch},categories);
const inventory=JSON.parse(fs.readFileSync('data/collection_entries.json','utf8'));
const entryFilter=patch=>ui.filterSourceEntries(inventory.entries,{...ui.DEFAULT_STATE,...patch});
test('every imported occurrence preserves its original collection, label, URL and section',()=>{
 assert.equal(new Set(inventory.entries.map(e=>e.id)).size,inventory.entries.length);
 const sourceIndex=new Set(JSON.parse(fs.readFileSync('data/source_links.json','utf8')).sources.map(s=>s.url));
 const sourceMarkdown=fs.readFileSync('sources.md','utf8');
 for(const c of inventory.collections){
  const original=JSON.parse(fs.readFileSync(c.inventory_file,'utf8')).links;
  const actual=entryFilter({collection:c.id});assert.equal(actual.length,original.length);
  original.forEach((e,i)=>{
   assert.equal(actual[i].url,e.url);assert.equal(actual[i].label,e.label||e.url);
   assert.equal(actual[i].section,Array.isArray(e.section)?e.section.join(' / '):e.section||'Not recorded');
   assert.equal(actual[i].scope,e.scope||'uncertain');
   assert.ok(sourceIndex.has(e.url));assert.ok(sourceMarkdown.includes(e.url));
  });
 }
 assert.equal(entryFilter({}).length,inventory.entry_count);
});
test('both requested GitHub lists are complete and independently filterable',()=>{
 assert.equal(entryFilter({collection:'blaiszik'}).length,274);
 assert.equal(entryFilter({collection:'sedaoturak'}).length,90);
 const requested=inventory.entries.filter(e=>['blaiszik','sedaoturak'].includes(e.collection));
 assert.equal(new Set(requested.map(e=>e.url)).size,296);
});
test('source-entry search combines collection and scope and searches original sections',()=>{
 const rows=entryFilter({collection:'sedaoturak',scope:'crystal_related',q:'materials'});
 assert.ok(rows.length>0);assert.ok(rows.every(e=>e.collection==='sedaoturak'&&e.scope==='crystal_related'&&ui.matchesQuery(e,'materials')));
 assert.ok(entryFilter({collection:'blaiszik',q:'BOOM'}).some(e=>e.url==='https://github.com/FLASK-LLNL/BOOM'));
 const sectionOnly={...inventory.entries[0],label:'Example',url:'https://example.org',collection_name:'Example collection',section:'Special handbook section'};
 assert.equal(ui.filterSourceEntries([sectionOnly],{...ui.DEFAULT_STATE,q:'"special handbook"'}).length,1);
 assert.equal(entryFilter({q:'no_such_matverse_source_entry_0294'}).length,0);
});
test('source CSV retains original labels, URLs and collection provenance',()=>{
 const rows=entryFilter({collection:'blaiszik',q:'BOOM'}),csv=ui.csvFor(rows,'sources');
 assert.ok(csv.includes('"collection_name"'));assert.ok(csv.includes('"section"'));
 for(const r of rows){assert.ok(csv.includes(r.url));assert.ok(csv.includes(r.collection_name));}
});
test('all catalog releases remain discoverable',()=>assert.equal(filter({}).length,datasets.length));
test('provider and dataset names search regardless of case and punctuation',()=>{
 assert.ok(filter({q:'LEMAT-TRAJ'}).some(d=>d.id==='lemat-traj'));
 assert.ok(filter({q:'LeMaterial'}).some(d=>d.id==='lemat-traj'));
});
test('multiple search terms must match; quotes retain phrases',()=>{
 const rows=filter({q:'"band gap" DFT'});assert.ok(rows.length>0);assert.ok(rows.every(d=>ui.matchesQuery(d,'"band gap" DFT',categories)));
 assert.equal(filter({q:'no_such_matverse_dataset_0294'}).length,0);
});
test('category and access filters combine',()=>{
 const rows=filter({category:'bulk_computed',access:'open'});assert.ok(rows.length>0);assert.ok(rows.every(d=>d.category==='bulk_computed'&&d.access==='open'));
});
test('configuration filtering preserves the frame/material distinction',()=>{
 const rows=filter({unit:'configurations'});assert.ok(rows.some(d=>d.id==='mptrj'));assert.ok(!rows.some(d=>d.id==='materials-project'));
});
test('unknown sizes have a dedicated filter',()=>{
 const rows=filter({unit:'unknown'});assert.equal(rows.length,datasets.filter(d=>d.count===null).length);assert.ok(rows.length>0);
});
test('numeric sort keeps unranked entries last in either direction',()=>{
 for(const sort of ['largest','smallest']){
  const rows=filter({sort});const known=rows.filter(d=>d.count!==null);assert.ok(rows.slice(known.length).every(d=>d.count===null));
  for(let i=1;i<known.length;i++)assert.ok(sort==='largest'?known[i-1].count>=known[i].count:known[i-1].count<=known[i].count);
 }
});
test('default view sorts by category and descending volume',()=>{
 const rows=filter({});const ranks=Object.keys(categories);
 for(let i=1;i<rows.length;i++){
  assert.ok(ranks.indexOf(rows[i-1].category)<=ranks.indexOf(rows[i].category));
  if(rows[i-1].category===rows[i].category&&rows[i].count!==null)assert.ok(rows[i-1].count>=rows[i].count);
 }
});
test('license filter distinguishes documented terms from gaps',()=>{
 assert.ok(filter({license:'unknown'}).length>0);
 assert.ok(filter({license:'documented'}).every(d=>!ui.licenseUnknown(d)));
});
test('resource directory is searchable separately',()=>assert.ok(ui.filterResources(resources,{q:'NOMAD'}).some(d=>d.name.includes('NOMAD'))));
test('CSV preserves null counts, multiline text and quoted source JSON',()=>{
 const csv=ui.csvFor([{id:'test',name:'a,"b"\nc',count:null,sources:[{url:'https://example.org'}]}]);
 assert.ok(csv.startsWith('\uFEFF'));assert.ok(csv.includes('"a,""b""\nc"'));assert.ok(csv.includes('https://example.org'));
 assert.ok(ui.csvFor([{name:'=1+1'}]).includes("'=1+1"));
});
test('rendered content escapes markup and labels count precision',()=>{
 assert.equal(ui.escapeHTML('<img src=x onerror=alert(1)>'),'&lt;img src=x onerror=alert(1)&gt;');
 assert.equal(ui.formatCount({count:null}),'Unranked');
 assert.equal(ui.formatCount({count:1000,count_precision:'approximate'}),'~1,000');
 assert.equal(ui.formatCount({count:1000,count_precision:'lower_bound'}),'≥1,000');
});
test('every Starrydata project is searchable with three direct file links',()=>{
 const projects=datasets.filter(d=>d.tags.includes('project-subset')&&d.tags.includes('Starrydata'));
 const manifest=JSON.parse(fs.readFileSync('data/starrydata_files.json','utf8'));
 assert.equal(projects.length,Object.keys(manifest.project_counts).length);
 assert.equal(projects.length,14);assert.equal(manifest.files.length,45);
 const rows=filter({q:'Starrydata project-subset'});assert.ok(projects.every(p=>rows.some(d=>d.id===p.id)));
 for(const p of projects){for(const k of ['papers','samples','curves'])assert.ok(p.links[k].endsWith('.csv.gz'));assert.equal(p.count_unit,'samples');}
});
