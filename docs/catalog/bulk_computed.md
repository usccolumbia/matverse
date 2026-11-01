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

**Tags:** None assigned.

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

<a id="materials-project"></a>
## Materials Project

Structure-centered computed properties for inorganic materials with API and bulk distribution routes.

**Size:** 200,487 materials entries (source wording: 200,487).

**Scope:** Release described by the cited source

**Release:** Homepage v2026.04.13 snapshot. **Year:** 2026.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** crystal structure; formation energy; electronic structure; elasticity; phase diagrams.

**Access:** registration. **Dataset license:** CC BY 4.0 for core data; GNoME-origin data carry separate BY-NC acceptance.

**Official routes:** [homepage](https://materialsproject.org/) · [data](https://docs.materialsproject.org/downloading-data) · [paper](https://doi.org/10.1063/1.4812323)

**Evidence:**

- [Materials Project — primary documentation](https://doi.org/10.17188/1693272) (checked 2026-11-01): Provider homepage snapshot reports 200,487 materials and identifies database v2026.04.13.
- [Materials Project database versions](https://docs.materialsproject.org/changes/database-versions) (checked 2026-11-01): Version history documents separate BY-NC acceptance for the GNoME dataset and changes in collection membership.

**Reuse and interpretation notes:**

- A dated provider-page figure, not an authenticated query of the latest live database.
- Different property collections cover different subsets; molecule and electrode totals are separate.
- Track GNoME-origin licensing and database version when using API data.

**Tags:** None assigned.

<a id="jarvis-dft-3d"></a>
## JARVIS-DFT 3D

NIST first-principles bulk materials collection with electronic, elastic and related property labels.

**Size:** ~76,000 structure records (source wording: ~76,000).

**Scope:** Release described by the cited source

**Release:** dft_3d / 2022-12-12 downloader release. **Year:** 2022.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** crystal structure; OptB88vdW properties; TBmBJ band gaps for subset; elasticity.

**Access:** open. **Dataset license:** CC BY 4.0 (3D Figshare dataset).

**Official routes:** [homepage](https://jarvis.nist.gov/) · [data](https://doi.org/10.6084/m9.figshare.6815699) · [code](https://github.com/usnistgov/jarvis)

**Evidence:**

- [JARVIS-DFT 3D — primary documentation](https://github.com/usnistgov/jarvis/blob/master/jarvis/db/figshare.py) (checked 2026-11-01): Official downloader describes the dft_3d release as 76k and points to jdft_3d-12-12-2022.json.
- [JARVIS-DFT 3D Figshare metadata](https://api.figshare.com/v2/articles/6815699) (checked 2026-11-01): Identifies the 2022-12-12 bulk data file and the CC BY 4.0 data license.

**Reuse and interpretation notes:**

- Version-pinned bulk downloader count; not a live tally of every JARVIS family database.
- Individual properties are available for subsets; JARVIS-2D and specialized cohorts are listed separately.

**Tags:** None assigned.

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
