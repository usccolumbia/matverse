# Contributing to MatVerse

Add corrections or datasets through an issue or pull request. Prefer an official versioned release, author repository, dataset card, deposit metadata or primary data descriptor. A review or an awesome-list is a lead, not sufficient evidence for a precise count.

1. Edit `data/datasets.json`; use `data/resources.json` for repositories, portals, APIs, mirrors and adjacent resources.
2. Supply a stable slug, one category, release/version, explicit count unit/scope, access and dataset-specific license. Use `null` with precision `unknown` if size is unverified. Do not substitute byte size, atom count, paper count or force components for structure count.
3. Give an evidence URL and short paraphrase for every numeric claim. Record the check date. Distinguish reported precision from independent verification. Record arithmetic in `count_derivation`; never sum overlapping subsets.
4. State parentage, repeated releases, mixed structure availability, missing label coverage and access constraints. Keep computational, generated, MLIP-predicted and experimentally measured labels distinguishable.
5. Run `python3 scripts/build_catalog.py`, `python3 scripts/build_sources.py`, and `python3 scripts/build_site.py`. Check each with `--check`, then run `node --test tests/ui.test.cjs`. Review the Markdown, CSV and HTML changes. All source URLs belong in the generated root `sources.md`; collection inventories live under `research/collection_*.json`.

Update dates and evidence when sizes change. Retain the old release context in a caveat or changelog if the new denominator differs. The catalog's verification date is set in `scripts/build_catalog.py` and its introductory prose; update both for a new curated release. Sources in individual records retain their own dates.

Maintain API, SDK and structured-download routes in `data/api_sources.json`. Record interface type, authentication, formats, related catalog IDs, documentation and a dated verification outcome. A successful metadata response or an empty record list is not a working data-payload check. Keep small public probe receipts under `research/provenance/`; do not run credentialed probes in CI. The regular catalog/site builders validate and regenerate the API guide, JARVIS audit and searchable view.

Do not commit API keys, personal data, downloaded dataset archives or complete third-party articles. Local research caches are ignored. Record public URLs, response hashes and concise evidence instead. Linking a restricted dataset is acceptable; mirroring its content requires the applicable rights.

The catalog metadata/prose use CC BY 4.0, and the Python scripts use MIT. Contributions follow those respective terms; upstream datasets retain their original licenses. Please cite original creators in downstream research.
