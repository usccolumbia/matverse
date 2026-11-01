# Search performance, 2026-11-01

Baseline: commit 8b3066c4a4f015fac468eae075cafa9e0706dcd4, 532 datasets, 103 resources, 35 API routes and 3,433 source entries. Local Node benchmark: 14 queries × 4 passes; every query runs the cross-view overview and the active dataset filter/sort. The same catalog and query sequence were used in both runs.

Median search calculation: 116.60 ms before, 4.41 ms after (26.5×). p95: 132.63 ms before, 8.51 ms after. One-time index construction: 80.12 ms. These measurements exclude browser DOM work, network loading and the 100 ms typing coalescing delay; they are not an end-to-end latency claim. Counts agree for every query. Regression tests also compare complete result identities and ordering before/after indexing, including phrases and superconductivity synonyms.

The final interface displays all matches on one page, per the user's preference. Hidden dataset detail panels are built on demand, and inactive-view DOM is cleared. No backend or search service is introduced.

Reproduce from repository root with `node scripts/benchmark_search.cjs`. To benchmark an older implementation, extract its web/app.js to a temporary .cjs file and pass that absolute path as the script argument. Raw timing/count results are in before.json and after.json.
