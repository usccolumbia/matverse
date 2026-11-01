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
