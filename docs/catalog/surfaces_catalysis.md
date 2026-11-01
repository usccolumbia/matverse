# Surfaces, interfaces and catalysis

[Back to MatVerse](../../README.md)

Checked 2026-11-01. Counts are source-reported or explicitly derived from release metadata; full datasets were not independently deduplicated.

<a id="oc20"></a>
## Open Catalyst 2020 (OC20)

Adsorbate-surface DFT relaxations and configurations for heterogeneous catalysis learning.

**Size:** 133,934,018 DFT configuration frames (source wording: 133,934,018 corrected S2EF training frames).

**Scope:** Released corrected S2EF training set, February 2021; excludes validation, test and optional MD/rattled additions.

**Release:** Corrected S2EF training files, February 2021. **Year:** 2020.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** periodic slab structure; adsorption energy; forces; relaxed geometry.

**Access:** open. **Dataset license:** Creative Commons Attribution 4.0 International.

**Official routes:** [homepage](https://opencatalystproject.org/) · [data](https://github.com/facebookresearch/fairchem/blob/main/docs/catalysts/datasets/oc20.md) · [paper](https://doi.org/10.1021/acscatal.0c04525) · [code](https://github.com/facebookresearch/fairchem)

Other denominators (not added to the ranking):

- 1,281,040 DFT relaxation systems: full original corpus in author paper v5
- 264,890,000 DFT single-point evaluations: approximate full original corpus in author paper v5

**Evidence:**

- [OC20 author paper v5](https://arxiv.org/abs/2010.09990) (checked 2026-11-01): Reports 1,281,040 DFT relaxations and approximately 264,890,000 single-point evaluations.
- [OC20 official task downloads and changelog](https://github.com/facebookresearch/fairchem/blob/main/docs/catalysts/datasets/oc20.md) (checked 2026-11-01): Changelog corrects S2EF training frames from 133,953,162 to 133,934,018; task data license CC BY 4.0.

**Reuse and interpretation notes:**

- Ranked count is the corrected released S2EF training subset. The full paper describes 1,281,040 relaxations and approximately 264,890,000 single-point evaluations across tasks.
- Relaxations are correlated systems/trajectories, not distinct catalyst materials.
- Bulk parent crystals derive from Materials Project; OC20 dense/MD/rattled subsets must not be blindly added.

**Tags:** surface, catalysis, DFT, MLIP, trajectory.

<a id="oc20-mads"></a>
## Open Catalyst 2020 Multiple Adsorbates

OC20 extension for coadsorption and coverage effects, with up to five adsorbates on a surface. The project lists 21,804,758 training frames and introduced the dataset with the UMA models.

**Size:** 21,804,758 configurations (source wording: 21,804,758).

**Scope:** 21,804,758 provider-reported training frames, up to5adsorbates per surface.

**Release:** OC20-mAds release as listed in Matbench Discovery at 8869a883a506. **Year:** 2025.

**Provenance:** DFT calculations; source-reported release metadata. **Structure availability:** `periodic_atomic`.

**Labels/content:** surface/adsorbate atomic coordinates; DFT energies; forces.

**Access:** open. **Dataset license:** CC-BY-4.0 (provider/benchmark release declaration).

**Official routes:** [homepage](https://github.com/facebookresearch/fairchem/blob/main/docs/catalysts/datasets/oc20_mads.md) · [data](https://dl.fbaipublicfiles.com/opencatalystproject/data/oc20mAds/oc20_multiads_train.tar.gz) · [paper](https://doi.org/10.48550/arXiv.2506.23971)

**Evidence:**

- [Matbench Discovery datasets table](https://matbench-discovery.materialsproject.org/data/sets) (checked 2026-11-01): Listed OC20-mAds: 21,804,758 configurations/structures; role training, created 2025-06-30, declared data license CC-BY-4.0. Counts and access refer to this listed release.
- [Pinned Matbench Discovery dataset metadata](https://github.com/janosh/matbench-discovery/blob/8869a883a5067015b815886d878bd7aaa3862d2d/data/datasets.yml) (checked 2026-11-01): Machine-readable OC20-mAds entry at revision 8869a883a5067015b815886d878bd7aaa3862d2d; retains structure/material counting distinction and release caveats.
- [FAIRChem provider dataset guide](https://github.com/facebookresearch/fairchem/blob/main/docs/catalysts/datasets/oc20_mads.md) (checked 2026-11-01): Provider guide establishes OC20-mAds release, CC BY4.0, download/checksum and counting definition. Counts were not recounted from large archives here.

**Reuse and interpretation notes:**

- Overlaps parent datasets and other named splits/releases; do not add these counts to independent-material totals.

**Tags:** Matbench-sets-20261101, OC20-mAds, Matbench Discovery, training, release-subset, Matbench-Discovery-data-sets-20261101.

<a id="oc20-slabs"></a>
## Open Catalyst 2020 Clean Slabs

Clean catalyst-surface structures used for UMA training. The released training and validation corpus contains 18,323,074 frames; surfaces appearing in any OC20 test split are excluded.

**Size:** 18,323,074 configurations (source wording: 18,323,074).

**Scope:** 18,323,074 provider-reported train+validation clean-surface frames; all OC20 test surfaces excluded.

**Release:** OC20-Slabs release as listed in Matbench Discovery at 8869a883a506. **Year:** 2025.

**Provenance:** DFT calculations; source-reported release metadata. **Structure availability:** `periodic_atomic`.

**Labels/content:** surface/adsorbate atomic coordinates; DFT energies; forces.

**Access:** open. **Dataset license:** CC-BY-4.0 (provider/benchmark release declaration).

**Official routes:** [homepage](https://github.com/facebookresearch/fairchem/blob/main/docs/catalysts/datasets/oc20_slabs.md) · [data](https://dl.fbaipublicfiles.com/opencatalystproject/data/oc20/oc20_slabs.tar.gz) · [paper](https://doi.org/10.48550/arXiv.2506.23971)

**Evidence:**

- [Matbench Discovery datasets table](https://matbench-discovery.materialsproject.org/data/sets) (checked 2026-11-01): Listed OC20-Slabs: 18,323,074 configurations/structures; role training, created 2025-06-30, declared data license CC-BY-4.0. Counts and access refer to this listed release.
- [Pinned Matbench Discovery dataset metadata](https://github.com/janosh/matbench-discovery/blob/8869a883a5067015b815886d878bd7aaa3862d2d/data/datasets.yml) (checked 2026-11-01): Machine-readable OC20-Slabs entry at revision 8869a883a5067015b815886d878bd7aaa3862d2d; retains structure/material counting distinction and release caveats.
- [FAIRChem provider dataset guide](https://github.com/facebookresearch/fairchem/blob/main/docs/catalysts/datasets/oc20_slabs.md) (checked 2026-11-01): Provider guide establishes OC20-Slabs release, CC BY4.0, download/checksum and counting definition. Counts were not recounted from large archives here.

**Reuse and interpretation notes:**

- Overlaps parent datasets and other named splits/releases; do not add these counts to independent-material totals.

**Tags:** Matbench-sets-20261101, OC20-Slabs, Matbench Discovery, training, release-subset, Matbench-Discovery-data-sets-20261101.

<a id="aqcat25"></a>
## AQCat25 heterogeneous-catalysis dataset

Spin-aware higher-fidelity DFT catalyst–intermediate data distributed as queryable metadata and ASE archives.

**Size:** ~13,500,000 DFT records/frames (source wording: 13.5 million DFT calculation trajectories).

**Scope:** Provider headline wording; approximately 5000 materials and 47000 intermediate–catalyst systems, not 13.5 million unique materials

**Release:** Provider dataset card, checked 2026-11-01. **Year:** 2025.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** total energy; adsorption energy; maximum force; spin-treatment metadata.

**Access:** registration. **Dataset license:** CC BY-NC-SA 4.0.

**Official routes:** [homepage](https://huggingface.co/datasets/SandboxAQ/aqcat25-dataset) · [data](https://huggingface.co/datasets/SandboxAQ/aqcat25-dataset) · [paper](https://arxiv.org/abs/2510.22938)

Other denominators (not added to the ranking):

- 5,000 materials: Approximate provider statement
- 47,000 intermediate–catalyst systems: Approximate provider statement

**Evidence:**

- [AQCat25 provider data card](https://huggingface.co/datasets/SandboxAQ/aqcat25-dataset) (checked 2026-11-01): Reports 13.5 million DFT calculation trajectories, about 5K materials and 47K catalyst systems; metadata uses frame_id; file access requires accepting conditions.

**Reuse and interpretation notes:**

- Provider headline uses trajectories while metadata is frame-indexed; exact trajectory/frame distinction was not independently reconciled.
- Accepting access conditions is required; raw file retrieval without acceptance returned 401.
- Noncommercial/share-alike licence; commercial arrangements are separate.
- Adsorbate–slab configurations are not bulk-crystal discovery results.

**Tags:** catalysis, spin, gated, collection-blaiszik.

<a id="oc22"></a>
## Open Catalyst 2022 (OC22)

Oxide-surface electrocatalyst configurations including adsorbates and bare surfaces.

**Size:** ~9,854,504 DFT configuration frames (source wording: ~9,854,504 single points from 62,331 relaxations).

**Scope:** Full OC22 corpus as stated in the final author-paper v3 abstract.

**Release:** Author paper v3, March 2023. **Year:** 2022.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** periodic slab structure; DFT total energy; forces; relaxed geometry.

**Access:** open. **Dataset license:** Creative Commons Attribution 4.0 International.

**Official routes:** [data](https://github.com/facebookresearch/fairchem/blob/main/docs/catalysts/datasets/oc22.md) · [paper](https://doi.org/10.1021/acscatal.2c05426) · [code](https://github.com/facebookresearch/fairchem)

Other denominators (not added to the ranking):

- 62,331 DFT relaxation systems: final paper v3

**Evidence:**

- [OC22 final author paper](https://arxiv.org/abs/2206.08917v3) (checked 2026-11-01): Final abstract reports 62,331 relaxations and about 9,854,504 single points.
- [OC22 official data documentation](https://github.com/facebookresearch/fairchem/blob/main/docs/catalysts/datasets/oc22.md) (checked 2026-11-01): License is CC BY 4.0; targets are total energies, with S2EF and initial-to-relaxed task files.

**Reuse and interpretation notes:**

- Older summaries use 62,521; this record explicitly uses final v3 count 62,331.
- Energy target convention differs from OC20 adsorption-energy targets.
- One system appears in many trajectory frames.

**Tags:** oxide, surface, catalysis, MLIP.

<a id="oc25"></a>
## Open Catalyst 2025 (OC25)

Explicit-solvent catalyst interfaces with solvent, ions and adsorbates across 88 elements.

**Size:** 7,801,261 DFT configuration evaluations (source wording: 7,801,261 DFT calculations; 1,511,270 unique solvent environments).

**Scope:** Total corpus in author-paper abstract; different from unique environment or substrate counts.

**Release:** 2025 author paper and official release. **Year:** 2025.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** periodic interface structure; total energy; forces; solvation energy.

**Access:** registration. **Dataset license:** Creative Commons Attribution 4.0 International (dataset).

**Official routes:** [data](https://huggingface.co/facebook/OC25) · [paper](https://arxiv.org/abs/2509.17862) · [code](https://github.com/facebookresearch/fairchem)

Other denominators (not added to the ranking):

- 1,511,270 unique explicit-solvent environments: 2025 paper full corpus

**Evidence:**

- [OC25 primary dataset paper](https://arxiv.org/html/2509.17862v1) (checked 2026-11-01): Abstract states 7,801,261 calculations across 1,511,270 unique explicit-solvent environments.
- [OC25 official data documentation](https://github.com/facebookresearch/fairchem/blob/main/docs/catalysts/datasets/oc25.md) (checked 2026-11-01): VASP RPBE+D3 energy/force labels, 88 elements and CC BY 4.0 dataset terms; HF download.

**Reuse and interpretation notes:**

- Unique solvent environments are not unique crystalline substrates.
- Dataset and accompanying model license terms are distinct.
- Access restrictions/gating must be checked on the official HF download page.

**Tags:** solid-liquid, interfaces, catalysis, MLIP.

<a id="oc20-neb"></a>
## Open Catalyst 2020 Nudged Elastic Band Benchmark

CatTSunami validation set of 932 nudged elastic band reaction paths covering desorption, dissociation, and transfer reactions on catalyst surfaces. Tests transition-state predictions from potentials trained on adsorption relaxations.

**Size:** 1,375,930 configurations (source wording: 1,375,930).

**Scope:** Benchmark-reported1,375,930 saved ASE frames across932 NEB trajectories, including repeated fixed endpoints; provider guide verifies932 paths and10frames periteration.

**Release:** OC20NEB release as listed in Matbench Discovery at 8869a883a506. **Year:** 2024.

**Provenance:** DFT calculations; source-reported release metadata. **Structure availability:** `periodic_atomic`.

**Labels/content:** surface/adsorbate atomic coordinates; DFT energies; forces; reaction pathways; transition-state energetics.

**Access:** open. **Dataset license:** CC-BY-4.0 (provider/benchmark release declaration).

**Official routes:** [homepage](https://github.com/facebookresearch/fairchem/blob/main/docs/catalysts/datasets/oc20neb.md) · [data](https://dl.fbaipublicfiles.com/opencatalystproject/data/oc20neb/oc20neb_dft_trajectories_04_23_24.tar.gz) · [paper](https://doi.org/10.48550/arXiv.2405.02078)

Other denominators (not added to the ranking):

- 821 source-defined parent materials: Benchmark metadata denominator; see release notes for identity definition. Not added to configurations.
- 932 NEB trajectories: Primary provider guide; includes desorption, dissociation and transfer reactions.

**Evidence:**

- [Matbench Discovery datasets table](https://matbench-discovery.materialsproject.org/data/sets) (checked 2026-11-01): Listed OC20NEB: 1,375,930 configurations/structures; role validation, created 2024-05-03, declared data license CC-BY-4.0. Counts and access refer to this listed release.
- [Pinned Matbench Discovery dataset metadata](https://github.com/janosh/matbench-discovery/blob/8869a883a5067015b815886d878bd7aaa3862d2d/data/datasets.yml) (checked 2026-11-01): Machine-readable OC20NEB entry at revision 8869a883a5067015b815886d878bd7aaa3862d2d; retains structure/material counting distinction and release caveats.
- [FAIRChem provider dataset guide](https://github.com/facebookresearch/fairchem/blob/main/docs/catalysts/datasets/oc20neb.md) (checked 2026-11-01): Provider guide establishes OC20NEB release, CC BY4.0, download/checksum and counting definition. Counts were not recounted from large archives here.

**Reuse and interpretation notes:**

- Counted 1,375,930 stored ASE frames across all 932 trajectories in the checksum-verified release (https://github.com/facebookresearch/fairchem/blob/main/docs/catalysts/datasets/oc20neb.md). This includes the two fixed endpoints saved at each NEB iteration. Materials counts 821 distinct parent bulk IDs encoded in the trajectory filenames.
- Overlaps parent datasets and other named splits/releases; do not add these counts to independent-material totals.
- Fixed endpoints repeat at each NEB iteration. These frames are correlated and not independent transition states.

**Tags:** Matbench-sets-20261101, OC20NEB, Matbench Discovery, validation, release-subset, Matbench-Discovery-data-sets-20261101.

<a id="bimetallic-catalysis-2019"></a>
## SUNCAT bimetallic adsorption calculations

Quantum ESPRESSO adsorption/hydrogenation calculations on bimetallic alloy and pure-metal slabs.

**Size:** ≥90,000 DFT calculations (source wording: >90,000 DFT calculations).

**Scope:** More than 90,000 systematic calculations on 1,998 alloy and 37 pure-metal surfaces in the primary study.

**Release:** Materials Cloud 2019.0015/v1. **Year:** 2019.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** adsorption energy; reaction energy; atomic slab geometry; adsorption site.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [paper](https://doi.org/10.1038/s41597-019-0080-z) · [data](https://doi.org/10.24435/materialscloud:2019.0015/v1)

**Evidence:**

- [Scientific Data primary data descriptor](https://doi.org/10.1038/s41597-019-0080-z) (checked 2026-11-01): Quantum ESPRESSO adsorption/hydrogenation calculations on bimetallic alloy and pure-metal slabs. More than 90,000 systematic calculations on 1,998 alloy and 37 pure-metal surfaces in the primary study.
- [Primary repository release metadata](https://archive.materialscloud.org/api/records/xxdhq-f1v83) (checked 2026-11-01): Confirms public release files and stated dataset terms; response hashes are saved in provider receipts.

**Reuse and interpretation notes:**

- Calculations include many adsorbates/sites per slab and are not 90,000 distinct materials.
- Catalysis-Hub is an access platform that aggregates this and other corpora; do not add platform totals to this release.
- Raw QE output archives expose periodic coordinates; bulk archives were not downloaded.

**Tags:** Scientific Data, survey:20261101, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="oc20-dense"></a>
## Open Catalyst 2020 Dense Adsorbate Sampling

AdsorbML validation dataset for finding low-energy adsorption configurations, using dense initial placement sampling for roughly 1,000 adsorbate-surface systems.

**Size:** 85,658 initial adsorption configurations (source wording: 85,658).

**Scope:** 85,658 distinct initial configurations for dense adsorption-placement evaluation, not every relaxed trajectory frame or independent parent bulk.

**Release:** OC20-Dense release as listed in Matbench Discovery at 8869a883a506. **Year:** 2022.

**Provenance:** DFT calculations; source-reported release metadata. **Structure availability:** `periodic_atomic`.

**Labels/content:** surface/adsorbate atomic coordinates; DFT energies; forces.

**Access:** open. **Dataset license:** CC-BY-4.0 (provider/benchmark release declaration).

**Official routes:** [homepage](https://github.com/facebookresearch/fairchem/blob/main/docs/catalysts/datasets/oc20dense.md) · [data](https://dl.fbaipublicfiles.com/opencatalystproject/data/adsorbml/oc20_dense_data.tar.gz) · [paper](https://doi.org/10.48550/arXiv.2211.16486)

Other denominators (not added to the ranking):

- 833 source-defined parent materials: Benchmark metadata denominator; see release notes for identity definition. Not added to configurations.

**Evidence:**

- [Matbench Discovery datasets table](https://matbench-discovery.materialsproject.org/data/sets) (checked 2026-11-01): Listed OC20-Dense: 85,658 configurations/structures; role validation, created 2022-11-29, declared data license CC-BY-4.0. Counts and access refer to this listed release.
- [Pinned Matbench Discovery dataset metadata](https://github.com/janosh/matbench-discovery/blob/8869a883a5067015b815886d878bd7aaa3862d2d/data/datasets.yml) (checked 2026-11-01): Machine-readable OC20-Dense entry at revision 8869a883a5067015b815886d878bd7aaa3862d2d; retains structure/material counting distinction and release caveats.
- [FAIRChem provider dataset guide](https://github.com/facebookresearch/fairchem/blob/main/docs/catalysts/datasets/oc20dense.md) (checked 2026-11-01): Provider guide establishes OC20-Dense release, CC BY4.0, download/checksum and counting definition. Counts were not recounted from large archives here.

**Reuse and interpretation notes:**

- Counts 85,658 initial atomic configurations, not all relaxation frames. Materials counts 833 distinct parent mp-IDs in oc20dense_mapping.pkl from the released mappings (https://github.com/facebookresearch/fairchem/blob/main/docs/catalysts/datasets/oc20dense.md). Multiple adsorbate-surface combinations share a parent material.
- Overlaps parent datasets and other named splits/releases; do not add these counts to independent-material totals.

**Tags:** Matbench-sets-20261101, OC20-Dense, Matbench Discovery, validation, release-subset, Matbench-Discovery-data-sets-20261101.

<a id="work-function-cleavage-surfaces"></a>
## Work function and cleavage energy surface database

High-throughput DFT work functions and cleavage energies for crystal-surface slabs, with structures, orientations, terminations and calculation metadata.

**Size:** 58,332 surface configuration records (source wording: 58,332 unrelaxed surface records; separate selected relaxed subset of 90).

**Scope:** WF-CE_database_58332.json; the 90 relaxed extreme-work-function records are an overlapping follow-up subset

**Release:** Zenodo v2.1, February 2024. **Year:** 2024.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** work function; cleavage energy; slab atomic structure; Miller index; surface termination; DFT total energy.

**Access:** open. **Dataset license:** Creative Commons Attribution Non Commercial 4.0 International (CC BY-NC 4.0).

**Official routes:** [homepage](https://zenodo.org/records/10703249) · [data](https://doi.org/10.5281/zenodo.10703249) · [paper](https://doi.org/10.1002/adfm.202401764)

**Evidence:**

- [Work Function and Cleavage Energy Database](https://zenodo.org/records/10703249) (checked 2026-11-01): Release describes 58,332 unrelaxed slab records, 90 selected relaxed records, and per-record slab geometries with MP IDs.
- [Zenodo release metadata](https://zenodo.org/api/records/10703249) (checked 2026-11-01): Version 2.1 metadata identifies CC BY-NC 4.0 licensing.

**Reuse and interpretation notes:**

- Configurations are surface orientation/termination slabs, not 58,332 distinct bulk compounds.
- Most records are unrelaxed slabs; 90 selected low/high-work-function slabs were ionically relaxed.
- Surface parent materials overlap Materials Project; follow-up relaxed records must not be added as independent materials.
- The non-commercial restriction matters for reuse.

**Tags:** surfaces, work function, cleavage energy, Materials Project derivative, collection:sedaoturak.

<a id="beast-db"></a>
## BEAST DB

Grand-canonical DFT electrochemical surface calculations at fixed potential and fixed charge in implicit solvent.

**Size:** ≥20,000 electrochemical DFT calculations (source wording: over 20,000 surface calculations).

**Scope:** Lower bound in the original 2024 primary paper.

**Release:** 2024 publication corpus. **Year:** 2024.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** structure; potential-dependent energy; electronic structure; reaction pathways.

**Access:** open. **Dataset license:** Not verified.

**Official routes:** [homepage](https://beastdb.nrel.gov/) · [paper](https://doi.org/10.1021/acs.jpcc.4c06826) · [code](https://github.com/Nick-Singstock/BEAST_DB_Manager)

**Evidence:**

- [BEAST DB primary author paper](https://arxiv.org/abs/2405.20239) (checked 2026-11-01): Describes over 20,000 surface calculations at consistent grand-canonical DFT settings in implicit solvent, both fixed potential and fixed charge.

**Reuse and interpretation notes:**

- Count is 2024 calculation scale, not a verified live 2026 total or count of unique catalysts.
- Original NREL hostname did not resolve from this audit environment; public availability is documented by the paper.
- Dataset-specific license not verified.

**Tags:** electrocatalysis, grand-canonical, DFT, potential-dependent.

<a id="homer-aluminum-gb-7304"></a>
## Homer aluminum grain-boundary structures across 5D space

Minimum-energy aluminum grain boundaries spanning macroscopic crystallographic character, with atomic coordinates and computed boundary properties.

**Size:** 7,304 minimum-energy grain-boundary structures (source wording: 7,304).

**Scope:** Released ZIP contains 7,304 minimized LAMMPS structures, one for each unique macroscopic grain boundary.

**Release:** Mendeley Data v1, DOI 10.17632/4ykjz4ngwt.1. **Year:** 2022.

**Provenance:** EAM-conjugate-gradient optimization of aluminum bicrystals over many microscopic initial configurations. **Structure availability:** `periodic_atomic`.

**Labels/content:** boundary energy; crystallographic character; excess volume; atomic coordinates.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [Release](https://data.mendeley.com/datasets/4ykjz4ngwt/1) · [Paper](https://doi.org/10.1016/j.actamat.2022.118006)

**Evidence:**

- [Computed Aluminum Grain Boundary Structures and Energies Covering the 5D Space](https://data.mendeley.com/datasets/4ykjz4ngwt/1) (checked 2026-11-01): Provider states 7,304 minimum-energy LAMMPS structure files plus property CSV and CC BY 4.0.

**Reuse and interpretation notes:**

- Only atoms within ±15 angstrom of the boundary plane are retained; files are truncated boundary regions.
- The 43,009,236 configurations minimized during search are not the count of structures in this release.
- Distinct from the existing FCC Cu dislocation–grain-boundary interaction corpus.

**Tags:** grain-boundaries, aluminum, EAM, interfaces, additional-materials-20261101.

<a id="sac-ncepu"></a>
## Computational Single-Atom Catalyst Database (NCEPU)

Graphene-supported transition-metal single-atom catalysts with systematically varied nonmetal coordination.

**Size:** 1,197 optimized catalyst configurations (source wording: 1,197 catalyst samples; 657 pass the study binding-energy criterion).

**Scope:** Initial 3d-metal/coordination corpus; subsequent 4d screening candidates are not added.

**Release:** 2025 JPCC publication corpus. **Year:** 2025.

**Provenance:** computed. **Structure availability:** `structure_linked`.

**Labels/content:** optimized structure identity; Bader charge; d-band center; binding energy; adsorption energy.

**Access:** open. **Dataset license:** Not verified.

**Official routes:** [data](https://catalysis-ncepu-hvkydg736ykqeq26d5gxrn.streamlit.app/) · [paper](https://doi.org/10.1021/acs.jpcc.5c00491) · [code](https://github.com/Weijie-Yang/AML)

**Evidence:**

- [Computational Single-Atom Catalyst Database primary article](https://pubs.acs.org/doi/10.1021/acs.jpcc.5c00491) (checked 2026-11-01): 1,197 optimized graphene SACs; 657 satisfy the binding-energy criterion and receive O2/O/NO adsorption labels; paper links Streamlit data and AML code.

**Reuse and interpretation notes:**

- The paper is CC BY-NC-ND 4.0; an independent dataset license was not verified.
- Portable periodic coordinate download from the Streamlit app was not verified, so structure level is conservatively structure-linked.
- The binding-energy screen is not a general proof of experimental stability or catalytic performance.

**Tags:** single-atom-catalyst, graphene, DFT.

<a id="si-organic-chain-slab-2026"></a>
## Organic chains chemisorbed on silicon surfaces

Quantum ESPRESSO optimized alkyl, alkenyl and alkynyl adsorption configurations on hydrogen-passivated Si(110) and Si(111) slabs.

**Size:** ≥700 optimized adsorbate–slab configurations (source wording: more than 700 optimized adsorption configurations).

**Scope:** Publication-described bulk release with organic C2–C18 chains, sampled orientations and two silicon facets; exact archive-member/configuration count not independently audited.

**Release:** Materials Cloud 2026.111, v6, 9 June 2026. **Year:** 2026.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** optimized periodic slab structure; Si–C bond dissociation energy; adsorption geometry; bond distances/angles; QE inputs/outputs.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [paper](https://doi.org/10.1038/s41597-026-07766-3) · [data](https://doi.org/10.24435/materialscloud:rm-r4) · [homepage](https://archive.materialscloud.org/record/2026.111)

**Evidence:**

- [Scientific Data descriptor](https://doi.org/10.1038/s41597-026-07766-3) (checked 2026-11-01): Reports more than 700 DFT-optimized chain/silicon configurations; Data Records specifies per-facet/type/chain/orientation QE input/output files and DataSummary.xls.
- [Materials Cloud v6 release metadata](https://archive.materialscloud.org/api/records/kp5c5-40408) (checked 2026-11-01): Confirms public DatasetNW_v6.zip of about 1.1 GiB with CC BY 4.0 rights; provider explains that silicon nanowire facets are represented with periodic slabs.

**Reuse and interpretation notes:**

- These are repeated organic-chain orientations and surface configurations, not 700 unique bulk materials.
- Nanowire surfaces are approximated by slabs; they are not explicit full nanowire geometries.
- The release includes data discussed in related Langmuir papers; preserve shared lineage rather than summing those papers as independent datasets.
- The large ZIP was not downloaded; >700 is a primary-paper lower bound, not an independent payload recount.

**Tags:** Scientific Data, survey:20261101, silicon, surface functionalization, Scientific-Data-descriptor, Scientific-Data-survey-20261101.

<a id="jarvis-surfacedb"></a>
## JARVIS / InterMat surface release

Surface calculation subset distributed with the InterMat release.

**Size:** 607 surface calculation records (source wording: 607).

**Scope:** Selected surfacedb release; not an additive total over JARVIS or a claim about latest portal coverage

**Release:** JARVIS surfacedb documentation / pinned downloader snapshot 2026-11-01. **Year:** Not verified.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** surface structure; surface properties; DFT.

**Access:** open. **Dataset license:** CC BY 4.0 (Figshare deposit).

**Official routes:** [homepage](https://pages.nist.gov/jarvis/databases/) · [code](https://github.com/usnistgov/jarvis/blob/3b0c9d0f0c15759135de857dbc93e010db01eb29/jarvis/db/figshare.py) · [data](https://figshare.com/ndownloader/files/46355689) · [release](https://doi.org/10.6084/m9.figshare.25832614)

**Evidence:**

- [JARVIS-Tools dataset table](https://pages.nist.gov/jarvis/databases/) (checked 2026-11-01): The named surfacedb row reports 607 data points.
- [Pinned JARVIS Figshare downloader](https://github.com/usnistgov/jarvis/blob/3b0c9d0f0c15759135de857dbc93e010db01eb29/jarvis/db/figshare.py) (checked 2026-11-01): Confirms the surfacedb route or dedicated helper and the raw-file grouping.
- [Figshare release metadata](https://api.figshare.com/v2/articles/25832614) (checked 2026-11-01): Identifies the deposited files and reports the CC BY 4.0 dataset license.

**Reuse and interpretation notes:**

- Documentation supplies the 607-record count; the full surface archive was not independently recounted.
- The web portal may require registration; the linked public file route is separate.

**Tags:** JARVIS, surfacedb, release-snapshot.

<a id="jarvis-interfacedb"></a>
## JARVIS InterfacDB / InterMat interface release

InterMat interface calculations with initial and final structures and electronic offsets.

**Size:** 593 interface calculation records (source wording: 593).

**Scope:** Selected interfacedb release; not an additive total over JARVIS or a claim about latest portal coverage

**Release:** JARVIS interfacedb documentation / pinned downloader snapshot 2026-11-01. **Year:** Not verified.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** interface structure; band offsets; DFT energy; band gap.

**Access:** open. **Dataset license:** CC BY 4.0 (Figshare deposit).

**Official routes:** [homepage](https://jarvis.nist.gov/interfacedb) · [code](https://github.com/usnistgov/jarvis/blob/3b0c9d0f0c15759135de857dbc93e010db01eb29/jarvis/db/figshare.py) · [data](https://figshare.com/ndownloader/files/46355692) · [release](https://doi.org/10.6084/m9.figshare.25832614)

**Evidence:**

- [JARVIS-Tools dataset table](https://pages.nist.gov/jarvis/databases/) (checked 2026-11-01): The named interfacedb row reports 593 data points.
- [Pinned JARVIS Figshare downloader](https://github.com/usnistgov/jarvis/blob/3b0c9d0f0c15759135de857dbc93e010db01eb29/jarvis/db/figshare.py) (checked 2026-11-01): Confirms the interfacedb route or dedicated helper and the raw-file grouping.
- [Figshare release metadata](https://api.figshare.com/v2/articles/25832614) (checked 2026-11-01): Identifies the deposited files and reports the CC BY 4.0 dataset license.
- [Independent small-archive row count](https://figshare.com/ndownloader/files/46355692) (checked 2026-11-01): Complete ZIP archive parsed locally on 2026-11-01: 593 JSON records. Hash and record-key receipt: research/provenance/optimade_discovery_20261101.json.

**Reuse and interpretation notes:**

- The 593-row archive is the selected Figshare release. Portal coverage and later Interface.csv files need not have the same denominator.
- The web portal may require registration; the linked public file route is separate.

**Tags:** JARVIS, interfacedb, release-snapshot.

<a id="gbdb-elemental-metals"></a>
## GBDB elemental-metal grain-boundary DFT database

DFT grain-boundary structures and properties across elemental FCC, BCC and HCP metals.

**Size:** 327 grain-boundary structures (source wording: 327).

**Scope:** Publication cohort contains 327 grain boundaries across 58 elements.

**Release:** 2020 paper cohort; current Crystalium route checked 2026-11-01. **Year:** 2020.

**Provenance:** High-throughput scaled-template DFT calculations by Zheng and collaborators; distributed through Materials Project and Crystalium. **Structure availability:** `periodic_atomic`.

**Labels/content:** grain-boundary energy; work of separation; initial and relaxed structures.

**Access:** open. **Dataset license:** Not verified for released data.

**Official routes:** [Provider](https://crystalium.materialyze.ai/) · [Paper](https://doi.org/10.1016/j.actamat.2019.12.030) · [Author manuscript](https://perssongroup.lbl.gov/papers/zheng-2020-grain-boundary.pdf)

Other denominators (not added to the ranking):

- 58 elements: Element coverage of the paper cohort

**Evidence:**

- [Grain boundary properties of elemental metals](https://perssongroup.lbl.gov/papers/zheng-2020-grain-boundary.pdf) (checked 2026-11-01): Paper states 327 structures across 58 elements, and distribution on Materials Project and Crystalium.
- [Live Crystalium Fe data endpoint](https://crystalium.materialyze.ai/data/Fe) (checked 2026-11-01): Returned 10 Fe grain-boundary records including lattice/site coordinates, boundary energies, and work of separation alongside separate surface records.

**Reuse and interpretation notes:**

- Count is the documented paper cohort rather than an independently enumerated live total.
- Crystalium also supplies surfaces; those are excluded from this grain-boundary cohort.
- DFT values differ in provenance from empirical-potential GB datasets.

**Tags:** grain-boundaries, DFT, metals, interfaces, additional-materials-20261101.

<a id="elemental-surface-energy-2016"></a>
## Elemental crystal surface energies and Wulff shapes

DFT surface energies, periodic slab CIFs and Wulff-shape quantities for elemental crystal polymorphs.

**Size:** ≥100 elemental crystal polymorphs (source wording: >100 elemental crystal polymorphs).

**Scope:** Lower bound in primary article; about 70 elements with multiple facets and terminations per polymorph.

**Release:** Dryad v1 / 2016 publication. **Year:** 2016.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** surface energy; Miller index; slab structure; Wulff area fraction; surface anisotropy; shape factor.

**Access:** open. **Dataset license:** CC0 1.0.

**Official routes:** [paper](https://doi.org/10.1038/sdata.2016.80) · [data](https://doi.org/10.5061/dryad.f2n6f)

**Evidence:**

- [Scientific Data primary data descriptor](https://doi.org/10.1038/sdata.2016.80) (checked 2026-11-01): DFT surface energies, periodic slab CIFs and Wulff-shape quantities for elemental crystal polymorphs. Lower bound in primary article; about 70 elements with multiple facets and terminations per polymorph.
- [Primary repository release metadata](https://datadryad.org/api/v2/datasets/doi%3A10.5061%2Fdryad.f2n6f) (checked 2026-11-01): Confirms public release files and stated dataset terms; response hashes are saved in provider receipts.

**Reuse and interpretation notes:**

- Polymorphs, surface terminations and slab calculations are different counting units.
- Surfaces.json and VASP-details JSON are companion views of the same corpus.
- Different provenance/workflow from JARVIS surface and work-function records; parent MP identities can overlap.
- Dryad metadata/file inventory is public; payload download returned 401 in this audit.

**Tags:** Scientific Data, survey:20261101, Scientific-Data-descriptor, Scientific-Data-survey-20261101.
