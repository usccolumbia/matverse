# Specialized transport, magnetism and mechanics dataset research

Checked 2026-11-01. This is a local candidate package, not a catalog edit. `additions.json` contains twelve complete dataset-schema records. `leads.json` records added, already covered, and unresolved dispositions; title-only leads deliberately have null DOI identifiers. No publication, canonical data, UI, scripts, Git history/index or external messages were changed.

## Questions and coverage

RQ1: Which paper-backed specialized transport, magnetic and mechanical releases are missing from the current MatVerse catalog? RQ2: What is actually counted, how is origin/measurement condition represented, and what access/license can be established? RQ3: Which plausible additions would duplicate an existing release or remain too uncertain to promote?

The search perspectives were thermal/phonon transport, thermoelectric measurements and computed transport, magnetism and magnetocaloric properties, and mechanical/elastic/hardness data. Twelve actual `paper-search/scripts/search.py --sources openalex --per-source 50 --query ...` calls were retained, without final `--limit`. `query_manifest.json` lists exact queries, hit counts and network status. A highly conjunctive NEMAD/teMatDb/ESTM/Wenzhou query returned zero, so it was supplemented by broader thermoelectric curation and provider-specific follow-ups. OpenAlex is discovery metadata; counts, units, license and access were checked against author/provider sites, publisher full texts, source repositories, Zenodo and Figshare metadata. A later OpenAlex ID lookup supplements the DOI identifiers where possible.

The required Obsidian core notes and relevant AI-datasets project note were read before research. They favor preservation of provenance, clear condition/origin separation and evidence limits. No vault changes were necessary for this research-only subtask.

## Proposed records and comparison

| Candidate | Catalog counting unit | Useful distinction / evidence limit |
|---|---:|---|
| NEMAD magnetic | 67,573 paper-release entries | Curie–Néel temperatures plus coercivity, moment and magnetization metadata; not merely another copy of the CDE transition-temperature release. Full-site data license unknown. |
| NEMAD thermoelectric | 7,123 compound entries | A separate mixed experimental/computed corpus on the same platform (approximately 66% experimental), with property-specific temperatures. Full live export and licensing unverified. |
| teMatDb272 | 272 curated sample curve sets | Self-consistent ZT filtering; 355 raw sets and 14,717 temperature-property pairs are separate units. Deposit CC BY 4.0. |
| ESTM / SIMD | 5,205 composition-temperature observations | Actual XLSX downloaded and shape/units checked; 880 material identities reported by paper. ESTM is separate from the repository's Starrydata slice. No dataset license verified. |
| WenzhouTE | 3,607 calculated materials on live homepage | Adds approximate transport/thermomechanical computations for MP identities. Slack lattice conductivity must not be merged with anharmonic-BTE conductivity as equivalent evidence. |
| HH130 | 130 half-Heusler compounds | Contains 31,891 configurations and 390 specialized MLIPs; thermal-transport analysis covers only 80 compounds. Provider HTTP 502 in this audit; publication release is verified. |
| DAX-Ti | 282 alloy entries | Room-temperature Young modulus, strength, hardness, strain, phases and processing; Zenodo static-0.1.0 CC BY 4.0. |
| Gorsse Cu alloys | 1,831 observation records | Approximately 150 compositions but many processing states; dataset CC0, unlike paper CC BY. |
| Cu-Cr-X figure extraction | 3,018 observation records | Independent extraction release; potential source overlap with Cu-alloy compilation. Figshare v2 CC BY 4.0. |
| polyVERSE load-hardness | 2,480 composition-load observations | CSV row count checked; measured load explicitly retained. Custom GTRC license and inconsistent GPa/MPa wording require care. |
| LLM magnetocaloric database | 6,614 current raw CSV rows | Paper says 6,615; current MP-linked human-corrected CSV has 714 rows, not paper's 752. Field-dependent extracted values and scaled 5 T training targets differ. |
| FatigueData-CMA2022 | 272 test-condition datasets | Curves with processing/load/environment metadata; contains both metallic glasses and crystalline MPEAs. Figshare v2 CC BY 4.0. |

