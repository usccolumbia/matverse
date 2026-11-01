# Research provenance

`data/datasets.json` is the maintained catalog. The four perspective JSON files and companion notes in this folder preserve the initial 2026-11-01 research staging; later integration corrections and normalized fields live in the maintained catalog. They should not be used to regenerate current records automatically.

- `BRIEF.md`: research questions and boundaries.
- `search_log.json`: perspective query summaries and limitations.
- `source_fetch_manifest.json`: selected source-document fetch statuses, timestamps, byte counts and SHA-256 hashes; unsuccessful probes are retained as unsuccessful probes.
- `provenance/`: source response receipts, count arithmetic, file inventories and selected rights audits. These do not contain dataset payloads or complete third-party articles.
- `core_sources*.json`: public URL lists used for initial documentation probes, including failed or superseded routes.
- `fetch_sources.py`: small-document fetch helper; full responses remain in an ignored local cache.

The original research caches under `cache/` and `evidence-*/` are ignored by Git. Some raw responses were retained in a separate local temporary cache during research. Source receipts identify the exact public documents read; a response hash does not itself validate the scientific content. A documentation check is not an end-to-end download or independent audit of every data row.

The [methods](../docs/METHODOLOGY.md) describe count interpretation and maintenance. The generated [catalog manifest](../data/catalog_manifest.json) hashes the maintained catalog inputs and rendered outputs. No credentials or private authentication material are needed to rebuild the catalog views.
