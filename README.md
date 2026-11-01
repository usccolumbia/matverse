# MatVerse

**A source-verified atlas of crystal materials datasets.**

115 dataset and release records · 12 categories · 179 distinct dataset evidence URLs · checked **November 1, 2026**

MatVerse surveys periodic crystal structures and their associated data: experimental crystallography, computed inorganic solids, machine-learning interatomic potential (MLIP) configurations, 2D materials, porous frameworks, molecular crystals, surfaces, and property and discovery benchmarks. It also includes crystal-related experimental property collections that supply compositions or measurements without complete atomic coordinates.

The catalog includes **LeMat, MateriaViva Open, Alexandria, OMat24, Matbench Discovery/WBM, Scientific Data descriptors and Starrydata**, alongside established databases and newer releases. It is a broad, living survey rather than an exhaustive census. A record can be a dataset, a named subset, or a release; records are not necessarily independent corpora.

[Read the survey](docs/SURVEY.md) · [Full JSON](data/datasets.json) · [CSV export](data/datasets.csv) · [Repository and resource directory](docs/resources.md) · [Scientific Data index](docs/scientific-data.md) · [ACS paper crosswalk](docs/review-crosswalk.md) · [Lineage and overlap](docs/overlap.md) · [Methods and schema](docs/METHODOLOGY.md)

## Read the counts correctly

- **Structures/materials:** usually equilibrium or curated structural records. Polymorphs, temperatures, disorder models and functional variants can create several records per composition.
- **Configurations/frames:** snapshots from relaxation, molecular dynamics or perturbation. Millions of frames can originate from far fewer parent crystals.
- **Property records/samples/patterns:** observations, literature samples or characterization data. These may have no atom-resolved structure.
- **Aggregates and derivatives overlap.** LeMat, MateriaViva, parent databases, benchmark subsets and format mirrors cannot be added into one material total.
- **Access and licensing are separate.** A free website, model license or open-access paper does not establish a dataset's redistribution rights. Unverified terms remain explicit.

Each linked dataset card records the release, unit, count evidence, available structure level, provenance, labels, access, license and caveats. There are 5 records with unverified size; these remain unranked. Counts are mostly provider-reported, with selected metadata sums and small-file recounts identified explicitly. “Checked” means the documentation was inspected; it does not mean every payload was downloaded, every row audited, or each claim independently reproduced.

## Browse by category

