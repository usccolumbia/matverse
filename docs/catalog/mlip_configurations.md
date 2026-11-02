# Bulk and mixed-domain MLIP configurations

[Back to MatVerse](../../README.md)

Checked 2026-11-02. Counts are source-reported or explicitly derived from release metadata; full datasets were not independently deduplicated.

<a id="cosmos-sevennet-omni"></a>
## COSMOSDataset

COSMOS Dataset (Combined Organic, Surface and Materials Open Source Dataset) aggregates 15 publicly available ab initio databases spanning molecules, inorganic crystals, metal and oxide surfaces, and metal-organic frameworks, covering levels of theory from generalized gradient approximation to hybrid functionals. It also includes a domain-bridging set, sampled from OC20, OC22, MatPES, ODAC23, OMol25, and QCML dataset and recomputed with MPtrj-consistent computational settings, which facilitates cross-domain knowledge transfer in a multi-task training framework. For detailed information about the dataset composition, see Table 1 from [the paper](https://arxiv.org/abs/2510.11241).

**Size:** 242,788,218 aggregate configurations (source wording: 242,788,218).

**Scope:** Benchmark-reported242,788,218 configurations in the COSMOS training assembly; not a single deposited payload or deduplicated crystal population.

**Release:** COSMOSDataset release as listed in Matbench Discovery at 8869a883a506. **Year:** 2025.

**Provenance:** Fifteen pre-existing ab-initio datasets plus a new domain-bridging DFT layer; heterogeneous computational settings. **Structure availability:** `mixed`.

**Labels/content:** cross-domain structures; energies; forces; multiple levels of theory.

**Access:** mixed. **Dataset license:** CC-BY-4.0 declared for assembly/deposit; individual parent terms retained.

**Official routes:** [homepage](https://figshare.com/articles/software/SevenNet-Omni_checkpoint/30399814) · [data](https://figshare.com/articles/software/SevenNet-Omni_checkpoint/30399814) · [paper](https://doi.org/10.1038/s41467-026-70195-8)

**Evidence:**

- [Matbench Discovery datasets table](https://matbench-discovery.materialsproject.org/data/sets) (checked 2026-11-01): Listed COSMOSDataset: 242,788,218 configurations/structures; role training, created 2025-10-21, declared data license CC-BY-4.0. Counts and access refer to this listed release.
- [Pinned Matbench Discovery dataset metadata](https://github.com/janosh/matbench-discovery/blob/8869a883a5067015b815886d878bd7aaa3862d2d/data/datasets.yml) (checked 2026-11-01): Machine-readable COSMOSDataset entry at revision 8869a883a5067015b815886d878bd7aaa3862d2d; retains structure/material counting distinction and release caveats.
- [SevenNet-Omni domain-bridging deposit](https://api.figshare.com/v2/articles/30399814) (checked 2026-11-01): Provider confirms15 open-source parent datasets plus a DBS recomputation layer, links parent domains and describes db_label source provenance. Deposit distributes DBS and benchmark/DFT results, not a monolithic242.8M-frame parent archive.

**Reuse and interpretation notes:**

- Overlaps parent datasets and other named splits/releases; do not add these counts to independent-material totals.
- Mixed molecular, bulk, surface and MOF domains. Access and rights of original parents must be checked individually; listed CC BY4.0 metadata does not replace each parent license.
- SevenNet-Omni DBS already has its own catalog entry; this umbrella is overlapping assembly metadata.

**Tags:** Matbench-sets-20261101, COSMOSDataset, Matbench Discovery, training, aggregate-overlap, Matbench-Discovery-data-sets-20261101.

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

<a id="solid26"></a>
## SoLiD26 solid–liquid interface configurations

Aqueous metal/electrode–electrolyte interfaces and selected liquid/solid references from VASP PBE+D3 calculations.

**Size:** 15,379,823 atomic configuration frames (source wording: 15,379,823).

**Scope:** Aqueous metal/electrode–electrolyte interfaces and selected liquid/solid references from VASP PBE+D3 calculations.

**Release:** Materials Cloud 2026.189 v1; preprint v2 (2026-10-21). **Year:** 2026.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** positions and periodic cell; total energy; atomic forces; ASE constraints.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [paper](https://arxiv.org/abs/2609.28013v2) · [data](https://doi.org/10.24435/materialscloud:yp-vw) · [repository](https://github.com/team-capex/SoLiD26)

**Evidence:**

- [SoLiD26 revised preprint](https://arxiv.org/html/2609.28013v2) (checked 2026-11-01): Reports 15,379,823 configurations, up to 576 atoms and 15 elements; revised Data Availability links the public archive.
- [Materials Cloud SoLiD26 v1](https://archive.materialscloud.org/records/azpq0-1qe97) (checked 2026-11-01): Published 2026-10-13, open under CC BY 4.0; lists 16 compressed ASE-LMDB shards, checksums, README and split indices.

**Reuse and interpretation notes:**

- Frames derive mainly from AIMD, not 15.38 million independent equilibrium crystals.
- The first preprint said available by request; the revised paper and October public deposit supersede that access statement.
- ASE fixed-atom constraints can zero returned forces; provider directs users to raw forces or get_forces(apply_constraint=False).
- Full 63.8 GiB compressed release was not downloaded or independently recounted.

**Tags:** additional-materials-20261101.

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

<a id="salex-omat24-validation"></a>
## Subsampled Alexandria Validation Set

Validation subset of the subsampled Alexandria dataset, containing ~500k structures for evaluating model performance during training. Filtered to remove structure prototype overlap with WBM.

**Size:** 553,218 configurations (source wording: 553,218).

**Scope:** sAlex Validation: validation release listed by Matbench Discovery; numerical count is source-reported, not a MatVerse payload recount.

**Release:** sAlex Validation release as listed in Matbench Discovery at 8869a883a506. **Year:** 2024.

**Provenance:** DFT calculations; source-reported release metadata. **Structure availability:** `periodic_atomic`.

**Labels/content:** atomic coordinates; energies (eV); forces (eV/Å); stress (eV/Å³).

**Access:** open. **Dataset license:** CC-BY-4.0 (provider/benchmark release declaration).

**Official routes:** [homepage](https://huggingface.co/datasets/fairchem/OMAT24#salex-dataset) · [data](https://dl.fbaipublicfiles.com/opencatalystproject/data/omat/241018/sAlex/val.tar.gz) · [paper](https://doi.org/10.48550/arXiv.2410.12771)

Other denominators (not added to the ranking):

- 170,905 source-defined parent materials: Benchmark metadata denominator; see release notes for identity definition. Not added to configurations.

**Evidence:**

- [Matbench Discovery datasets table](https://matbench-discovery.materialsproject.org/data/sets) (checked 2026-11-01): Listed sAlex Validation: 553,218 configurations/structures; role validation, created 2024-10-16, declared data license CC-BY-4.0. Counts and access refer to this listed release.
- [Pinned Matbench Discovery dataset metadata](https://github.com/janosh/matbench-discovery/blob/8869a883a5067015b815886d878bd7aaa3862d2d/data/datasets.yml) (checked 2026-11-01): Machine-readable sAlex Validation entry at revision 8869a883a5067015b815886d878bd7aaa3862d2d; retains structure/material counting distinction and release caveats.
- [OMat24 and sAlex provider card](https://huggingface.co/datasets/fairchem/OMAT24) (checked 2026-11-01): Provider table separates10,447,765 training frames from553,218 validation frames. This entry counts only the validation subset.

**Reuse and interpretation notes:**

- Overlaps parent datasets and other named splits/releases; do not add these counts to independent-material totals.
- Contained in existing sAlex train+validation catalog aggregate; not additive to that entry.

**Tags:** Matbench-sets-20261101, sAlex Validation, Matbench Discovery, validation, release-subset, Matbench-Discovery-data-sets-20261101.

<a id="matpes-pbe-2025-1"></a>
## MatPES2025.1 — PBE

A dataset containing 434,712 structures from ~300K molecular dynamics simulations, providing potential energy surfaces that are valuable for training ML interatomic potentials.

**Size:** 434,712 configurations (source wording: 434,712).

**Scope:** Frozen2025.1 PBE labels: 434,712 matpes_id configurations from 110,317 parent MP IDs according to benchmark recount; not the corrected2025.2 release.

**Release:** MatPES PBE release as listed in Matbench Discovery at 8869a883a506. **Year:** 2025.

**Provenance:** DFT calculations; source-reported release metadata. **Structure availability:** `periodic_atomic`.

**Labels/content:** atomic coordinates; energy; forces; stress.

**Access:** open. **Dataset license:** Not verified for frozen2025.1 payload: current Hugging Face dataset card declares BSD-3-Clause; Matbench registry lists MIT. Verify release-specific data terms..

**Official routes:** [homepage](https://matpes.ai) · [data](https://s3.us-east-1.amazonaws.com/materialsproject-contribs/MatPES_2025_1/MatPES-PBE-2025.1.json.gz) · [paper](https://doi.org/10.48550/arXiv.2503.04070)

Other denominators (not added to the ranking):

- 110,317 source-defined parent materials: Benchmark metadata denominator; see release notes for identity definition. Not added to configurations.

**Evidence:**

- [Matbench Discovery datasets table](https://matbench-discovery.materialsproject.org/data/sets) (checked 2026-11-01): Listed MatPES PBE: 434,712 configurations/structures; role training, created 2025-03-06, declared data license MIT. Counts and access refer to this listed release.
- [Pinned Matbench Discovery dataset metadata](https://github.com/janosh/matbench-discovery/blob/8869a883a5067015b815886d878bd7aaa3862d2d/data/datasets.yml) (checked 2026-11-01): Machine-readable MatPES PBE entry at revision 8869a883a5067015b815886d878bd7aaa3862d2d; retains structure/material counting distinction and release caveats.
- [MatPES provider version and format documentation](https://github.com/materialyzeai/matpes) (checked 2026-11-01): Provider identifies2025.1 initial release and newer2025.2 release with duplicate removal and Bader/DDEC6 charges; supports version-specific PBE and r2SCAN downloads. Numeric2025.1 counts retained from benchmark metadata.
- [MatPES current dataset card licensing](https://huggingface.co/datasets/materialyze/matpes/blob/main/README.md) (checked 2026-11-01): Front matter explicitly declares license:bsd-3-clause. This conflicts with the Matbench registryMIT label; the2025.1 frozen-file terms were not independently resolved.

**Reuse and interpretation notes:**

- Counted 434,712 distinct matpes_id records and 110,317 distinct provenance.original_mp_id values in MatPES-PBE-2025.1.json.gz (https://s3.us-east-1.amazonaws.com/materialsproject-contribs/MatPES_2025_1/MatPES-PBE-2025.1.json.gz). Materials counts the parent MP materials across the sampled MD frames.
- Overlaps parent datasets and other named splits/releases; do not add these counts to independent-material totals.
- PBE and r2SCAN geometries overlap but computed labels differ. A default SDK request now returns2025.2, so specify2025.1 to reproduce this card.
- License-source mismatch: the current Hugging Face dataset card declares BSD-3-Clause, while the benchmark registry lists MIT. A code-repository badge is not sufficient to establish the frozen2025.1 data license.

**Tags:** Matbench-sets-20261101, MatPES PBE, Matbench Discovery, training, release-subset, Matbench-Discovery-data-sets-20261101.

<a id="matpes"></a>
## MatPES

Compact potential-energy-surface data sampled from extensive MD and labeled with PBE and r2SCAN.

**Size:** ~400,000 sampled configurations (source wording: ~400,000).

**Scope:** Release described by the cited source

**Release:** 2025.1 size reference; 2025.2 available since 2026-04-15. **Year:** 2025.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** PBE/r2SCAN energy; forces; stress; atomic charges in 2025.2.

**Access:** open. **Dataset license:** BSD 3-Clause (current Hugging Face dataset card); Matbench directory lists MIT, so verify historical frozen-release terms separately..

**Official routes:** [homepage](https://matpes.ai/) · [data](https://huggingface.co/datasets/materialyze/matpes) · [paper](https://arxiv.org/abs/2503.04070) · [code](https://github.com/materialyzeai/matpes)

**Evidence:**

- [MatPES — primary documentation](https://github.com/materialyzeai/matpes) (checked 2026-11-01): Author repository describes the initial 2025.1 release as about 400,000 structures; 2025.2 adds charge labels and removes a small number of duplicates.
- [MatPES current provider data card](https://huggingface.co/datasets/MatPES/MatPES) (checked 2026-11-01): Current data-card metadata declares BSD-3-Clause, conflicting with the MIT license listed by the benchmark directory; exact historical release terms require separate verification.

**Reuse and interpretation notes:**

- 400k is a rounded original-release reference; exact 2025.2 rows were not independently verified.
- 281 million MD snapshots are the sampling pool, not 281 million DFT configurations.
- PBE and r2SCAN labels must not be counted as twice as many independent geometries.
- License provenance correction: the current provider data card declares BSD-3-Clause while the benchmark lists MIT; do not treat a code license as confirmed dataset terms. Verify the terms for the exact downloaded release.

**Tags:** None assigned.

<a id="matpes-r2scan-2025-1"></a>
## MatPES2025.1 — r2SCAN

A dataset containing 387,897 structures from ~300K molecular dynamics simulations, providing potential energy surfaces that are valuable for training ML interatomic potentials.

**Size:** 387,897 configurations (source wording: 387,897).

**Scope:** Frozen2025.1 r2SCAN labels: 387,897 matpes_id configurations from 89,719 parent MP IDs according to benchmark recount; not the corrected2025.2 release.

**Release:** MatPES r2SCAN release as listed in Matbench Discovery at 8869a883a506. **Year:** 2025.

**Provenance:** DFT calculations; source-reported release metadata. **Structure availability:** `periodic_atomic`.

**Labels/content:** atomic coordinates; energy; forces; stress.

**Access:** open. **Dataset license:** Not verified for frozen2025.1 payload: current Hugging Face dataset card declares BSD-3-Clause; Matbench registry lists MIT. Verify release-specific data terms..

**Official routes:** [homepage](https://matpes.ai) · [data](https://s3.us-east-1.amazonaws.com/materialsproject-contribs/MatPES_2025_1/MatPES-R2SCAN-2025.1.json.gz) · [paper](https://doi.org/10.48550/arXiv.2503.04070)

Other denominators (not added to the ranking):

- 89,719 source-defined parent materials: Benchmark metadata denominator; see release notes for identity definition. Not added to configurations.

**Evidence:**

- [Matbench Discovery datasets table](https://matbench-discovery.materialsproject.org/data/sets) (checked 2026-11-01): Listed MatPES r2SCAN: 387,897 configurations/structures; role training, created 2025-03-06, declared data license MIT. Counts and access refer to this listed release.
- [Pinned Matbench Discovery dataset metadata](https://github.com/janosh/matbench-discovery/blob/8869a883a5067015b815886d878bd7aaa3862d2d/data/datasets.yml) (checked 2026-11-01): Machine-readable MatPES r2SCAN entry at revision 8869a883a5067015b815886d878bd7aaa3862d2d; retains structure/material counting distinction and release caveats.
- [MatPES provider version and format documentation](https://github.com/materialyzeai/matpes) (checked 2026-11-01): Provider identifies2025.1 initial release and newer2025.2 release with duplicate removal and Bader/DDEC6 charges; supports version-specific PBE and r2SCAN downloads. Numeric2025.1 counts retained from benchmark metadata.
- [MatPES current dataset card licensing](https://huggingface.co/datasets/materialyze/matpes/blob/main/README.md) (checked 2026-11-01): Front matter explicitly declares license:bsd-3-clause. This conflicts with the Matbench registryMIT label; the2025.1 frozen-file terms were not independently resolved.

**Reuse and interpretation notes:**

- Counted 387,897 distinct matpes_id records and 89,719 distinct provenance.original_mp_id values in MatPES-R2SCAN-2025.1.json.gz (https://s3.us-east-1.amazonaws.com/materialsproject-contribs/MatPES_2025_1/MatPES-R2SCAN-2025.1.json.gz). Materials counts the parent MP materials across the sampled MD frames.
- Overlaps parent datasets and other named splits/releases; do not add these counts to independent-material totals.
- PBE and r2SCAN geometries overlap but computed labels differ. A default SDK request now returns2025.2, so specify2025.1 to reproduce this card.
- License-source mismatch: the current Hugging Face dataset card declares BSD-3-Clause, while the benchmark registry lists MIT. A code-repository badge is not sufficient to establish the frozen2025.1 data license.

**Tags:** Matbench-sets-20261101, MatPES r2SCAN, Matbench Discovery, training, release-subset, Matbench-Discovery-data-sets-20261101.

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

<a id="polyanion-sodium-cathode-2025"></a>
## Polyanion sodium cathode atomic structure and dynamics

Periodic DFT cathode configurations with energies, forces, magnetic moments and Bader charges for a subset.

**Size:** 298,144 periodic atomic configurations (source wording: 298,144 configurations; 113,532 with atomic charges).

**Scope:** Combined dataset including 113,532 charge-labeled structures and 184,612 additional optimization configurations.

**Release:** DTU Data 27202446 v5, publication release. **Year:** 2025.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** periodic structure; total energy; atomic forces; atomic magnetic moments; Bader charges for subset; 1000 K ionic dynamics.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [homepage](https://doi.org/10.11583/DTU.27202446.v5) · [data](https://doi.org/10.11583/DTU.27202446.v5) · [paper](https://doi.org/10.1038/s41597-025-05799-8) · [code](https://github.com/dtu-energy/cathode-generation-workflow)

Other denominators (not added to the ranking):

- 113,532 charge-labeled configurations: Subset of the complete 298,144 configurations
- 184,612 additional configurations without charges: Completes the 298,144-configuration release

**Evidence:**

- [DTU author release v5](https://api.figshare.com/v2/articles/27202446/versions/5) (checked 2026-11-01): Release states 113,532 charge-labeled and 184,612 additional configurations, with a complete 298,144-configuration Combined.xyz; declares CC BY 4.0 and fixes charge signs in v5.
- [Primary sodium cathode descriptor](https://www.nature.com/articles/s41597-025-05799-8) (checked 2026-11-01): Covers four polyanionic cathode structure types with Fe/Mn/Co/Ni, sampling optimization, AIMD and active-learning MD configurations.

**Reuse and interpretation notes:**

- Configurations are highly correlated frames/optimization steps, not unique compounds.
- Combined.xyz files and per-family/submethod files overlap; do not add all file counts.
- Only 113,532 configurations have Bader charges.
- MD sampling temperature is 1000 K; this is not a database of measured room-temperature conductivity.

**Tags:** sodium-ion, battery-cathodes, MLIP, charge, forces, property-focused, OpenAlex-survey-20261101, Scientific-Data-descriptor.

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

<a id="sevennet-omni-dbs"></a>
## SevenNet-Omni domain-bridging set (DBS)

New single-point DFT labels align geometries sampled across molecular, bulk, surface and MOF parent datasets.

**Size:** ~125,000 cross-domain DFT configuration records (source wording: 125,000).

**Scope:** New single-point DFT labels align geometries sampled across molecular, bulk, surface and MOF parent datasets.

**Release:** Primary release/documentation checked 2026-11-01. **Year:** 2026.

**Provenance:** computed. **Structure availability:** `mixed`.

**Labels/content:** energy; forces; periodic/molecular geometry; db_label source identifiers.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [paper](https://doi.org/10.1038/s41467-026-70195-8) · [data](https://doi.org/10.6084/m9.figshare.30399814.v3)

**Evidence:**

- [SevenNet-Omni paper](https://arxiv.org/html/2510.11241v3) (checked 2026-11-01): Methods reports about 125,000 DBS geometries selected from MatPES, OC20, OC22, ODAC23, OMol25 and QCML with new compatible VASP single points.
- [DBS Figshare v3 metadata](https://api.figshare.com/v2/articles/30399814) (checked 2026-11-01): CC BY 4.0; identifies dbs_total.extxyz (779,700,511 bytes), parent-source db_label semantics and separate benchmark/model files.

**Reuse and interpretation notes:**

- The count is the bridging set, not the much larger 15-dataset aggregate used to train the model.
- Geometries overlap existing parent corpora; new labels do not imply new independent material identities.
- Includes isolated molecules and other non-crystal domains; select the periodic subset for solid-only work.
- Large DBS payload not downloaded; approximate paper count retained.

**Tags:** additional-materials-20261101.

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

<a id="mad-original-2025"></a>
## Massive Atomic Diversity

Compact training corpus spanning 85 elements, including bulk and two-dimensional crystals, surfaces, clusters, molecular crystals, and molecular fragments. Uses consistent all-electron DFT calculations for PET-MAD potentials.

**Size:** 95,595 configurations (source wording: 95,595).

**Scope:** 95,595 configurations reported for the filtered original MAD/PET-MAD benchmark cohort; not MAD-1.5 or MAD-1.6 and not an independently recounted archive.

**Release:** MAD release as listed in Matbench Discovery at 8869a883a506. **Year:** 2025.

**Provenance:** DFT calculations; source-reported release metadata. **Structure availability:** `mixed`.

**Labels/content:** atomic coordinates; PBEsol energies; forces; AiiDA provenance.

**Access:** open. **Dataset license:** CC-BY-4.0 (provider/benchmark release declaration).

**Official routes:** [homepage](https://www.nature.com/articles/s41597-025-06109-y) · [data](https://archive.materialscloud.org/records/h41qv-1n493) · [paper](https://doi.org/10.1038/s41597-025-06109-y)

**Evidence:**

- [Matbench Discovery datasets table](https://matbench-discovery.materialsproject.org/data/sets) (checked 2026-11-01): Listed MAD: 95,595 configurations/structures; role training, created 2025-09-25, declared data license CC-BY-4.0. Counts and access refer to this listed release.
- [Pinned Matbench Discovery dataset metadata](https://github.com/janosh/matbench-discovery/blob/8869a883a5067015b815886d878bd7aaa3862d2d/data/datasets.yml) (checked 2026-11-01): Machine-readable MAD entry at revision 8869a883a5067015b815886d878bd7aaa3862d2d; retains structure/material counting distinction and release caveats.
- [Original PET-MAD Materials Cloud release](https://archive.materialscloud.org/records/h41qv-1n493) (checked 2026-11-01): 2025-09-25 versioned deposit contains data.tar.gz, scripts, README and AiiDA archive; declares CC BY4.0.95,595filtered count is retained from benchmark metadata.

**Reuse and interpretation notes:**

- The PET-MAD paper (https://www.nature.com/articles/s41467-025-65662-7) reports 95,595 configurations after filtering. The Materials Cloud release includes training, validation, and test splits and AiiDA provenance.
- Overlaps parent datasets and other named splits/releases; do not add these counts to independent-material totals.
- Mixed stable/modified solids, molecules, clusters and surfaces; this count is not a number of bulk equilibrium crystals.

**Tags:** Matbench-sets-20261101, MAD, Matbench Discovery, training, release-subset, Matbench-Discovery-data-sets-20261101, Scientific-Data-descriptor.

<a id="nb-ta-v-bcc-dft"></a>
## Nb–Ta–V BCC solid-solution DFT configurations

Four VASP configuration/relaxation corpora for 128-site binary NbTa, NbV, TaV and ternary NbTaV alloys.

**Size:** 19,800 sampled starting alloy configurations (source wording: 19,800 sampled starting alloy configurations).

**Scope:** 3,100 configurations for each of three binaries plus 10,500 ternary configurations; trajectory steps and shared pure-element endpoints are additional/overlapping records.

**Release:** 2024 four-system release. **Year:** 2024.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** periodic structure; total energy; forces; stress; relaxation outputs.

**Access:** open. **Dataset license:** CC BY 4.0 (inspected Figshare mirrors).

**Official routes:** [paper](https://doi.org/10.1038/s41597-024-03720-3) · [data](https://doi.org/10.13139/OLCF/2217644)

**Evidence:**

- [Scientific Data primary data descriptor](https://doi.org/10.1038/s41597-024-03720-3) (checked 2026-11-01): Four VASP configuration/relaxation corpora for 128-site binary NbTa, NbV, TaV and ternary NbTaV alloys. 3,100 configurations for each of three binaries plus 10,500 ternary configurations; trajectory steps and shared pure-element endpoints are additional/overlapping records.
- [Primary repository release metadata](https://api.figshare.com/v2/articles/25824178) (checked 2026-11-01): Confirms public release files and stated dataset terms; response hashes are saved in provider receipts.

**Reuse and interpretation notes:**

- Configurations at fixed composition are alternative atomic arrangements, not unique compounds.
- Three binary datasets cover 31 compositions each; ternary covers 105.
- Raw output archives are many GB and were not downloaded; calculation-file inventory was verified in metadata.
- Ternary corpus is split into two Figshare parts; these are file parts, not independent datasets.

**Tags:** Scientific Data, survey:20261101, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="iaea-cascadesdb"></a>
## IAEA CascadesDB collision-cascade simulations

Atomistic irradiation-damage simulations for elemental metals, including collision cascades, vacancy clusters and dislocation debris.

**Size:** 17,024 collision-cascade simulations (source wording: 17,024).

**Scope:** Provider homepage reports 17,024 simulations distributed in 320 archives, approximately 815 GB.

**Release:** Live provider snapshot checked 2026-11-01. **Year:** 2026.

**Provenance:** IAEA-curated contributions from independently published molecular-dynamics radiation-damage studies. **Structure availability:** `periodic_atomic`.

**Labels/content:** atomic coordinates; PKA energy; temperature; interatomic potential; cascade duration; defect morphology.

**Access:** open. **Dataset license:** CC BY 4.0 for data and metadata unless individually stated otherwise.

**Official routes:** [Provider](https://cascadesdb.org/) · [Browse](https://cascadesdb.org/cdbmeta/browse) · [Documentation](https://cascadesdb.org/cdbmeta/doc) · [License](https://cascadesdb.org/licence/)

Other denominators (not added to the ranking):

- 320 archives: Live distribution archive count; not independent materials

**Evidence:**

- [IAEA CascadesDB homepage](https://cascadesdb.org/) (checked 2026-11-01): Live HTML states 17,024 simulations in 320 archives; deposits use plain-text XYZ files.
- [CascadesDB metadata specification](https://cascadesdb.org/cdbmeta/doc) (checked 2026-11-01): Documents material lattice, simulation box, recoil conditions, code and archive fields.
- [CascadesDB data licence](https://cascadesdb.org/licence/) (checked 2026-11-01): Explicitly applies CC BY 4.0 to data and metadata unless stated otherwise.

**Reuse and interpretation notes:**

- Simulations, archives and coordinate frames are different denominators.
- Elemental bulk, surfaces and initially damaged cells are mixed; inspect metadata before reuse.
- Underlying contributor releases may overlap other irradiation datasets.

**Tags:** irradiation, collision-cascades, vacancies, molecular-dynamics, additional-materials-20261101.

<a id="carbon-gap20"></a>
## Carbon GAP-20 DFT reference database

Carbon crystal, disordered and other atomistic reference configurations generated for fitting GAP-20.

**Size:** ~17,000 DFT atomic configurations (source wording: 17,000).

**Scope:** Carbon crystal, disordered and other atomistic reference configurations generated for fitting GAP-20.

**Release:** Primary release/documentation checked 2026-11-01. **Year:** 2020.

**Provenance:** computed. **Structure availability:** `mixed`.

**Labels/content:** atomic geometry; DFT energy; forces; potential-fitting configurations.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [paper](https://doi.org/10.1063/5.0005084) · [data](https://doi.org/10.17863/CAM.54529)

**Evidence:**

- [Cambridge Carbon GAP 20 deposit](https://www.repository.cam.ac.uk/items/ac362ef1-fa35-4bd4-8b56-2fde6d7b1d2c) (checked 2026-11-01): Declares CC BY 4.0; archive description identifies total generated training data (approximately 17,000 configurations) and a smaller selected fitting file.

**Reuse and interpretation notes:**

- Approximate count refers to the total generated database, not the selected fit or unique equilibrium carbon allotropes.
- Original GAP-20 and revised GAP-20U are related releases, not disjoint corpora.
- Archive metadata inspected; original full training archive not independently recounted.

**Tags:** additional-materials-20261101.

<a id="ti-ti64-multiphase"></a>
## Multiphase Ti and Ti-6Al-4V MLIP configurations

PBE-labelled periodic configurations spanning alpha, beta, omega and liquid titanium and Ti-6Al-4V.

**Size:** 15,563 selected training configurations (source wording: 15,563 selected training configurations).

**Scope:** Independently parsed final files: 6,640 frames in combined_data_oct24_2023.extxyz and 8,923 in ti64_combined_data_May30.extxyz; not a sum of all archive variants.

**Release:** Zenodo 15114121, 31 March 2025. **Year:** 2025.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** energy; atomic forces; virial stress; periodic structure.

**Access:** open. **Dataset license:** CC BY 4.0; British Crown Owned Copyright attribution retained in metadata.

**Official routes:** [paper](https://doi.org/10.1038/s41597-025-05302-3) · [data](https://doi.org/10.5281/zenodo.15114121)

**Evidence:**

- [Scientific Data primary data descriptor](https://doi.org/10.1038/s41597-025-05302-3) (checked 2026-11-01): PBE-labelled periodic configurations spanning alpha, beta, omega and liquid titanium and Ti-6Al-4V. Independently parsed final files: 6,640 frames in combined_data_oct24_2023.extxyz and 8,923 in ti64_combined_data_May30.extxyz; not a sum of all archive variants.
- [Primary repository release metadata](https://zenodo.org/api/records/15114121) (checked 2026-11-01): Confirms public release files and stated dataset terms; response hashes are saved in provider receipts.

**Reuse and interpretation notes:**

- The archive also includes earlier Ti64 April08 data, model files and overlapping training variants; these were not added to the selected count.
- Includes liquid configurations as well as crystalline phases.
- Frames are correlated/sampled configurations, not 15,563 compounds.
- Both selected payload MD5 values match provider metadata.

**Tags:** Scientific Data, survey:20261101, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="siox-ace24"></a>
## SiOx-ACE-24 silicon–oxygen reference configurations

Active-learning silicon–oxygen configurations spanning stoichiometries and structural order.

**Size:** 11,428 normalized training configurations (source wording: 11,428).

**Scope:** Active-learning silicon–oxygen configurations spanning stoichiometries and structural order.

**Release:** Named load-atoms cohort; original deposit checked 2026-11-01. **Year:** 2024.

**Provenance:** computed. **Structure availability:** `mixed`.

**Labels/content:** atomic coordinates and cell; DFT energy; DFT forces; available stress/virial fields.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [paper](https://doi.org/10.1038/s41467-024-45840-9) · [data](https://zenodo.org/records/10419194) · [loader](https://jla-gardner.github.io/load-atoms/datasets/SiOx-ACE-24.html)

**Evidence:**

- [SiOx-ACE-24 loader metadata](https://jla-gardner.github.io/load-atoms/datasets/SiOx-ACE-24.html) (checked 2026-11-01): Explicitly reports 11,428 structures, labels and source citation; normalization/importer route inspected without executing downloaded code.
- [SiOx-ACE-24 silicon–oxygen reference configurations original deposit metadata](https://zenodo.org/api/records/10419194) (checked 2026-11-01): Named original release, public payload inventory and data rights inspected independently; selected normalized cohort differs from unrelated archive files.

**Reuse and interpretation notes:**

- Includes structures from Si-GAP-18 and SiO2-GAP-22 plus new active-learning configurations; parent and combined counts overlap.
- Counts are reported by the normalized-data documentation; complete original large payloads were not downloaded or independently recounted.

**Tags:** additional-materials-20261101.

<a id="carbon-gap20u"></a>
## Carbon GAP-20U revised training configurations

Revised optB88-vdW carbon training data with converged labels and energy/force/stress fields.

**Size:** 6,088 DFT reference configurations (source wording: 6,088).

**Scope:** Revised optB88-vdW carbon training data with converged labels and energy/force/stress fields.

**Release:** Primary release/documentation checked 2026-11-01. **Year:** 2022.

**Provenance:** computed. **Structure availability:** `mixed`.

**Labels/content:** atomic geometry; energy; forces; virial/stress; configuration type.

**Access:** open. **Dataset license:** GPL-3.0.

**Official routes:** [data](https://doi.org/10.17863/CAM.84096) · [paper](https://doi.org/10.1063/5.0005084) · [loader](https://jla-gardner.github.io/load-atoms/datasets/C-GAP-20U.html)

**Evidence:**

- [Cambridge revised carbon training deposit](https://doi.org/10.17863/CAM.84096) (checked 2026-11-01): Lists train_GAP20_optB88vdW.xyz.gz under GPL v3.0.
- [C-GAP-20U normalized metadata](https://jla-gardner.github.io/load-atoms/datasets/C-GAP-20U.html) (checked 2026-11-01): 6,088 structures /400,275 atoms with revised DFT labels; GPLv3. Independently confirmed both counts from complete gzipped extXYZ.

**Reuse and interpretation notes:**

- Includes fragments and noncrystalline configurations as well as periodic solids.
- Related to original GAP-20; do not add the two release populations as independent materials.

**Tags:** additional-materials-20261101.

<a id="mp-noncrystalline-aimd"></a>
## Materials Project non-crystalline AIMD and diffusivity database

Ab initio molecular-dynamics liquid and quenched inorganic systems, with ionic diffusivities and non-equilibrium structures.

**Size:** 5,120 5000 K AIMD parent systems (source wording: 5,120).

**Scope:** The paper reports 5,120 systems in the 5000 K cohort, spanning 4,849 distinct compositions. Lower-temperature runs and trajectory frames are additional dependent observations.

**Release:** 2024 publication cohort; 5000 K and multi-temperature releases. **Year:** 2024.

**Provenance:** MPMorph AIMD workflows seeded from Materials Project compositions; non-crystalline trajectories are new calculations. **Structure availability:** `periodic_atomic`.

**Labels/content:** AIMD structures; ionic diffusivity; energies; forces; temperature.

**Access:** open. **Dataset license:** Not verified for dataset files; MPContribs labels project CCA4, but release-file terms were not independently checked.

**Official routes:** [Provider](https://contribs.materialsproject.org/projects/amorphous_diffusivity) · [Code](https://github.com/Tinaatucsd/DFT_amorphous_structure) · [Trajectories](https://materialsproject-contribs.s3.amazonaws.com/index.html#amorphous_diffusivity/) · [Paper](https://doi.org/10.1038/s41524-024-01469-2)

Other denominators (not added to the ranking):

- 4,849 compositions: Distinct compositions in the 5000 K cohort
- 220 selected compounds: Lower-temperature cohort; not added to parent system count

**Evidence:**

- [Non-crystalline structure database paper](https://www.nature.com/articles/s41524-024-01469-2) (checked 2026-11-01): Data scope distinguishes 5,120 5000 K systems, 4,849 compositions, and 220 compounds studied at lower temperatures; data availability names MPContribs and Figshare.
- [Author data/code repository](https://github.com/Tinaatucsd/DFT_amorphous_structure) (checked 2026-11-01): README links downloadable structure/diffusivity JSON and the full AIMD trajectory distribution.
- [Live MPContribs project](https://contribs.materialsproject.org/projects/amorphous_diffusivity) (checked 2026-11-01): Download controls include structures and tables; temperature and element-specific diffusivities are displayed. Project badge reads CCA4.

**Reuse and interpretation notes:**

- The phase cannot universally be assigned as glass versus liquid; do not label every system an amorphous solid.
- System count is not the number of unique compositions or trajectory snapshots.
- No all-payload enumeration or deduplication was performed.

**Tags:** amorphous, liquids, AIMD, diffusivity, non-crystalline, additional-materials-20261101.

<a id="p-gap20"></a>
## P-GAP-20 phosphorus reference configurations

Phosphorus crystals, liquids, nanostructures and fragments generated partly through GAP random-structure searching.

**Size:** 4,798 normalized training configurations (source wording: 4,798).

**Scope:** Phosphorus crystals, liquids, nanostructures and fragments generated partly through GAP random-structure searching.

**Release:** Named load-atoms cohort; original deposit checked 2026-11-01. **Year:** 2020.

**Provenance:** computed. **Structure availability:** `mixed`.

**Labels/content:** atomic coordinates and cell; DFT energy; DFT forces; available stress/virial fields.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [paper](https://doi.org/10.1038/s41467-020-19168-z) · [data](https://zenodo.org/records/4003703) · [loader](https://jla-gardner.github.io/load-atoms/datasets/P-GAP-20.html)

**Evidence:**

- [P-GAP-20 loader metadata](https://jla-gardner.github.io/load-atoms/datasets/P-GAP-20.html) (checked 2026-11-01): Explicitly reports 4,798 structures, labels and source citation; normalization/importer route inspected without executing downloaded code.
- [P-GAP-20 phosphorus reference configurations original deposit metadata](https://zenodo.org/api/records/4003703) (checked 2026-11-01): Named original release, public payload inventory and data rights inspected independently; selected normalized cohort differs from unrelated archive files.

**Reuse and interpretation notes:**

- Mixed molecular/nanostructured/periodic domain; retain configuration types and labels.
- Counts are reported by the normalized-data documentation; complete original large payloads were not downloaded or independently recounted.

**Tags:** additional-materials-20261101.

<a id="mace-mp-mof0-training"></a>
## MACE-MP-MOF0 DFT training configurations

Periodic MOF configurations with DFT energies, forces and stress for fine-tuning MACE-MP-MOF0.

**Size:** 4,311 DFT configuration frames (source wording: 4,311).

**Scope:** Current downloadable v2 archive: 3,611 train, 331 validation and 369 test extXYZ frames

**Release:** ddmms/data mace-mof-0/v2/data_training.tar.xz, checked 2026-11-01. **Year:** 2025.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** crystal structure; DFT energy; DFT forces; DFT stress.

**Access:** open. **Dataset license:** CC BY 4.0 (explicit mace-mof-0 folder data license).

**Official routes:** [dataset](https://github.com/ddmms/data/tree/main/mace-mof-0) · [download](https://raw.githubusercontent.com/ddmms/data/main/mace-mof-0/v2/data_training.tar.xz) · [paper](https://doi.org/10.1038/s41524-025-01611-8)

Other denominators (not added to the ranking):

- 127 curated parent MOFs: Provider curated input-CIF set; not configuration-frame count

**Count derivation:** Parse atom-count-prefixed complete extXYZ frames in the three v2 archive splits; 3,611 + 331 + 369 = 4,311.

**Evidence:**

- [MACE-MP-MOF0 dataset README](https://raw.githubusercontent.com/ddmms/data/main/mace-mof-0/README.md) (checked 2026-11-01): States v2 contains the DFT dataset split into train/test/validation; separately provides 127 curated input CIFs, 70 out-of-sample QMOF MOFs and phonon/property results.
- [MACE-MP-MOF0 data license](https://raw.githubusercontent.com/ddmms/data/main/mace-mof-0/LICENSE) (checked 2026-11-01): Explicitly licenses all data in this repository under CC BY 4.0, requiring citation of the associated publication.
- [MACE-MP-MOF0 v2 training payload](https://raw.githubusercontent.com/ddmms/data/main/mace-mof-0/v2/data_training.tar.xz) (checked 2026-11-01): Parsed extXYZ frame boundaries: train.xyz 3,611; valid.xyz 331; test.xyz 369. Comment fields include Lattice, species/pos, dft_forces, dft_energy and dft_stress.

**Reuse and interpretation notes:**

- Current released archive count 4,311 differs from the final article claim of 4,764 DFT data points; catalog count deliberately scopes the inspected payload.
- Configurations are correlated samples from a curated 127-MOF parent set, including QMOF-derived frameworks; not 4,311 distinct compounds.
- The broader GitHub folder includes models and derived properties; they are not counted as additional DFT frames.

**Tags:** MOF, MACE, DFT, forces, stress, phonon, additional-materials-20261101.

<a id="go-mace23"></a>
## GO-MACE-23 graphene-oxide reference cohort

CASTEP/PBE graphene-oxide configurations spanning compositions and functional groups.

**Size:** 3,816 normalized training configurations (source wording: 3,816).

**Scope:** CASTEP/PBE graphene-oxide configurations spanning compositions and functional groups.

**Release:** Named load-atoms cohort; original deposit checked 2026-11-01. **Year:** 2024.

**Provenance:** computed. **Structure availability:** `mixed`.

**Labels/content:** atomic coordinates and cell; DFT energy; DFT forces; available stress/virial fields.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [paper](https://doi.org/10.1002/anie.202410088) · [data](https://zenodo.org/records/14066557) · [loader](https://jla-gardner.github.io/load-atoms/datasets/GO-MACE-23.html)

**Evidence:**

- [GO-MACE-23 loader metadata](https://jla-gardner.github.io/load-atoms/datasets/GO-MACE-23.html) (checked 2026-11-01): Explicitly reports 3,816 structures, labels and source citation; normalization/importer route inspected without executing downloaded code.
- [GO-MACE-23 graphene-oxide reference cohort original deposit metadata](https://zenodo.org/api/records/14066557) (checked 2026-11-01): Named original release, public payload inventory and data rights inspected independently; selected normalized cohort differs from unrelated archive files.

**Reuse and interpretation notes:**

- Count selects the iter-12-filtered training/testing cohort, not every model or generated production frame in the archive.
- Counts are reported by the normalized-data documentation; complete original large payloads were not downloaded or independently recounted.

**Tags:** additional-materials-20261101.

<a id="sio2-gap22"></a>
## SiO2-GAP-22 silica training cohort

Iteratively generated silica reference structures with energy and force labels.

**Size:** 3,074 normalized training configurations (source wording: 3,074).

**Scope:** Iteratively generated silica reference structures with energy and force labels.

**Release:** Named load-atoms cohort; original deposit checked 2026-11-01. **Year:** 2022.

**Provenance:** computed. **Structure availability:** `mixed`.

**Labels/content:** atomic coordinates and cell; DFT energy; DFT forces; available stress/virial fields.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [paper](https://doi.org/10.1038/s41524-022-00768-w) · [data](https://zenodo.org/records/6353684) · [loader](https://jla-gardner.github.io/load-atoms/datasets/SiO2-GAP-22.html)

**Evidence:**

- [SiO2-GAP-22 loader metadata](https://jla-gardner.github.io/load-atoms/datasets/SiO2-GAP-22.html) (checked 2026-11-01): Explicitly reports 3,074 structures, labels and source citation; normalization/importer route inspected without executing downloaded code.
- [SiO2-GAP-22 silica training cohort original deposit metadata](https://zenodo.org/api/records/6353684) (checked 2026-11-01): Named original release, public payload inventory and data rights inspected independently; selected normalized cohort differs from unrelated archive files.

**Reuse and interpretation notes:**

- The normalized training cohort is selected from an archive that also contains fitted potential and generated amorphous models.
- Counts are reported by the normalized-data documentation; complete original large payloads were not downloaded or independently recounted.

**Tags:** additional-materials-20261101.

<a id="asi-paracrystalline-models"></a>
## Paracrystalline/amorphous silicon structural models

Synthetic silicon models spanning continuous-random-network, paracrystalline and polycrystalline order.

**Size:** 3,069 final melt–quench configuration frames (source wording: 3,069).

**Scope:** Synthetic silicon models spanning continuous-random-network, paracrystalline and polycrystalline order.

**Release:** Primary release/documentation checked 2026-11-01. **Year:** 2025.

**Provenance:** model-generated; MTP-labeled. **Structure availability:** `periodic_atomic`.

**Labels/content:** periodic atomic coordinates; MTP-labeled energy/forces; structural order descriptors; quench/density metadata.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [paper](https://doi.org/10.1038/s41467-025-57406-4) · [data](https://doi.org/10.5281/zenodo.14203730) · [repository](https://github.com/lamrosset/aSi-data)

**Evidence:**

- [a-Si author repository](https://github.com/lamrosset/aSi-data) (checked 2026-11-01): 3,069 structures and approximately 1.3 million atoms; each model is the final snapshot from a melt–quench MD trajectory.
- [a-Si v1.0.0 deposit](https://zenodo.org/api/records/14203730) (checked 2026-11-01): 2025 research-data release with XYZ/dataframe/code archive; CC BY 4.0 metadata.

**Reuse and interpretation notes:**

- The energy/force targets are machine-potential outputs, not independently evaluated DFT labels for every structure.
- The separate 100,000-atom demonstration models are not added to the 3,069-model cohort.
- An amorphous-to-crystalline structural library, not a collection of 3,069 new equilibrium crystal phases.

**Tags:** additional-materials-20261101.

<a id="gst-gap22-pbe"></a>
## GST-GAP-22 PBE reference cohort

Ge–Sb–Te phase-change reference configurations along the GeTe–Sb2Te3 pseudobinary line.

**Size:** 2,692 normalized training configurations (source wording: 2,692).

**Scope:** Ge–Sb–Te phase-change reference configurations along the GeTe–Sb2Te3 pseudobinary line.

**Release:** Named load-atoms cohort; original deposit checked 2026-11-01. **Year:** 2023.

**Provenance:** computed. **Structure availability:** `mixed`.

**Labels/content:** atomic coordinates and cell; DFT energy; DFT forces; available stress/virial fields.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [paper](https://doi.org/10.1038/s41928-023-01030-x) · [data](https://zenodo.org/records/8208202) · [loader](https://jla-gardner.github.io/load-atoms/datasets/GST-GAP-22.html)

**Evidence:**

- [GST-GAP-22 loader metadata](https://jla-gardner.github.io/load-atoms/datasets/GST-GAP-22.html) (checked 2026-11-01): Explicitly reports 2,692 structures, labels and source citation; normalization/importer route inspected without executing downloaded code.
- [GST-GAP-22 PBE reference cohort original deposit metadata](https://zenodo.org/api/records/8208202) (checked 2026-11-01): Named original release, public payload inventory and data rights inspected independently; selected normalized cohort differs from unrelated archive files.

**Reuse and interpretation notes:**

- The 2,692-record cohort uses PBE; the archive also contains PBEsol databases, models and much larger production simulations. Do not label all archive files as the same cohort.
- Counts are reported by the normalized-data documentation; complete original large payloads were not downloaded or independently recounted.

**Tags:** additional-materials-20261101.

<a id="si-gap18"></a>
## Si-GAP-18 silicon training cohort

Silicon reference structures selected with CUR, labeled with CASTEP/PW91.

**Size:** 2,475 normalized training configurations (source wording: 2,475).

**Scope:** Silicon reference structures selected with CUR, labeled with CASTEP/PW91.

**Release:** Named load-atoms cohort; original deposit checked 2026-11-01. **Year:** 2018.

**Provenance:** computed. **Structure availability:** `mixed`.

**Labels/content:** atomic coordinates and cell; DFT energy; DFT forces; available stress/virial fields.

**Access:** open. **Dataset license:** CC BY-NC-SA 4.0 (load-atoms distribution; original Zenodo metadata uses other-open).

**Official routes:** [paper](https://doi.org/10.1103/PhysRevX.8.041048) · [data](https://zenodo.org/records/1250555) · [loader](https://jla-gardner.github.io/load-atoms/datasets/Si-GAP-18.html)

**Evidence:**

- [Si-GAP-18 loader metadata](https://jla-gardner.github.io/load-atoms/datasets/Si-GAP-18.html) (checked 2026-11-01): Explicitly reports 2,475 structures, labels and source citation; normalization/importer route inspected without executing downloaded code.
- [Si-GAP-18 silicon training cohort original deposit metadata](https://zenodo.org/api/records/1250555) (checked 2026-11-01): Named original release, public payload inventory and data rights inspected independently; selected normalized cohort differs from unrelated archive files.

**Reuse and interpretation notes:**

- Crystalline, liquid, amorphous, surface and defect configurations are not independent bulk material identities.
- License is scoped to the normalized distribution; the original deposit has a less-specific other-open label.
- Counts are reported by the normalized-data documentation; complete original large payloads were not downloaded or independently recounted.

**Tags:** additional-materials-20261101.

<a id="chalcogenide-vacancy-reconstructions"></a>
## Chalcogenide vacancy structure-reconstruction dataset

DFT relaxation landscapes for neutral cation vacancies in chalcogenides, used to train defect reconstruction surrogate potentials.

**Size:** ~130 neutral cation-vacancy defects (source wording: ~130).

**Scope:** Provider describes approximately 130 defect types across approximately 50 chalcogenide hosts, each with 14 or 15 initial distortions and relaxation trajectories.

**Release:** Zenodo v1, DOI 10.5281/zenodo.10579527. **Year:** 2024.

**Provenance:** ShakeNBreak structure searches and VASP DFT relaxations; processed M3GNet training/validation configurations derived from the same trajectories. **Structure availability:** `periodic_atomic`.

**Labels/content:** relaxed structures; relaxation trajectories; energies; forces; stresses; distortion energies.

**Access:** open. **Dataset license:** Not verified; Zenodo metadata did not expose an explicit dataset licence.

**Official routes:** [Release](https://zenodo.org/records/10579527) · [Paper](https://doi.org/10.1038/s41524-024-01303-9) · [Workflow](https://github.com/ireaml/defects_workflow)

**Evidence:**

- [Machine-learning structural reconstructions dataset](https://zenodo.org/records/10579527) (checked 2026-11-01): Release describes about 130 neutral cation vacancies, about 50 hosts, POSCAR/CONTCAR/vasprun.xml data and processed structure-energy-force-stress dictionaries.

**Reuse and interpretation notes:**

- Defect count excludes distortions, ionic frames, and pristine-host relaxations.
- Some ionic steps are electronically unconverged and the supplied parser removes them.
- Full 20.7 GB archives were not downloaded.

**Tags:** vacancies, chalcogenides, defect-reconstructions, MLIP, DFT, additional-materials-20261101.

<a id="electroface-trajectories"></a>
## ElectroFace electrochemical interface trajectories

AIMD and ML-accelerated aqueous interface trajectories, periodic structures, inputs and available forces/velocities.

**Size:** 71 trajectory archive packages (source wording: 71 trajectory archive packages).

**Scope:** Provider dataset v4.1 independently lists 71 .traj.zip and 71 structure packages; the publication described 69 trajectories.

**Release:** AI4EC Dataverse v4.1, 23 June 2025. **Year:** 2025.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** atomic trajectories; periodic cell; interface structure; available forces/velocities; MLIP training subsets.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [paper](https://doi.org/10.1038/s41597-025-05338-5) · [data](https://doi.org/10.12463/AI4EC/8NPZZC)

**Evidence:**

- [Scientific Data primary data descriptor](https://doi.org/10.1038/s41597-025-05338-5) (checked 2026-11-01): AIMD and ML-accelerated aqueous interface trajectories, periodic structures, inputs and available forces/velocities. Provider dataset v4.1 independently lists 71 .traj.zip and 71 structure packages; the publication described 69 trajectories.
- [Primary repository release metadata](https://dataverse.ai4ec.ac.cn/api/datasets/:persistentId/?persistentId=doi:10.12463/AI4EC/8NPZZC) (checked 2026-11-01): Confirms public release files and stated dataset terms; response hashes are saved in provider receipts.

**Reuse and interpretation notes:**

- 71 packages reflect the inspected release, compared with 69 in the publication; pin the version.
- AIMD and MLMD are distinct provenance layers; trajectories do not all carry force labels.
- Charge-neutral solid-water interfaces; no general fixed-potential/electric-double-layer claim.
- Trajectory coordinates are compressed with reduced precision; the paper recommends force recomputation for MLIP training.

**Tags:** Scientific Data, survey:20261101, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="fenicr-irradiated-relaxed-md"></a>
## Fe–Ni–Cr irradiated and relaxed atomistic configurations

Two LAMMPS atomistic states for comparing radiation-damaged austenitic alloy structure with a relaxed reference.

**Size:** 2 released atomistic sample configurations (source wording: 2).

**Scope:** One post-irradiation state and one relaxed reference; atom counts and the preceding approximately 180 cascades are not additional released samples.

**Release:** RepOD V1, DOI 10.18150/HOMYLH. **Year:** 2026.

**Provenance:** Molecular-dynamics configurations supporting the atomistic radiation-induced ductile-to-brittle transition study. **Structure availability:** `periodic_atomic`.

**Labels/content:** atomic positions; velocities; species types; simulation box; irradiation state.

**Access:** open. **Dataset license:** CC BY 4.0 (explicit file-level licences).

**Official routes:** [Release](https://repod.icm.edu.pl/dataset.xhtml?persistentId=doi%3A10.18150%2FHOMYLH) · [Metadata](https://repod.icm.edu.pl/api/datasets/:persistentId/?persistentId=doi:10.18150/HOMYLH) · [Paper](https://doi.org/10.1016/j.ijmecsci.2025.110567)

**Evidence:**

- [RepOD released dataset metadata](https://repod.icm.edu.pl/api/datasets/:persistentId/?persistentId=doi:10.18150/HOMYLH) (checked 2026-11-01): V1 has two unrestricted files with CC BY 4.0; descriptions specify 262,080 atoms after irradiation and 1,048,320 atoms in the relaxed reference.

**Reuse and interpretation notes:**

- The two samples have different cell sizes; direct paired per-atom subtraction is inappropriate.
- Not a release of 180 separate cascade trajectories.
- Only archive metadata was inspected; atomistic payloads were not downloaded.

**Tags:** irradiation, Fe-Ni-Cr, alloys, molecular-dynamics, radiation-damage, additional-materials-20261101.

<a id="amorphous-alumina-deep-potential"></a>
## Amorphous alumina bulk/surface DFT training release

Extended-XYZ reference configurations for crystalline and amorphous alumina, plus large bulk/slab structures and trained Deep Potential models.

**Size:** Unranked DFT reference configurations (source wording: Not verified).

**Scope:** Repository contains many trajectory XYZ files; frame count was not independently enumerated, so file count and atom counts are not substituted.

**Release:** Author GitHub main snapshot checked 2026-11-01. **Year:** 2026.

**Provenance:** Active learning for amorphous Al2O3 bulk and surfaces with crystalline seed configurations. **Structure availability:** `periodic_atomic`.

**Labels/content:** energies; forces; stress; lattice vectors; representative LAMMPS structures.

**Access:** open. **Dataset license:** GPL-3.0 as explicitly applied to the repository containing data; inspect downstream distribution obligations.

**Official routes:** [Release](https://github.com/CSIprinceton/amorphous_alumina) · [Paper](https://doi.org/10.1016/j.actamat.2026.122611)

**Evidence:**

- [Author alumina dataset repository](https://github.com/CSIprinceton/amorphous_alumina) (checked 2026-11-01): README identifies extended XYZ DFT energies/forces/stresses/lattice vectors and bulk/surface LAMMPS structures. Repository licence explicitly states GNU GPL v3.
- [Repository release tree](https://api.github.com/repos/CSIprinceton/amorphous_alumina/git/trees/main?recursive=1) (checked 2026-11-01): Tree confirms data/amorphous and data/crystalline XYZ payloads, separate model files and representative structures.

**Reuse and interpretation notes:**

- Model committee members and atoms per cell are not independent configuration counts.
- Unranked until XYZ frames are enumerated; no numerical size inferred from the paper or file sizes.

**Tags:** amorphous, alumina, surfaces, Deep-Potential, active-learning, additional-materials-20261101.

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
