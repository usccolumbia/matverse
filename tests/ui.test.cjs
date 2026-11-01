const test=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const ui=require('../web/app.js');
const datasets=JSON.parse(fs.readFileSync('data/datasets.json','utf8'));
const resources=JSON.parse(fs.readFileSync('data/resources.json','utf8'));
const apiSources=JSON.parse(fs.readFileSync('data/api_sources.json','utf8'));
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
test('superconductor terminology variants all find both 3DSC structure datasets',()=>{
 for(const q of ['superconductor','superconductors','superconductivity','superconducting','SuperCon','3DSC']){
  const ids=filter({q}).map(d=>d.id);
  assert.ok(ids.includes('3dsc-mp'),q+' misses 3DSC_MP');assert.ok(ids.includes('3dsc-icsd'),q+' misses 3DSC_ICSD');
 }
 assert.ok(filter({q:'"critical temperature" 3DSC'}).some(d=>d.id==='3dsc-mp'));
 assert.ok(filter({q:'critical temperature 3DSC'}).some(d=>d.id==='3dsc-mp'));
 assert.ok(filter({q:'Tc 3DSC'}).some(d=>d.id==='3dsc-mp'));
 assert.ok(ui.matchesQuery({properties:['critical temperature']},'temperature'));
 assert.ok(!ui.matchesQuery({url:'https://example.org/scratch'},'Tc'));
 assert.ok(!ui.matchesQuery({name:'semiconductor crystals'},'superconductor'));
});
test('global search exposes 3DSC even when a selected source collection has no 3DSC entry',()=>{
 const scoped={...ui.DEFAULT_STATE,view:'sources',collection:'blaiszik',scope:'crystal_related',q:'3DSC'};
 assert.equal(ui.filterSourceEntries(inventory.entries,scoped).length,0);
 const overview=ui.searchOverview({datasets,resources,categories,sourceEntries:inventory.entries},scoped.q);
 assert.ok(overview.datasets.some(d=>d.id==='3dsc-mp'));assert.ok(overview.datasets.some(d=>d.id==='3dsc-icsd'));
 const opened=ui.globalSearchState(scoped.q,'datasets');
 assert.equal(opened.collection,'');assert.equal(opened.scope,'');assert.equal(opened.q,'3DSC');
 assert.ok(ui.filterDatasets(datasets,opened,categories).some(d=>d.id==='3dsc-mp'));
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
test('NOMAD has a main dataset result linked to its API with an explicit bulk-entry denominator',()=>{
 for(const q of ['NOMAD','FAIRmat','novel materials discovery']){
  assert.ok(filter({q}).some(d=>d.id==='nomad-bulk'),q+' misses the NOMAD dataset');
 }
 const record=datasets.find(d=>d.id==='nomad-bulk');
 const receipt=JSON.parse(fs.readFileSync('research/nomad_20261101/bulk-response.json','utf8'));
 assert.equal(record.count,receipt.pagination.total);
 assert.equal(record.count_unit,'public bulk-crystal archive entries');
 assert.ok(apiSources.find(a=>a.id==='nomad-native').catalog_ids.includes(record.id));
});
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
test('API search combines interface and authentication and remains visible in global search',()=>{
 const state={...ui.DEFAULT_STATE,view:'apis',q:'Materials Project',api_kind:'native_api',api_auth:'api_key'};
 const native=ui.filterAPIs(apiSources,state);
 assert.deepEqual(native.map(r=>r.id),['mp-native']);
 const standard=ui.filterAPIs(apiSources,{...state,api_kind:'optimade',api_auth:'none'});
 assert.ok(standard.some(r=>r.id==='mp-optimade'));
 assert.equal(ui.filterAPIs(apiSources,{...state,q:'not_a_real_provider_293'}).length,0);
 const global=ui.searchOverview({datasets,resources,categories,sourceEntries:inventory.entries,apiSources},'OPTIMADE');
 assert.ok(global.apis.some(r=>r.id==='jarvis-optimade'));
 assert.ok(global.apis.some(r=>r.id==='mp-optimade'));
 const cleared=ui.globalSearchState(state.q,'apis');assert.equal(cleared.api_auth,'');assert.equal(cleared.api_kind,'');
});
test('API exports preserve authentication, verification limits and source evidence',()=>{
 const rows=ui.filterAPIs(apiSources,{...ui.DEFAULT_STATE,q:'JARVIS'});
 const csv=ui.csvFor(rows,'apis');
 for(const field of ['entrypoint','auth','auth_notes','verification','sources','limitations'])assert.ok(csv.includes('"'+field+'"'));
 const jarvis=rows.find(r=>r.id==='jarvis-optimade');
 assert.equal(jarvis.verification.status,'empty_response');
 assert.ok(csv.includes('empty_response'));assert.ok(csv.includes(jarvis.entrypoint));
 assert.equal(apiSources.find(r=>r.id==='mp-native').verification.status,'auth_required');
 assert.equal(apiSources.find(r=>r.id==='huggingface').verification.status,'metadata_verified');
});
test('JARVIS inventory covers every homepage row, documented release and downloader name',()=>{
 const c=JSON.parse(fs.readFileSync('research/collection_jarvis_databases.json','utf8'));
 const home=c.links.filter(e=>e.section==='JARVIS homepage / Databases');
 const docs=c.links.filter(e=>e.section==='JARVIS-Tools / Figshare based databases');
 assert.equal(home.length,13);assert.equal(docs.length,65);
 assert.deepEqual(home.map(e=>Number(e.label.split('.')[0])),[1,2,3,4,5,6,7,9,10,11,12,13,14]);
 assert.equal(new Set(c.links.filter(e=>e.registry_key).map(e=>e.registry_key)).size,66);
 assert.equal(entryFilter({collection:'jarvis_databases'}).length,c.links.length);
 for(const e of home)assert.ok((e.catalog_ids||[]).length+(e.resource_urls||[]).length>0,e.label);
 for(const name of ['stm','wtbh_electron','wtbh_phonon'])assert.equal(docs.find(e=>e.label===name).registry_key,null);
});
test('Scientific Data descriptor and new-release searches agree with the journal index',()=>{
 const journal=JSON.parse(fs.readFileSync('data/scientific_data_index.json','utf8'));
 const mapped=new Set(journal.descriptors.flatMap(d=>d.catalog_ids));
 const found=filter({q:'"Scientific-Data-descriptor"'});
 assert.equal(found.length,journal.catalog_records);
 assert.deepEqual(new Set(found.map(d=>d.id)),mapped);
 assert.equal(filter({q:'"Scientific-Data-survey-20261101"'}).length,journal.new_catalog_records);
 for(const id of ['mp-elastic-2015','mp-piezo-2015','mp-dfpt-phonons-2018','3dsc-mp','3dsc-icsd'])assert.ok(mapped.has(id));
 const sourceRows=entryFilter({collection:'sdata_20261101'});
 assert.ok(sourceRows.length>=journal.title_candidates);
 assert.ok(sourceRows.some(e=>e.section==='Unreviewed broad title candidate'&&e.scope==='uncertain'));
});

test('additional-materials search finds every integrated release while keeping model labels explicit',()=>{
 const receipt=JSON.parse(fs.readFileSync('research/additional_20261101/integration_receipt.json','utf8'));
 const rows=filter({q:'"additional-materials-20261101"'});
 assert.deepEqual(new Set(rows.map(d=>d.id)),new Set(receipt.new_dataset_ids));
 assert.ok(rows.find(d=>d.id==='solid26').count_unit.includes('configuration'));
 assert.ok(rows.find(d=>d.id==='asi-paracrystalline-models').provenance.includes('MTP'));
 assert.equal(rows.find(d=>d.id==='ultera-2025').access,'restricted');
});

test('every MateriaViva property is individually searchable with exact provenance and denominators',()=>{
 const manifest=JSON.parse(fs.readFileSync('research/materiaviva_properties_20261101/property_manifest.json','utf8'));
 const rows=filter({category:'materials_properties'});
 assert.equal(rows.length,148);
 assert.equal(rows.reduce((s,d)=>s+d.count,0),manifest.rows);
 for(const d of rows){
  const p=d.property_dataset,m=manifest.per_property[p.property_key];
  assert.equal(d.count,m.rows);assert.equal(p.structures,m.structures);assert.equal(p.unit,m.unit);assert.equal(p.value_kind,m.kind);
  assert.deepEqual(Object.fromEntries(p.upstream_sources.map(u=>[u.source_id,u.values])),m.sources);
  assert.equal(p.upstream_sources.reduce((s,u)=>s+u.values,0),d.count);
  assert.ok(filter({category:'materials_properties',q:p.property_key}).some(r=>r.id===d.id));
  assert.ok(filter({category:'materials_properties',q:d.properties[0]}).some(r=>r.id===d.id));
  assert.ok(d.links.data.includes('/resolve/'+p.revision+'/properties/'+p.property_key+'.parquet'));
  assert.equal(d.count_unit,'property values');assert.equal(d.structure_level,'structure_linked');
 }
 for(const [q,key] of [['superconductor Tc','tc-superconducting'],['ionic conductivity','ionic-conductivity'],['band gap','band-gap'],['NMR EFG','nmr-efg-max'],['SHG','shg-coefficient']]){
  assert.ok(filter({category:'materials_properties',q}).some(r=>r.id==='materiaviva-property-'+key),q);
 }
 assert.equal(filter({category:'materials_properties',q:'Matvina'}).length,148);
});

test('property access view and exports distinguish direct delivery from all upstream providers',()=>{
 const d=datasets.find(d=>d.id==='materiaviva-property-band-gap'),p=d.property_dataset;
 const html=ui.propertyAccessHTML(d);
 assert.ok(html.includes('DIRECT ACCESS SOURCE'));assert.ok(html.includes('ORIGINAL SOURCES / INDIRECT ACCESS'));
 assert.ok(html.includes(p.direct_access));assert.ok(html.includes(p.direct_download));
 for(const u of p.upstream_sources){assert.ok(html.includes(u.url.replaceAll('&','&amp;')));assert.ok(html.includes(u.values.toLocaleString('en-US')));}
 assert.equal(ui.propertyAccessHTML(datasets.find(d=>!d.property_dataset)),'');
 const csv=ui.csvFor([d]);assert.ok(csv.includes('"property_dataset"'));assert.ok(csv.includes('direct_access'));assert.ok(csv.includes('upstream_sources'));
 const escaped=ui.propertyAccessHTML({...d,property_dataset:{...p,provider:'<script>alert(1)</script>'}});
 assert.ok(!escaped.includes('<script>'));assert.ok(escaped.includes('&lt;script&gt;'));
});

test('Data.gov selection retains eight new datasets and avoids CAMEO and conditional thermoelectric double counts',()=>{
 const receipt=JSON.parse(fs.readFileSync('research/datagov_20261101/integration_receipt.json','utf8'));
 assert.equal(receipt.new_dataset_ids.length,8);
 const rows=filter({q:'Data.gov-selection-20261101'});
 assert.deepEqual(new Set(rows.map(d=>d.id)),new Set([...receipt.new_dataset_ids,...receipt.existing_selected_ids]));
 assert.ok(!datasets.some(d=>d.id==='gdr-low-temperature-thermoelectric-2016'));
 assert.ok(resources.some(r=>r.kind==='conditional thermoelectric development dataset'));
 assert.ok(apiSources.some(r=>r.id==='nist-insulation'&&r.verification.status==='sample_verified'));
 assert.equal(entryFilter({collection:'datagov_20261101'}).length,320);
});

test('Matbench directory preserves every row and separates released datasets from adjacent resources',()=>{
 const audit=JSON.parse(fs.readFileSync('research/matbench_coverage_20261101/audit.json','utf8'));
 const receipt=JSON.parse(fs.readFileSync('research/matbench_coverage_20261101/integration_receipt.json','utf8'));
 assert.equal(audit.entries.length,46);assert.equal(audit.all_keys_agree,true);
 const entries=entryFilter({collection:'matbench_discovery_20261101'});assert.equal(entries.length,46);
 const ids=new Set(datasets.map(d=>d.id));const urls=new Set(resources.map(r=>r.url));
 for(const e of audit.entries){assert.ok(entries.some(x=>x.url===e.detail_url));assert.ok(e.catalog_ids.length||e.resource_url);for(const id of e.catalog_ids)assert.ok(ids.has(id));if(e.resource_url)assert.ok(urls.has(e.resource_url));}
 assert.equal(receipt.new_dataset_ids.length,13);
 assert.equal(datasets.find(d=>d.id==='materials-project').count,271325);
 assert.equal(datasets.find(d=>d.id==='mp-frozen-2022').count,154718);
 assert.equal(datasets.find(d=>d.id==='salex-omat24-validation').count,553218);
 assert.ok(audit.important_scope_notes.Alex.includes('equilibrium'));
});
