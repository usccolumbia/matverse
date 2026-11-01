# Research provenance

The [OpenAlex specialized-property expansion](openalex_property_20261101/BRIEF.md) preserves a [42-run search/traversal manifest](openalex_property_20261101/search_manifest.json), normalized work ledger, independent perspective notes and source/count receipts. Raw primary-source bodies, dataset payloads and SQLite caches remain ignored. The maintained catalog integrates 35 additions and an expanded DDSE/DigBat lineage record; staging JSON is historical input, not an automatic replacement for current canonical metadata.

`data/datasets.json` is the maintained catalog. The four perspective JSON files and companion notes in this folder preserve the initial 2026-11-01 research staging; later integration corrections and normalized fields live in the maintained catalog. They should not be used to regenerate current records automatically.

- `BRIEF.md`: research questions and boundaries.
- `search_log.json`: perspective query summaries and limitations.
- `source_fetch_manifest.json`: selected source-document fetch statuses, timestamps, byte counts and SHA-256 hashes; unsuccessful probes are retained as unsuccessful probes.
- `provenance/`: source response receipts, count arithmetic, file inventories and selected rights audits. These do not contain dataset payloads or complete third-party articles.
- `core_sources*.json`: public URL lists used for initial documentation probes, including failed or superseded routes.
- `fetch_sources.py`: small-document fetch helper; full responses remain in an ignored local cache.

The original research caches under `cache/` and `evidence-*/` are ignored by Git. Some raw responses were retained in a separate local temporary cache during research. Source receipts identify the exact public documents read; a response hash does not itself validate the scientific content. A documentation check is not an end-to-end download or independent audit of every data row.

The [methods](../docs/METHODOLOGY.md) describe count interpretation and maintenance. The generated [catalog manifest](../data/catalog_manifest.json) hashes the maintained catalog inputs and rendered outputs. No credentials or private authentication material are needed to rebuild the catalog views.

The [JARVIS inventory](collection_jarvis_databases.json) freezes 13 homepage rows, 65 documentation entries and 66 downloader names (82 combined occurrences, including four registry-only names). The [API probe receipts](provenance/api_probes_20261101.json) preserve bounded public requests and distinguish record retrieval from metadata, empty responses and access failures. [Provider discovery and archive receipts](provenance/optimade_discovery_20261101.json) also record bounded binary archive prefixes; incomplete prefixes were not used to infer row counts. Only the complete small interface and vacancy ZIPs were independently counted. No downloaded source code was executed.

The [Scientific Data journal survey](sdata_20261101/README.md) preserves a complete 9,304-record Crossref journal metadata snapshot, 1,514 broad title candidates and three topical primary-source audits plus a final coverage pass, integrating 90 new records. [The collection inventory](collection_sdata_20261101.json) separates verified catalog mappings from unresolved bibliographic leads. Full pagination is not a claim of complete publisher indexing or full-text review of every candidate.

The [additional-materials search](additional_20261101/README.md) integrates 50 further releases from four topical research packages, with count/rights/lineage qualifications and source-entry dispositions. It also records corrections to 23 misparsed journal-import years and a compact local search-page header.


## November 1 property and source-list extensions

- [MateriaViva property tables](materiaviva_properties_20261101/integration_receipt.json): all148 pinned property manifests and56 original source IDs, separately searchable with direct/indirect routes. [Payload checks](materiaviva_properties_20261101/sample_verification.json).
- [Data.gov attachment](datagov_20261101/integration_receipt.json):320 parsed result occurrences;8new datasets,18resources, public SRD81API. Primary audits cover the shortlist, notall2469searchresults.
- [Matbench Discovery directory](matbench_coverage_20261101/audit.json):46displayed rows/registry entries,13new named datasets/releases and8resources. Family mappings retain unresolved exactrelease boundaries.
