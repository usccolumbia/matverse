# Two-dimensional and layered materials

[Back to MatVerse](../../README.md)

Checked 2026-11-01. Counts are source-reported or explicitly derived from release metadata; full datasets were not independently deduplicated.

<a id="c2db"></a>
## Computational 2D Materials Database (C2DB)

DFT and many-body properties of monolayer crystals, with experimental-derived and generated candidates.

**Size:** 16,789 database rows (source wording: 16,789 rows).

**Scope:** Version table entry dated 2024-05-01, not the stale introductory description.

**Release:** 2024-05-01 release listed on official 2DHub page. **Year:** 2024.

**Provenance:** mixed. **Structure availability:** `periodic_atomic`.

**Labels/content:** structure; formation energy; electronic band structure; magnetism; elasticity; optical response.

**Access:** mixed. **Dataset license:** Not verified.

**Official routes:** [homepage](https://2dhub.org/c2db/c2db.html) · [paper](https://doi.org/10.1088/2053-1583/ac1059)

**Evidence:**

- [C2DB official release history](https://2dhub.org/c2db/c2db.html) (checked 2026-11-01): Release table lists 16,789 rows for 2024-05-01; full dataset is provided upon request.

**Reuse and interpretation notes:**

- The overview still says around 4,000; the release table is more recent.
- Full download requires an author request; browsing is public.
- Legacy CMR declares CC BY-SA 4.0 globally, but current 2DHub release-specific data license was not verified.

**Tags:** monolayers, DFT, many-body, nonadditive.

<a id="bidb"></a>
## van der Waals Bilayer Database (BiDB)

Stacked homobilayers with DFT interlayer energies and detailed properties for the stable subset.

**Size:** 8,451 homobilayer configurations (source wording: 8,451 homobilayers from 1,052 monolayers).

**Scope:** All stacking configurations in the 2024 study; detailed labels for 2,586 stable bilayers.

**Release:** 2024 publication dataset. **Year:** 2024.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** interlayer binding energy; electronic properties; magnetism; vibrations.

**Access:** open. **Dataset license:** Not verified.

**Official routes:** [homepage](https://2dhub.org/bidb/bidb.html) · [data](https://2dhub.org/bidb/bidb.html) · [paper](https://doi.org/10.1038/s41467-024-45003-w)

**Evidence:**

- [BiDB official page](https://2dhub.org/bidb/bidb.html) (checked 2026-11-01): 8,451 homobilayers are constructed from 1,052 monolayers; 2,586 stable bilayers have expanded labels and an ASE database is linked.

**Reuse and interpretation notes:**

- Count includes multiple stackings of the same monolayer, not 8,451 distinct chemistries.
- C2DB-derived monolayers overlap the parent family.

**Tags:** bilayers, stacking, DFT.

<a id="2dmatpedia"></a>
## 2DMatPedia

Top-down exfoliation of Materials Project layered parents and bottom-up chemical substitution.

**Size:** 6,351 monolayer structures (source wording: 6,351 monolayer records).

**Scope:** Official 2019 Figshare JSONL archive, independently counted 6,351 parseable records.

**Release:** Figshare v3, 2019. **Year:** 2019.

**Provenance:** mixed. **Structure availability:** `periodic_atomic`.

**Labels/content:** structure; formation energy; exfoliation energy; band gap; electronic structure.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [homepage](http://www.2dmatpedia.org/) · [data](https://figshare.com/articles/dataset/7699910/3) · [paper](https://doi.org/10.1038/s41597-019-0097-3)

**Evidence:**

- [2DMatPedia official Figshare metadata](https://api.figshare.com/v2/articles/7699910) (checked 2026-11-01): Version 3 releases monolayer structures and properties under CC BY 4.0.
- [2DMatPedia official JSONL data](https://ndownloader.figshare.com/files/14399918) (checked 2026-11-01): Downloaded JSONL contains exactly 6,351 parseable structure records; local SHA-256 retained.
- [2DMatPedia author paper](https://arxiv.org/abs/1901.09487) (checked 2026-11-01): Top-down screening and bottom-up element substitutions produce the monolayer collection.
- [2DMatPedia, an open computational database of two-dimensional materials from top-down and bottom-up approaches — Scientific Data descriptor](https://doi.org/10.1038/s41597-019-0097-3) (checked 2026-11-01): Publisher DOI and Crossref metadata verify the corresponding Scientific Data descriptor; the selected release count is supported by the other evidence listed here.

**Reuse and interpretation notes:**

- Generated substitutions are not experimental materials discoveries.
- Overlap with Materials Project and other monolayer collections requires structure-level checks.

**Tags:** Scientific Data, monolayers, chemical-substitution, DFT, Scientific-Data-descriptor.

<a id="mc2d"></a>
## Materials Cloud Two-Dimensional Structure Database (MC2D)

Computational exfoliation of experimentally reported layered bulk crystals, with AiiDA provenance.

**Size:** 3,077 monolayer compounds (source wording: 3,077 extracted monolayers; 2,710 optimized structures).

**Scope:** 2022.84 archive contains 3,077 extracted structures, not all DFT optimized.

**Release:** Materials Cloud 2022.84 v1 / 2023 paper. **Year:** 2022.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** structure; exfoliation energy; electronic band structure.

**Access:** open. **Dataset license:** Creative Commons Attribution 4.0 International.

**Official routes:** [homepage](https://mc2d.materialscloud.org/) · [data](https://archive.materialscloud.org/records/17gf6-84915) · [paper](https://doi.org/10.1021/acsnano.2c11510)

**Evidence:**

- [MC2D archived release](https://archive.materialscloud.org/records/17gf6-84915) (checked 2026-11-01): Archive contains 3,077 extracted structures, 2,710 optimized structures and 2,345 electronic band structures.
- [MC2D record metadata](https://archive.materialscloud.org/api/records/17gf6-84915) (checked 2026-11-01): File license is CC BY 4.0.

**Reuse and interpretation notes:**

- Bulk sources include ICSD, COD and MPDS; derived structures may overlap other 2D databases.
- The 3,077 count is broader than the optimized or easily exfoliable subsets.

**Tags:** exfoliation, AiiDA, DFT.

<a id="qpod"></a>
## Quantum Point Defects Database (QPOD)

Intrinsic point defects in monolayers across charge states, with electronic and optical properties.

**Size:** 2,061 defect-charge-state rows (source wording: 2,061 rows representing 500 distinct intrinsic point defects).

**Scope:** Release table lists 2,061 rows; distinct defects are counted separately.

**Release:** 2022-07-11 release table. **Year:** 2022.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** defect formation energy; charge transitions; electronic levels; magneto-optical properties; spin coherence.

**Access:** open. **Dataset license:** Not verified.

**Official routes:** [homepage](https://2dhub.org/qpod/qpod.html) · [paper](https://doi.org/10.1038/s41524-022-00730-w)

**Evidence:**

- [QPOD official page](https://2dhub.org/qpod/qpod.html) (checked 2026-11-01): 500 distinct intrinsic defects are evaluated in multiple charge states; version table lists 2,061 rows.

**Reuse and interpretation notes:**

- Rows include different charge states; do not report them as 2,061 distinct defects.
- Derived from C2DB host materials.

**Tags:** defects, charge-states, DFT.

<a id="jarvis-2d"></a>
## JARVIS-DFT 2D snapshot

NIST monolayer materials subset with optB88-vdW and related calculated properties.

**Size:** 1,103 2D material records (source wording: 1,103 records in downloaded archive (documentation lists 1,109)).

**Scope:** Actual d2-12-12-2022.json.zip payload linked by current jarvis-tools.

**Release:** d2-12-12-2022.json / Figshare v8. **Year:** 2022.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** structure; formation energy; exfoliation energy; band gap; elasticity; dielectric response.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [homepage](https://pages.nist.gov/jarvis/databases/) · [data](https://figshare.com/articles/dataset/6815705) · [paper](https://doi.org/10.1038/s41524-020-00440-1) · [code](https://github.com/usnistgov/jarvis)

**Evidence:**

- [JARVIS-DFT 2D Figshare release](https://api.figshare.com/v2/articles/6815705) (checked 2026-11-01): v8 metadata declares CC BY 4.0 and links the dated 2022 archive.
- [Official JARVIS 2D payload](https://ndownloader.figshare.com/files/38521268) (checked 2026-11-01): Independent JSON array count of downloaded archive is 1,103; payload SHA-256 retained.
- [JARVIS data registry](https://pages.nist.gov/jarvis/databases/) (checked 2026-11-01): Documentation reports 1,109 for dft_2d, differing from the linked archive.

**Reuse and interpretation notes:**

- Named subset of JARVIS; do not add its count to the entire JARVIS family.
- Documentation and actual payload counts disagree; this record ranks the verified archive.

**Tags:** NIST, DFT, snapshot, family-subset.

<a id="bmds-bilayers-760"></a>
## BMDS bilayer electronic and transport dataset

Ground-state stacking and electronic/transport properties for nonmagnetic-parent homobilayers selected from C2DB.

**Size:** 760 bilayer materials (source wording: 760 bilayer materials).

**Scope:** Published relaxed bilayer cohort, excluding failed interlayer separations.

**Release:** Figshare v2. **Year:** 2023.

**Provenance:** computed. **Structure availability:** `structure_linked`.

**Labels/content:** stacking; binding energy; interlayer charge transfer; SOC band gap; effective mass; Seebeck coefficient; conductivity over relaxation time.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [paper](https://doi.org/10.1038/s41597-023-02146-7) · [data](https://doi.org/10.6084/m9.figshare.21799475.v2)

**Evidence:**

- [Scientific Data primary data descriptor](https://doi.org/10.1038/s41597-023-02146-7) (checked 2026-11-01): Ground-state stacking and electronic/transport properties for nonmagnetic-parent homobilayers selected from C2DB. Published relaxed bilayer cohort, excluding failed interlayer separations.
- [Primary repository release metadata](https://api.figshare.com/v2/articles/21799475) (checked 2026-11-01): Confirms public release files and stated dataset terms; response hashes are saved in provider receipts.

**Reuse and interpretation notes:**

- Derived from C2DB monolayers; different from the existing 2024 BiDB release.
- Release inventory includes tables, plots and stacking-generation prototype code; full ready-made coordinates for all 760 were not verified.
- Transport values with unknown relaxation time remain sigma/tau, not measured conductivity.

**Tags:** Scientific Data, survey:20261101, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="cmr-c2dm-2015"></a>
## CMR C2DM transition-metal monolayer electronic structures (2015)

Original monolayer dichalcogenide/oxide electronic-structure and GW campaign, released separately from the later C2DB.

**Size:** 494 ASE calculation/structure rows (source wording: 494).

**Scope:** The released c2dm.db systems table counted without adding spectra, property columns or functional results as independent materials.

**Release:** Provider ASE database snapshot 2026-11-01. **Year:** 2015.

**Provenance:** DFT / first-principles calculations. **Structure availability:** `periodic_atomic`.

**Labels/content:** atomic structures; PBE/LDA/GLLB-SC band edges and gaps; G0W0 quasiparticle results for a subset.

**Access:** open. **Dataset license:** Not verified: CMR index declares CC BY-SA 4.0, while the browser footer declares CC BY-NC 4.0; dataset-specific scope requires clarification.

**Official routes:** [homepage](https://cmr.fysik.dtu.dk/c2dm/c2dm.html) · [download](https://wiki.fysik.dtu.dk/cmr-files/c2dm.db)

Other denominators (not added to the ranking):

- 216 distinct name/phase keys: Derived from released key_value_pairs; not a structural deduplication.

**Evidence:**

- [CMR C2DM transition-metal monolayer electronic structures (2015) provider project page](https://cmr.fysik.dtu.dk/c2dm/c2dm.html) (checked 2026-11-01): Describes the property campaign and links its named ASE database.
- [CMR C2DM transition-metal monolayer electronic structures (2015) downloadable ASE database](https://wiki.fysik.dtu.dk/cmr-files/c2dm.db) (checked 2026-11-01): Independently inspected SQLite systems table: 494 rows, all with populated positions, cell and atomic-number blobs; payload SHA-256 is preserved in the evidence manifest.
- [CMR repository terms](https://cmr.fysik.dtu.dk/) (checked 2026-11-01): Repository-wide CC BY-SA 4.0 declaration; browser terms differ.

**Reuse and interpretation notes:**

- 494 calculation rows represent 216 distinct name/phase keys; functional repeats and subset GW coverage are not additional unique materials.
- Atomic coordinate availability was checked in the released ASE database; cross-catalog structural overlap has not been deduplicated.
- Strong overlap with later C2DB is expected; this is a separately downloadable 2015 GW/functional release, not 494 new monolayers.

**Tags:** cmr, electronic-structure, semiconductors, additional-materials-20261101.

<a id="zhou-2d-spin-hall-426"></a>
## Zhou–Poncé–Charlier 2D spin-Hall / Wannier dataset

Relativistic Wannier Hamiltonians and spin-Hall calculations for nonmagnetic monolayers, with detailed transport inputs for selected candidates.

**Size:** 426 nonmagnetic monolayers (source wording: 426).

**Scope:** 210 metals and 216 insulators in the Wannier-Hamiltonian cohort; selected-material transport folders are not added.

**Release:** Materials Cloud v2, 2026-06-18; DOI 10.24435/materialscloud:yv-h7. **Year:** 2026.

**Provenance:** First-principles DFT and Wannier interpolation; monolayers drawn from existing 2D collections. **Structure availability:** `periodic_atomic`.

**Labels/content:** fully relativistic DFT bands; Wannier Hamiltonians; spin Hall conductivity; selected phonon/EPW charge transport inputs.

**Access:** open. **Dataset license:** CC BY 4.0 (record metadata).

**Official routes:** [homepage](https://archive.materialscloud.org/records/rfcdy-wcy32) · [doi](https://doi.org/10.24435/materialscloud:yv-h7) · [paper](https://www.nature.com/articles/s41699-025-00562-4)

**Count derivation:** Sum of disjoint metal/insulator cohorts listed in release README; 210 + 216 = 426.

**Evidence:**

- [Materials Cloud spin-Hall dataset v2](https://archive.materialscloud.org/records/rfcdy-wcy32) (checked 2026-11-01): Provider gives 426 nonmagnetic monolayers and provides Data.7z with a separate README.
- [Materials Cloud v2 metadata](https://archive.materialscloud.org/api/records/rfcdy-wcy32) (checked 2026-11-01): Declares CC BY 4.0, open public files and versioned archive checksums.
- [Spin-Hall archive README](https://archive.materialscloud.org/api/records/rfcdy-wcy32/files/README.txt/content) (checked 2026-11-01): Separately confirms 210 metallic and 216 insulating material directories, each with QE aiida.in/aiida.out, Wannier inputs, bands and Hamiltonian; selected transport folders have separate scope.

**Reuse and interpretation notes:**

- The structures overlap parent 2D databases; new content is the relativistic Wannier/spin-transport campaign.
- Uniform transport and electron-phonon data are not promised for all 426 materials.
- The 390 MiB archive was not downloaded; metadata and its independently downloaded README establish the released layout.

**Tags:** spintronics, spin-hall, wannier, two-dimensional, additional-materials-20261101.

<a id="2d-alloys"></a>
## 2D-Alloy Database

DFT structures and formation thermodynamics for transition-metal dichalcogenide alloy monolayers.

**Size:** 400 alloy monolayers (source wording: 400 monolayer TMDC alloys).

**Scope:** Provider-described 1T and 2H alloy collection

**Release:** 2DHub provider documentation updated 2026-09-30. **Year:** 2025.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** atomic structures; formation enthalpy at 0 K; formation free energy at 1000 K; hydrogen binding energy for subset.

**Access:** open. **Dataset license:** Not verified.

**Official routes:** [homepage](https://2dhub.org/2dalloys/2dalloys.html) · [data](https://2dhub.org/_downloads/93db2a0b33028278cf5e22b17a3994f7/2dalloys.db) · [paper](https://doi.org/10.1021/jacs.4c13863)

**Evidence:**

- [2DHub: 2D-Alloy Database](https://2dhub.org/2dalloys/2dalloys.html) (checked 2026-11-01): Provider specifies 400 1T/2H TMDC alloys, atomic structures, PBE thermodynamics and downloadable ASE database.

**Reuse and interpretation notes:**

- A computational alloy cohort, not 400 experimentally synthesized monolayers.
- Free download availability does not establish a verified redistribution licence.

**Tags:** 2D, alloys, DFT, collection-blaiszik.

<a id="hetdb"></a>
## van der Waals 2D Heterostructure Database (HetDB)

Relaxed heterobilayers selected for commensurability, small strain and tractable cell size.

**Size:** 336 heterobilayer structures (source wording: 336 heterobilayers from 44 monolayers).

**Scope:** Official database description viewed 2026-11-01.

**Release:** 2025 publication dataset. **Year:** 2025.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** relaxed structure; electronic band structure; band alignment.

**Access:** open. **Dataset license:** Not verified.

**Official routes:** [homepage](https://2dhub.org/hetdb/hetdb.html) · [paper](https://doi.org/10.1103/cl8c-8f1f)

**Evidence:**

- [HetDB official page](https://2dhub.org/hetdb/hetdb.html) (checked 2026-11-01): 336 heterobilayers from 44 monolayers are relaxed with PBE-D3; cells have fewer than 300 atoms and in-plane strain below 1%.

**Reuse and interpretation notes:**

- Selection excludes large mismatch or large supercell combinations.
- Count is bilayer combinations, not independent monolayer chemistries.

**Tags:** heterostructures, DFT, interfaces.

<a id="ac2d-amorphous-graphene"></a>
## AC-2D-22 amorphous graphene benchmark subset

Monte Carlo bond-switched graphene models selected from the paper Figure 3 structural comparisons.

**Size:** 150 selected 200-atom configurations (source wording: 150).

**Scope:** Monte Carlo bond-switched graphene models selected from the paper Figure 3 structural comparisons.

**Release:** Primary release/documentation checked 2026-11-01. **Year:** 2022.

**Provenance:** model-generated; C-GAP-17-labeled. **Structure availability:** `periodic_atomic`.

**Labels/content:** atomic coordinates; C-GAP-17 forces; local atomic energies; MC criterion and beta.

**Access:** open. **Dataset license:** CC BY 4.0 original deposit; CC BY-NC-SA 4.0 normalized load-atoms distribution.

**Official routes:** [paper](https://doi.org/10.1039/D2SC04326B) · [data](https://zenodo.org/records/7221166) · [loader](https://jla-gardner.github.io/load-atoms/datasets/AC-2D-22.html)

**Evidence:**

- [AC-2D-22 subset definition](https://jla-gardner.github.io/load-atoms/datasets/AC-2D-22.html) (checked 2026-11-01): Explicit 150 structures /30,000 atoms; importer selects Figure 3 final-structure folders with C-GAP-17 labels.
- [Original amorphous-graphene deposit](https://zenodo.org/api/records/7221166) (checked 2026-11-01): Original data.tar.gz is open and metadata declares CC BY 4.0; normalized loader declares CC BY-NC-SA 4.0.

**Reuse and interpretation notes:**

- A selected Figure 3 subset, not all configurations in the original archive.
- Local energies and forces are potential-generated targets rather than fresh DFT for every model.
- Original and normalized routes declare different licenses; preserve the terms of the chosen distribution.

**Tags:** additional-materials-20261101.
