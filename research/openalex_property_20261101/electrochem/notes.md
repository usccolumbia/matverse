# Electrochemical and ionic-transport property dataset survey

Verified 2026-11-01. Local research artifacts only; canonical catalog, application files and Git were not edited.

## Research brief and coverage

RQ1: Which reusable solid-electrolyte, battery-electrode and ionic-transport datasets provide specialized properties beyond broad crystal-energy databases? RQ2: What is actually counted and how much atomic structure is available? RQ3: Which collections overlap, and which claimed database releases remain unverified?

The perspectives were expert-curated experimental conductivity, automated extraction, battery electrode properties, vacancy/solute diffusion, migration-path barriers, and adjacent liquid electrolyte experiments. Perspectives ran serially within this subtask; no extra agents were spawned. Discovery used the required real `paper-search/scripts/search.py --sources openalex --per-source 50 --query ...` calls, without a final `--limit`. The configured default cache directory was unwritable; successful runs used a temporary `PAPER_CACHE_DIR`, without changing the script.

| Receipt | Query | Raw hits | Returned after within-query dedup |
|---|---|---:|---:|
| 01 | solid electrolyte ionic conductivity database | 50 | 50 |
| 02 | battery electrode materials property dataset | 50 | 50 |
| 03 | experimental ionic conductivity database lithium | 50 | 50 |
| 04 | diffusion coefficient materials dataset | 50 | 50 |
| 05 | diffusion database dilute solute materials | 50 | 50 |
| 06 | battery electrolyte conductivity dataset CALiSol | 10 | 10 |
| 07 | ionic migration barriers dataset | 50 | 49 |
| 08 | conductivity electrolyte formulations experiments | 50 | 50 |
| 09 | solid electrolyte conductivity dataset Laskowski | 50 | 50 |

Total: **410 raw hits, 409 returned records, 381 DOI/title-deduplicated discovery records**. These are received-result counts, not all OpenAlex matching works or all possible datasets. Forty-two dataset-related candidates/companions and explicitly screened false positives are in `leads.json`; 35 have retrieved OpenAlex IDs. Ten distinct releases have full schema records in `additions.json`. Some candidate rows are versions or publications for the same added release and must not be counted as independent databases. Source metadata is in `candidate_metadata.json`; query coverage/status/advisories are retained in `query_receipts.json` and original outputs.

OpenAlex was the only automated scholarly discovery source. Primary publisher/provider/repository pages and machine-readable metadata were used to verify additions. Crossref, Semantic Scholar, arXiv APIs and Chinese databases were not separately searched. **英文库没检索到 ≠ 没人研究过**. English-index retrieval and a 50-result cap per query cannot establish an exhaustive research census or absence of Chinese-language releases. High-precision follow-ups and provider-link snowballing supplemented discovery; citation counts were not used for ranking.

## Verified additions and distinctions

