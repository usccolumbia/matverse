# MOFs, COFs and zeolites

[Back to MatVerse](../../README.md)

Checked 2026-11-01. Counts are source-reported or explicitly derived from release metadata; full datasets were not independently deduplicated.

<a id="odac25"></a>
## Open Direct Air Capture 2025 (ODAC25)

Expanded MOF adsorption configurations for CO2, water, N2 and O2, including functionalized and synthetic frameworks.

**Size:** ~70,000,000 DFT configuration frames (source wording: nearly 70 million DFT single points across nearly 15,000 MOFs).

**Scope:** Rounded full corpus size in author documentation.

**Release:** 2025 release. **Year:** 2025.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** structure; total energy; forces; adsorption energy.

**Access:** registration. **Dataset license:** Creative Commons Attribution 4.0 International (dataset).

**Official routes:** [data](https://huggingface.co/facebook/ODAC25) · [paper](https://arxiv.org/abs/2508.03162) · [code](https://github.com/facebookresearch/fairchem)

**Evidence:**

- [ODAC25 official dataset documentation](https://github.com/facebookresearch/fairchem/blob/main/docs/dac/datasets/odac25.md) (checked 2026-11-01): Nearly 70M PBE-D3 calculations across nearly 15,000 MOFs; four adsorbates; dataset license CC BY 4.0.
- [ODAC25 official access page](https://huggingface.co/facebook/ODAC25/tree/main) (checked 2026-11-01): Download requires an account, contact sharing and acceptance; model weights have separate FAIR Chemistry terms.

**Reuse and interpretation notes:**

- 70 million is rounded configuration scale, not 70 million distinct MOFs.
- Data and model terms differ; the CC BY data license does not describe model weights.
- Supersedes ODAC23 with changed data-generation/reference conventions.

**Tags:** MOF, adsorption, MLIP, trajectory.

<a id="odac23"></a>
## Open Direct Air Capture 2023 (ODAC23)

MOFs with CO2 and water adsorbates, including defective frameworks, for energy/force learning.

**Size:** 38,983,748 DFT configuration frames (source wording: 38,983,748 DFT single points; 176,032 relaxations; 8,412 frameworks).

**Scope:** All original train, validation and test splits reported in Table 1.

**Release:** 2023 corpus / 2024 ACS Central Science descriptor. **Year:** 2023.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** structure; total energy; forces; adsorption energy; DDEC charges.

**Access:** open. **Dataset license:** Creative Commons Attribution 4.0 International.

**Official routes:** [homepage](https://open-dac.github.io/) · [data](https://github.com/facebookresearch/fairchem/blob/main/docs/dac/datasets/odac23.md) · [paper](https://doi.org/10.1021/acscentsci.3c01629) · [code](https://github.com/facebookresearch/fairchem)

Other denominators (not added to the ranking):

- 176,032 DFT relaxation systems: original full corpus
- 8,412 pristine and defective MOF frameworks: original full corpus

**Evidence:**

- [ODAC23 author paper Table 1](https://arxiv.org/html/2311.00341v2) (checked 2026-11-01): Table totals are 38,983,748 configurations, 176,032 relaxations and 8,412 frameworks (pristine plus defective).
- [ODAC23 official download documentation](https://github.com/facebookresearch/fairchem/blob/main/docs/dac/datasets/odac23.md) (checked 2026-11-01): Data license is CC BY 4.0; current documentation deprecates ODAC23 in favor of ODAC25.

**Reuse and interpretation notes:**

- Superseded for new projects by ODAC25; retain for benchmark reproduction.
- Current docs overview contains smaller rounded S2EF counts inconsistent with the original full paper; this record explicitly uses the original full corpus.
- Do not combine ODAC23 and ODAC25 energies as if reference and k-point conventions were identical.
- Frameworks derive from CoRE MOF; do not add counts as distinct materials.

**Tags:** MOF, adsorption, MLIP, trajectory, superseded.

<a id="pcod-zeolites"></a>
## Deem hypothetical zeolites / PCOD SLC-good

Monte Carlo-generated zeolite-like frameworks filtered for low classical-force-field energy.

**Size:** ~331,000 hypothetical zeolite frameworks (source wording: 331k SLC-good structures; full v2 paper reports >2.6 million unique structures).

**Scope:** Public SLC-good v2.1 subset offered on author download page.

**Release:** v2.1 SLC-good download subset. **Year:** 2011.

**Provenance:** generated. **Structure availability:** `periodic_atomic`.

**Labels/content:** structure; classical energy; density; symmetry.

**Access:** open. **Dataset license:** Not verified.

**Official routes:** [homepage](https://mwdeem.org/PCOD/index.html) · [data](https://mwdeem.org/PCOD/index.html) · [paper](https://doi.org/10.1039/C0CP02255A)

**Evidence:**

- [Deem PCOD author download page](https://mwdeem.org/PCOD/index.html) (checked 2026-11-01): Provides three archives for the 331k SLC-good subset of v2.1; distinguishes it from the larger full database and original >2.6M unique-structure paper.

**Reuse and interpretation notes:**

- The same page also mentions over four million full-database structures; denominator/version differ.
- Do not label the downloadable 331k subset as a 2.6M download.
- Force-field energies are not experimental syntheses or DFT validation.

**Tags:** zeolite, hypothetical, historical, subset.

<a id="boyd-woo"></a>
## Boyd-Woo hypothetical MOFs for wet flue-gas capture

Topologically generated MOFs with MEPO-QEq charges and adsorption/process screening labels.

**Size:** 324,426 generated MOF structures (source wording: 324,426 hypothetical MOFs).

**Scope:** Full Materials Cloud release described by the 2019 archive.

**Release:** Materials Cloud 2018.0016 v3, deposited 2019. **Year:** 2019.

**Provenance:** generated. **Structure availability:** `periodic_atomic`.

**Labels/content:** structure; partial charges; CO2 uptake; working capacity; gas mixture adsorption.

**Access:** open. **Dataset license:** Creative Commons Attribution 4.0 International.

**Official routes:** [data](https://archive.materialscloud.org/records/nsp7v-2dk91) · [paper](https://doi.org/10.1038/s41586-019-1798-7)

**Evidence:**

- [Boyd-Woo Materials Cloud archive](https://archive.materialscloud.org/records/nsp7v-2dk91) (checked 2026-11-01): Deposit contains 324,426 hypothetical MOFs; more than 8,000 received refined simulations. MEPO-QEq charges are provided.
- [Boyd-Woo file rights](https://archive.materialscloud.org/api/records/nsp7v-2dk91) (checked 2026-11-01): Release metadata declares CC BY 4.0.

**Reuse and interpretation notes:**

- ARC-MOF and QMOF reuse some structures from this family.
- Charge-generation validation is not proof of synthesizability.
- Only the refined subset has the higher-fidelity calculations.

**Tags:** MOF, hypothetical, carbon-capture, GCMC.

<a id="arc-mof"></a>
## ab initio REPEAT Charge MOF Database (ARC-MOF)

Diverse collection assembled from experimental and hypothetical MOF databases with DFT-derived charges.

**Size:** ~280,000 MOF structures (source wording: ~280,000 MOFs).

**Scope:** Rounded count in the v7 depositor description; not an independently counted exact archive size.

**Release:** Zenodo v7 (2025); structure archive ARCMOF_20241004. **Year:** 2025.

**Provenance:** mixed. **Structure availability:** `periodic_atomic`.

**Labels/content:** structure; REPEAT partial charges; adsorption; chemical descriptors; geometric descriptors.

**Access:** open. **Dataset license:** Creative Commons Attribution 4.0 International.

**Official routes:** [data](https://zenodo.org/records/16802743) · [paper](https://doi.org/10.1021/acs.chemmater.2c02485) · [code](https://github.com/uowoolab)

**Evidence:**

- [ARC-MOF v7](https://zenodo.org/records/16802743) (checked 2026-11-01): Description reports approximately 280,000 experimental and generated MOFs, REPEAT charges, descriptors and adsorption; v5/v6 removed erroneous structures.
- [ARC-MOF rights metadata](https://zenodo.org/api/records/16802743) (checked 2026-11-01): v7 API metadata declares cc-by-4.0.

**Reuse and interpretation notes:**

- The rounded description persists through revisions; exact current archive count remains unverified.
- all_structures archives describe the larger candidate universe; they are not additive ARC-MOF structures.
- Strong overlap with Boyd-Woo, CoRE, hMOF and other source families.

**Tags:** MOF, DFT-charges, curation, nonadditive.

<a id="redd-coffee"></a>
## ReDD-COFFEE

Ready-to-use hypothetical COFs with system-specific force fields derived from first principles.

**Size:** 268,687 generated COF structures (source wording: 268,687 COFs).

**Scope:** Full v1 repository, including 2D and 3D structures across linkage chemistries.

**Release:** Materials Cloud 2023.13 v1. **Year:** 2023.

**Provenance:** generated. **Structure availability:** `periodic_atomic`.

**Labels/content:** structure; force-field parameters; energetics.

**Access:** open. **Dataset license:** Creative Commons Attribution Non Commercial Share Alike 4.0 International.

**Official routes:** [data](https://archive.materialscloud.org/records/y5gs8-pyj90) · [paper](https://doi.org/10.1039/D3TA00470H)

**Evidence:**

- [ReDD-COFFEE v1](https://archive.materialscloud.org/record/2023.13) (checked 2026-11-01): Author deposit states 268,687 COFs with system-specific force fields; file rights are CC BY-NC-SA 4.0.
- [ReDD-COFFEE deposited file rights](https://archive.materialscloud.org/records/y5gs8-pyj90) (checked 2026-11-01): File rights specify CC BY-NC-SA 4.0, distinct from the archive metadata license.

**Reuse and interpretation notes:**

- Force fields are approximations derived for the hypothetical frameworks.
- Files carry CC BY-NC-SA 4.0; the metadata license is separate.

**Tags:** COF, hypothetical, force-fields.

<a id="hmof-wilmer"></a>
## Wilmer hypothetical MOF database (hMOF)

Combinatorial assembly of MOF building blocks with computed pore and gas-storage properties.

**Size:** 137,953 generated MOF structures (source wording: 137,953 hypothetical MOFs).

**Scope:** Original Wilmer et al. corpus, not a filtered JARVIS or MOFX mirror.

**Release:** Original 2011/2012 publication corpus. **Year:** 2012.

**Provenance:** generated. **Structure availability:** `periodic_atomic`.

**Labels/content:** structure; pore size; surface area; methane adsorption.

**Access:** mixed. **Dataset license:** Not verified.

**Official routes:** [homepage](http://hmofs.northwestern.edu/) · [paper](https://doi.org/10.1038/nchem.1192)

**Evidence:**

- [Wilmer et al., Nature Chemistry](https://www.nature.com/articles/nchem.1192) (checked 2026-11-01): Original study generated 137,953 MOFs from 102 building blocks and calculated pore and methane-storage properties.
- [Author-hosted original paper](https://chemgroups.northwestern.edu/hupp/Publications/316.pdf) (checked 2026-11-01): Author paper confirms 137,953 generated structures from 102 building blocks.

**Reuse and interpretation notes:**

- Count is historical; downstream exports can contain fewer structures, including the NIST hMOF mirror.
- Original portal access and an explicit reusable data license were not established in this audit.
- Generated geometries do not establish synthesis or thermodynamic stability.

**Tags:** MOF, hypothetical, GCMC, historical.

<a id="mosaec-db"></a>
## MOSAEC MOF Database (MOSAEC-DB)

Experimental MOFs processed with solvent removal and chemical-consistency checks.

**Size:** ~124,000 processed MOF structures (source wording: ~124,000 MOF crystal structures).

**Scope:** Rounded count stated by the authors in the open metadata deposit.

**Release:** 1.0.0-release, January 2025. **Year:** 2025.

**Provenance:** experimental. **Structure availability:** `periodic_atomic`.

**Labels/content:** structure; activation status; chemical descriptors; partial charges; structural error flags.

**Access:** mixed. **Dataset license:** Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International; CIF access also requires CSD license.

**Official routes:** [data](https://zenodo.org/records/15808197) · [paper](https://doi.org/10.1039/D4SC07438F) · [code](https://github.com/uowoolab/MOSAEC-DB)

**Evidence:**

- [MOSAEC-DB author deposit](https://zenodo.org/records/15808197) (checked 2026-11-01): Approximately 124,000 processed experimental CSD structures; descriptors are open, while CIFs require a valid CSD license. Data terms are CC BY-NC-SA 4.0.

**Reuse and interpretation notes:**

- Licensing/access of downloadable descriptors differs from CSD structural files.
- Shares experimental source entries with CoRE and QMOF; preprocessing variants are not new independently synthesized materials.

**Tags:** MOF, experimental-derived, curation, restricted-CIF.

<a id="hcof-mercado"></a>
## Mercado hypothetical 2D and 3D COFs

Reticularly assembled hypothetical COFs evaluated for methane storage.

**Size:** 69,840 generated COF structures (source wording: 69,840 hypothetical COFs).

**Scope:** v3 CIF/property archive assembled from 666 linkers.

**Release:** Materials Cloud 2018.0003 v3. **Year:** 2018.

**Provenance:** generated. **Structure availability:** `periodic_atomic`.

**Labels/content:** structure; density; surface area; methane uptake; heat of desorption; deliverable capacity.

**Access:** open. **Dataset license:** Creative Commons Attribution 4.0 International.

**Official routes:** [data](https://archive.materialscloud.org/records/cjhyq-nr115) · [paper](https://doi.org/10.1021/acs.chemmater.8b01425)

**Evidence:**

- [Hypothetical COF Materials Cloud archive](https://archive.materialscloud.org/records/cjhyq-nr115) (checked 2026-11-01): 69,840 COFs assembled from 666 linkers into 2D-layered and 3D structures; CIFs and GCMC properties are released.
- [Hypothetical COF rights](https://archive.materialscloud.org/api/records/cjhyq-nr115) (checked 2026-11-01): File license is CC BY 4.0.

**Reuse and interpretation notes:**

- Classical simulation/storage predictions do not validate synthesis or DFT stability.
- 2D and 3D COFs are combined in this porous-framework category.

**Tags:** COF, hypothetical, GCMC.

<a id="core-mof"></a>
## CoRE MOF Database

Experimental-derived MOF structures curated for simulation and classified for structural validity.

**Size:** 43,439 MOF structure records (source wording: 43,439 full-family records; 9,256 openly deposited SI structures).

**Scope:** Full 2025 family across SI, CSD-modified and CSD-unmodified branches; includes CR and NCR.

**Release:** CoRE MOF 2025 v1.0. **Year:** 2025.

**Provenance:** mixed. **Structure availability:** `periodic_atomic`.

**Labels/content:** structure; pore geometry; topology; predicted partial charges; predicted stability; adsorption.

**Access:** mixed. **Dataset license:** CC BY 4.0 for Zenodo SI deposit; CSD-derived files have additional CCDC access terms.

**Official routes:** [homepage](https://chung-research-group.github.io/CoRE%20MOF%20Database.dc.html) · [data](https://zenodo.org/records/15621349) · [paper](https://doi.org/10.1016/j.matt.2025.102140) · [code](https://github.com/mtap-research/CoRE-MOF-Tools)

Other denominators (not added to the ranking):

- 9,256 open SI structure records: 2025 v1.0 Zenodo subset
- 2,737 computation-ready open SI structure records: 2025 v1.0 SI subset

**Evidence:**

- [CoRE MOF 2025 v1.0](https://zenodo.org/records/15621349) (checked 2026-11-01): Full family 43,439 = 9,256 SI + 21,009 CSD-modified + 13,174 CSD-unmodified; SI has 2,737 CR and 6,519 NCR entries. CSD update is marked not updated.
- [CoRE MOF 2024 release history](https://zenodo.org/records/15055758) (checked 2026-11-01): Prior family had 40,837 records and 8,300 SI structures. ASR/FSR duplicates and a recommended unique screening list are documented.
- [CoRE MOF 2025 deposit metadata](https://zenodo.org/api/records/15621349) (checked 2026-11-01): The SI file deposit declares CC BY 4.0; CSD branches have separate access terms.

**Reuse and interpretation notes:**

- Ranked count is the full mixed-access family; the open SI subset has 9,256 structures. The full family is not wholly computation-ready.
- Public 2025 SI contains 9,256 structures; modified CSD files require email registration and unmodified CSD files a CCDC license.
- 2025 deposit labels the CSD branches not updated; verify distribution before using those counts as available downloads.
- ASR and FSR variants can derive from the same original structure; use the release-specific recommended screening list.

**Tags:** MOF, experimental-derived, curation, release-family.

<a id="zeo-1"></a>
## Zeo-1

Periodic zeolite geometry-optimization trajectories with energies, gradients and stresses for potential fitting.

**Size:** 32,550 geometry-optimization frames (source wording: 32,550 geometries from 226 systems).

**Scope:** All optimization iterations, not independent zeolite frameworks.

**Release:** Materials Cloud 2021.171; Scientific Data 2022. **Year:** 2022.

**Provenance:** computed. **Structure availability:** `periodic_atomic`.

**Labels/content:** structure; energy; nuclear gradient; stress; Hirshfeld charges.

**Access:** open. **Dataset license:** Creative Commons Attribution 4.0 International.

**Official routes:** [data](https://archive.materialscloud.org/records/3xmh2-vv758) · [paper](https://doi.org/10.1038/s41597-022-01160-5)

**Evidence:**

- [Zeo-1 Scientific Data descriptor](https://www.nature.com/articles/s41597-022-01160-5.pdf) (checked 2026-11-01): Technical validation states 226 systems and 32,550 geometries; energies, gradients and stresses are given at each step.
- [Zeo-1 archived rights](https://archive.materialscloud.org/api/records/3xmh2-vv758) (checked 2026-11-01): Archive file license is CC BY 4.0.

**Reuse and interpretation notes:**

- 32,550 is a frame count; only 226 systems underlie the trajectories.
- Parent structures derive from IZA; structural-family overlap is expected.

**Tags:** zeolite, DFT, MLIP, trajectory, Scientific Data.

<a id="qmof"></a>
## Quantum MOF Database (QMOF)

Periodic DFT structures and electronic properties for MOFs and coordination polymers.

**Size:** ≥20,000 DFT-optimized structures (source wording: 20,000+ MOFs and coordination polymers).

**Scope:** Current author README lower bound; no exact current row count inferred from older papers.

**Release:** Figshare v18 / current author documentation. **Year:** 2025.

**Provenance:** mixed. **Structure availability:** `periodic_atomic`.

**Labels/content:** structure; DFT total energy; band gap; partial charges; spin density.

**Access:** open. **Dataset license:** CC BY 4.0.

**Official routes:** [homepage](https://github.com/Andrew-S-Rosen/QMOF) · [data](https://figshare.com/articles/dataset/13147324/18) · [paper](https://doi.org/10.1038/s41524-022-00796-6) · [code](https://github.com/Andrew-S-Rosen/QMOF)

**Evidence:**

- [QMOF author repository](https://github.com/Andrew-S-Rosen/QMOF) (checked 2026-11-01): Current author README describes 20,000+ MOFs and coordination polymers, CC BY 4.0 data, and no trajectories.
- [QMOF official Figshare metadata](https://api.figshare.com/v2/articles/13147324) (checked 2026-11-01): Current version is 18 with CC BY 4.0 data; separate QMOF-Thermo archive is present.

**Reuse and interpretation notes:**

- 20,375 is a historical widely cited count; later release notes removed individual structures, so it is not asserted as the current exact count.
- Includes experimental-derived and hypothetical MOFs; overlaps CoRE, Boyd-Woo and other MOF families.
- QMOF-Thermo is separately packaged and not added into this structure count.

**Tags:** MOF, DFT, electronic-properties.

<a id="core-cof"></a>
## Computation-Ready Experimental COF Database (CoRE COF)

Solvent-free and disorder-free COF structures compiled from experimental literature and reconstructed when coordinates were missing.

**Size:** 1,242 COF structure files (source wording: 1,242 CIFs).

**Scope:** CoRE-COFs_DT1242-v7.0.zip; independent archive inventory excluding macOS metadata.

**Release:** DT1242-v7.0; Git commit edbb24a, 2024-03-13. **Year:** 2024.

**Provenance:** mixed. **Structure availability:** `periodic_atomic`.

**Labels/content:** structure; framework geometry.

**Access:** open. **Dataset license:** Not verified.

**Official routes:** [homepage](https://github.com/core-cof/CoRE-COF-Database) · [data](https://github.com/core-cof/CoRE-COF-Database/blob/master/CoRE-COFs_DT1242-v7.0.zip) · [paper](https://doi.org/10.1016/j.ces.2017.05.004)

**Evidence:**

- [CoRE COF author repository](https://github.com/core-cof/CoRE-COF-Database) (checked 2026-11-01): v7 archive contains 1,242 CIFs; README states coordinate-free literature structures were reconstructed from experimental reports.
- [CoRE COF v7 archive](https://raw.githubusercontent.com/core-cof/CoRE-COF-Database/master/CoRE-COFs_DT1242-v7.0.zip) (checked 2026-11-01): Independent CIF inventory gives 1,242 files; ZIP SHA-256 and filename manifest retained.

**Reuse and interpretation notes:**

- Repository has a software-worded MIT license; explicit applicability to third-party experimental CIFs was not verified.
- Different preprocessing from CURATED COFs; source structures overlap.
- Historical counts 187/280/309/449/591/613 refer to older versions.

**Tags:** COF, experimental-derived, reconstructed, snapshot.

<a id="curated-cofs"></a>
## CURATED covalent organic frameworks

Literature COFs with tracked corrections, DFT-optimized structures, DDEC charges and adsorption workflows.

**Size:** 871 valid COF structures (source wording: 871 valid COFs plus 110 discarded entries).

**Scope:** July 2022 valid subset; excluded/discarded structures are not added.

**Release:** July 2022 extension; Materials Cloud archive updated 2023-11-02. **Year:** 2022.

**Provenance:** mixed. **Structure availability:** `periodic_atomic`.

**Labels/content:** structure; DDEC charges; pore geometry; adsorption isotherms; process performance.

**Access:** open. **Dataset license:** Creative Commons Attribution 4.0 International (Materials Cloud files).

**Official routes:** [homepage](https://materialscloud-org.github.io/mc-frontend/discover/curated-cofs) · [data](https://archive.materialscloud.org/records/1xf71-nf390) · [paper](https://doi.org/10.1021/acscentsci.9b00619) · [code](https://github.com/danieleongari/CURATED-COFs)

**Evidence:**

- [CURATED COFs archive release history](https://archive.materialscloud.org/records/1xf71-nf390) (checked 2026-11-01): July 2022 update contains 871 valid COFs and 110 discarded structures.
- [CURATED COFs file license](https://archive.materialscloud.org/api/records/1xf71-nf390) (checked 2026-11-01): Materials Cloud files carry CC BY 4.0.

**Reuse and interpretation notes:**

- 871 is a dated release count, not a claim about all COFs known in 2026.
- The GitHub repository can include discarded original structures and uses a separate software license.
- Built on CoRE-COF sources; substantial overlap is expected.

**Tags:** COF, DFT, AiiDA, curation.

<a id="iza-zeolites"></a>
## IZA Database of Zeolite Structures

Authoritative framework-type descriptions and representative crystallographic structures.

**Size:** 270 framework topology types (source wording: 270 approved framework type codes).

**Scope:** Approved IZA codes as of latest stated July 2026 update; not all chemical structures.

**Release:** Framework type codes updated 2026-07-30. **Year:** 2026.

**Provenance:** experimental. **Structure availability:** `periodic_atomic`.

**Labels/content:** representative structure; topology; powder diffraction; framework composition; spectra.

**Access:** open. **Dataset license:** Not verified.

**Official routes:** [homepage](https://www.iza-structure.org/databases/) · [data](https://www.iza-structure.org/IZA-SC/ftc_table.php)

**Evidence:**

- [IZA Framework Type Codes](https://europe.iza-structure.org/IZA-SC_FTC.php) (checked 2026-11-01): 270 framework codes assigned; latest approval July 10, 2026 and page updated July 30, 2026.
- [IZA official database](https://www.iza-structure.org/databases/) (checked 2026-11-01): Provides representative crystallographic data, powder patterns, references, topology descriptions and compositions.

**Reuse and interpretation notes:**

- 270 counts framework types, not compositions, CIF files or individual experimental samples.
- Intergrowths/disordered structures form a separate integrated collection.

**Tags:** zeolite, experimental, topology.