- [Aggregated and deduplicated crystal collections](#aggregated-crystals) (3)
- [Computed bulk inorganic crystals](#bulk-computed) (8)
- [Experimental crystallography and reference collections](#experimental-crystallography) (9)
- [Bulk and mixed-domain MLIP configurations](#mlip-configurations) (14)
- [Two-dimensional and layered materials](#two-dimensional) (7)
- [MOFs, COFs and zeolites](#porous-frameworks) (15)
- [Molecular crystals and ice](#molecular-crystals) (3)
- [Surfaces, interfaces and catalysis](#surfaces-catalysis) (5)
- [Computed properties and prediction benchmarks](#property-benchmarks) (24)
- [Crystal generation and discovery benchmarks](#generation-benchmarks) (6)
- [Experimental properties and literature extraction](#experimental-properties) (16)
- [Diffraction, spectroscopy and characterization](#diffraction-spectroscopy) (5)

## Ranked catalog

Sizes descend **within each category**. Approximate figures use `~`, source lower bounds use `≥`, and unverified sizes appear last. Units remain explicit: these are volume rankings, not quality rankings. Click a dataset for its release, official download links, evidence and caveats.

<a id="aggregated-crystals"></a>
### Aggregated and deduplicated crystal collections

| Dataset / release | Reported size | Counted unit | Access | Data license |
|---|---:|---|---|---|
| [MateriaViva Open](docs/catalog/aggregated_crystals.md#materiaviva-open) | 10,903,588 | deduplicated crystal structures | open | Per row: CC BY 4.0, CC0 1.0, CC BY-SA 4.0, public domain, or MIT (provider declarations) |
| [LeMat-Bulk](docs/catalog/aggregated_crystals.md#lemat-bulk) | 6,725,590 | structure records | open | CC BY 4.0 |
| [LeMat-BulkUnique](docs/catalog/aggregated_crystals.md#lemat-bulkunique) | 5,438,436 | functional-specific unique records | open | CC BY 4.0 (card license section) |

<a id="bulk-computed"></a>
### Computed bulk inorganic crystals

| Dataset / release | Reported size | Counted unit | Access | Data license |
|---|---:|---|---|---|
| [Alexandria](docs/catalog/bulk_computed.md#alexandria) | ~5,800,000 | DFT-relaxed structures | open | CC BY 4.0 (provider About page) |
| [AFLOW](docs/catalog/bulk_computed.md#aflow) | 3,929,948 | database entries | open | Provider terms: free for scientific, academic and non-commercial use; other use prohibited |
| [OQMD](docs/catalog/bulk_computed.md#oqmd) | 1,407,395 | materials entries | open | CC BY 4.0 (OQMD download terms) |
| [GNoME released stable-materials set](docs/catalog/bulk_computed.md#gnome) | ~381,000 | novel structure records | open | CC BY-NC 4.0 (data); Apache 2.0 applies to code |
| [Carolina Materials Database](docs/catalog/bulk_computed.md#carolina) | 214,436 | inorganic materials entries | open | CC BY 4.0 (provider Terms of Use) |
| [Materials Project](docs/catalog/bulk_computed.md#materials-project) | 200,487 | materials entries | registration | CC BY 4.0 for core data; GNoME-origin data carry separate BY-NC acceptance |
| [JARVIS-DFT 3D](docs/catalog/bulk_computed.md#jarvis-dft-3d) | ~76,000 | structure records | open | CC BY 4.0 (3D Figshare dataset) |
| [Materials Cloud 3D (MC3D)](docs/catalog/bulk_computed.md#mc3d) | 32,013 | unique optimized structures | open | CC BY 4.0 (Materials Cloud record) |

<a id="experimental-crystallography"></a>
### Experimental crystallography and reference collections

| Dataset / release | Reported size | Counted unit | Access | Data license |
|---|---:|---|---|---|
| [Cambridge Structural Database (CSD)](docs/catalog/experimental_crystallography.md#csd) | 1,431,347 | crystal structures | mixed | Not verified |
| [Crystallography Open Database (COD)](docs/catalog/experimental_crystallography.md#cod) | 535,025 | entries | open | CC0 |
| [Materials Platform for Data Science (MPDS / PAULING FILE)](docs/catalog/experimental_crystallography.md#mpds-pauling-file) | 424,820 | crystalline structures | mixed | Not verified |
| [NIMS AtomWork-Adv](docs/catalog/experimental_crystallography.md#atomwork-adv) | 409,723 | crystal structures | commercial | Not verified |
| [Pearson's Crystal Data](docs/catalog/experimental_crystallography.md#pearsons-crystal-data) | ~395,000 | structural datasets | commercial | Not verified |
| [Inorganic Crystal Structure Database (ICSD)](docs/catalog/experimental_crystallography.md#icsd) | 347,985 | crystal structures | commercial | Not verified |
| [NIMS AtomWork](docs/catalog/experimental_crystallography.md#atomwork) | 82,000 | crystal structures | registration | Not verified |
| [MAGNDATA](docs/catalog/experimental_crystallography.md#magndata) | ≥2,000 | magnetic structures | mixed | Not verified |
| [American Mineralogist Crystal Structure Database (AMCSD)](docs/catalog/experimental_crystallography.md#amcsd) | Unranked | crystal structures | open | Not verified |

<a id="mlip-configurations"></a>
### Bulk and mixed-domain MLIP configurations

| Dataset / release | Reported size | Counted unit | Access | Data license |
|---|---:|---|---|---|
| [LeMat-Traj](docs/catalog/mlip_configurations.md#lemat-traj) | 121,274,458 | atomic configurations | open | CC BY 4.0 |
| [Open Materials 2024 (OMat24)](docs/catalog/mlip_configurations.md#omat24) | 101,849,946 | atomic configurations | open | CC BY 4.0 |
| [ELEMENTA public core release](docs/catalog/mlip_configurations.md#elementa-public) | ~39,000,000 | atomic configurations | open | CC BY-NC 4.0 |
| [sAlex25](docs/catalog/mlip_configurations.md#salex25) | ~14,000,000 | out-of-equilibrium configurations | open | CC BY 4.0 (Alexandria provider terms) |
| [sAlex (OMat24 distribution)](docs/catalog/mlip_configurations.md#salex-omat24) | 11,000,983 | atomic configurations | open | CC BY 4.0 |
| [ELEMENTA Spin](docs/catalog/mlip_configurations.md#elementa-spin) | ~4,700,000 | magnetic configuration frames | open | CC BY-NC 4.0 |
| [Materials Project Trajectory (MPtrj)](docs/catalog/mlip_configurations.md#mptrj) | 1,580,395 | atomic configurations | open | MIT (Figshare dataset record) |
| [MP-ALOE](docs/catalog/mlip_configurations.md#mp-aloe) | 909,792 | DFT configuration frames | open | Not verified for downloadable dataset |
| [MatPES](docs/catalog/mlip_configurations.md#matpes) | ~400,000 | sampled configurations | open | BSD 3-Clause (Hugging Face dataset card) |
| [ALIGNN-FF training dataset](docs/catalog/mlip_configurations.md#alignn-ff) | 307,113 | energy-labeled configurations | open | Not verified for training download |
| [Massive Atomic Diversity (MAD-1.5)](docs/catalog/mlip_configurations.md#mad15) | 216,803 | atomic configurations | open | Not verified for this archived version |
| [MPF.2021.2.8](docs/catalog/mlip_configurations.md#mpf2021) | 187,687 | ionic-step configurations | open | CC BY 4.0 (Figshare record) |
| [Massive Atomic Diversity (MAD-1.6)](docs/catalog/mlip_configurations.md#mad16) | Unranked | atomic configurations | open | CC BY 4.0 (Materials Cloud archive metadata) |
| [OpenLAM TrainingSet](docs/catalog/mlip_configurations.md#openlam-training) | Unranked | atomic configurations | mixed | Not verified |

<a id="two-dimensional"></a>
### Two-dimensional and layered materials

| Dataset / release | Reported size | Counted unit | Access | Data license |
|---|---:|---|---|---|
| [Computational 2D Materials Database (C2DB)](docs/catalog/two_dimensional.md#c2db) | 16,789 | database rows | mixed | Not verified |
| [van der Waals Bilayer Database (BiDB)](docs/catalog/two_dimensional.md#bidb) | 8,451 | homobilayer configurations | open | Not verified |
| [2DMatPedia](docs/catalog/two_dimensional.md#2dmatpedia) | 6,351 | monolayer structures | open | CC BY 4.0 |
| [Materials Cloud Two-Dimensional Structure Database (MC2D)](docs/catalog/two_dimensional.md#mc2d) | 3,077 | monolayer compounds | open | Creative Commons Attribution 4.0 International |
| [Quantum Point Defects Database (QPOD)](docs/catalog/two_dimensional.md#qpod) | 2,061 | defect-charge-state rows | open | Not verified |
| [JARVIS-DFT 2D snapshot](docs/catalog/two_dimensional.md#jarvis-2d) | 1,103 | 2D material records | open | CC BY 4.0 |
| [van der Waals 2D Heterostructure Database (HetDB)](docs/catalog/two_dimensional.md#hetdb) | 336 | heterobilayer structures | open | Not verified |

<a id="porous-frameworks"></a>
### MOFs, COFs and zeolites

| Dataset / release | Reported size | Counted unit | Access | Data license |
|---|---:|---|---|---|
| [Open Direct Air Capture 2025 (ODAC25)](docs/catalog/porous_frameworks.md#odac25) | ~70,000,000 | DFT configuration frames | registration | Creative Commons Attribution 4.0 International (dataset) |
| [Open Direct Air Capture 2023 (ODAC23)](docs/catalog/porous_frameworks.md#odac23) | 38,983,748 | DFT configuration frames | open | Creative Commons Attribution 4.0 International |
| [Deem hypothetical zeolites / PCOD SLC-good](docs/catalog/porous_frameworks.md#pcod-zeolites) | ~331,000 | hypothetical zeolite frameworks | open | Not verified |
| [Boyd-Woo hypothetical MOFs for wet flue-gas capture](docs/catalog/porous_frameworks.md#boyd-woo) | 324,426 | generated MOF structures | open | Creative Commons Attribution 4.0 International |
| [ab initio REPEAT Charge MOF Database (ARC-MOF)](docs/catalog/porous_frameworks.md#arc-mof) | ~280,000 | MOF structures | open | Creative Commons Attribution 4.0 International |
| [ReDD-COFFEE](docs/catalog/porous_frameworks.md#redd-coffee) | 268,687 | generated COF structures | open | Creative Commons Attribution Non Commercial Share Alike 4.0 International |
| [Wilmer hypothetical MOF database (hMOF)](docs/catalog/porous_frameworks.md#hmof-wilmer) | 137,953 | generated MOF structures | mixed | Not verified |
| [MOSAEC MOF Database (MOSAEC-DB)](docs/catalog/porous_frameworks.md#mosaec-db) | ~124,000 | processed MOF structures | mixed | Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International; CIF access also requires CSD license |
| [Mercado hypothetical 2D and 3D COFs](docs/catalog/porous_frameworks.md#hcof-mercado) | 69,840 | generated COF structures | open | Creative Commons Attribution 4.0 International |
| [CoRE MOF Database](docs/catalog/porous_frameworks.md#core-mof) | 43,439 | MOF structure records | mixed | CC BY 4.0 for Zenodo SI deposit; CSD-derived files have additional CCDC access terms |
| [Zeo-1](docs/catalog/porous_frameworks.md#zeo-1) | 32,550 | geometry-optimization frames | open | Creative Commons Attribution 4.0 International |
| [Quantum MOF Database (QMOF)](docs/catalog/porous_frameworks.md#qmof) | ≥20,000 | DFT-optimized structures | open | CC BY 4.0 |
| [Computation-Ready Experimental COF Database (CoRE COF)](docs/catalog/porous_frameworks.md#core-cof) | 1,242 | COF structure files | open | Not verified |
| [CURATED covalent organic frameworks](docs/catalog/porous_frameworks.md#curated-cofs) | 871 | valid COF structures | open | Creative Commons Attribution 4.0 International (Materials Cloud files) |
| [IZA Database of Zeolite Structures](docs/catalog/porous_frameworks.md#iza-zeolites) | 270 | framework topology types | open | Not verified |

<a id="molecular-crystals"></a>
### Molecular crystals and ice

| Dataset / release | Reported size | Counted unit | Access | Data license |
|---|---:|---|---|---|
| [Open Molecular Crystals 2025 (OMC25)](docs/catalog/molecular_crystals.md#omc25) | 26,257,042 | DFT configuration frames | mixed | Creative Commons Attribution 4.0 International (dataset) |
| [X23 diffusion Monte Carlo benchmark](docs/catalog/molecular_crystals.md#x23-dmc) | 23 | benchmark crystal systems | open | Not verified |
| [DMC-ICE13](docs/catalog/molecular_crystals.md#dmc-ice13) | 13 | benchmark periodic ice polymorphs | open | Not verified |

<a id="surfaces-catalysis"></a>
### Surfaces, interfaces and catalysis

| Dataset / release | Reported size | Counted unit | Access | Data license |
|---|---:|---|---|---|
| [Open Catalyst 2020 (OC20)](docs/catalog/surfaces_catalysis.md#oc20) | 133,934,018 | DFT configuration frames | open | Creative Commons Attribution 4.0 International |
| [Open Catalyst 2022 (OC22)](docs/catalog/surfaces_catalysis.md#oc22) | ~9,854,504 | DFT configuration frames | open | Creative Commons Attribution 4.0 International |
| [Open Catalyst 2025 (OC25)](docs/catalog/surfaces_catalysis.md#oc25) | 7,801,261 | DFT configuration evaluations | registration | Creative Commons Attribution 4.0 International (dataset) |
| [BEAST DB](docs/catalog/surfaces_catalysis.md#beast-db) | ≥20,000 | electrochemical DFT calculations | open | Not verified |
| [Computational Single-Atom Catalyst Database (NCEPU)](docs/catalog/surfaces_catalysis.md#sac-ncepu) | 1,197 | optimized catalyst configurations | open | Not verified |

<a id="property-benchmarks"></a>
### Computed properties and prediction benchmarks

| Dataset / release | Reported size | Counted unit | Access | Data license |
|---|---:|---|---|---|
| [WBM / Matbench Discovery stability test set](docs/catalog/property_benchmarks.md#wbm-matbench-discovery) | 256,963 | structure entries | open | CC BY 4.0 |
| [Matbench mp_e_form](docs/catalog/property_benchmarks.md#matbench-mp-e-form) | 132,752 | task samples | open | Not verified |
| [Matbench mp_gap / mp_is_metal (shared source cohort)](docs/catalog/property_benchmarks.md#matbench-mp-electronic) | 106,113 | task samples | open | Not verified |
| [LeMat-Rho](docs/catalog/property_benchmarks.md#lemat-rho) | 69,117 | materials | open | CC BY 4.0 |
| [Materials Project / Ricci electronic transport database](docs/catalog/property_benchmarks.md#mp-boltztrap-transport) | ~48,000 | materials | open | Creative Commons Zero v1.0 Universal (CC0-1.0) |
| [Materials Project Phonon database v1.1](docs/catalog/property_benchmarks.md#mp-phonon-2026) | 26,413 | materials | open | Creative Commons Attribution 4.0 International |
| [Phonix anharmonic phonon database](docs/catalog/property_benchmarks.md#phonix) | 20,912 | unique materials | open | Creative Commons Attribution 4.0 International |
| [OMDB-GAP1](docs/catalog/property_benchmarks.md#omdb-gap1) | 12,500 | materials | open | Not verified |
| [Matbench log_gvrh / log_kvrh (shared source cohort)](docs/catalog/property_benchmarks.md#matbench-elastic) | 10,987 | task samples | open | Not verified |
| [SNUMAT hybrid-functional band-gap dataset](docs/catalog/property_benchmarks.md#snumat-hybrid-gap) | 10,481 | materials | open | CC BY 4.0 |
| [PhononDB / MDR harmonic phonon calculation database](docs/catalog/property_benchmarks.md#phonondb-mdr) | 10,034 | material calculation entries | open | Creative Commons BY Attribution 4.0 International |
| [PhononDB lattice thermal conductivity (MDR)](docs/catalog/property_benchmarks.md#phonondb-mdr-ltc) | 4,811 | listed material calculation entries | open | Not verified |
| [Matbench dielectric](docs/catalog/property_benchmarks.md#matbench-dielectric) | 4,764 | task samples | open | Not verified |
| [AFLOW AEL–AGL thermomechanical cohort (2017)](docs/catalog/property_benchmarks.md#aflow-ael-agl-2017) | ≥3,500 | materials | open | Free for scientific, academic and non-commercial purposes; any other use prohibited (AFLUX documentation) |
| [SuperBand electronic-band / superconductivity dataset](docs/catalog/property_benchmarks.md#superband) | 2,474 | materials | open | Creative Commons Attribution 4.0 (database); MIT (software) |
| [Materials Project / Petretto DFPT phonons (2018)](docs/catalog/property_benchmarks.md#mp-dfpt-phonons-2018) | 1,521 | materials | open | Not verified |
| [Matbench phonons](docs/catalog/property_benchmarks.md#matbench-phonons) | 1,265 | task samples | open | Not verified |
| [Materials Project elastic tensor release (2015)](docs/catalog/property_benchmarks.md#mp-elastic-2015) | 1,181 | materials | open | Creative Commons Zero v1.0 Universal (CC0-1.0) |
| [JARVIS superconductivity 3D DFT cohort](docs/catalog/property_benchmarks.md#jarvis-supercon-3d) | 1,058 | materials | open | CC BY 4.0 |
| [Materials Project dielectric tensor release (2017)](docs/catalog/property_benchmarks.md#mp-dielectric-2017) | 1,056 | materials | open | Creative Commons Zero v1.0 Universal (CC0-1.0) |
| [Materials Project piezoelectric tensor release (2015)](docs/catalog/property_benchmarks.md#mp-piezo-2015) | 941 | materials | open | Creative Commons Zero v1.0 Universal (CC0-1.0) |
| [Matbench jdft2d](docs/catalog/property_benchmarks.md#matbench-jdft2d) | 636 | task samples | open | Not verified |
| [JARVIS superconductivity 2D DFT cohort](docs/catalog/property_benchmarks.md#jarvis-supercon-2d) | 161 | materials | open | CC BY 4.0 |
| [Phono3py 103-compound finite-displacement dataset (PBEsol)](docs/catalog/property_benchmarks.md#phonondb-103-pbesol) | 103 | compounds | open | Not verified |

<a id="generation-benchmarks"></a>
### Crystal generation and discovery benchmarks

| Dataset / release | Reported size | Counted unit | Access | Data license |
|---|---:|---|---|---|
| [OpenLAM Crystal Philately challenge collection](docs/catalog/generation_benchmarks.md#openlam-crystal-philately) | ≥19,800,000 | valid structures | registration | Not verified |
| [Alex-MP reference dataset (MatterGen public release)](docs/catalog/generation_benchmarks.md#alex-mp-mattergen-reference) | 845,997 | structures | open | Not verified |
| [Alex-MP-20 (MatterGen)](docs/catalog/generation_benchmarks.md#alex-mp20-mattergen) | 607,684 | structures | open | Creative Commons Attribution 4.0 International (upstream MP-20 and Alexandria data-release READMEs) |
| [MP-20 (CDVAE benchmark)](docs/catalog/generation_benchmarks.md#mp20-cdvae) | 45,231 | structures | open | Not verified |
| [Perov-5 / Matbench perovskites](docs/catalog/generation_benchmarks.md#perov5-cdvae-matbench) | 18,928 | structures | open | Not verified |
| [Carbon-24 (CDVAE benchmark)](docs/catalog/generation_benchmarks.md#carbon24-cdvae) | 10,153 | structures | open | Not verified |

<a id="experimental-properties"></a>
### Experimental properties and literature extraction

| Dataset / release | Reported size | Counted unit | Access | Data license |
|---|---:|---|---|---|
| [ChemDataExtractor battery materials database (2020)](docs/catalog/experimental_properties.md#cde-battery-2020) | 292,313 | property records | open | CC BY 4.0 |
| [High Throughput Experimental Materials Database (HTEM)](docs/catalog/experimental_properties.md#htem) | ≥140,000 | entries | mixed | Not verified |
| [Starrydata2 experimental materials datasets](docs/catalog/experimental_properties.md#starrydata2) | 106,815 | samples | open | CC BY 4.0 |
| [3DSC_ICSD](docs/catalog/experimental_properties.md#3dsc-icsd) | 86,490 | matched crystal structures | mixed | CC BY 4.0 (public labels/IDs only; underlying ICSD CIFs separately licensed) |
| [LeMat-Synth synthesis-procedure corpus](docs/catalog/experimental_properties.md#lemat-synth) | ~81,000 | source papers | mixed | Not verified |
| [Solid-state synthesis recipes with impurity phases](docs/catalog/experimental_properties.md#solid-state-synthesis-impurities) | 80,806 | synthesis reactions | open | CC BY 4.0 |
| [ChemDataExtractor/Snowball Curie–Néel dataset (2025)](docs/catalog/experimental_properties.md#cde-curie-neel-2025) | 56,037 | property records | open | CC BY 4.0 |
| [ChemDataExtractor Curie and Néel database (2018)](docs/catalog/experimental_properties.md#cde-curie-neel-2018) | 39,822 | property records | open | Not verified |
| [Text-mined solution-based inorganic synthesis procedures](docs/catalog/experimental_properties.md#text-mined-solution-synthesis) | 35,675 | synthesis procedures | open | CC BY 4.0 |
| [Digital Hydrogen Platform (DigHyd)](docs/catalog/experimental_properties.md#dighyd) | ≥30,000 | data entries | open | Not verified |
| [ChemDataExtractor thermoelectric materials database](docs/catalog/experimental_properties.md#cde-thermoelectric) | 22,805 | property records | open | MIT |
| [Text-mined inorganic solid-state synthesis recipes](docs/catalog/experimental_properties.md#text-mined-solid-state-synthesis) | 19,488 | synthesis entries | open | CC BY 4.0 |
| [3DSC_MP](docs/catalog/experimental_properties.md#3dsc-mp) | 5,773 | matched crystal structures | open | CC BY 4.0 |
| [DigBat / Dynamic Database of Solid-State Electrolytes](docs/catalog/experimental_properties.md#digbat) | 3,816 | experimental electrolyte materials | open | Not verified |
| [HYPOD-X: quasicrystals and approximants](docs/catalog/experimental_properties.md#hypod-x) | 1,448 | composition/sample instances | open | CC BY 4.0 |
| [MDR SuperCon Datasheet](docs/catalog/experimental_properties.md#mdr-supercon) | Unranked | records | open | Creative Commons BY Attribution 4.0 International |

<a id="diffraction-spectroscopy"></a>
### Diffraction, spectroscopy and characterization

| Dataset / release | Reported size | Counted unit | Access | Data license |
|---|---:|---|---|---|
| [ICDD Powder Diffraction File PDF-5+](docs/catalog/diffraction_spectroscopy.md#icdd-pdf5) | ≥1,126,200 | reference entries | commercial | Limited, nonexclusive, and nontransferable license |
| [opXRD: Open Experimental Powder X-ray Diffraction Database](docs/catalog/diffraction_spectroscopy.md#opxrd) | 92,552 | diffraction patterns | open | CC BY 4.0 |
| [MDR XAFS DB](docs/catalog/diffraction_spectroscopy.md#mdr-xafs) | 2,264 | collection items | open | CC BY-NC-SA 4.0 for whole database; individual data CC BY or CC BY-NC-SA |
| [Raman Open Database (ROD)](docs/catalog/diffraction_spectroscopy.md#raman-open-database) | 1,133 | entries | open | CC0 |
| [RRUFF mineral spectroscopy and diffraction](docs/catalog/diffraction_spectroscopy.md#rruff) | Unranked | samples | open | Not verified |

## Maintain and cite

Edit [data/datasets.json](data/datasets.json), then run `python3 scripts/build_catalog.py`. Run `python3 scripts/build_catalog.py --check` before opening a pull request. See [CONTRIBUTING.md](CONTRIBUTING.md) for count and source requirements.

Please cite each original dataset when reusing it. Use [CITATION.cff](CITATION.cff) to cite this catalog. Catalog text and metadata are CC BY 4.0; scripts are MIT. Listed datasets retain their own terms. MatVerse hosts catalog metadata and links; it does not mirror the dataset payloads.