| Dataset | Count and structure granularity | Why it is distinct |
|---|---|---|
| [OBELiX](https://github.com/NRC-Mila/OBELiX) | 599 measured entries, 321 CIFs | Room-temperature benchmark with explicit structure-match provenance; overlaps Liverpool/Laskowski. |
| [Liverpool Ionics](https://www.nature.com/articles/s41524-022-00951-z?error=cookies_not_supported) | 820 measurements; 403 near-room-temperature compositions | Expert ACIS curation, structural-family labels; not a full coordinate collection. |
| [Caltech structure–conductivity](https://data.caltech.edu/records/23mvv-6gk43) | 571 experimental compounds | ICSD identifier joins, CC0 metadata; model predictions are a separate CSV. |
| [Shon–Min extraction](https://github.com/shonyeajin/Ionical_conductivity_database) | 4,924 extracted records | Extends CDE battery corpus with ionic-conductivity parsing; not equivalently validated to expert datasets. |
| [UW CMG diffusion](https://doi.org/10.6084/m9.figshare.1546772.v10) | >400 host–solute systems | Computed Arrhenius/jump parameters, expanded from original six-host study. |
| [Fluoride electrode pairs](https://doi.org/10.6084/m9.figshare.c.6231423.v1) | 807 reaction pairs | Voltage/capacity/energy labels with MP parent IDs; 168 direct pairs overlap. |
| [Migration barriers archive](https://doi.org/10.5281/zenodo.17240095) | 621 pathways | Periodic endpoints and literature DFT-NEB labels; live GitHub has 619. |
| [Sodium polyanion cathodes](https://doi.org/10.11583/DTU.27202446.v5) | 298,144 configurations | Energy/forces/moments; 113,532 have Bader charges. Four structure families, not 298,144 compounds. |
| [Oxygen migration perovskites](https://doi.org/10.6084/m9.figshare.7180817.v2) | >40 perovskites | Oxygen vacancy barriers and descriptors, archived workbook/raw calculations. |
| [Materials Cloud FPMD screen](https://archive.materialscloud.org/records/5zenj-34e64) | Exact released-system count unknown | FPMD trajectories, periodic structures and one complete AiiDA provenance example; ~60 shortlisted candidates described. |

Atomic-coordinate coverage determines which models can use a dataset. The two coordinate-rich migration/FPMD releases support path- or trajectory-based learning, whereas Liverpool and the text-mined collection primarily support composition/family models. OBELiX bridges these approaches with partial CIF coverage. Caltech and the fluoride pairs link structural identities without establishing open redistribution rights for every upstream coordinate file. The sodium release addresses a different target—potential-energy surfaces and charge response—so its frame count cannot be compared as a material-count advantage over experimental conductivity data.

## Critical reconciliations and evidence limits

**Liverpool counts and publication year.** The article was published 16 January 2023 despite its DOI containing 2022. Its 434 measured plus 31 extrapolated room-temperature entries are 465 records covering 403 compositions. The Foundry 372-row derivative is recorded as a lead/subset rather than a second independent addition. Provider terms require a licence for commercial extraction/reutilisation. The provider endpoint failed local certificate verification, while the publisher full text and indexed provider statement supplied count/terms evidence.

**Migration versions.** The Zenodo payload contains exactly 621 entries and matches `md5:878646be7126dd30175576a494b726b4`, declared by its metadata. The live GitHub payload contains 619. The [2025 data descriptor](https://doi.org/10.1038/s41597-025-06196-x) reports 443 compositions; this is its published convention, not an independent composition-standardization audit. The 2026 model paper uses the 619-entry variant. Saved payloads preserve this discrepancy rather than silently combining them.

**Experimental versus computed versus extracted.** Published or text-extracted values are not interchangeable with measured values independently validated against source papers. Shon–Min's extraction has explicitly limited coverage of reference materials, and the full extracted corpus is not proved entirely crystalline. Calculated migration barriers are not direct conductivity measurements. A lower barrier alone does not demonstrate a physically stable, synthesizable electrolyte or electrochemical compatibility.

**Overlaps.** DigBat/DDSE, CDE-battery-2020 and Starrydata battery subsets already exist locally and are not re-added. OBELiX explicitly cross-references Liverpool and Laskowski. Caltech shares Laskowski lineage. UW CMG overlaps the existing MAST-ML educational slice. Fluoride reaction labels derive from Simmate/MP. Sodium Combined.xyz and per-family files overlap. These resources should not be summed into a total number of unique materials.

**Large archives.** Only the ~9 MB migration payloads were downloaded and counted. Sodium XYZ archives, the 4.19 GB perovskite raw archive and 16.4 GiB FPMD release were verified from primary metadata/file manifests, not independently processed. The Materials Cloud README confirms that full screening provenance is supplied only for Li7NbO6; every screened structure does not have a full provenance archive in the release.

## Adjacent resources and unresolved leads

[CALiSol-23](https://pmc.ncbi.nlm.nih.gov/articles/PMC11237020/) has 13,825 liquid electrolyte measurement points from 27 papers and [KIT's 5,035 experiments](https://zenodo.org/records/7244939) has an openly licensed CSV. Both are useful ionic-transport resources but remain **leads** because this catalog expansion concerns crystalline materials. Their measurement/temperature rows are not crystal counts.

A [2026 Li/Na CHGNet-NEB database](https://cpb.cpsjournals.org/EN/10.1088/1674-1056/ae88e2) reports 6,928 materials and 20,320 paths, but a public reusable data package and licence were not resolved. A >400 inorganic/polymer-composite SSE database, the original Laskowski 1,346-record table, Mg23-element mobility assessment and Ni26-system diffusion/creep descriptor remain explicit leads pending release/version checks. Biomedical diffusion/imaging false positives are retained with exclusion reasons. These unresolved entries are not evidence that data do not exist.

## Deliverables and verification

`additions.json` passed the project's `data/dataset.schema.json` using jsonschema. `leads.json` retains DOI, retrieved OpenAlex ID where available, treatment and evidence. `manifest.json` preserves SHA-256 and byte sizes of local receipts, metadata and payloads; it is refreshed after report completion. No source counts or paper metadata were supplied from memory.