Distinct release does not mean disjoint measurements or novel materials. NEMAD magnetic has a separate author/provider extraction lineage from Court/Cole CDE/Snowball Curie–Néel corpora. Its structural and broader magnetic features make it independently useful, but overlapping source articles and repeated measurements are likely. No shared-source equivalence or row-level novelty was established. The same caution applies to thermoelectric releases against CDE and Starrydata, and between the two copper-alloy compilations. All sources should be linked and deduplicated by source DOI, material/sample, processing and condition before aggregation.

## Counts, conditions and uncertainty that should survive integration

WenzhouTE's homepage reports 1,915 + 1,692 = 3,607 calculated materials. Its paper text instead reports 1,915 + 1,656 = 3,571 screened materials. The candidate explicitly uses the dated homepage cohort, includes the arithmetic and reports the discrepancy. This is not a manually resolved correction to the publication.

The MCE filename `modified6125.csv` is not an authoritative count. Parsing the fetched CSV with Python's CSV reader gave 6,614 data rows excluding its header; the paper describes 6,615. Likewise, `725.csv` and `725_updated.csv` currently each have 714 data rows, whereas the paper describes 752 matched materials. These units are retained rather than silently substituted. Raw magnetic fields are strings with T/kOe/range values. The paper's maximum-per-material values after linear scaling to 5 T are derived machine-learning targets. They cannot be represented as a uniform collection of measurements made at 5 T.

The hardness CSV has exactly 2,480 data rows and contains composition, load, hardness, category and type. It does not carry units in the column names. The paper abstract reports GPa while a later conclusion gives MPa. The proposed row preserves that ambiguity rather than applying a guessed conversion. The repository LICENSE expressly covers code, data and documentation; it is a custom GTRC license with redistribution/modification conditions and restrictions on commercial-gain sale. It is not CC BY or an unrestricted open-data license. Computed semiempirical hardness records in the repository are separate from the cataloged experimental file.

For FatigueData-CMA2022, preserve material class because metallic glasses are outside a crystalline-only subset. Authors insert default assumptions when the source does not specify the environment: uniaxial, 25 °C in air and Kt=1. These assumptions must be labeled as imputations. Similarly, crystallographic descriptors in NEMAD and phase labels in alloy compilations do not establish a complete periodic atomic structure. The schema records these tables conservatively as composition-only unless a verified structure link/release supports more.

## Unpromoted leads and access limits

UCSB's foundational thermoelectric release, TEXplorer, the 2026 agentic thermoelectric-extraction paper, the Court/Cole MCE release, the expanded MPEA mechanical compilation, soft magnetic composites, HEA toughness and EKHI are retained in `leads.json`. Reasons include unresolved deposit routes, inconsistent counting units, unverified license or adjacent material-state scope. These leads are not assertions that the release is unusable. The existing Ricci transport, MP elastic, CDE thermoelectric, Phonix and PhononDB releases were explicitly checked as duplicate exclusions.

Some direct PMC requests returned a JavaScript browser-check page with HTTP 200. Those raw responses were preserved but are not evidence of article content. Author-submitted full text was successfully retrieved through Europe PMC for Ti, Cu, NEMAD magnetic and WenzhouTE; the publisher/browser search supplied additional primary text. HH130 provider homepage and ZIP both returned HTTP 502. An attempted teMatDb raw CSV path returned 404; the versioned Zenodo metadata and README are valid evidence, but a common stored-unit convention for all curves was not verified. These failed checks are recorded, not treated as confirmed downloads. No access credentials were read or saved.

`primary/` preserves fetched metadata, selected source files, source text and access receipts. The downloaded ESTM sheet and experimental-hardness/MCE CSV snapshots support the direct row-count checks. `receipt.json` inventories hashes and validation status for this package. Dataset-scale archives were not downloaded; this is a discovery and metadata audit, not scientific reproduction or row-level data validation.
