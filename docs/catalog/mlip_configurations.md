# Bulk and mixed-domain MLIP configurations

[Back to MatVerse](../../README.md)

Checked 2026-11-01. Counts are source-reported or explicitly derived from release metadata; full datasets were not independently deduplicated.

<a id="lemat-traj"></a>
## LeMat-Traj

Standardized relaxation trajectories from Materials Project, Alexandria and OQMD.

**Size:** 121,274,458 atomic configurations (source wording: 121,274,458).

**Scope:** Release described by the cited source

**Release:** Main metadata/API snapshot, verified 2026-11-01. **Year:** 2025.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** energy; forces; stress; magnetic moments where present.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [homepage](https://huggingface.co/datasets/LeMaterial/LeMat-Traj)

**Count derivation:** sum of five published config row counts; 112,932,152 + 7,259,866 + 497,451 + 172,366 + 412,623 = 121,274,458.

**Evidence:**

- [LeMat-Traj — primary documentation](https://huggingface.co/datasets/LeMaterial/LeMat-Traj) (checked 2026-11-01): Config metadata and datasets-server API report 112,932,152 PBE, 7,259,866 PBEsol, 497,451 r2SCAN, 172,366 SCAN and 412,623 non-compatible rows; their sum is 121,274,458.
- [LeMat-Traj dataset server metadata](https://datasets-server.huggingface.co/info?dataset=LeMaterial%2FLeMat-Traj) (checked 2026-11-01): API corroborates each of the five config row counts used in the sum.

**Reuse and interpretation notes:**

- Count is derived by summing the five configuration-row counts, not the number of parent crystals.
- Narrative per-source tables in the card disagree with config metadata; the ranking uses metadata corroborated by the datasets-server API.
- Large overlap with Alexandria trajectories, MPtrj and upstream databases.

**Tags:** trajectories, multi-functional.

<a id="omat24"></a>
## Open Materials 2024 (OMat24)

Non-equilibrium inorganic DFT data generated through rattling, AIMD and relaxation.

**Size:** 101,849,946 atomic configurations (source wording: 101,849,946).

**Scope:** Release described by the cited source

**Release:** 2024-10-18 train + corrected 2024-12-20 validation. **Year:** 2024.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** energy; forces; stress.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [homepage](https://huggingface.co/datasets/facebook/OMAT24) · [data](https://huggingface.co/datasets/facebook/OMAT24) · [paper](https://doi.org/10.1038/s43588-026-00996-w) · [code](https://github.com/facebookresearch/fairchem)

**Count derivation:** train + corrected validation; excludes sAlex and overlapping 1M subsplit; 100,824,585 + 1,025,361 = 101,849,946.

**Evidence:**

- [Open Materials 2024 (OMat24) — primary documentation](https://huggingface.co/datasets/facebook/OMAT24) (checked 2026-11-01): Card reports 100,824,585 training and 1,025,361 corrected validation configurations for OMat24 itself.

**Reuse and interpretation notes:**

- Rank uses explicitly listed main train+validation rows; the paper headline >110 million calculations has a broader scope.
- sAlex is hosted on the same card and listed separately here; the 1M subsplit is not additional data.
- Original validation data contained duplicates; corrected validation was uploaded 2024-12-20.

**Tags:** None assigned.

<a id="elementa-public"></a>
## ELEMENTA public core release

Low-prior DFT-labeled atomic configurations with explicitly bounded composition coverage.

**Size:** ~39,000,000 atomic configurations (source wording: nearly 39 million).

**Scope:** Release described by the cited source

**Release:** First public release; card checked 2026-11-01. **Year:** 2026.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** structure; DFT energy and force targets.

**Access:** open. **Dataset license:** CC BY-NC 4.0.

**Official routes:** [homepage](https://huggingface.co/datasets/kairosmaterial/ELEMENTA)

**Evidence:**

- [ELEMENTA public core release — primary documentation](https://huggingface.co/datasets/kairosmaterial/ELEMENTA) (checked 2026-11-01): Public card describes nearly 39 million core frames and a separate complete 4.7 million-frame Spin archive.

**Reuse and interpretation notes:**

- This public subset is smaller than the full 210-million-frame corpus described by the authors.
- Nearly 39 million is a rounded provider figure; archives were not downloaded or independently counted.
- Separate Spin archive is not included in this row.

**Tags:** None assigned.

<a id="salex25"></a>
## sAlex25

Alexandria subset for interatomic-potential training from structural relaxation paths.

**Size:** ~14,000,000 out-of-equilibrium configurations (source wording: ~14 million).

**Scope:** Release described by the cited source

**Release:** sAlex25; 2026 expansion paper. **Year:** 2026.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** energy; forces; stress.

**Access:** open. **Dataset license:** CC BY 4.0 (Alexandria provider terms).

**Official routes:** [homepage](https://alexandria.icams.rub.de/datasets.html) · [data](https://alexandria.icams.rub.de/datasets.html) · [paper](https://doi.org/10.1088/2515-7639/ae6620)

**Evidence:**

- [sAlex25 — primary documentation](https://doi.org/10.1088/2515-7639/ae6620) (checked 2026-11-01): 2026 primary expansion paper describes sAlex25 as 14 million out-of-equilibrium structures containing forces and stresses.

**Reuse and interpretation notes:**

- Version differs from the sAlex supplied with OMat24; versions and parent trajectories overlap.
- Do not add trajectory frames to the Alexandria equilibrium-structure total.

**Tags:** None assigned.

<a id="salex-omat24"></a>
## sAlex (OMat24 distribution)

Subsampled Alexandria trajectories supplied with the OMat24 release.

**Size:** 11,000,983 atomic configurations (source wording: 11,000,983).

**Scope:** Release described by the cited source

**Release:** 2024-10-18 sAlex train/validation. **Year:** 2024.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** energy; forces; stress.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [homepage](https://huggingface.co/datasets/facebook/OMAT24)

**Count derivation:** sAlex train + validation; 10,447,765 + 553,218 = 11,000,983.

**Evidence:**

- [sAlex (OMat24 distribution) — primary documentation](https://huggingface.co/datasets/facebook/OMAT24) (checked 2026-11-01): Card lists sAlex train=10,447,765 and validation=553,218.

**Reuse and interpretation notes:**

- Separate from the main OMat24 generated data, but overlaps Alexandria and later sAlex releases.

**Tags:** None assigned.

<a id="elementa-spin"></a>
## ELEMENTA Spin

DFT-resolved magnetic initializations distributed alongside ELEMENTA.

**Size:** ~4,700,000 magnetic configuration frames (source wording: ~4.7 million).

**Scope:** Release described by the cited source

**Release:** Provider page snapshot, checked 2026-11-01. **Year:** 2026.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** structure; magnetic-state energy landscape.

**Access:** open. **Dataset license:** CC BY-NC 4.0.

**Official routes:** [homepage](https://huggingface.co/datasets/kairosmaterial/ELEMENTA)

**Evidence:**

- [ELEMENTA Spin — primary documentation](https://huggingface.co/datasets/kairosmaterial/ELEMENTA) (checked 2026-11-01): Card identifies the separate ELEMENTA_spin.extxyz archive as the complete 4.7 million-frame Spin dataset.

**Reuse and interpretation notes:**

- Magnetic initializations are configurations, not 4.7 million distinct crystals.
- Shares the ELEMENTA family and hosting page.

**Tags:** None assigned.

<a id="mptrj"></a>
## Materials Project Trajectory (MPtrj)

Selected GGA/GGA+U static and relaxation frames used to train CHGNet.

**Size:** 1,580,395 atomic configurations (source wording: 1,580,395).

**Scope:** Release described by the cited source

**Release:** MP 2022.9-derived MPtrj / 2023 release. **Year:** 2023.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** energy; forces; stress; magnetic moments; band gap where present.

**Access:** open. **Dataset license:** MIT (Figshare dataset record).

**Official routes:** [homepage](https://github.com/CederGroupHub/chgnet) · [data](https://doi.org/10.6084/m9.figshare.23713842) · [paper](https://doi.org/10.1038/s42256-023-00716-3)

**Evidence:**

- [Materials Project Trajectory (MPtrj) — primary documentation](https://api.figshare.com/v2/articles/23713842) (checked 2026-11-01): Figshare description gives 1,580,395 structures and energies from MP version 2022.9; record license is MIT.

**Reuse and interpretation notes:**

- Frames derive from roughly 146k parent compounds; not 1.58 million materials.
- Missing magnetic moments are null, not zero; stress sign and units need explicit conversion.
- Overlaps the source MP database and LeMat trajectories.

**Tags:** None assigned.

<a id="mp-aloe"></a>
## MP-ALOE

Active-learning r2SCAN data emphasizing off-equilibrium inorganic structures.

**Size:** 909,792 DFT configuration frames (source wording: 909,792).

**Scope:** Release described by the cited source

**Release:** 2025 published dataset. **Year:** 2025.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** r2SCAN energy; forces; stress.

**Access:** open. **Dataset license:** Not verified for downloadable dataset.

**Official routes:** [homepage](https://doi.org/10.1038/s41524-025-01834-9) · [paper](https://arxiv.org/abs/2507.05559) · [data](https://doi.org/10.1038/s41524-025-01834-9)

**Evidence:**

- [MP-ALOE — primary documentation](https://doi.org/10.1038/s41524-025-01834-9) (checked 2026-11-01): Primary paper reports 909,792 frames from 303,264 three-step structure relaxations, covering 89 elements.

**Reuse and interpretation notes:**

- The approximately 100 million generated candidates are a selection pool, not the DFT-labeled release.
- Paper data-availability section gives the distribution route; exact dataset license was not verified in this audit.

**Tags:** None assigned.

<a id="matpes"></a>
## MatPES

Compact potential-energy-surface data sampled from extensive MD and labeled with PBE and r2SCAN.

**Size:** ~400,000 sampled configurations (source wording: ~400,000).

**Scope:** Release described by the cited source

**Release:** 2025.1 size reference; 2025.2 available since 2026-04-15. **Year:** 2025.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** PBE/r2SCAN energy; forces; stress; atomic charges in 2025.2.

**Access:** open. **Dataset license:** BSD 3-Clause (Hugging Face dataset card).

**Official routes:** [homepage](https://matpes.ai/) · [data](https://huggingface.co/datasets/materialyze/matpes) · [paper](https://arxiv.org/abs/2503.04070) · [code](https://github.com/materialyzeai/matpes)

**Evidence:**

- [MatPES — primary documentation](https://github.com/materialyzeai/matpes) (checked 2026-11-01): Author repository describes the initial 2025.1 release as about 400,000 structures; 2025.2 adds charge labels and removes a small number of duplicates.

**Reuse and interpretation notes:**

- 400k is a rounded original-release reference; exact 2025.2 rows were not independently verified.
- 281 million MD snapshots are the sampling pool, not 281 million DFT configurations.
- PBE and r2SCAN labels must not be counted as twice as many independent geometries.

**Tags:** None assigned.

<a id="alignn-ff"></a>
## ALIGNN-FF training dataset

JARVIS-derived force-field training structures and force labels.

**Size:** 307,113 energy-labeled configurations (source wording: 307,113).

**Scope:** Release described by the cited source

**Release:** 2023 ALIGNN-FF dataset. **Year:** 2023.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** energy; forces.

**Access:** open. **Dataset license:** Not verified for training download.

**Official routes:** [homepage](https://github.com/usnistgov/alignn) · [data](https://github.com/usnistgov/jarvis/blob/master/jarvis/db/figshare.py) · [paper](https://doi.org/10.1039/D2DD00096B)

**Evidence:**

- [ALIGNN-FF training dataset — primary documentation](https://doi.org/10.1039/D2DD00096B) (checked 2026-11-01): Primary ALIGNN-FF paper reports 307,113 energies and 3,197,795 force labels across 72,708 compounds.

**Reuse and interpretation notes:**

- Configuration count differs from parent-compound count and force-component count.
- Overlaps the JARVIS structure family.

**Tags:** None assigned.

<a id="mad15"></a>
## Massive Atomic Diversity (MAD-1.5)

Compact all-electron r2SCAN dataset spanning crystals, surfaces, clusters and molecules.

**Size:** 216,803 atomic configurations (source wording: 216,803).

**Scope:** Release described by the cited source

**Release:** MAD-1.5, arXiv v2. **Year:** 2026.

**Provenance:** computed. **Structure availability:** `mixed`.

**Labels/content:** r2SCAN energy; forces; stress for periodic subsets.

**Access:** open. **Dataset license:** Not verified for this archived version.

**Official routes:** [homepage](https://arxiv.org/html/2603.02089v2)

**Evidence:**

- [Massive Atomic Diversity (MAD-1.5) — primary documentation](https://arxiv.org/html/2603.02089v2) (checked 2026-11-01): Table 1 reports 216,803 structures across 14 subsets; the set contains both periodic and isolated configurations.

**Reuse and interpretation notes:**

- Includes isolated atoms, dimers, trimers and molecules; count is not periodic crystals alone.
- Non-spin-polarized electronic-structure settings limit magnetic applications.
- Newer MAD-1.6 archive is tracked separately; revisions overlap.

**Tags:** None assigned.

<a id="mpf2021"></a>
## MPF.2021.2.8

Selected Materials Project snapshots used for the universal M3GNet potential.

**Size:** 187,687 ionic-step configurations (source wording: 187,687).

**Scope:** Release described by the cited source

**Release:** 2021-02-08 source / original MPF release. **Year:** 2022.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** energy; forces; stress.

**Access:** open. **Dataset license:** CC BY 4.0 (Figshare record).

**Official routes:** [homepage](https://github.com/materialsvirtuallab/m3gnet) · [data](https://doi.org/10.6084/m9.figshare.19470599) · [paper](https://doi.org/10.1038/s41524-024-01227-4)

**Evidence:**

- [MPF.2021.2.8 — primary documentation](https://www.nature.com/articles/s41524-024-01227-4) (checked 2026-11-01): Primary DIRECT-sampling paper states 187,687 ionic steps from 62,783 MP compounds as of 2021-02-08.

**Reuse and interpretation notes:**

- A subset of MP trajectories, not an independent collection of new compounds.
- Figshare notes version reversion and pymatgen compatibility requirements.

**Tags:** None assigned.

<a id="carbon-data-gap17"></a>
## Carbon-data synthetic atomistic trajectories

Carbon melt–quench–anneal trajectories spanning crystalline, graphitic and amorphous environments, labeled by C-GAP-17.

**Size:** 114,660 MD snapshots (source wording: 546 trajectories × 210 snapshots = 114,660 snapshots).

**Scope:** Arithmetic from provider trajectory and per-trajectory snapshot counts; raw trajectory files not independently enumerated

**Release:** Provider README, checked 2026-11-01. **Year:** 2022.

**Provenance:** computed. **Structure availability:** `mixed`.

**Labels/content:** synthetic local energies; forces; density; temperature; time.

**Access:** open. **Dataset license:** Not verified.

**Official routes:** [homepage](https://github.com/jla-gardner/carbon-data) · [data](https://github.com/jla-gardner/carbon-data/tree/main/results) · [paper](https://arxiv.org/abs/2211.16443)

Other denominators (not added to the ranking):

- 546 trajectories: Provider-described uncorrelated runs
- 22,932,000 atomic environments: 546 × 210 snapshots × 200 atoms; headline rounded to 22.9 million

**Evidence:**

- [Carbon-data author README](https://raw.githubusercontent.com/jla-gardner/carbon-data/main/README.md) (checked 2026-11-01): Specifies 546 trajectories, 210 snapshots each and 200 atoms per snapshot; labels come from C-GAP-17.

**Reuse and interpretation notes:**

- The 22.9-million headline counts atomic environments, not structures or materials.
- Energies and forces are generated by a fitted potential, not newly calculated DFT reference labels.
- Includes amorphous and molecular-like carbon environments alongside crystalline phases.
- Data licence was not verified.

**Tags:** carbon, synthetic-labels, MD, collection-blaiszik.

<a id="mad16"></a>
## Massive Atomic Diversity (MAD-1.6)

Updated mixed-domain r2SCAN reference set with a compatible PBE subset.

**Size:** Unranked atomic configurations (source wording: Not verified).

**Scope:** Release described by the cited source

**Release:** MAD-1.6 archive, October 2026. **Year:** 2026.

**Provenance:** computed. **Structure availability:** `mixed`.

**Labels/content:** energy; forces; stress where available.

**Access:** open. **Dataset license:** CC BY 4.0 (Materials Cloud archive metadata).

**Official routes:** [homepage](https://archive.materialscloud.org/records/ffd5a-1hc37)

**Evidence:**

- [Massive Atomic Diversity (MAD-1.6) — primary documentation](https://archive.materialscloud.org/records/ffd5a-1hc37) (checked 2026-11-01): Archive README identifies MAD-1.6 train/validation/test and rejected-frame files, plus a PBE subset; no independently verified total used here.
- [MAD-1.6 Materials Cloud metadata](https://archive.materialscloud.org/api/records/ffd5a-1hc37) (checked 2026-11-01): Archive rights metadata identify CC BY 4.0; this audit did not recount the configuration payloads.

**Reuse and interpretation notes:**

- A current archive exists, but total frame count has not been verified; do not substitute the MAD-1.5 total.
- Rejected frames and PBE recomputations should not be added blindly to r2SCAN geometry counts.

**Tags:** None assigned.

<a id="openlam-training"></a>
## OpenLAM TrainingSet

Multitask collection for large atomistic models covering solids, surfaces, liquids and molecular systems.

**Size:** Unranked atomic configurations (source wording: Not verified).

**Scope:** Release described by the cited source

**Release:** OpenLAM-TrainingSet-v1 (2025); later model variants use revised collections. **Year:** 2025.

**Provenance:** computed. **Structure availability:** `mixed`.

**Labels/content:** energy; forces; virial where present.

**Access:** mixed. **Dataset license:** Not verified.

**Official routes:** [homepage](https://www.aissquare.com/datasets/detail?pageType=datasets&name=OpenLAM-TrainingSet-v1&id=308)

**Evidence:**

- [OpenLAM TrainingSet — primary documentation](https://www.aissquare.com/datasets/detail?pageType=datasets&name=OpenLAM-TrainingSet-v1&id=308) (checked 2026-11-01): LAMBench and DPA-3 primary documentation identify AIS Square as the public training-set distribution; no consistently verified total was extracted.

**Reuse and interpretation notes:**

- Collection overlaps upstream public datasets and includes non-crystal domains.
- Model parameter counts (3M, 5M, 7M) are not dataset sizes.
- License and downloadable counts must be checked for the selected component/version.

**Tags:** None assigned.
