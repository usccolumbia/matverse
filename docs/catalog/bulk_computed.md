# Computed bulk inorganic crystals

[Back to MatVerse](../../README.md)

Checked 2026-11-01. Counts are source-reported or explicitly derived from release metadata; full datasets were not independently deduplicated.

<a id="alexandria"></a>
## Alexandria

High-throughput inorganic structure database, with separate functional releases, trajectories and convex-hull subsets.

**Size:** ~5,800,000 DFT-relaxed structures (source wording: ~5.8 million).

**Scope:** Release described by the cited source

**Release:** 2025-07-02 PBE release, described in 2026 paper. **Year:** 2026.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** crystal structure; energy.

**Access:** open. **Dataset license:** CC BY 4.0 (provider About page).

**Official routes:** [homepage](https://alexandria.icams.rub.de/) · [data](https://alexandria.icams.rub.de/datasets.html) · [paper](https://doi.org/10.1088/2515-7639/ae6620)

**Evidence:**

- [Alexandria — primary documentation](https://doi.org/10.1088/2515-7639/ae6620) (checked 2026-11-01): 2026 expansion paper reports approximately 5.8 million structures; provider release page lists the complete PBE database dated 2025-07-02.

**Reuse and interpretation notes:**

- The figure describes a release, not a live recount or all trajectories.
- Convex-hull stability is computed relative to the reference set; synthesis and dynamical stability require separate evidence.

**Tags:** PBE, PBEsol, SCAN.

<a id="aflow"></a>
## AFLOW

High-throughput DFT library of inorganic crystals, alloys and prototype decorations.

**Size:** 3,929,948 database entries (source wording: 3,929,948).

**Scope:** Release described by the cited source

**Release:** Provider page snapshot, checked 2026-11-01. **Year:** Not verified.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** crystal structure; energy.

**Access:** open. **Dataset license:** Provider terms: free for scientific, academic and non-commercial use; other use prohibited.

**Official routes:** [homepage](https://aflow.org/) · [data](https://aflow.org/API/aflowlib_stats/) · [code](https://github.com/aflow-org/aflow)

**Evidence:**

- [AFLOW — primary documentation](https://aflow.org/API/aflowlib_stats/) (checked 2026-11-01): Live statistics response gives Aflow_DBs.total.count=3,929,948 and 205,973 chemical systems.
- [AFLOW documentation and data disclaimer](https://aflow.org/documentation/) (checked 2026-11-01): The data disclaimer limits free use to scientific, academic and non-commercial purposes.

**Reuse and interpretation notes:**

- Entries and calculated properties are different counters.
- The open-source software license is not the data license; see AFLOW API disclaimer.
- Contains hypothetical and experimentally seeded structures, with overlaps across databases.

**Tags:** None assigned.

<a id="oqmd"></a>
## OQMD

Open Quantum Materials Database of DFT thermodynamic and structural properties.

**Size:** 1,407,395 materials entries (source wording: 1,407,395).

**Scope:** Release described by the cited source

**Release:** Provider page snapshot, checked 2026-11-01. **Year:** Not verified.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** crystal structure; energy.

**Access:** open. **Dataset license:** CC BY 4.0 (OQMD download terms).

**Official routes:** [homepage](https://oqmd.org/) · [data](https://oqmd.org/download/)

**Evidence:**

- [OQMD — primary documentation](https://oqmd.org/) (checked 2026-11-01): Official homepage indexed text reports 1,407,395 materials.

**Reuse and interpretation notes:**

- Count verified in provider search-index content; direct HTTP fetch returned 502 during this audit.
- Predominantly computed entries, including prototype decorations; not a count of experimental discoveries.

**Tags:** OQDM (user-listed spelling).

<a id="jarvis-qetb"></a>
## JARVIS-QETB / TB3PY DFT database

DFT configurations used to fit periodic-table tight-binding parameters; the library mirror is a dated release.

**Size:** 829,574 DFT structure records (source wording: 829,574).

**Scope:** Selected qe_tb release; not an additive total over JARVIS or a claim about latest portal coverage

**Release:** JARVIS qe_tb documentation / pinned downloader snapshot 2026-11-01. **Year:** Not verified.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** crystal structure; DFT energy; PBEsol calculations; tight-binding training.

**Access:** open. **Dataset license:** CC BY 4.0 (Figshare deposit).

**Official routes:** [homepage](https://jarvis.nist.gov/jarvisqetb) · [code](https://github.com/usnistgov/jarvis/blob/3b0c9d0f0c15759135de857dbc93e010db01eb29/jarvis/db/figshare.py) · [data](https://ndownloader.figshare.com/files/29070555) · [release](https://doi.org/10.6084/m9.figshare.15127788) · [paper](https://doi.org/10.1103/PhysRevMaterials.7.044603)

**Evidence:**

- [JARVIS-Tools dataset table](https://pages.nist.gov/jarvis/databases/) (checked 2026-11-01): The named qe_tb row reports 829,574 data points.
- [Pinned JARVIS Figshare downloader](https://github.com/usnistgov/jarvis/blob/3b0c9d0f0c15759135de857dbc93e010db01eb29/jarvis/db/figshare.py) (checked 2026-11-01): Confirms the qe_tb route or dedicated helper and the raw-file grouping.
- [Figshare release metadata](https://api.figshare.com/v2/articles/15127788) (checked 2026-11-01): Identifies the deposited files and reports the CC BY 4.0 dataset license.
- [TB3PY primary paper](https://arxiv.org/abs/2112.11585) (checked 2026-11-01): The DFT database supplies training calculations for two- and three-body tight-binding parameters; the paper describes nearly one million calculations.

**Reuse and interpretation notes:**

- The documentation lists 829,574 data points; the homepage rounds to 800,000+ and the downloader message says 860k. These are separate source wordings, not independent structure totals.
- The web portal may require registration; the linked public file route is separate.

**Tags:** JARVIS, qe_tb, release-snapshot.

<a id="gnome"></a>
## GNoME released stable-materials set

Public structure release accompanying Graph Networks for Materials Exploration.

**Size:** ~381,000 novel structure records (source wording: ~381,000).

**Scope:** Release described by the cited source

**Release:** Public stable-materials set; June 2024 overlap update. **Year:** 2023.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** crystal structure; energy.

**Access:** open. **Dataset license:** CC BY-NC 4.0 (data); Apache 2.0 applies to code.

**Official routes:** [homepage](https://github.com/google-deepmind/materials_discovery) · [data](https://github.com/google-deepmind/materials_discovery/blob/main/DATASET.md) · [paper](https://doi.org/10.1038/s41586-023-06735-9)

**Evidence:**

- [GNoME released stable-materials set — primary documentation](https://github.com/google-deepmind/materials_discovery/blob/main/DATASET.md) (checked 2026-11-01): Author DATASET.md describes approximately 381,000 novel structures and a summary revised to reduce overlap with June 2024 external database snapshots.

**Reuse and interpretation notes:**

- Ranked by the released novel stable-materials set, not the paper headline of 2.2 million candidate crystals.
- Stability and novelty depend on the calculation protocol and reference database snapshots.
- Non-commercial data license; do not inherit the repository code license.

**Tags:** None assigned.

<a id="materials-project"></a>
## Materials Project

Structure-centered computed properties for inorganic materials with API and bulk distribution routes.

**Size:** 271,325 crystal structure records (source wording: 271,325).

**Scope:** Materials Explorer displayed structure/material records reported by the user on 2026-11-01; not distinct compositions or uniform property coverage

**Release:** Materials Explorer count reported 2026-11-01. **Year:** 2026.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** crystal structure; formation energy; electronic structure; elasticity; phase diagrams.

**Access:** registration. **Dataset license:** CC BY 4.0 for core data; GNoME-origin data carry separate BY-NC acceptance.

**Official routes:** [homepage](https://materialsproject.org/) · [data](https://docs.materialsproject.org/downloading-data) · [paper](https://doi.org/10.1063/1.4812323)

**Evidence:**

- [Materials Project Materials Explorer — current count correction](https://next-gen.materialsproject.org/materials) (checked 2026-11-01): User reports 271,325 structures displayed by Materials Explorer on 2026-11-01. This supersedes the older 200,487-entry homepage snapshot used in this catalog. Direct automated verification was blocked by HTTP 403 and a browser challenge; the live database release identifier was not confirmed.
- [Materials Project — primary documentation](https://doi.org/10.17188/1693272) (checked 2026-11-01): Historical provider homepage snapshot reported 200,487 materials and identified database v2026.04.13. Retained as provenance; superseded for the catalog's current size by the user-reported Materials Explorer count.
- [Materials Project database versions](https://docs.materialsproject.org/changes/database-versions) (checked 2026-11-01): Version history documents separate BY-NC acceptance for the GNoME dataset and changes in collection membership.

**Reuse and interpretation notes:**

- Current Explorer count supplied by the user on 2026-11-01; automated verification was blocked and the corresponding database version was not confirmed.
- Different property collections cover different subsets; molecule and electrode totals are separate.
- Track GNoME-origin licensing and database version when using API data.

**Tags:** None assigned.

<a id="carolina"></a>
## Carolina Materials Database

Generated and computationally screened inorganic crystals hosted by the Carolina Materials Database.

**Size:** 214,436 inorganic materials entries (source wording: 214,436).

**Scope:** Release described by the cited source

**Release:** Provider page snapshot, checked 2026-11-01. **Year:** Not verified.

**Provenance:** generated. **Structure availability:** `periodic_atomic`.

**Labels/content:** crystal structure; energy.

**Access:** open. **Dataset license:** CC BY 4.0 (provider Terms of Use).

**Official routes:** [homepage](http://www.carolinamatdb.org/)

**Evidence:**

- [Carolina Materials Database — primary documentation](http://www.carolinamatdb.org/) (checked 2026-11-01): Provider homepage states 214,436 inorganic materials and separately more than 250,000 calculated properties.

**Reuse and interpretation notes:**

- Generated candidates and calculated properties do not establish experimental synthesis.
- Homepage text contains typographical space-group wording; no inference about full space-group coverage is made.

**Tags:** None assigned.

<a id="pbesol-scan-175k-2022"></a>
## PBEsol/SCAN 175k crystalline-material reference cohort

Matched PBEsol-relaxed and SCAN single-point calculations with pymatgen ComputedStructureEntry records.

**Size:** ~175,000 crystalline material records (source wording: ~175,000 crystalline material records).

**Scope:** Approximate cohort size in primary descriptor; PBEsol and SCAN records describe the same materials.

**Release:** Materials Cloud 2021.164 legacy release. **Year:** 2022.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** PBEsol geometry; PBEsol energy; SCAN single-point energy; band gap.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [paper](https://doi.org/10.1038/s41597-022-01177-w) · [data](https://doi.org/10.24435/materialscloud:ka-br)

**Evidence:**

- [Scientific Data primary data descriptor](https://doi.org/10.1038/s41597-022-01177-w) (checked 2026-11-01): Matched PBEsol-relaxed and SCAN single-point calculations with pymatgen ComputedStructureEntry records. Approximate cohort size in primary descriptor; PBEsol and SCAN records describe the same materials.
- [Primary repository release metadata](https://archive.materialscloud.org/api/records/cnyp0-05c11) (checked 2026-11-01): Confirms public release files and stated dataset terms; response hashes are saved in provider receipts.

**Reuse and interpretation notes:**

- Historical functional-specific release overlaps Alexandria-family data and upstream MP/AFLOW/group calculations; not independent structure totals.
- SCAN calculations use PBEsol geometries rather than separately SCAN-relaxed structures.
- The cited 2021.164 record has a newer version; pin this legacy record for reproducibility.

**Tags:** Scientific Data, survey:20261101, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="mp-frozen-2022"></a>
## MP v2022.10.28

Entire Materials Project dataset from October 2022.

**Size:** 154,718 relaxed material entries (source wording: 154,718).

**Scope:** Frozen October28,2022 MP computed-entry archive, one distinct material ID per entry; historical snapshot, separate from current Materials Project271,325 structures.

**Release:** MP 2022 release as listed in Matbench Discovery at 8869a883a506. **Year:** 2022.

**Provenance:** DFT calculations; source-reported release metadata. **Structure availability:** `periodic_atomic`.

**Labels/content:** crystal structures; formation energies; computed entries.

**Access:** open. **Dataset license:** CC-BY-4.0 (provider/benchmark release declaration).

**Official routes:** [homepage](https://docs.materialsproject.org/changes/database-versions#v2022.10.28) · [data](https://figshare.com/files/40344436) · [paper](https://doi.org/10.1063/1.4812323)

Other denominators (not added to the ranking):

- 154,718 source-defined parent materials: Benchmark metadata denominator; see release notes for identity definition. Not added to configurations.

**Evidence:**

- [Matbench Discovery datasets table](https://matbench-discovery.materialsproject.org/data/sets) (checked 2026-11-01): Listed MP 2022: 154,718 configurations/structures; role training, created 2022-10-28, declared data license CC-BY-4.0. Counts and access refer to this listed release.
- [Pinned Matbench Discovery dataset metadata](https://github.com/janosh/matbench-discovery/blob/8869a883a5067015b815886d878bd7aaa3862d2d/data/datasets.yml) (checked 2026-11-01): Machine-readable MP 2022 entry at revision 8869a883a5067015b815886d878bd7aaa3862d2d; retains structure/material counting distinction and release caveats.
- [Matbench Discovery release metadata](https://api.figshare.com/v2/articles/22715158) (checked 2026-11-01): Archive metadata supplies the frozen MP computed-entry file; the maintained benchmark registry reports154,718 entries. Full file not recounted here.

**Reuse and interpretation notes:**

- The frozen computed-entry archive (https://figshare.com/files/40344436) contains 154,718 entries with distinct material IDs, matching the energy table (https://figshare.com/files/49083124). Each entry represents one relaxed material.
- Overlaps parent datasets and other named splits/releases; do not add these counts to independent-material totals.
- Historical subset of Materials Project; the current live database is not this frozen training release.

**Tags:** Matbench-sets-20261101, MP 2022, Matbench Discovery, training, release-subset, Matbench-Discovery-data-sets-20261101.

<a id="dxmag-heusler-quaternary"></a>
## DXMag Computational HeuslerDB — quaternary ML

Heusler-family crystal and magnetic-property release; ML-relaxed ground states with magnetic and phonon predictions.

**Size:** 131,544 provider-reported compounds (source wording: 131,544).

**Scope:** Public quaternary ML release; counts refer to compounds rather than configurations.

**Release:** CSV 2026-03-10; provider page checked 2026-11-01. **Year:** 2026.

**Provenance:** MLIP structure optimization and transfer-learned property estimates; trained on ternary Heusler DFT. **Structure availability:** `periodic_atomic`.

**Labels/content:** MLIP structures and energies; ML predicted hull distances; ML predicted magnetic moments; ML predicted minimum phonon frequency; ML predicted Curie/Néel temperatures; ML predicted magnetic anisotropy.

**Access:** open. **Dataset license:** CC BY 4.0 (explicit database declaration).

**Official routes:** [homepage](https://www.nims.go.jp/group/spintheory/database/) · [download](https://www.nims.go.jp/group/spintheory/database/DXMag_HeuslerDB_quaternary_2026-03-10.csv) · [paper](https://www.nature.com/articles/s41524-026-02013-0)

**Evidence:**

- [NIMS DXMag Computational HeuslerDB](https://www.nims.go.jp/group/spintheory/database/) (checked 2026-11-01): Lists 131,544 compounds for this family, dates the public CSV, distinguishes DFT from MLIP/regression labels, and explicitly licenses the database CC BY 4.0.
- [DXMag quaternary ML CSV](https://www.nims.go.jp/group/spintheory/database/DXMag_HeuslerDB_quaternary_2026-03-10.csv) (checked 2026-11-01): HTTP 206 sample confirms cell, positions and atomic-number columns; ML_cell, ML_e, Tc_ML, Phonon_ML, MAE_ML and moment fields.

**Reuse and interpretation notes:**

- The count is the provider compound denominator, not the number of magnetic/structural calculations or property values.
- CSV headers and representative coordinate-bearing records were checked using a 64 KiB HTTP range; the full CSV was not independently recounted.
- Property values are model predictions; they are not fresh DFT calculations or experimental verification.
- Separate composition-family release from the ternary DFT training domain; possible structures shared with other catalogs have not been deduplicated.

**Tags:** heusler, magnetism, quaternary, ml-predictions, additional-materials-20261101.

<a id="dxmag-heusler-ternary"></a>
## DXMag Computational HeuslerDB — ternary DFT

Heusler-family crystal and magnetic-property release; DFT configurations for ternary compounds.

**Size:** 106,235 DFT calculation rows (source wording: 106,235).

**Scope:** Public 2026-09-16 CSV rows; magnetic and structural variants are separate entries, not unique compounds.

**Release:** CSV 2026-09-16; provider page checked 2026-11-01. **Year:** 2025.

**Provenance:** DFT (PBE), multiple structural and magnetic configurations. **Structure availability:** `periodic_atomic`.

**Labels/content:** relaxed structures; formation energies and hull distances; magnetic moments; phonons for a subset; KKR Curie/Néel temperature estimates for a subset.

**Access:** open. **Dataset license:** CC BY 4.0 (explicit database declaration).

**Official routes:** [homepage](https://www.nims.go.jp/group/spintheory/database/) · [download](https://www.nims.go.jp/group/spintheory/database/DXMag_HeuslerDB_2026-09-16.csv) · [paper](https://doi.org/10.1016/j.actamat.2025.121312)

Other denominators (not added to the ranking):

- 27,864 provider-reported compounds: Provider family-level denominator; not reconciled to the public CSV calculation rows or literal composition strings.
- 18,792 distinct literal composition strings: Derived from the public CSV composition column; no chemical reduction or structural deduplication.

**Evidence:**

- [NIMS DXMag Computational HeuslerDB](https://www.nims.go.jp/group/spintheory/database/) (checked 2026-11-01): Provider lists 27,864 ternary compounds and more than 100,000 structural/magnetic entries, dates the public CSV and explicitly licenses the database CC BY 4.0.
- [DXMag ternary DFT CSV](https://www.nims.go.jp/group/spintheory/database/DXMag_HeuslerDB_2026-09-16.csv) (checked 2026-11-01): Complete CSV independently contains 106,235 rows with unique UUIDs and populated cell, positions and atomic-number columns; 18,792 distinct literal composition strings. SHA-256 preserved.

**Reuse and interpretation notes:**

- 106,235 counts structural/magnetic calculation rows; it is not a unique-compound count.
- Provider reports 27,864 compounds, while the public file has 18,792 literal composition strings; these denominators were not reconciled or chemically deduplicated.
- Phonon, band/DOS and ordering-temperature coverage are subsets; they do not add unique structures.
- Anomalous Hall/Nernst columns are currently omitted from the public CSV; the web dashboard is NIMS-network only.

**Tags:** heusler, magnetism, ternary, dft, additional-materials-20261101.

<a id="dxmag-heusler-alld"></a>
## DXMag Computational HeuslerDB — all-d ML

Heusler-family crystal and magnetic-property release; ML-relaxed ground states with magnetic and phonon predictions.

**Size:** 105,763 provider-reported compounds (source wording: 105,763).

**Scope:** Public all-d ML release; counts refer to compounds rather than configurations.

**Release:** CSV 2026-03-10; provider page checked 2026-11-01. **Year:** 2026.

**Provenance:** MLIP structure optimization and transfer-learned property estimates; trained on ternary Heusler DFT. **Structure availability:** `periodic_atomic`.

**Labels/content:** MLIP structures and energies; ML predicted hull distances; ML predicted magnetic moments; ML predicted minimum phonon frequency; ML predicted Curie/Néel temperatures; ML predicted magnetic anisotropy.

**Access:** open. **Dataset license:** CC BY 4.0 (explicit database declaration).

**Official routes:** [homepage](https://www.nims.go.jp/group/spintheory/database/) · [download](https://www.nims.go.jp/group/spintheory/database/DXMag_HeuslerDB_alld_2026-03-10.csv) · [paper](https://www.nature.com/articles/s41524-026-02013-0)

**Evidence:**

- [NIMS DXMag Computational HeuslerDB](https://www.nims.go.jp/group/spintheory/database/) (checked 2026-11-01): Lists 105,763 compounds for this family, dates the public CSV, distinguishes DFT from MLIP/regression labels, and explicitly licenses the database CC BY 4.0.
- [DXMag all-d ML CSV](https://www.nims.go.jp/group/spintheory/database/DXMag_HeuslerDB_alld_2026-03-10.csv) (checked 2026-11-01): HTTP 206 sample confirms cell, positions and atomic-number columns; ML_cell, ML_e, Tc_ML, Phonon_ML, MAE_ML and moment fields.

**Reuse and interpretation notes:**

- The count is the provider compound denominator, not the number of magnetic/structural calculations or property values.
- CSV headers and representative coordinate-bearing records were checked using a 64 KiB HTTP range; the full CSV was not independently recounted.
- Property values are model predictions; they are not fresh DFT calculations or experimental verification.
- Separate composition-family release from the ternary DFT training domain; possible structures shared with other catalogs have not been deduplicated.

**Tags:** heusler, magnetism, alld, ml-predictions, additional-materials-20261101.

<a id="camd-crystal-discoveries-2022"></a>
## CAMD autonomous crystal discovery corpus

DFT-relaxed inorganic crystal structures and formation/hull energies from autonomous active-learning campaigns.

**Size:** 96,640 crystal structure records (source wording: 96,640 crystal structure records).

**Scope:** CAMD2022 release with 26,435 distinct formulas and 1,457 chemical systems as reported by provider.

**Release:** CAMD2022 Figshare v1. **Year:** 2022.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** crystal structure; formation energy; energy above hull; matminer features.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [paper](https://doi.org/10.1038/s41597-022-01438-8) · [data](https://doi.org/10.6084/m9.figshare.19601956.v1)

**Evidence:**

- [Scientific Data primary data descriptor](https://doi.org/10.1038/s41597-022-01438-8) (checked 2026-11-01): DFT-relaxed inorganic crystal structures and formation/hull energies from autonomous active-learning campaigns. CAMD2022 release with 26,435 distinct formulas and 1,457 chemical systems as reported by provider.
- [Primary repository release metadata](https://api.figshare.com/v2/articles/19601956) (checked 2026-11-01): Confirms public release files and stated dataset terms; response hashes are saved in provider receipts.

**Reuse and interpretation notes:**

- Only 894 structures are within 1 meV/atom of the source hull; most records are higher-energy candidates.
- Computed hull proximity does not establish synthesis, dynamical stability or experimental discovery.
- Two JSON files with/without features describe the same structures and must not be added.

**Tags:** Scientific Data, survey:20261101, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="jarvis-dft-3d"></a>
## JARVIS-DFT 3D

NIST first-principles bulk materials collection with electronic, elastic and related property labels.

**Size:** ~75,993 structure records (source wording: 75,993).

**Scope:** Release described by the cited source

**Release:** dft_3d / 2022-12-12 downloader release. **Year:** 2022.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** crystal structure; OptB88vdW properties; TBmBJ band gaps for subset; elasticity.

**Access:** open. **Dataset license:** CC BY 4.0 (3D Figshare dataset).

**Official routes:** [homepage](https://jarvis.nist.gov/) · [data](https://doi.org/10.6084/m9.figshare.6815699) · [code](https://github.com/usnistgov/jarvis) · [portal](https://jarvis.nist.gov/jarvisdft)

**Evidence:**

- [JARVIS-DFT 3D — primary documentation](https://github.com/usnistgov/jarvis/blob/master/jarvis/db/figshare.py) (checked 2026-11-01): Official downloader describes the dft_3d release as 76k and points to jdft_3d-12-12-2022.json.
- [JARVIS-DFT 3D Figshare metadata](https://api.figshare.com/v2/articles/6815699) (checked 2026-11-01): Identifies the 2022-12-12 bulk data file and the CC BY 4.0 data license.
- [JARVIS-Tools named-release count](https://pages.nist.gov/jarvis/databases/) (checked 2026-11-01): The dft_3d row reports 75,993 data points for the named downloader release.

**Reuse and interpretation notes:**

- Version-pinned bulk downloader count; not a live tally of every JARVIS family database.
- Individual properties are available for subsets; JARVIS-2D and specialized cohorts are listed separately.
- The portal homepage separately reports 77,096 JARVIS-DFT materials in its statistics and 80,000+ in descriptive text. Figshare also lists a newer September 2025 archive; this record continues to identify the named December 2022 downloader snapshot.

**Tags:** None assigned.

<a id="multinary-perovskite-66516"></a>
## Theoretical multinary perovskite oxides

DFT-optimized multinary oxide structures initialized by SPuDS, with MP-compatible formation and decomposition enthalpies.

**Size:** 66,516 optimized oxide entries (source wording: 66,516 optimized oxide entries).

**Scope:** Published cohort; 59,708 classified as perovskites after relaxation.

**Release:** 2023 MPContribs publication dataset. **Year:** 2023.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** crystal structure; formation enthalpy; decomposition enthalpy; oxidation-state assignment; tolerance factors; perovskite classification.

**Access:** open. **Dataset license:** Provider displays CCA4 (Creative Commons Attribution 4.0); exact linked licence text not exposed in parsed page.

**Official routes:** [paper](https://doi.org/10.1038/s41597-023-02127-w) · [data](https://contribs.materialsproject.org/projects/Multinary_Oxides)

**Evidence:**

- [Scientific Data primary data descriptor](https://doi.org/10.1038/s41597-023-02127-w) (checked 2026-11-01): DFT-optimized multinary oxide structures initialized by SPuDS, with MP-compatible formation and decomposition enthalpies. Published cohort; 59,708 classified as perovskites after relaxation.
- [Primary repository release metadata](https://contribs.materialsproject.org/projects/Multinary_Oxides) (checked 2026-11-01): Confirms public release files and stated dataset terms; response hashes are saved in provider receipts.

**Reuse and interpretation notes:**

- The 69,407 SPuDS starting compositions exceed the final 66,516 optimized records; do not substitute the input-pool count.
- Not every relaxed record remains a perovskite.
- Entries also have MP IDs and overlap Materials Project; these are not independent materials to add to MP totals.

**Tags:** Scientific Data, survey:20261101, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="mip3d-release"></a>
## MIP-3d materials informatics release

Three-dimensional crystal calculations with tabulated energies, band gaps, bulk moduli, band degeneracy and thermoelectric subsets.

**Size:** 33,078 metadata/property records (source wording: 33,078 metadata/property records).

**Scope:** Independently counted RECORDS array in the v7 MIP-3d.json export; separate raw-calculation archives have not been equated to this count.

**Release:** Figshare v7. **Year:** 2021.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** energy; band gap; bulk modulus; magnetic moment; band-edge degeneracy; DOS and band-structure output subsets.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [paper](https://doi.org/10.1038/s41597-021-01022-6) · [data](https://doi.org/10.6084/m9.figshare.13655276.v7)

**Evidence:**

- [Scientific Data primary data descriptor](https://doi.org/10.1038/s41597-021-01022-6) (checked 2026-11-01): Three-dimensional crystal calculations with tabulated energies, band gaps, bulk moduli, band degeneracy and thermoelectric subsets. Independently counted RECORDS array in the v7 MIP-3d.json export; separate raw-calculation archives have not been equated to this count.
- [Primary repository release metadata](https://api.figshare.com/v2/articles/13655276/versions/7) (checked 2026-11-01): Confirms public release files and stated dataset terms; response hashes are saved in provider receipts.
- [MIP-3d companion input archive](https://api.figshare.com/v2/articles/13655276/versions/7) (checked 2026-11-01): mip3d.tar.gz checksum matches provider metadata; its archive includes periodic POSCAR inputs for Relax, SCF and Band stages. Coordinate coverage was sampled, not joined one-to-one against all 33,078 JSON rows.

**Reuse and interpretation notes:**

- The >80,000 structural source pool is not the downloadable 33,078-row calculation export.
- JSON export contains metadata/properties without coordinates; companion mip3d.tar.gz was downloaded and verified to contain VASP POSCAR files across calculation stages.
- Approximately 4,400 electrical-transport entries and >12,000 equations of state are subsets, not the full record count.
- Many source identities originate in ICSD; do not infer open rights to all original ICSD structures.

**Tags:** Scientific Data, survey:20261101, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="mc3d"></a>
## Materials Cloud 3D (MC3D)

Reproducible DFT geometries seeded from experimental crystallography with complete AiiDA provenance.

**Size:** 32,013 unique optimized structures (source wording: 32,013).

**Scope:** Release described by the cited source

**Release:** PBEsol-v2 (2025 paper). **Year:** 2025.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** crystal structure; energy.

**Access:** open. **Dataset license:** CC BY 4.0 (Materials Cloud record).

**Official routes:** [homepage](https://www.materialscloud.org/discover/mc3d) · [data](https://archive.materialscloud.org/records/szjaf-cfv74) · [paper](https://arxiv.org/abs/2508.19223)

**Evidence:**

- [Materials Cloud 3D (MC3D) — primary documentation](https://arxiv.org/abs/2508.19223) (checked 2026-11-01): Primary paper reports 72,589 curated unique stoichiometric input structures and 32,013 optimized structures in PBEsol-v2.

**Reuse and interpretation notes:**

- 32,013 is the optimized release, not the larger curated input set.
- Computed relaxed coordinates derived from experimental sources; not new experimental measurements.

**Tags:** None assigned.

<a id="layered-intercalation-bandstructures"></a>
## Layered intercalation crystal band structures

Intercalant/host crystal configurations with comparable electronic band paths and VASP inputs and outputs.

**Size:** 9,024 intercalated crystal records (source wording: 9,024 intercalated crystal records).

**Scope:** 9,024 listed intercalation compounds; 9,004 have band-derived properties. Host-related records form separate associated subsets.

**Release:** Figshare v1. **Year:** 2024.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** band structure; band gap; formation energy; Fermi energy; spin splitting; periodic structure.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [paper](https://doi.org/10.1038/s41597-024-04008-2) · [data](https://doi.org/10.6084/m9.figshare.26885734)

**Evidence:**

- [Scientific Data primary data descriptor](https://doi.org/10.1038/s41597-024-04008-2) (checked 2026-11-01): Intercalant/host crystal configurations with comparable electronic band paths and VASP inputs and outputs. 9,024 listed intercalation compounds; 9,004 have band-derived properties. Host-related records form separate associated subsets.
- [Primary repository release metadata](https://api.figshare.com/v2/articles/26885734) (checked 2026-11-01): Confirms public release files and stated dataset terms; response hashes are saved in provider receipts.

**Reuse and interpretation notes:**

- The 9,004 band-structure count differs from the 9,024 composition/energy table.
- 142 bulk hosts, 188 vacancy-containing hosts and 142 single layers are separate related configurations; do not describe their sum as unique new compounds.
- Parent structures overlap MP/literature; band gaps use a semilocal vdW-corrected workflow rather than GW/HSE references.

**Tags:** Scientific Data, survey:20261101, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="dtm-max-phases-8712"></a>
## Double-transition-metal MAX-phase precursors

VASP structure and energetics corpus for layered double-transition-metal MXene precursor phases.

**Size:** 8,712 MAX-phase configuration records (source wording: 8,712 MAX-phase configuration records).

**Scope:** Publication/Zenodo 1.0 double-transition-metal precursor dataset.

**Release:** Zenodo 1.0. **Year:** 2023.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** atomic structure; DFT total energy; formation/stability quantities.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [paper](https://doi.org/10.1038/s41597-023-02755-2) · [data](https://doi.org/10.5281/zenodo.8400682)

**Evidence:**

- [Scientific Data primary data descriptor](https://doi.org/10.1038/s41597-023-02755-2) (checked 2026-11-01): VASP structure and energetics corpus for layered double-transition-metal MXene precursor phases. Publication/Zenodo 1.0 double-transition-metal precursor dataset.
- [Primary repository release metadata](https://zenodo.org/api/records/8400682) (checked 2026-11-01): Confirms public release files and stated dataset terms; response hashes are saved in provider receipts.

**Reuse and interpretation notes:**

- These are bulk MAX precursor phases, not 8,712 free-standing MXene monolayers.
- Alternative ordering/configurations can share chemical composition.
- Provider offers DTM.json; its payload was not independently recounted.

**Tags:** Scientific Data, survey:20261101, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="all-electron-hybrid-7024"></a>
## All-electron hybrid-functional materials database

FHI-aims PBEsol/HSE06 electronic-structure and stability calculations with ASE databases and processed properties.

**Size:** 7,024 inorganic material records (source wording: 7,024 inorganic material records).

**Scope:** Publication/archived materials cohort; processed property coverage varies by quantity.

**Release:** Figshare v1; NOMAD 2025.05.01-1. **Year:** 2025.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** HSE06 band gap; PBEsol electronic structure; formation energy; phase stability; Pourbaix stability; atomic structure.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [paper](https://doi.org/10.1038/s41597-025-05867-z) · [data](https://doi.org/10.6084/m9.figshare.28375538.v1)

**Evidence:**

- [Scientific Data primary data descriptor](https://doi.org/10.1038/s41597-025-05867-z) (checked 2026-11-01): FHI-aims PBEsol/HSE06 electronic-structure and stability calculations with ASE databases and processed properties. Publication/archived materials cohort; processed property coverage varies by quantity.
- [Primary repository release metadata](https://api.figshare.com/v2/articles/28375538) (checked 2026-11-01): Confirms public release files and stated dataset terms; response hashes are saved in provider receipts.

**Reuse and interpretation notes:**

- ASE databases include calculations not successfully parsed by NOMAD; source-specific counts can differ.
- Not all rows have formation/stability properties; elements serve as reference states.
- Contains re-calculated existing structures, not 7,024 independently new compounds.

**Tags:** Scientific Data, survey:20261101, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="sacada"></a>
## SACADA three-periodic carbon allotropes

Literature-indexed experimental/hypothetical carbon nets, optimized structures and computed physical-property references.

**Size:** 1,661 carbon allotrope table entries (source wording: 1,661).

**Scope:** Literature-indexed experimental/hypothetical carbon nets, optimized structures and computed physical-property references.

**Release:** Live table snapshot 2026-11-01; HTML update label 2024-02-15. **Year:** 2016.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** CIF structures; topology and symmetry; density; band gap; relative energy; elastic moduli and estimated hardness.

**Access:** open. **Dataset license:** Not verified; public browsing/download does not establish redistribution rights.

**Official routes:** [homepage](https://www.sacada.info/) · [data](https://www.sacada.info/sacada_3D.php) · [paper](https://doi.org/10.1002/anie.201600655)

**Evidence:**

- [SACADA provider documentation](https://www.sacada.info/) (checked 2026-11-01): Describes unique 3-periodic carbon allotropes, separate ideal-net and optimized CIFs and DFT-derived property fields.
- [SACADA live table response](https://www.sacada.info/scd_ajax.php) (checked 2026-11-01): Public GET contract read from the site HTML; independently counted 1,661 rows with 1,661 unique IDs.
- [SACADA diamond example](https://www.sacada.info/ca_data.php?id=1) (checked 2026-11-01): Public ZIP inspected: dia/dia.cif and dia/dia_IN.cif; cell and atomic-coordinate fields present.

**Reuse and interpretation notes:**

- Table entries are allotrope/net records, not experimentally realized phases.
- Some records are topology-only or change topology on optimization; coordinate and property completeness varies.
- Ideal-net and optimized CIFs represent the same entry and are not counted twice.
- Only a sample coordinate ZIP was inspected; table-row count does not certify a complete CIF for every row.

**Tags:** additional-materials-20261101.

<a id="hoip-2017"></a>
## Hybrid organic–inorganic perovskite DFT dataset

Hybrid-perovskite periodic CIFs with PBE/HSE06 band gaps, dielectric responses and stability-related quantities.

**Size:** 1,346 optimized hybrid-perovskite compounds (source wording: 1,346 optimized hybrid-perovskite compounds).

**Scope:** Final cohort in the 2017 descriptor; six DFT runs per compound produce 8,076 calculations.

**Release:** Dryad publication release / NOMAD 2017.03.15-1. **Year:** 2017.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** PBE band gap; HSE06 band gap; ionic/electronic dielectric constant; refractive index; optimized CIF; relative energy.

**Access:** open. **Dataset license:** CC0 1.0.

**Official routes:** [paper](https://doi.org/10.1038/sdata.2017.57) · [data](https://doi.org/10.5061/dryad.gq3rg)

**Evidence:**

- [Scientific Data primary data descriptor](https://doi.org/10.1038/sdata.2017.57) (checked 2026-11-01): Hybrid-perovskite periodic CIFs with PBE/HSE06 band gaps, dielectric responses and stability-related quantities. Final cohort in the 2017 descriptor; six DFT runs per compound produce 8,076 calculations.
- [Primary repository release metadata](https://datadryad.org/api/v2/datasets/doi%3A10.5061%2Fdryad.gq3rg) (checked 2026-11-01): Confirms public release files and stated dataset terms; response hashes are saved in provider receipts.

**Reuse and interpretation notes:**

- Properties and structure are computed for prototype-generated candidates, not 1,346 experimentally confirmed compounds.
- The 8,076 calculation runs are repeated workflows for the same 1,346 final compounds.
- CIF comment lines carry property labels and must be preserved when converting formats.

**Tags:** Scientific Data, survey:20261101, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="hex-high-pressure-elements"></a>
## HEX high-pressure elemental crystals

Ground-state elemental crystal references and evolutionary-search comparison structures for H through La at four pressures.

**Size:** 228 element-pressure ground-state cases (source wording: 228 element-pressure ground-state cases).

**Scope:** 57 elements at 0, 100, 200 and 300 GPa in DB_GS; repeated phases across pressure remain separate cases.

**Release:** Figshare collection v1 / article 25403968 v1. **Year:** 2024.

**Provenance:** mixed. **Structure availability:** `periodic_atomic`.

**Labels/content:** ground-state crystal structure; relative enthalpy; volume; Wyckoff positions; pressure.

**Access:** open. **Dataset license:** CC0 1.0.

**Official routes:** [paper](https://doi.org/10.1038/s41597-024-03447-1) · [data](https://doi.org/10.6084/m9.figshare.c.7119778.v1)

**Evidence:**

- [Scientific Data primary data descriptor](https://doi.org/10.1038/s41597-024-03447-1) (checked 2026-11-01): Ground-state elemental crystal references and evolutionary-search comparison structures for H through La at four pressures. 57 elements at 0, 100, 200 and 300 GPa in DB_GS; repeated phases across pressure remain separate cases.
- [Primary repository release metadata](https://api.figshare.com/v2/articles/25403968) (checked 2026-11-01): Confirms public release files and stated dataset terms; response hashes are saved in provider receipts.

**Reuse and interpretation notes:**

- Only 57 elemental compositions, not 228 distinct chemical compositions.
- ZIP has 457 real CIFs: 228 GS, 228 EA and one MISS; auxiliary and duplicate structures must not be counted as new materials.
- A naive count gives 914 .cif names because macOS resource forks duplicate real files; those were explicitly excluded.
- Search cells have eight atoms; ZPE and some relativistic/correlation effects are outside the baseline workflow.

**Tags:** Scientific Data, survey:20261101, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="nist-mras-amorphous"></a>
## NIST MRAS amorphous structural models

Amorphous silicon, silica, hafnia, zirconium–copper and alumina structures generated by relaxation of random molecular arrangements.

**Size:** 50 final amorphous structure files (source wording: 50).

**Scope:** Ten CONTCAR structures in each of Si_Final, SiO2_Final, HfO2_Final, ZrCu_Final and Al2O3_Final; exploratory Si_Base structures are excluded.

**Release:** NIST mds2-3831 v1.0.1. **Year:** 2025.

**Provenance:** Worden–Cockayne–Garrity random-arrangement relaxation workflows at NIST. **Structure availability:** `periodic_atomic`.

**Labels/content:** atomic structures; cell density; mean density; generation workflow.

**Access:** open. **Dataset license:** NIST Open License; see linked dataset-specific metadata and NIST terms.

**Official routes:** [Release](https://data.nist.gov/od/id/mds2-3831) · [Archive](https://data.nist.gov/od/ds/mds2-3831/Amorphous_Molecule_Construction.zip) · [Readme](https://data.nist.gov/od/ds/mds2-3831/README.txt) · [License](https://www.nist.gov/open/license)

**Evidence:**

- [NIST MRAS release metadata](https://data.nist.gov/od/id/mds2-3831) (checked 2026-11-01): Names five material systems and an open-licence URL; downloadable ZIP has publisher SHA-256 153d2889f34a86db89fbf08b96e64f8ac2312ea71dd74a57128b1ee5b264435c.
- [NIST MRAS README](https://data.nist.gov/od/ds/mds2-3831/README.txt) (checked 2026-11-01): Final directories contain ten CONTCAR systems apiece with density headers and workflows. Downloaded archive inventory confirms 50 final structures.

**Reuse and interpretation notes:**

- The archive also contains 240 exploratory silicon CONTCAR files; these are excluded from the final model count.
- Computed amorphous models are not experimental determinations of atomic structure.

**Tags:** amorphous, silica, hafnia, alumina, metallic-glasses, additional-materials-20261101.

<a id="nlr-matdb"></a>
## NLR MatDB (formerly NRELMatDB)

Computational database for renewable-energy materials with relaxed crystal structures, formation thermochemistry and GW electronic/optical properties.

**Size:** Unranked materials (source wording: Not verified).

**Scope:** No current numeric release size was verified from the official portal

**Release:** Official portal snapshot checked 2026-11-01. **Year:** Not verified.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** DFT GGA+U relaxed crystal structure; formation enthalpy; chemical-potential stability range; decomposition enthalpy; GW band gap; dielectric function; absorption spectrum.

**Access:** open. **Dataset license:** Not verified.

**Official routes:** [homepage](https://materials.nlr.gov/) · [data](https://materials.nlr.gov/) · [paper](https://doi.org/10.1103/PhysRevB.85.115104) · [code](https://github.com/pylada/pylada-light)

**Evidence:**

- [NLR MatDB official portal](https://materials.nlr.gov/) (checked 2026-11-01): Current provider describes stoichiometric fully ordered materials, DFT-relaxed structures, thermochemistry and GW electronic data, with methodology citations.
- [NLR MatDB help](https://materials.nlr.gov/help) (checked 2026-11-01): Identifies the current computational materials database, its institutional team and photovoltaic-materials discovery scope.

**Reuse and interpretation notes:**

- Old collection URL materials.nrel.gov returned an error; the current official service is materials.nlr.gov.
- Count and explicit dataset license remain unverified.
- Planned defect and surface properties listed on the homepage are not treated as released data.
- The cited formation-energy methodology paper is not a complete frozen dataset descriptor.

**Tags:** renewable energy, electronic structure, GW, thermochemistry, NREL, NLR, collection:sedaoturak.
