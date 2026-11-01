const fs=require('node:fs'), {performance}=require('node:perf_hooks');
const ui=require(require('node:path').resolve(process.argv[2]||'web/app.js'));
const catalog={datasets:JSON.parse(fs.readFileSync('data/datasets.json')),resources:JSON.parse(fs.readFileSync('data/resources.json')),apiSources:JSON.parse(fs.readFileSync('data/api_sources.json')),sourceEntries:JSON.parse(fs.readFileSync('data/collection_entries.json')).entries,categories:JSON.parse(fs.readFileSync('data/summary.json')).categories};
const start=performance.now();if(ui.prepareSearchIndex)ui.prepareSearchIndex(catalog);
const indexMs=performance.now()-start;
const queries=['s','su','sup','super','superconductor','t','th','thermoelectric','N','NO','NOMAD','"Materials Project"','band gap','Tc'];
const times=[],counts=[];
for(let repeat=0;repeat<4;repeat++)for(const q of queries){const start=performance.now();const results=ui.searchOverview(catalog,q);ui.filterDatasets(catalog.datasets,{...ui.DEFAULT_STATE,q},catalog.categories);times.push(performance.now()-start);if(!repeat)counts.push(Object.values(results).map(r=>r.length));}
times.sort((a,b)=>a-b);
console.log(JSON.stringify({indexMs,medianMs:times[Math.floor(times.length/2)],p95Ms:times[Math.floor(times.length*.95)],maxMs:Math.max(...times),queries,counts},null,2));
