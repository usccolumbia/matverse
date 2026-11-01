# Dataset repositories, discovery tools and adjacent resources

[Back to MatVerse](../README.md)

These resources are navigation layers, collections, APIs, format mirrors or adjacent data. They are not additional independent crystal datasets and are not included in size rankings.

| Resource | Role | Description |
|---|---|---|
| [JARVIS-OPTIMADE](https://jarvis.nist.gov/optimade/jarvisdft/) | API | Standardized JARVIS-DFT structure queries. API reachability and authentication are recorded separately in the API source registry. |
| [OPTIMADE provider registry](https://providers.optimade.org/) | API registry | Machine-readable index of provider index-metadatabases; follow each provider links endpoint to discover child database base URLs. |
| [Broadband Electromagnetic Properties of Engineered Flexible Absorber Materials](https://doi.org/10.18434/mds2-2911) | adjacent composite electromagnetic measurements | Version 1.0.0 CSV figure data for PDMS/barium-hexaferrite nanoparticle composites up to 110 GHz. On-wafer calibration/de-embedding, finite-element calculations and mixing models support reuse. Values include extracted/model-derived effective properties and should not be treated as direct intrinsic single-crystal constants. NIST non-SRD reuse terms; no crystal count. |
| [Aged and unaged flexible unidirectional composite laminate tensile testing for soft body armor applications](https://doi.org/10.18434/M32078) | adjacent composite tensile dataset | PPTA flexible UD laminate tensile data across aging, displacement rate, gauge length, width and orientation, with raw CSV, summary spreadsheets and failure videos. README/catalog disagree on an example specimen dimension and 75% vs 76% aging RH; check specimen files and methods before pooling. Testing nominal 23°C/30%RH; README states no tensile standard exists for this material. NIST non-SRD terms; no crystal count. |
| [Data of High-Temperature Dynamic LCM Testing Setup](https://gdr.openei.org/submissions/1449) | adjacent drilling-material performance dataset | Nine XLSX test files plus two methods papers for polymer/fiber additives in 5 wt% bentonite mud, fracture widths 1000/3000µm and 100–400 psi. Downloaded water-control workbook has time, filtrate, pressure and temperature columns. One catalog description says 130°F while filename says 300°F; verify actual test records before pooling. CC BY 4.0; fluid/sealing system performance, no crystal count. |
| [Lost Circulation Materials in Geothermal Drilling: Thermal Degradation, Viscosity, Compression, and Flow Loop Tests](https://gdr.openei.org/submissions/1660) | adjacent drilling-material performance dataset | Thermal degradation, viscosity, compression and flow-loop measurements for lost-circulation materials, with photos and methods papers. Downloaded degradation workbook contains 7 material tabs, temperature/time, mass-before/after and grams units; full archive coverage was not audited. Catalog reports 90–250°C tests and material/condition-coded files. CC BY 4.0; heterogeneous drilling additives and system performance, no crystal count. |
| [WebFF](https://webff-documentation.readthedocs.io/en/latest/Introduction.html) | adjacent force-field repository and curation infrastructure | Documented repository for molecular-dynamics force-field parameters for organic and soft materials, using XML schemas and NIST curation infrastructure. Documentation describes public search/download and authorized-account curation. The documentation was reachable, but the live webff.nist.gov data portal could not be confirmed in this audit. Force-field parameterizations are not crystal datasets; a blanket data license was not verified. |
| [EAF Slag Characterization](https://doi.org/10.23719/1531971) | adjacent industrial-solid leaching dataset | Three verified XLSX files for EAF slag pH-dependent leaching, acid-neutralization and fraction comparisons. Workbooks retain sample/test IDs, mg/L, mg/kg-dry, liquid/solid ratios, detection limits, LeachXS 3.0.79 processing and 2025 review dates. Below-limit values use half detection limits; means and replicates coexist. EPA default U.S. public-domain terms. Industrial-solid reuse reference with no atomic crystal structure count. |
| [ANI-1x Active-Learning Molecular Dataset](https://github.com/aiqm/ANI1x_datasets) | adjacent molecular or polymer dataset | Active-learning molecular configurations sampled with dynamics, normal modes, torsions, and dimers. Provides energies, forces, charges, and multipoles for organic molecules containing hydrogen, carbon, nitrogen, and oxygen. Molecular/polymer reference resource, outside the periodic-crystal ranking. Approximately five million configurations of 64,000 molecules and molecular complexes, following the authors' ANI-1x description (https://pmc.ncbi.nlm.nih.gov/articles/PMC6602931/). Both counts are rounded. Label availability varies across methods and properties; missing HDF5 values are not computed results. The same archive includes ANI-1ccx, approximately 500,000 selected configurations relabeled with an approximate CCSD(T)/CBS scheme. They overlap ANI-1x and are not added to its structure count. |
| [Open Molecules 2025](https://github.com/facebookresearch/fairchem/blob/main/docs/molecules/datasets/omol25.md) | adjacent molecular or polymer dataset | Molecular energies and forces spanning neutral organics, biomolecules, electrolytes, and metal complexes across 83 elements. Configurations include varying total charges and spin multiplicities, with structures up to roughly 350 atoms. Molecular/polymer reference resource, outside the periodic-crystal ranking. Counts the 101,666,280-structure training split in Table 1 (https://arxiv.org/html/2505.08762v1#S2.T1). The 4M and neutral subsets overlap it; validation and evaluation splits are additional. Dataset downloads require a Hugging Face account and access request. The data use CC-BY-4.0, not the separate FAIR Chemistry license for model weights. OPoly26 (/data/opoly26) extends coverage to polymers. The electronic-structure subset (/data/omol25-electronic) provides richer ORCA outputs for approximately four million existing OMol25 configurations. |
| [Open Molecules 2025 Electronic-Structure Subset](https://github.com/facebookresearch/fairchem/blob/main/docs/molecules/datasets/omol25_elec.md) | adjacent molecular or polymer dataset | Rich electronic-structure outputs for an approximately four-million-configuration subset of OMol25, including wavefunction files, density matrices, and raw ORCA outputs for learning properties beyond energies and forces. Molecular/polymer reference resource, outside the periodic-crystal ranking. Rounded subset size reported by the project. These configurations overlap OMol25 (/data/omol25); they are not additional structures. The documented subset is distributed through Argonne's application process and Globus. The much larger full-corpus electronic-output archive is available only on request and is not counted here. |
| [Open Polymers 2026](https://arxiv.org/abs/2512.23117) | adjacent molecular or polymer dataset | Polymer-derived clusters with varying monomers, chain lengths, architectures, and solvation, including configurations with up to 360 atoms. Uses the OMol25 level of theory to extend molecular potentials to polymer environments. Molecular/polymer reference resource, outside the periodic-crystal ranking. The paper (https://arxiv.org/html/2512.23117v1) lists 6,099,878 training, 210,924 validation, and 259,740 test structures, totaling 6,570,542 configurations. Distributed from the OMol25 Hugging Face page under CC-BY-4.0. Account and access-request requirements apply there. |
| [Quantum Chemistry of 134 Thousand Small Organic Molecules](https://springernature.figshare.com/collections/Quantum_chemistry_structures_and_properties_of_134_kilo_molecules/978904) | adjacent molecular or polymer dataset | Equilibrium geometries and quantum-chemical properties of small organic molecules with up to nine heavy atoms. Includes energies, harmonic frequencies, dipoles, polarizabilities, and thermochemical properties, rather than off-equilibrium force trajectories. Molecular/polymer reference resource, outside the periodic-crystal ranking. Counts the full 133,885-molecule archive. The authors' README (https://springernature.figshare.com/articles/dataset/Readme_file_Data_description_for_Quantum_chemistry_structures_and_properties_of_134_kilo_molecules_/1057641) flags 3,054 structures failing a geometry-to-SMILES consistency check; filtered benchmark variants should state their exclusions. |
| [Revised Molecular Dynamics 17](https://figshare.com/articles/dataset/Revised_MD17_dataset_rMD17_/12672038) | adjacent molecular or polymer dataset | Molecular-dynamics configurations of ten molecules with energies and forces recomputed using tight convergence and dense integration grids. Provides fixed training and test splits for evaluating molecular force-field learning. Molecular/polymer reference resource, outside the periodic-crystal ranking. Materials counts the ten molecules in the release (https://doi.org/10.6084/m9.figshare.12672038.v4). Nine have 100,000 configurations each; azobenzene has 99,988 after failed calculations, giving 999,988 total structures. Frames come from correlated time series. The authors recommend using the supplied small training splits rather than treating large random frame samples as independent data. |
| [Small-Molecule/Protein Interaction Chemical Energies 2](https://github.com/openmm/spice-dataset) | adjacent molecular or polymer dataset | Molecular conformations for learning energies, forces, charges, and multipoles across 17 elements. Covers drug-like molecules, peptides, solvated species, ion pairs, water clusters, and noncovalent interactions. Molecular/polymer reference resource, outside the periodic-crystal ranking. Approximately two million conformations. The version-2 table (https://github.com/openmm/spice-dataset#spice-a-dataset-for-training-machine-learning-potentials) lists 2,008,628, but version 2.0.1 removes configurations with broken bonds. The count is rounded rather than presenting the older total as an exact size for the corrected release. The dataset is CC0; the accompanying generation scripts have a separate MIT license. |
| [Data for Advanced Metrology Suite for Linking Residual Stress to Fundamental Properties of Thermoset Packaging Materials](https://data.nist.gov/od/id/mds2-3698) | adjacent packaging-polymer metrology dataset | DSC, rheology, DIC, vapor uptake and stress-bench data for a commercial encapsulant epoxy, with CSV/XLSX/MAT, calibration images and method notes. Catalog describes about 2.5 GB and links ECTC 2025 paper 10.1109/ECTC51687.2025.00078. Not independently bulk-downloaded or recounted; _hold and current file routes may overlap. NIST non-SRD terms; adjacent cure/residual-stress resource, no crystal count. |
| [Aged and unaged PBIA-based copolymer testing for soft body armor applications](https://data.nist.gov/od/id/mds2-2123) | adjacent polymer aging dataset | Three PBIA-based fibers: tensile, FTIR and moisture data with CSV/XLS/ODS exports and hydrothermal-aging condition codes. README names ASTM D3822/C1557, FTIR cm−1/absorbance units and nominal 23°C/30%RH testing. Its citation mistakenly points to laminate DOI M32078; catalog identifies PBIA as M32123/mds2-2123. Polymer resource under NIST non-SRD terms; archive contents not independently recounted. |
| [A Materials Properties Dataset for Elastomeric Foam Impact Mitigating Materials](https://data.nist.gov/od/id/mds2-2606) | adjacent polymer mechanics dataset | Elastic impact foams: raw/processed DMA, DIC, compression, drop-tower, micro-CT, FTIR and DSC data with analysis tools. Strong reuse documentation includes batch/specimen IDs, geometry and uncertainty. VN01 notes report frequency ±5%, moduli ±8%, temperature ±0.1°C; its SHA-256 matches provider. A catalog-listed EVA1 notes file returned 404. Noncrystalline polymer/foam resource; no unique-crystal count. NIST non-SRD reuse terms apply. |
| [Data for A Switchable Longitudinal & Shear BLS Microscope for Comprehensive Modulus Imaging of Semiconductor Packaging Materials](https://data.nist.gov/od/id/mds2-4059) | adjacent polymer modulus imaging dataset | Longitudinal/shear BLS maps and comparison nanoindentation/DMA for proof-of-concept packaging epoxies. TXT headers give GHz/GPa/µm units; raw spectra, fits and code are documented. Calibration uses VIPA free spectral ranges; lab 21±2°C/35±5%RH. Derived moduli assume density/refractive index and filtering; README erroneously cites companion DOI 3725, so retain 4059 identifier. Polymer resource, no crystal count; NIST non-SRD terms. |
| [Polymer Property Predictor and Database (PPPDB)](https://pppdb.uchicago.edu/) | adjacent polymer phase-property database and tools | CHiMaD-associated polymer data and prediction tools covering Flory–Huggins interaction parameters, glass-transition temperatures and cloud points, with phase-diagram and structure-factor applications. Public property tables were accessible without signing in. Periodic atomic structures and a database-wide reuse license were not verified. |
| [Polymer Properties Database (PolymerDatabase.com)](https://polymerdatabase.com/home.html) | adjacent polymer reference (availability limited) | User-nominated polymer reference endpoint retained for discovery provenance. The requested page and HTTP, root-domain and www variants returned a hosting-provider page saying the site is temporarily unavailable, rather than polymer data, on the audit date. Original content, registration conditions and data licensing could not be verified; this observation is not a formal end-of-service claim. |
| [Data for A Dual Mode Brillouin/Low-Frequency Raman Spectroscopy Microscope for Local Mechanical Property Imaging for Semiconductor Packaging Materials](https://data.nist.gov/od/id/mds2-3725) | adjacent polymer spectroscopy dataset | BLS/low-frequency Raman raw spectra, fits and time/temperature axes for epoxy cure, glass transition and hyperspectral mapping. Calibration uses LaAlO3 Raman reference and VIPA free spectral ranges; lab 21±2°C/35±5%RH. Units and figure mappings are documented; masks and model fits must remain distinct from measured signals. Polymer resource under NIST non-SRD terms. |
| [PoLyInfo](https://polymer.nims.go.jp/) | adjacent polymer-property database | NIMS literature-derived polymer properties with chemical constitutive structures, sample, preparation and measurement information. Chemical polymer structures do not imply periodic atomic crystal structures. Access requires DICE registration, an eligible email domain and a MatNavi usage application; bulk acquisition and scraping are prohibited, and redistribution requires written NIMS permission. A separate paid-dataset route is advertised. |
| [Near Infrared Spectra of Origin-defined and Real-world Textiles (NIR-SORT): A spectroscopic and materials characterization dataset for known provenance and post-consumer fabrics](https://data.nist.gov/od/id/mds2-3325) | adjacent textile spectroscopy benchmark | NIR-SORT provides textile spectra, microscopy, data dictionary, conditions, reference/uncertainty schemas, utility scripts and NIST data/code terms. Catalog describes 113 fabrics and nominal 7 replicates on 3 instruments; inspected root SampleInformation.csv has 64 rows/64 unique IDs, so 113 is unconfirmed as a reconciled payload count. Consumer fabric content is nominal garment-label information, explicitly uncorroborated. Polymer/textile resource; MDF is a mirror, no crystal count. |
| [Battery Archive](https://batteryarchive.org/) | adjacent_experimental_data_portal | Cross-institution battery cycling and disruptive-test data; cell-performance resource adjacent to crystal datasets. Full CSV files requested by email. |
| [JARVIS-DFT2](https://jarvis.nist.gov/jarvisdft2) | alternate portal | Second JARVIS-DFT portal listed with the same broad DFT description; linked to the existing DFT family without adding a duplicate 80,000+ count. |
| [Archived Wikipedia List of Superconductors (IEEE-linked PDF)](https://webdisk.science.upjs.sk/~martin_gmitra/Theory%20of%20Condensed%20Matter/Supporting%20Materials/11/List_of_superconductors_wikipedia.pdf) | archived reference list | IEEE-linked historical list hosted on an academic website. It is retained as a source-navigation route; currency, row count and independent validation were not established, so it is not ranked as a new dataset. |
| [JARVIS-Leaderboard](https://pages.nist.gov/jarvis_leaderboard/) | benchmark collection | Reproducible methods and datasets spanning theory and experiments; benchmark data points overlap underlying source datasets. |
| [Matbench v0.1 suite](https://matbench.materialsproject.org/) | benchmark suite | Thirteen property-prediction tasks from ten underlying sources; includes both composition-only and structure inputs. The catalogue groups shared structure cohorts and does not sum tasks as unique crystals. |
| [Materials Cloud OPTIMADE Client](https://optimadeclient.materialscloud.io/) | browser client | Browser interface to select an OPTIMADE provider and child database, filter structures and inspect/download results. A client for existing providers, not an independent crystal dataset. |
| [OPTIMADE clients directory](https://www.optimade.org/clients) | client directory | Official comparison of Materials Cloud OPTIMADE Client, optimade.science, optimade-python-tools and Swagger/OpenAPI interfaces; distinguishes individual-database and federated searches. |
| [ACerS-NIST Phase Equilibria Diagrams Database (SRD 31)](https://www.nist.gov/srd/nist-standard-reference-database-31) | commercial evaluated reference database | Version 6.0 (2025) provides 34,000 phase-equilibrium diagrams with expert literature evaluations for inorganic systems. Current primary page offers paid single/multiple-user products and directs Phase Online orders to ACerS. Diagram totals are not unique materials; joint NIST/ACerS copyright and commercial access preclude describing this as an open data download. Free PED Editor software is separate from database access. |
| [SpringerMaterials](https://materials.springer.com/) | commercial_database_portal | Commercial curated materials-property platform covering several source collections. |
| [IEEE CSC Superconductor Properties Wiki](https://wiki.ieeecsc.org/) | community property-reference wiki | Community-maintained superconducting parameters with literature citations, including Tc, Jc, critical fields, specific heat, gap and structure parameters. IEEE advertises thousands of materials; an independently verified record count, data export and dataset-wide license were not established. IEEE states that it verifies publication provenance rather than entry accuracy. |
| [GDR low-temperature geothermal thermoelectric material measurements](https://gdr.openei.org/submissions/692) | conditional thermoelectric development dataset | Small BiSbTe/BiSeTe development tables: 19 specimen rows plus 10 module rows. Useful for a narrowly defined device study; missing per-row temperature, stoichiometry and uncertainty limit general property learning. Density values above 100% and a module resistance-unit inconsistency require source resolution. |
| [LeMat-GenBench](https://github.com/LeMaterial/lemat-genbench) | crystal-generation evaluation framework | Evaluates generated crystals using validity, distribution, diversity, novelty, and stability metrics with multi-MLIP/hull configurations; its reference datasets overlap LeMat-Bulk. Framework code is Apache licensed; not an additional crystal count. |
| [NIST Materials Data Repository](https://materialsdata.nist.gov/) | data_repository | Materials research deposits from NIST and the wider community; terms are defined per provider and collection. |
| [NIST 62 / NIST–NRIM superconductors Version 2.0 publication](https://www.nist.gov/publications/nist-62-nistnrim-high-temperature-superconductors-database-version-20) | database documentation | R. G. Munro’s NIST publication page (16 October 2008) documents evaluated superconducting, thermal, mechanical and crystallographic properties from 1987–1996 literature. Treated as documentation of the already cataloged NIST SRD 62 / WebHTS database family; the page does not establish a separate downloadable corpus or new release denominator. |
| [Computational Materials Repository (CMR)](https://cmr.fysik.dtu.dk/) | database portal | DTU portal for project-specific ASE databases spanning low-dimensional materials, bulk crystals, perovskites, surfaces and related benchmarks. Provides project documentation, browser routes, downloadable databases and an OPTIMADE route. Provider states CMR databases use CC BY-SA 4.0. Portal totals are not an additional crystal dataset. |
| [JARVIS-DMFT](https://jarvis.nist.gov/jarvisbdft) | database portal | Dynamical mean-field theory portal listed by JARVIS. Current count, public machine payload and dataset license were not established; access redirects to login. |
| [Organic Materials Database (OMDB)](https://omdb.mathub.io/) | database portal | Electronic and magnetic information portal for periodic organic and organometallic crystals, including band structures, DOS and magnetic-excitation tools. Named downloads distinguish DFT-labelled OMDB-GAP1 from COD model predictions. Public browsing is limited and named downloads currently redirect to free-registration login; a current full-family count and dataset-wide reuse license were not verified. |
| [UCSD Superconducting Research Database (Schuller group)](https://srd.physics.ucsd.edu/) | database reference | Community database of materials tested for superconductivity, inviting researchers to upload results to reduce redundant testing. Live endpoint returned server errors during verification; current material/test counts, positive/negative/untested status definitions, crystal-file availability, uploader authentication and license remain unverified. This UCSD project is separate from NIST SRD 62. |
| [Catalysis-Hub / CatHub](https://www.catalysis-hub.org/) | database_portal | Open surface-reaction collection with geometries, reaction energies and linked calculations; primary 2019 descriptor reported >100,000 adsorption/reaction energies, which is a historical property count rather than a current count of unique materials. |
| [Digital Catalysis Platform (DigCat)](https://www.digcat.org/) | database_portal | Experimental-performance and computational-structure platform. Provider page currently reports >0.4M experimental and >0.4M computational records; a 2024 author preprint reports >400k performance records and >300k structures. Counts are version-dependent and not a unique-material ranking; bulk data license not verified. |
| [MOFX-DB](https://mof.tech.northwestern.edu/) | database_portal | Adsorption-data portal aggregating experimental and hypothetical MOFs, COFs and zeolites. Source datasets overlap CoRE, hMOF, ToBaCCo and IZA; portal totals are not additional unique structures. |
| [NIMS MatNavi](https://mits.nims.go.jp/en/) | database_portal | Registered browsing across inorganic, metallic, thermophysical and other materials databases; mass downloading and scraping prohibited. |
| [Data Resources for Materials Science](https://github.com/sedaoturak/data-resources-for-materials-science) | dataset collection | User-supplied dataset/resource collection. All inspected document links, scope labels and revision provenance are preserved in sources.md; linked dataset counts require their own primary evidence. |
| [ColabFit Exchange](https://materials.colabfit.org/) | dataset exchange | Searchable atomistic datasets and standardized configurations; tracks separate property and configuration identifiers, including mixed molecular and periodic domains. |
| [Matbench Discovery data sets](https://matbench-discovery.materialsproject.org/data/sets) | dataset registry and benchmark | Registry of model training/reference/test datasets and a discovery-style stability benchmark. User-nominated page returned HTTP 403; its first-party GitHub registry and WBM documentation were used. |
| [NIMS MatDaCs](https://mat-dacs.dxmt.nims.go.jp/en/) | dataset_discovery_catalog | Discovery catalogue for materials databases and computational tools, including provider links and openness notes. |
| [Digital Hydrogen-S](https://digital-hydrogen.com/storage) | dataset_portal_pending_primary_verification | Solid-state hydrogen-storage data portal identified in the supplied review. Primary paper exists; primary content and current portal totals could not be independently inspected. |
| [SevenNet-Omni domain bridging set](https://doi.org/10.6084/m9.figshare.30399814) | domain bridging data | Primary paper makes the bridging DFT data available through this deposit. Distinguish recomputed bridging structures from the 15 overlapping source datasets and their mixed-domain frame total. |
| [JARVIS Figshare curated datasets](https://pages.nist.gov/jarvis/databases/) | download registry | Named datasets, historical snapshots and third-party mirrors distributed through jarvis-tools; all table entries are inventoried with their download routes. |
| [Machine Learning Materials Datasets / MAST-ML education](https://figshare.com/articles/dataset/MAST-ML_Education_Datasets/7017254) | educational dataset collection | Three MIT-licensed educational tables for MAST-ML: dilute-solute diffusion, perovskite stability and adjacent metallic-glass properties. Feature rows have no atomic coordinates; source families and packaging must remain distinct. |
| [NIST Property Data Summaries for Advanced Materials (SRD 150)](https://srdata.nist.gov/CeramicDataPortal/pds) | evaluated property reference summaries | Condition-specific literature property summaries, including alumina, silicon carbide and titanium diboride. The alumina table documents units, temperatures, material purity/density and uncertainty notation. Data content last updated 2002; derived summaries overlap SRD30 and topical databases and should not be added to their counts. No open redistribution license verified; portal states copyright/all rights reserved. |
| [Sandia Technical Reference for Hydrogen Compatibility of Materials](https://www.sandia.gov/matlstechref/) | evaluated technical handbook | Reference chapters compile deformation, fracture and fatigue evidence for hydrogen service; archive SAND2012-7321 (2012) and individually revised chapters. Downloadable PDF verified. Chapters are not independent material records; the complementary structured database currently says under construction, with a new Granta MI link planned for Fall 2026. No collection-specific data reuse license verified. |
| [JARVIS Universal Search](https://jarvis.nist.gov/jarvisus) | federated search | Search layer across JARVIS databases; it does not contribute a new independent data count. |
| [LeMaterial Atompack](https://huggingface.co/datasets/LeMaterial/Atompack) | format mirror | Public atomistic datasets repackaged for streaming in Atompack format. The card identifies upstream MatPES, MP-ALOE, MPtrj, OMat24 and OC20; do not count format mirrors as new datasets. |
| [Awesome Materials & Chemistry Datasets](https://github.com/blaiszik/awesome-matchem-datasets) | github_collection | Broad discovery list of materials and chemistry datasets; verify each numerical claim at the originating repository. |
| [matminer dataset collection](https://github.com/hackingmaterials/matminer) | github_collection | Python loaders and dataset metadata for community materials datasets; retain original dataset citations and licences. |
| [Roberts superconductive-materials survey (1976; literature through March 1975)](https://doi.org/10.1063/1.555540) | historical evaluated data tables | B. W. Roberts reference compilation of critical temperatures, critical fields, composition and crystal-structure types, including negative experiments. IEEE labels it by the 1975 literature cutoff; the publication is Journal of Physical and Chemical Reference Data 5, 581 (1976). Retained as a reference source rather than a separately counted modern dataset. |
| [Roberts Properties of Selected Superconductive Materials, 1978 Supplement](https://doi.org/10.6028/NBS.TN.983) | historical reference supplement | NBS Technical Note 983 supplements the earlier survey with literature through fall 1977, including Tc, critical fields, crystal structure and negative experiments. No independent structure or sample total is inferred from this publication. |
| [REMI: REsource for Materials Informatics](https://pages.nist.gov/remi/) | instructional resource and dataset directory | NIST pre-alpha notebook/resource index with tagged tutorials, learning resources and directly linked experimental combinatorial libraries. Owning GitHub repository is archived; directory entries are not additive datasets. |
| [nanoHUB Machine Learning Lab Module](https://nanohub.org/tools/intromllab) | interactive educational module | Version1.7 introductory materials-ML notebook and teaching module. Public descriptions/supporting-document list are readable; running the tool requires login. Program license is GPL3-or-later; example-data rights require separate checking. |
| [NIST Interatomic Potentials Repository](https://www.ctcms.nist.gov/potentials/) | interatomic model and validation resource | Developer-submitted/vetted interatomic potentials with source references, parameter files and reproducible property-evaluation tools (iprPy). Useful for selecting and testing atomistic models; model-specific domains and licenses apply. Potential counts and calculated test results are not a new independent crystal-structure corpus. |
| [OpenKIM](https://openkim.org/) | interatomic-model archive and testing infrastructure | Versioned archive of physics-based and machine-learning interatomic potentials, with model verification, property tests, simulation interfaces and a public query API. Crystal Genome organizes model-generated crystal-property predictions. Models and their test results must not be counted as independent experimentally measured or DFT-labeled crystals; an archive-wide data license was not verified. |
| [OPTIMADE](https://www.optimade.org/) | interoperability API | Common API specification for querying structure providers; a federation/interface, not an additional independent dataset. |
| [Scientific Data materials Data Descriptors](https://www.nature.com/sdata/) | journal_collection | Scientific Data materials descriptors and linked deposits. A journal-wide metadata search and topical primary-source audit are documented in MatVerse; article metadata and unreviewed leads remain separate from verified dataset releases. |
| [MaterialsWeb](https://materialsweb.org/) | legacy database portal | Hennig-group portal historically covering calculated 2D materials, bulk materials and computational benchmarks. Author paper released an 826-monolayer cohort in 2017. Current host failed TLS access in the 2026-11-01 audit, so live browsing, bulk downloads, current totals and data reuse rights remain unverified. |
| [CatApp](https://cmr.fysik.dtu.dk/catapp/catapp.html) | legacy_property_database | Legacy reaction/activation-energy table for elementary surface reactions. The ~3,000-reaction scale is historical; CatApp does not supply detailed atomic geometries, so it is a navigation/property resource. |
| [JARVIS-ChemNLP](https://jarvis.nist.gov/jarvischemnlp) | literature discovery | Chemical-formula search over open-access papers; a text discovery service, not another crystal-structure corpus. |
| [Tran et al. review: Superconductor Discovery in the Emerging Paradigm of Materials Informatics](https://doi.org/10.1021/acs.chemmater.4c01757) | literature review | 2024 Chemistry of Materials review by Huan Tran, Hieu-Chi Dam, Christopher Kuenneth, Vu Ngoc Tuoc and Hiori Kino, 36(22), 10939–10966. Surveys computational hydrides and superconductivity informatics, including composition tables, structure matching, EPC computation and literature extraction. Used for discovery leads; current releases were checked at author repositories. |
| [CERN STEAM Materials Library (SMaLi)](https://steam.docs.cern.ch/libraries/materials/) | material-property model library | Collection of coded material-property functions for superconducting-magnet engineering, with C implementations and wrappers for Python, MATLAB, GetDP and COMSOL. Documentation includes HTS/LTS critical-current-density models. This is a model/software library, not a counted experimental crystal database. |
| [Materials Data Facility / Foundry](https://www.materialsdatafacility.org/) | materials repository and data-access platform | Materials-data publication and discovery services with a searchable deposit catalog. Foundry supplies schemas and programmatic loading for structured subsets. Access and reuse terms vary by deposit; deposit counts are not unique-crystal totals. |
| [NIST MGI Materials Data Resources](https://www.nist.gov/mgi/materials-data-resources) | materials resource directory | NIST directory of materials repositories, registries, schemas, phase-data resources and atomistic-potential services. It is a discovery resource, not an additional crystal dataset; access and reuse terms belong to each linked provider. Its Materials Resource Registry link currently redirects to the MGI landing page. |
| [MatterSim training data availability](https://github.com/microsoft/mattersim/blob/main/MODEL_CARD.md) | model and availability reference | Public model cards describe training data sizes and released checkpoints. This survey did not verify a complete public training-data download, so checkpoint sizes are not ranked as datasets. |
| [SCLib / JZIS superconducting-transition records](https://jzis.org/materials) | model-curated literature-data portal | Additional primary-source lead outside the IEEE list. Public snapshot reports 13,282 transition results from 6,122 papers, with sample/criterion/condition provenance and CSV downloads. Model checks and sampled-batch checks are not individual expert validation. Project-created data use CC BY 4.0, while upstream-source terms remain applicable; no independent crystal count is claimed here. |
| [AFLOW AEL/AGL thermomechanical property libraries](https://aflow.org/documentation/) | property-library access resource | Distinct AFLOW workflows exposing elastic tensors/moduli and Debye/thermal estimates through AFLUX. Current property-bearing cohort sizes were not verified; no independent current materials count is claimed. |
| [Materials Cloud Archive](https://archive.materialscloud.org/) | repository platform | Versioned dataset deposits with DOI records, files and, for selected datasets, AiiDA provenance graphs. Each deposit needs its own count and license. |
| [NOMAD Repository and Archive](https://nomad-lab.eu/) | repository platform | Code-agnostic raw and normalized computational and experimental archives. Provider snapshot reports 19,425,275 entries and 4,346,100 represented materials; these heterogeneous counters are not a count of unique bulk crystals. |
| [OpenAlex specialized-property discovery](https://openalex.org/) | scholarly discovery | Scholarly metadata search used to discover specialized materials property datasets; citations and retrieved works are not material records. |
| [Configurable Data Curation System (CDCS / MDCS)](https://www.nist.gov/itl/ai/applied-ai-research-group/configurable-data-curation-system-cdcs/about-cdcs) | scientific data curation software infrastructure | NIST software infrastructure for schema-based capture, sharing, transformation and federated discovery of structured scientific data. Materials Data Curation System is a materials-oriented implementation. It is not a standalone dataset: deployment-specific access and data terms apply. The software carries the NIST Software Licensing Statement, with separate third-party terms. |
| [CAMEO1.0 active-learning demonstration software](https://data.nist.gov/od/id/mds2-2480) | software and already-represented benchmark data | MATLAB autonomous-experiment simulation with Fe-Ga-Pd demonstration data. All four demonstration arrays are byte-for-byte identical to the existing REMI Fe-Ga-Pd corpus; do not add a second dataset/count. Bundled Graph Cut components have their own restrictive notices. |
| [NIST–NREL Zn–Sn–Ti–O interlaboratory reproducibility study](https://data.nist.gov/od/id/86CF87E90A931F6FE05324570681D1922065) | specialist study and partial data/code release | Strong cross-laboratory metrology case study with reported95% agreement intervals of0.1–0.2eV for band gap,24–29nm for thickness and0.08–0.37 orders of magnitude for sheet resistance. Current v1.0.7 archive includes cluster/XRD peak/three-spectrum CSVs and notebooks; full measurement extraction depends on hte.registry.nist.gov. HTEM/HTE source overlap and full-payload accessibility remain unresolved, so it is retained as a resource without an independent corpus count. |
| [IEEE CSC Superconductor Databases & Resources](https://ieeecsc.org/learning-hub/superconductor-databases-resources) | subject-resource directory | Navigation directory linking the CSC wiki, UCI, NIST reference sources, OSD, existing MP/NIMS resources, Robinson wire data and CERN materials models. Its thirteen scientific routes are not thirteen independent datasets. |
| [JARVIS-Tools Notebooks](https://github.com/JARVIS-Materials-Design/jarvis-tools-notebooks) | tools and notebook collection | Archived tutorial repository for electronic structure, force fields, AI and experiments; directs continued development to atomgptlab/jarvis-tools-notebooks. Inventoried README links are navigation resources, not extra dataset counts. |
| [SMAX Maximum Entropy Dataset](https://arxiv.org/abs/2602.23489) | unreleased training dataset | Chemistry-agnostic maximum-entropy configurations for robust interatomic potentials under extreme thermodynamic conditions, augmented with relaxed structures and lower-energy environments. Used to train the GRACE SMAX models. Unreleased training corpus; public models are separate. The paper (https://arxiv.org/html/2602.23489v1) reports 1,660,322 training and 33,064 test configurations, totaling 1,693,386 structures. As checked on 2026-09-13, the paper's data-availability statement promises the dataset on manuscript acceptance. Pretrained SMAX models (https://gracemaker.readthedocs.io/en/latest/gracemaker/foundation/#smax-models) are listed separately; their availability does not establish a public dataset release. |
| [MatterGen MP-20 reprocessed release](https://github.com/microsoft/mattergen/tree/main/data-release/mp-20) | versioned benchmark derivative | PBE-recomputed and element-filtered MP-20 derivative with its own distributed files; keep separate provenance from CDVAE MP-20. Exact file-row count was not verified, so not added as an independently sized dataset. |

## Evidence

### A Materials Properties Dataset for Elastomeric Foam Impact Mitigating Materials

- [A Materials Properties Dataset for Elastomeric Foam Impact Mitigating Materials — Data.gov primary-agency metadata](https://catalog.data.gov/dataset/a-materials-properties-dataset-for-elastomeric-foam-impact-mitigating-materials) (2026-11-01): Data descriptor DOI10.1038/s41597-023-02092-4; catalog advertises212 resources including payload/hash pairs, not212 independent materials.
- [Downloaded foam specimen/test notes](https://data.nist.gov/od/ds/ark:/88434/mds2-2606/DMA_data/VN01/VN01_notes_DMA_data.txt) (2026-11-01): Defines geometry with standard deviations, test60°C to−30°C and0.3–30rad/s, and measurement uncertainty; SHA-256 verified.
- [DMA data framework](https://data.nist.gov/od/ds/ark:/88434/mds2-2606/DMA_data/data_framework_DMA.txt) (2026-11-01): Documents native instrument files, XLS metadata tab, frequency/temperature tabs and material/batch/specimen naming.

### ACerS-NIST Phase Equilibria Diagrams Database (SRD 31)

- [SRD31 current product and release](https://www.nist.gov/srd/nist-standard-reference-database-31) (2026-11-01): Current NIST page documents v6.0 (2025), 34,000 diagrams, expert critical evaluations and paid products.

### AFLOW AEL/AGL thermomechanical property libraries

- [Official AFLOW REST/AFLUX documentation](https://aflow.org/documentation/) (2026-11-01): Documents AEL elastic and AGL thermal keys; states data free for scientific, academic and non-commercial purposes.

### Aged and unaged flexible unidirectional composite laminate tensile testing for soft body armor applications

- [Aged and unaged flexible unidirectional composite laminate tensile testing for soft body armor applications — Data.gov primary-agency metadata](https://catalog.data.gov/dataset/aged-and-unaged-flexible-unidirectional-composite-laminate-tensile-testing-for-soft-body-a) (2026-11-01): Catalog describes accelerated70°C aging up to150days and3crosshead rates/3gauge lengths.
- [Downloaded UD tensile README](https://data.nist.gov/od/ds/8B3BFE0480BD4943E053245706812C692078/UD_tensile_strip_readme.txt) (2026-11-01): Documents folder codes,raw CSV and multiple-format specimen summaries, test conditions and method DOI10.3791/58991.

### Aged and unaged PBIA-based copolymer testing for soft body armor applications

- [Aged and unaged PBIA-based copolymer testing for soft body armor applications — Data.gov primary-agency metadata](https://catalog.data.gov/dataset/aged-and-unaged-pbia-based-copolymer-testing-for-soft-body-armor-applications) (2026-11-01): Primary agency catalog links tensile/FTIR/moisture ZIPs and SHA-256 files.
- [Downloaded PBIA README](https://data.nist.gov/od/ds/mds2-2123/copolymer_PPTA_readme.txt) (2026-11-01): Defines four aging conditions, file schemas and mechanical-test methods; no additional restrictions stated.

### ANI-1x Active-Learning Molecular Dataset

- [Matbench Discovery dataset listing](https://matbench-discovery.materialsproject.org/data/sets) (2026-11-01): ANI-1x: reported5,000,000 configurations/geometries; access public; declared license CC0-1.0. This is a discovery resource, not a new periodic crystal count.
- [Pinned Matbench Discovery dataset metadata](https://github.com/janosh/matbench-discovery/blob/8869a883a5067015b815886d878bd7aaa3862d2d/data/datasets.yml) (2026-11-01): Preserves release-specific counts, primary download routes and caveats; no large payload audited.

### Archived Wikipedia List of Superconductors (IEEE-linked PDF)

- [IEEE CSC linked reference list](https://ieeecsc.org/learning-hub/superconductor-databases-resources) (2026-11-01): Directory explicitly links the archived Wikipedia superconductors list PDF.

### Awesome Materials & Chemistry Datasets

- [Awesome Materials & Chemistry Datasets](https://github.com/blaiszik/awesome-matchem-datasets) (2026-11-01): README groups structural, property, synthesis and other chemistry/materials datasets with links.

### Battery Archive

- [Battery Archive provider home](https://batteryarchive.org/) (2026-11-01): Offers cycling/disruptive-test visualization; complete cell CSVs available by contacting the provider.

### Broadband Electromagnetic Properties of Engineered Flexible Absorber Materials

- [Broadband Electromagnetic Properties of Engineered Flexible Absorber Materials — Data.gov primary-agency metadata](https://catalog.data.gov/dataset/broadband-electromagnetic-properties-of-engineered-flexible-absorber-materials) (2026-11-01): CSV files distinguish calculated/extracted permittivity/permeability and distributed circuit parameters.
- [Downloaded versioned absorber README](https://data.nist.gov/od/ds/mds2-2911/README.txt) (2026-11-01): Lists figure/file scope,30%/60% weight loading, mTRL/series-resistor calibration and model-based extraction.
- [Downloaded effective-permittivity CSV](https://data.nist.gov/od/ds/mds2-2911/Figure%207a.csv) (2026-11-01): Public structured numeric payload inspected; figure-derived effective values, not an independent crystal census.

### CAMEO1.0 active-learning demonstration software

- [NIST CAMEO release](https://data.nist.gov/od/id/mds2-2480) (2026-11-01): Downloaded archive includes FeGaPd_CMP,DFT_regions,Mag,XRD; each byte hash matches existing REMI nist-pages source. Current metadata version1.0.1.

### Catalysis-Hub / CatHub

- [Catalysis-Hub primary data descriptor](https://pmc.ncbi.nlm.nih.gov/articles/PMC6538711/) (2026-11-01): 2019 descriptor documents linked geometries, calculation settings, reaction and activation energies; contributing studies have different scopes.

### CatApp

- [CatApp official CMR page](https://cmr.fysik.dtu.dk/catapp/catapp.html) (2026-11-01): Provides calculated reaction and activation energies on metal surfaces with the 2012 publication reference.
- [Catalysis-Hub primary descriptor discussion of CatApp](https://pmc.ncbi.nlm.nih.gov/articles/PMC6538711/) (2026-11-01): Explains that CatApp covers more than 3,000 reactions but lacks atomic structures and detailed calculation output.

### CERN STEAM Materials Library (SMaLi)

- [CERN STEAM Materials documentation](https://steam.docs.cern.ch/libraries/materials/) (2026-11-01): Identifies material-property C code, wrappers, documentation and the CERN GitLab source repository.
- [SMaLi reference documentation](https://steam-material-library.docs.cern.ch/) (2026-11-01): Documents superconducting critical current and HTS/LTS critical-current-density function families.

### ColabFit Exchange

- [ColabFit Exchange](https://materials.colabfit.org/) (2026-11-01): Searchable atomistic datasets and standardized configurations; tracks separate property and configuration identifiers, including mixed molecular and periodic domains.

### Computational Materials Repository (CMR)

- [CMR official portal](https://cmr.fysik.dtu.dk/) (2026-11-01): Defines each project as an ASE database with a project page and browse/download access; links an OPTIMADE endpoint and states all CMR databases are CC BY-SA 4.0.
- [2DHub official portal](https://2dhub.org/) (2026-11-01): Current home for C2DB and related 2D databases, links back to CMR; these named datasets are already separate catalog records.

### Configurable Data Curation System (CDCS / MDCS)

- [NIST — About CDCS](https://www.nist.gov/itl/ai/applied-ai-research-group/configurable-data-curation-system-cdcs/about-cdcs) (2026-11-01): Describes XML-schema-driven data capture, curation and transformation, document storage and federation across curation instances; the user-supplied older organizational path resolves here.
- [NIST — Materials Data Curation System source repository](https://github.com/usnistgov/MDCS) (2026-11-01): Provides the materials implementation and describes schema-generated forms, REST retrieval, document storage and federated search.
- [MDCS — NIST Software Licensing Statement](https://github.com/usnistgov/MDCS/blob/develop/LICENSE.md) (2026-11-01): Permits use, modification and distribution subject to retaining the notice, marking changes and acknowledging NIST; third-party components have separate terms.

### Data for A Dual Mode Brillouin/Low-Frequency Raman Spectroscopy Microscope for Local Mechanical Property Imaging for Semiconductor Packaging Materials

- [Data for A Dual Mode Brillouin/Low-Frequency Raman Spectroscopy Microscope for Local Mechanical Property Imaging for Semiconductor Packaging Materials — Data.gov primary-agency metadata](https://catalog.data.gov/dataset/data-for-a-dual-mode-brillouin-low-frequency-raman-spectroscopy-microscope-for-local-mecha-99ad6) (2026-11-01): Dataset accompanies IEEE ECTC2025 DOI10.1109/ECTC51687.2025.00288.
- [Downloaded BLS/LFR3725 README](https://data.nist.gov/od/ds/mds2-3725/ReadMe_20260427.txt) (2026-11-01): Specifies calibration, room conditions,GHz/cm−1/min/°C axes, masks and fit components.
- [Downloaded Raman spectrum](https://data.nist.gov/od/ds/ark:/88434/mds2-3725/Fig2/Fig2_data.txt) (2026-11-01): Experimental and fitted component columns are separately supplied in a public text payload.

### Data for A Switchable Longitudinal & Shear BLS Microscope for Comprehensive Modulus Imaging of Semiconductor Packaging Materials

- [Data for A Switchable Longitudinal & Shear BLS Microscope for Comprehensive Modulus Imaging of Semiconductor Packaging Materials — Data.gov primary-agency metadata](https://catalog.data.gov/dataset/data-for-a-switchable-longitudinal-shear-bls-microscope-for-comprehensive-modulus-imaging--c473d) (2026-11-01): Two epoxy sample designs; public payload/hash pairs and CADRE access route.
- [Downloaded BLS4059 README](https://data.nist.gov/od/ds/ark:/88434/mds2-4059/4059_ReadMe_20260421.txt) (2026-11-01): Defines raw/fit data, calibration, cure schedules, missing-value masks, assumed density1.20g/cm³/index1.55 and interpolation/filtering; provider SHA-256 matches.
- [Downloaded BLS Young modulus map](https://data.nist.gov/od/ds/ark:/88434/mds2-4059/Fig4/Fig4d_Youngs_modulus.txt) (2026-11-01): Structured map with index coordinates and Young modulus inGPa inspected.

### Data for Advanced Metrology Suite for Linking Residual Stress to Fundamental Properties of Thermoset Packaging Materials

- [Data for Advanced Metrology Suite for Linking Residual Stress to Fundamental Properties of Thermoset Packaging Materials — Data.gov primary-agency metadata](https://catalog.data.gov/dataset/data-for-advanced-metrology-suite-for-linking-residual-stress-to-fundamentalproperties-of--43ee8) (2026-11-01): Primary catalog lists raw/processed/notes andCADRE project navigation; full numerical-quality assessment is outside this check.

### Data of High-Temperature Dynamic LCM Testing Setup

- [Data of High-Temperature Dynamic LCM Testing Setup — Data.gov primary-agency metadata](https://catalog.data.gov/dataset/data-of-high-temperature-dynamic-lcm-testing-setup) (2026-11-01): DOI10.15121/1986090; tests at120/300°F are described, with a temperature metadata conflict.
- [Downloaded LCM water-control workbook](https://gdr.openei.org/files/1449/HT%20Dyn%20LCM%20Water_1000m_120F.xlsx) (2026-11-01): Workbook independently opened; sheet records2019-09-26,120°F and named pressure/filtrate/time channels.

### Data Resources for Materials Science

- [Data Resources for Materials Science](https://github.com/sedaoturak/data-resources-for-materials-science) (2026-11-01): Inspected the complete README source and extracted public links by section; adjacent and uncertain links remain labeled in the inventory.

### Digital Catalysis Platform (DigCat)

- [DigCat provider laboratory page](https://www.li-lab-cat-design.com/code--database.html) (2026-11-01): Provider reports >0.4 million experimental data and >0.4 million computational data and identifies the current platform/publication.
- [DigCat 2024 author preprint](https://www.cambridge.org/engage/chemrxiv/article-details/6760cd4381d2151a02fb5356) (2026-11-01): Reports >400,000 experimental performance records and >300,000 structures; denominator and release differ from later claims.

### Digital Hydrogen-S

- [Crossref publisher-deposited Digital Hydrogen-S metadata](https://api.crossref.org/works/10.1016/j.ijhydene.2026.153434) (2026-11-01): Confirms author paper title, DOI and Elsevier PII S0360319926000716; does not verify database counts.

### EAF Slag Characterization

- [EAF Slag Characterization — Data.gov primary-agency metadata](https://catalog.data.gov/dataset/eaf-slag-characterization) (2026-11-01): Live9,662,778-byte ZIP inspected;3workbooks and35constituent sheets in the single-batch workbook.
- [Downloaded EAF workbook ZIP](https://pasteur.epa.gov/uploads/10.23719/1531971/OneDrive_1_1-31-2025%20%281%29.zip) (2026-11-01): All3XLSX opened; Scenario and Granular-Al tables carry units,test IDs,detection limits and substitution statements.
- [EPA data license](https://pasteur.epa.gov/license/sciencehub-license.html) (2026-11-01): EPA-produced data default to U.S.public domain unless otherwise specified; associated metadata limitations apply.

### GDR low-temperature geothermal thermoelectric material measurements

- [GDR692 primary release](https://gdr.openei.org/submissions/692) (2026-11-01): Three public files with Southern Research Institute/Novus provenance, DOE project EE0006746 and CC BY 4.0.
- [Released material workbook](https://gdr.openei.org/files/692/SR%20Thermoelectric%20Materials.xlsx) (2026-11-01): Independently counted 19 specimen IDs across two tables: 6 p-type BiSbTe and 13 n-type BiSeTe rows; units are embedded in headers.
- [Released methods document](https://gdr.openei.org/files/692/SR%20Thermoelectric%20Materials.docx) (2026-11-01): Describes mechanical alloying/hot pressing, rectangular cut bars and ULVAC ZEM-3 resistivity/Seebeck testing; discusses precursor oxygen contamination.

### IEEE CSC Superconductor Databases & Resources

- [IEEE CSC resource directory](https://ieeecsc.org/learning-hub/superconductor-databases-resources) (2026-11-01): Lists thirteen scientific resource routes, including two routes to WebHTS/SRD 62 and historical reference books/tables.
- [IEEE-listed route: CSC Wiki](https://wiki.ieeecsc.org/) (2026-11-01): Scientific route listed by the IEEE CSC directory; retained with its original role as a discovery or reference link. Listing alone does not independently validate this destination or establish a new dataset.
- [IEEE-listed route: Archived Wikipedia list](https://webdisk.science.upjs.sk/~martin_gmitra/Theory%20of%20Condensed%20Matter/Supporting%20Materials/11/List_of_superconductors_wikipedia.pdf) (2026-11-01): Scientific route listed by the IEEE CSC directory; retained with its original role as a discovery or reference link. Listing alone does not independently validate this destination or establish a new dataset.
- [IEEE-listed route: UCI Superconductivty Data](https://archive.ics.uci.edu/dataset/464/superconductivty+data) (2026-11-01): Scientific route listed by the IEEE CSC directory; retained with its original role as a discovery or reference link. Listing alone does not independently validate this destination or establish a new dataset.
- [IEEE-listed route: NIST SRD 62 metadata](https://data.nist.gov/od/id/ECBCC1C130112ED9E04306570681B10723) (2026-11-01): Scientific route listed by the IEEE CSC directory; retained with its original role as a discovery or reference link. Listing alone does not independently validate this destination or establish a new dataset.
- [IEEE-listed route: NIST legacy WebHTS portal](https://srdata.nist.gov/CeramicDataPortal/hit) (2026-11-01): Scientific route listed by the IEEE CSC directory; retained with its original role as a discovery or reference link. Listing alone does not independently validate this destination or establish a new dataset.
- [IEEE-listed route: Roberts survey](https://srd.nist.gov/jpcrdreprint/1.555540.pdf) (2026-11-01): Scientific route listed by the IEEE CSC directory; retained with its original role as a discovery or reference link. Listing alone does not independently validate this destination or establish a new dataset.
- [IEEE-listed route: Roberts 1978 supplement](https://books.google.com/books?id=bbHgTVWyFlkC) (2026-11-01): Scientific route listed by the IEEE CSC directory; retained with its original role as a discovery or reference link. Listing alone does not independently validate this destination or establish a new dataset.
- [IEEE-listed route: Clark OSD](http://osd.clarku.edu/public/about) (2026-11-01): Scientific route listed by the IEEE CSC directory; retained with its original role as a discovery or reference link. Listing alone does not independently validate this destination or establish a new dataset.
- [IEEE-listed route: Materials Project](https://next-gen.materialsproject.org) (2026-11-01): Scientific route listed by the IEEE CSC directory; retained with its original role as a discovery or reference link. Listing alone does not independently validate this destination or establish a new dataset.
- [IEEE-listed route: NIMS MatNavi](https://mits.nims.go.jp) (2026-11-01): Scientific route listed by the IEEE CSC directory; retained with its original role as a discovery or reference link. Listing alone does not independently validate this destination or establish a new dataset.
- [IEEE-listed route: MDR SuperCon Datasheet](https://mdr.nims.go.jp/collections/4c428a0c-d209-4990-ad1f-656d05d1cfe2) (2026-11-01): Scientific route listed by the IEEE CSC directory; retained with its original role as a discovery or reference link. Listing alone does not independently validate this destination or establish a new dataset.
- [IEEE-listed route: Robinson critical-current data](https://htsdb.wimbush.eu/about) (2026-11-01): Scientific route listed by the IEEE CSC directory; retained with its original role as a discovery or reference link. Listing alone does not independently validate this destination or establish a new dataset.
- [IEEE-listed route: CERN materials](https://steam.docs.cern.ch/libraries/materials/) (2026-11-01): Scientific route listed by the IEEE CSC directory; retained with its original role as a discovery or reference link. Listing alone does not independently validate this destination or establish a new dataset.

### IEEE CSC Superconductor Properties Wiki

- [IEEE CSC wiki description](https://ieeecsc.org/learning-hub/superconductor-databases-resources) (2026-11-01): Describes community property entries and explicitly limits its assurance to publication in peer-reviewed sources.

### JARVIS Figshare curated datasets

- [JARVIS Figshare curated datasets official documentation](https://jarvis.nist.gov/) (2026-11-01): Named datasets, historical snapshots and third-party mirrors distributed through jarvis-tools; all table entries are inventoried with their download routes.

### JARVIS Universal Search

- [JARVIS Universal Search official documentation](https://jarvis.nist.gov/) (2026-11-01): Search layer across JARVIS databases; it does not contribute a new independent data count.

### JARVIS-ChemNLP

- [JARVIS-ChemNLP official documentation](https://jarvis.nist.gov/) (2026-11-01): Chemical-formula search over open-access papers; a text discovery service, not another crystal-structure corpus.

### JARVIS-DFT2

- [JARVIS-DFT2 official documentation](https://jarvis.nist.gov/) (2026-11-01): Second JARVIS-DFT portal listed with the same broad DFT description; linked to the existing DFT family without adding a duplicate 80,000+ count.

### JARVIS-DMFT

- [JARVIS-DMFT official documentation](https://jarvis.nist.gov/) (2026-11-01): Dynamical mean-field theory portal listed by JARVIS. Current count, public machine payload and dataset license were not established; access redirects to login.

### JARVIS-Leaderboard

- [JARVIS-Leaderboard official documentation](https://jarvis.nist.gov/) (2026-11-01): Reproducible methods and datasets spanning theory and experiments; benchmark data points overlap underlying source datasets.

### JARVIS-OPTIMADE

- [JARVIS-OPTIMADE official documentation](https://jarvis.nist.gov/) (2026-11-01): Standardized JARVIS-DFT structure queries. API reachability and authentication are recorded separately in the API source registry.

### JARVIS-Tools Notebooks

- [Requested notebook README](https://raw.githubusercontent.com/JARVIS-Materials-Design/jarvis-tools-notebooks/master/README.md) (2026-11-01): Lists subject-grouped materials design tutorials and its explicitly linked successor.

### LeMat-GenBench

- [LeMat-GenBench official README](https://raw.githubusercontent.com/LeMaterial/lemat-genbench/main/README.md) (2026-11-01): Defines benchmark families, LeMat-Bulk novelty reference, input formats and comprehensive_multi_mlip_hull configuration.

### LeMaterial Atompack

- [LeMaterial Atompack](https://huggingface.co/datasets/LeMaterial/Atompack) (2026-11-01): Public atomistic datasets repackaged for streaming in Atompack format. The card identifies upstream MatPES, MP-ALOE, MPtrj, OMat24 and OC20; do not count format mirrors as new datasets.

### Lost Circulation Materials in Geothermal Drilling: Thermal Degradation, Viscosity, Compression, and Flow Loop Tests

- [Lost Circulation Materials in Geothermal Drilling: Thermal Degradation, Viscosity, Compression, and Flow Loop Tests — Data.gov primary-agency metadata](https://catalog.data.gov/dataset/lost-circulation-materials-in-geothermal-drilling-thermal-degradation-viscosity-compressio) (2026-11-01): DOI10.15121/2473672; methods papers and4experimental modalities.
- [Downloaded thermal-degradation workbook](https://gdr.openei.org/files/1660/DegradationTest_Information.xlsx) (2026-11-01): Seven sheet names and mass/temperature/time headers inspected; rows include replicates.

### Machine Learning Materials Datasets / MAST-ML education

- [Machine Learning Materials Datasets Figshare v5](https://api.figshare.com/v2/articles/7017254) (2026-11-01): Three educational datasets with property labels and descriptors; release is MIT licensed.
- [Attached dataset README](https://ndownloader.figshare.com/files/13008500) (2026-11-01): Explains normalized/raw diffusion energies, perovskite site/composition features and metallic-glass reduced transition temperature.

### Matbench Discovery data sets

- [Matbench Discovery dataset registry](https://raw.githubusercontent.com/janosh/matbench-discovery/main/data/datasets.yml) (2026-11-01): Registry describes WBM and numerous parent/training datasets; it is navigation/provenance context, not an additive dataset.

### Matbench v0.1 suite

- [Benchmarking Materials Property Prediction Methods](https://arxiv.org/abs/2005.00707) (2026-11-01): Thirteen tasks from ten experimental/DFT sources, 312 to 132k samples.

### Materials Cloud Archive

- [Materials Cloud Archive](https://archive.materialscloud.org/) (2026-11-01): Versioned dataset deposits with DOI records, files and, for selected datasets, AiiDA provenance graphs. Each deposit needs its own count and license.

### Materials Cloud OPTIMADE Client

- [Official OPTIMADE clients guide](https://www.optimade.org/clients) (2026-11-01): Browser interface to select an OPTIMADE provider and child database, filter structures and inspect/download results. A client for existing providers, not an independent crystal dataset.

### Materials Data Facility / Foundry

- [Materials Data Facility](https://www.materialsdatafacility.org/) (2026-11-01): Describes publication and discovery services and links Foundry. The non-www domain redirects here; both supplied routes returned the same final response body.
- [Foundry — official source repository](https://github.com/MLMI2-CSSI/foundry) (2026-11-01): Documents the Python client for searching, loading and obtaining schemas and citations for machine-learning-ready data, integrated with Materials Data Facility.
- [MDF publishing and discovery guides](https://connect.materialsdatafacility.org/how-to) (2026-11-01): Retained from the existing catalog record as its original guide route; this supplement independently verified the homepage and Foundry source repository.
- [MDF dataset search](https://www.materialsdatafacility.org/search) (2026-11-01): Dataset discovery UI uses the public MDF Globus Search index. Ten property queries returned 244 distinct public deposit subjects during this audit.

### MaterialsWeb

- [Hennig Materials Theory Lab resources](https://hennig.mse.ufl.edu/resources/) (2026-11-01): Provider lab explicitly links MaterialsWeb routes for 2D and bulk materials.
- [Topology-Scaling Identification of Layered Solids and Stable Exfoliated 2D Materials](https://arxiv.org/abs/1610.07673) (2026-11-01): Author paper identifies 826 monolayers and says optimized structures and related data were provided at MaterialsWeb; this is a historical paper cohort.
- [MaterialsWeb direct access check](https://www.materialsweb.org/) (2026-11-01): Requested HTTPS host could not be fetched by the web tool; independent standard urllib access reported a TLS unrecognized-name failure for www and bare host.

### matminer dataset collection

- [matminer dataset summary](https://hackingmaterials.lbl.gov/matminer/dataset_summary.html) (2026-11-01): Lists experimental and calculated datasets with descriptions and provenance.
- [matminer repository](https://github.com/hackingmaterials/matminer) (2026-11-01): Requests citation of original sources when using loaded datasets.

### MatterGen MP-20 reprocessed release

- [MatterGen MP-20 data-release README](https://raw.githubusercontent.com/microsoft/mattergen/main/data-release/mp-20/README.md) (2026-11-01): Describes CC BY 4.0 parent, excluded elements, PBE recomputation and hull filtering.

### MatterSim training data availability

- [MatterSim training data availability](https://github.com/microsoft/mattersim/blob/main/MODEL_CARD.md) (2026-11-01): Public model cards describe training data sizes and released checkpoints. This survey did not verify a complete public training-data download, so checkpoint sizes are not ranked as datasets.

### MOFX-DB

- [MOFX-DB primary descriptor](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=931567) (2026-11-01): Describes computational adsorption datasets across multiple source families and thermodynamic conditions.

### nanoHUB Machine Learning Lab Module

- [Public module page](https://nanohub.org/tools/intromllab) (2026-11-01): Public activity description identifies version1.7 and states login is required to run.
- [Tool license page](https://nanohub.org/resources/license?tool=intromllab_r36&tmpl=component) (2026-11-01): Program is GPL version3-or-later.

### Near Infrared Spectra of Origin-defined and Real-world Textiles (NIR-SORT): A spectroscopic and materials characterization dataset for known provenance and post-consumer fabrics

- [Near Infrared Spectra of Origin-defined and Real-world Textiles (NIR-SORT): A spectroscopic and materials characterization dataset for known provenance and post-consumer fabrics — Data.gov primary-agency metadata](https://catalog.data.gov/dataset/near-infrared-spectra-of-origin-defined-and-real-world-textiles-nir-sort-a-spectroscopic-a) (2026-11-01): Catalog cites Scientific Data DOI10.1038/s41597-026-07434-6 and mirror10.18126/61v0-rf98.
- [Downloaded NIR data dictionary](https://data.nist.gov/od/ds/ark:/88434/mds2-3325/DataDictionary.csv) (2026-11-01): Defines spectral units,nulls,uncertainty and environment fields; explicitly qualifies consumer label provenance.
- [Downloaded root fabric metadata](https://data.nist.gov/od/ds/ark:/88434/mds2-3325/SampleInformation.csv) (2026-11-01): Independently counted64rows and64unique Sample ID strings, differing from113fabric catalog scope.
- [Downloaded NIR-SORT license](https://data.nist.gov/od/ds/ark:/88434/mds2-3325/license.txt) (2026-11-01): NIST data terms permit worldwide royalty-free reuse with acknowledgment and modified-data notices; separate code terms.

### NIMS MatDaCs

- [NIMS MatDaCs: COD](https://mat-dacs.dxmt.nims.go.jp/en/list/350) (2026-11-01): Provider catalogue entry gives COD description and official link.
- [NIMS MatDaCs: AtomWork-Adv](https://mat-dacs.dxmt.nims.go.jp/en/list/316) (2026-11-01): Provider catalogue entry supplies database scope and access notes.

### NIMS MatNavi

- [NIMS MatNavi](https://mits.nims.go.jp/en/) (2026-11-01): Describes component databases, registration and prohibition of mass data acquisition.

### NIST 62 / NIST–NRIM superconductors Version 2.0 publication

- [NIST 62. NIST/NRIM High Temperature Superconductors Database: Version 2.0](https://www.nist.gov/publications/nist-62-nistnrim-high-temperature-superconductors-database-version-20) (2026-11-01): Primary NIST publication metadata identifies R. G. Munro, 2008-10-16, evaluated properties and 1987–1996 source literature; it supplies no entry count or distinct downloadable dataset.
- [NIST High Temperature Superconducting Materials Database search portal](https://srdata.nist.gov/CeramicDataPortal/hit) (2026-11-01): Same portal explicitly calls itself WebHTS and NIST Standard Reference Database 62, cites DOI 10.18434/T4KP8J and states last data-content update 1996.
- [NIST WebHTS Version 2.0 publication (1999)](https://www.nist.gov/publications/nist-www-high-temperature-superconducting-materials-database-webhts-version-20) (2026-11-01): Begley and Munro’s 1999 page describes the same evaluated oxide-superconductor property families; separate publication dates do not establish independent dataset releases.

### NIST Interatomic Potentials Repository

- [Attached Data.gov NIST IPR entry](https://catalog.data.gov/dataset/nist-interatomic-potentials-repository) (2026-11-01): Ranks 204/206 identify a force-field/model and evaluation repository, not a new equilibrium crystal collection.
- [NIST IPR primary provider](https://www.ctcms.nist.gov/potentials/) (2026-11-01): Provides model files, references and property-evaluation tools; warns that applicability varies by composition/domain and includes intentionally fictional potentials.

### NIST Materials Data Repository

- [NIST Materials Data Repository](https://materialsdata.nist.gov/) (2026-11-01): Public searchable materials repository; individual providers define data-use terms and review status varies.

### NIST MGI Materials Data Resources

- [NIST — Materials Data Resources](https://www.nist.gov/mgi/materials-data-resources) (2026-11-01): Lists general repositories and registries, schemas, phase-based resources and an interatomic-potential repository, with separate descriptions and destinations.
- [NIST Materials Resource Registry route](https://materials.registry.nist.gov/) (2026-11-01): The published registry endpoint resolved to https://www.nist.gov/mgi during this audit; this redirect does not establish formal end of service.

### NIST Property Data Summaries for Advanced Materials (SRD 150)

- [SRD150 sintered-alumina example](https://srdata.nist.gov/CeramicDataPortal/Pds/Scdaos) (2026-11-01): Validated summary gives material scope, property values by temperature, combined standard uncertainty notation and SRD30/literature references.
- [SRD150 scope and access](https://srdata.nist.gov/CeramicDataPortal/pds) (2026-11-01): Provides public reference summaries and links topical collections; evaluation levels vary across typical, evaluated and validated data.

### NIST–NREL Zn–Sn–Ti–O interlaboratory reproducibility study

- [NIST current primary release](https://data.nist.gov/od/id/86CF87E90A931F6FE05324570681D1922065) (2026-11-01): Old round-robin-data-update.zip returns404; current metadata links a verified8,753,821byte NIST-NREL-Interlaboratory-Figures-master.zip. Notebooks fetch primary records from the HTE registry; included CSVs cover selected analyses.
- [Primary interlaboratory paper](https://doi.org/10.1021/acscombsci.8b00158) (2026-11-01): Explicitly compares two laboratories and different measurement modalities, reporting type-dependent agreement and systematic differences.

### NOMAD Repository and Archive

- [NOMAD Repository and Archive](https://cloud.nomad-lab.eu/nomad-lab/) (2026-11-01): Code-agnostic raw and normalized computational and experimental archives. Provider snapshot reports 19,425,275 entries and 4,346,100 represented materials; these heterogeneous counters are not a count of unique bulk crystals.

### Open Molecules 2025

- [Matbench Discovery dataset listing](https://matbench-discovery.materialsproject.org/data/sets) (2026-11-01): OMol25: reported101,666,280 configurations/geometries; access public; declared license CC-BY-4.0. This is a discovery resource, not a new periodic crystal count.
- [Pinned Matbench Discovery dataset metadata](https://github.com/janosh/matbench-discovery/blob/8869a883a5067015b815886d878bd7aaa3862d2d/data/datasets.yml) (2026-11-01): Preserves release-specific counts, primary download routes and caveats; no large payload audited.

### Open Molecules 2025 Electronic-Structure Subset

- [Matbench Discovery dataset listing](https://matbench-discovery.materialsproject.org/data/sets) (2026-11-01): OMol25 Electronic: reported4,000,000 configurations/geometries; access public; declared license CC-BY-4.0. This is a discovery resource, not a new periodic crystal count.
- [Pinned Matbench Discovery dataset metadata](https://github.com/janosh/matbench-discovery/blob/8869a883a5067015b815886d878bd7aaa3862d2d/data/datasets.yml) (2026-11-01): Preserves release-specific counts, primary download routes and caveats; no large payload audited.

### Open Polymers 2026

- [Matbench Discovery dataset listing](https://matbench-discovery.materialsproject.org/data/sets) (2026-11-01): OPoly26: reported6,570,542 configurations/geometries; access public; declared license CC-BY-4.0. This is a discovery resource, not a new periodic crystal count.
- [Pinned Matbench Discovery dataset metadata](https://github.com/janosh/matbench-discovery/blob/8869a883a5067015b815886d878bd7aaa3862d2d/data/datasets.yml) (2026-11-01): Preserves release-specific counts, primary download routes and caveats; no large payload audited.

### OpenAlex specialized-property discovery

- [OpenAlex scholarly discovery](https://openalex.org/) (2026-11-01): Automatically retrieved scholarly metadata for the property-focused search; primary releases verify material data.

### OpenKIM

- [OpenKIM — About](https://openkim.org/about/) (2026-11-01): Describes the curated interatomic-potential archive, versioning and DOIs, KIM API, verification checks, and Crystal Genome property predictions using archived potentials.
- [OpenKIM Query API](https://query.openkim.org/) (2026-11-01): Documents public queries over model, test and associated result records; these are different record types rather than a unique-crystal census.
- [OpenKIM — Obtaining Models](https://openkim.org/doc/usage/obtaining-models/) (2026-11-01): Provides public instructions for obtaining archived models, including package and source distribution routes.

### OPTIMADE

- [OPTIMADE](https://www.optimade.org/) (2026-11-01): Common API specification for querying structure providers; a federation/interface, not an additional independent dataset.

### OPTIMADE clients directory

- [Official OPTIMADE clients guide](https://www.optimade.org/clients) (2026-11-01): Official comparison of Materials Cloud OPTIMADE Client, optimade.science, optimade-python-tools and Swagger/OpenAPI interfaces; distinguishes individual-database and federated searches.

### OPTIMADE provider registry

- [OPTIMADE provider registry official documentation](https://providers.optimade.org/) (2026-11-01): Machine-readable index of provider index-metadatabases; follow each provider links endpoint to discover child database base URLs.

### Organic Materials Database (OMDB)

- [OMDB provider description](https://omdb.mathub.io/page/about) (2026-11-01): Describes an organic/organometallic electronic-structure database with DFT and advanced query tools.
- [OMDB named data releases](https://omdb.mathub.io/dataset/) (2026-11-01): Lists the 12,500-material OMDB-GAP1 and 260,092-material COD prediction releases as distinct products.
- [OMDB terms](https://omdb.mathub.io/page/terms) (2026-11-01): Terms mention access quotas but do not identify a general data reuse license.
- [OMDB public materials browser](https://omdb.mathub.io/material) (2026-11-01): Anonymous browser explicitly limits visible data and offers free registration; the page-local displayed totals are not adopted as a full-family count.

### PoLyInfo

- [NIMS — PoLyInfo](https://polymer.nims.go.jp/) (2026-11-01): Describes polymer property and sample information; states account/application conditions, restrictions on mass acquisition and scraping, permission requirements for redistribution, and a fee-based dataset service.

### Polymer Properties Database (PolymerDatabase.com)

- [PolymerDatabase.com — current endpoint availability](https://polymerdatabase.com/home.html) (2026-11-01): HTTP 200 response contained an iPage hosting-provider temporary-unavailability page; HTTP and HTTPS/root/www variants returned the same response body.

### Polymer Property Predictor and Database (PPPDB)

- [PPPDB — Polymer Property Predictor and Database](https://pppdb.uchicago.edu/) (2026-11-01): Links polymer property databases and phase-diagram, random-phase structure-factor and cloud-point prediction applications; the HTTP endpoint upgrades to HTTPS.
- [PPPDB — Flory–Huggins Interaction Parameter Database](https://pppdb.uchicago.edu/chi) (2026-11-01): The public table presents polymer-pair interaction parameters, temperatures and literature references.
- [PPPDB — Glass Transition Temperature Database](https://pppdb.uchicago.edu/tg) (2026-11-01): A public table of polymer glass-transition data was accessible during the audit.
- [PPPDB — Cloud Point Database](https://pppdb.uchicago.edu/cloud_points) (2026-11-01): A public cloud-point data table was accessible during the audit.

### Quantum Chemistry of 134 Thousand Small Organic Molecules

- [Matbench Discovery dataset listing](https://matbench-discovery.materialsproject.org/data/sets) (2026-11-01): QM9: reported133,885 configurations/geometries; access public; declared license CC0-1.0. This is a discovery resource, not a new periodic crystal count.
- [Pinned Matbench Discovery dataset metadata](https://github.com/janosh/matbench-discovery/blob/8869a883a5067015b815886d878bd7aaa3862d2d/data/datasets.yml) (2026-11-01): Preserves release-specific counts, primary download routes and caveats; no large payload audited.

### REMI: REsource for Materials Informatics

- [Primary resource CSV](https://raw.githubusercontent.com/usnistgov/remi/nist-pages/_data/resources.csv) (2026-11-01): Homepage table lists instructional notebook resources and tags.
- [Open Access Data list](https://raw.githubusercontent.com/usnistgov/remi/nist-pages/data/index.md) (2026-11-01): Links experimental Fe–Co–Ni/Fe–Ga–Pd composition-spread data and major material databases.

### Revised Molecular Dynamics 17

- [Matbench Discovery dataset listing](https://matbench-discovery.materialsproject.org/data/sets) (2026-11-01): rMD17: reported999,988 configurations/geometries; access public; declared license CC0-1.0. This is a discovery resource, not a new periodic crystal count.
- [Pinned Matbench Discovery dataset metadata](https://github.com/janosh/matbench-discovery/blob/8869a883a5067015b815886d878bd7aaa3862d2d/data/datasets.yml) (2026-11-01): Preserves release-specific counts, primary download routes and caveats; no large payload audited.

### Roberts Properties of Selected Superconductive Materials, 1978 Supplement

- [NIST Technical Note 983 publication record](https://www.nist.gov/publications/properties-selected-superconductive-materials-1978-supplement) (2026-11-01): Official record confirms Roberts, 1978, title and DOI 10.6028/NBS.TN.983.

### Roberts superconductive-materials survey (1976; literature through March 1975)

- [Survey of superconductive materials and critical evaluation of selected properties](https://srd.nist.gov/jpcrdreprint/1.555540.pdf) (2026-11-01): Title/abstract identifies the 1976 publication, March 1975 literature cutoff and property tables.

### Sandia Technical Reference for Hydrogen Compatibility of Materials

- [Sandia reference collection](https://www.sandia.gov/matlstechref/) (2026-11-01): Primary page links archival report and dated alloy/polymer chapters; scientific scope is hydrogen-affected strength, fracture and fatigue.
- [Complementary database current access](https://www.sandia.gov/matlstechref/hydrogen-materials-technical-database/) (2026-11-01): States database is under construction and a new Granta MI link will be available Fall 2026; no current structured download verified.

### Scientific Data materials Data Descriptors

- [Scientific Data collections](https://www.nature.com/sdata/collections?page=3&type=collection) (2026-11-01): Lists a collection on characterisation/performance data of energy materials.
- [Scientific Data data policies](https://www.nature.com/sdata/policies/data-policies) (2026-11-01): Requires repository deposits; journal does not itself host datasets.
- [Scientific Data journal-index metadata harvest](https://api.crossref.org/journals/2052-4463/works) (2026-11-01): Complete cursor pagination through the 2026-11-01 publication cutoff returned 9,304 distinct indexed works; a broad title screen flagged 1,514 candidates, not all verified materials datasets. Receipts retained locally.

### SCLib / JZIS superconducting-transition records

- [SCLib public materials snapshot](https://jzis.org/materials) (2026-11-01): 2026-10-31 version 98b37554e5a6 reports 13,282 results, 7,556 material entries counted separately per paper and 6,122 papers; model-review limitations are explicit.
- [SCLib data license](https://raw.githubusercontent.com/JackZH26/SCLib_JZIS/main/LICENSE-DATA) (2026-11-01): Project-created data CC BY 4.0; original upstream terms remain in force.
- [SCLib provenance and upstream-license notes](https://raw.githubusercontent.com/JackZH26/SCLib_JZIS/main/DATA_SOURCES.md) (2026-11-01): Documents arXiv/NIMS/MP provenance routes and per-record upstream-license handling; provider statements require source-specific assessment.

### SevenNet-Omni domain bridging set

- [SevenNet-Omni domain bridging set](https://doi.org/10.6084/m9.figshare.30399814) (2026-11-01): Primary paper makes the bridging DFT data available through this deposit. Distinguish recomputed bridging structures from the 15 overlapping source datasets and their mixed-domain frame total.
- [Optimizing cross-domain transfer for universal machine learning interatomic potentials](https://www.nature.com/articles/s41467-026-70195-8) (2026-11-01): Data availability links the DBS database, in-house DFT results and selected benchmarks to Figshare 30399814.

### Small-Molecule/Protein Interaction Chemical Energies 2

- [Matbench Discovery dataset listing](https://matbench-discovery.materialsproject.org/data/sets) (2026-11-01): SPICE 2: reported2,000,000 configurations/geometries; access public; declared license CC0-1.0. This is a discovery resource, not a new periodic crystal count.
- [Pinned Matbench Discovery dataset metadata](https://github.com/janosh/matbench-discovery/blob/8869a883a5067015b815886d878bd7aaa3862d2d/data/datasets.yml) (2026-11-01): Preserves release-specific counts, primary download routes and caveats; no large payload audited.

### SMAX Maximum Entropy Dataset

- [Matbench Discovery dataset listing](https://matbench-discovery.materialsproject.org/data/sets) (2026-11-01): SMAX: reported1,693,386 configurations/geometries; access unreleased; declared license unreleased. This is a discovery resource, not a new periodic crystal count.
- [Pinned Matbench Discovery dataset metadata](https://github.com/janosh/matbench-discovery/blob/8869a883a5067015b815886d878bd7aaa3862d2d/data/datasets.yml) (2026-11-01): Preserves release-specific counts, primary download routes and caveats; no large payload audited.

### SpringerMaterials

- [SpringerMaterials publisher overview](https://www.springernature.com/gp/librarians/products/databases-solutions/springermaterials) (2026-11-01): Curated properties, figures and graphs platform.

### Tran et al. review: Superconductor Discovery in the Emerging Paradigm of Materials Informatics

- [ACS published review](https://pubs.acs.org/cmatex/article/36/22/10939/154808/Superconductor-Discovery-in-the-Emerging-Paradigm) (2026-11-01): Publisher-indexed page verifies title, five authors, pages, online publication 8 November 2024 and CC BY 4.0. Direct publisher requests returned 403.
- [Crossref publisher-deposited review metadata](https://api.crossref.org/works/10.1021/acs.chemmater.4c01757) (2026-11-01): Confirms DOI, title, authors, 2024-11-08 publication and CC BY 4.0 version-of-record license.
- [Author-posted full review manuscript](https://arxiv.org/html/2510.25971v1) (2026-11-01): Full manuscript is accessible; arXiv posting dated 29 October 2025 identifies the 2024 journal article. Dataset table identifies CompSC and the Stanev subset as leads.
- [Author review figure data](https://github.com/huantd/matsdata/tree/main/papers/supercond_2024_01) (2026-11-01): Author README identifies three CSV files for Figures 1, 3 and 15; these are figure-supporting files rather than a newly independent superconductor corpus.

### UCSD Superconducting Research Database (Schuller group)

- [Schuller group: Foundation of New Superconducting Research Database](https://ischuller.ucsd.edu/timeline-post/foundation-of-new-superconducting-research-database/) (2026-11-01): Project-owning UCSD group identifies the SRD as a database of materials tested for superconductivity and invites researcher uploads to avoid redundant experiments.
- [Schuller Nanoscience Group news archive](https://ischuller.ucsd.edu/) (2026-11-01): Group news dates the database-foundation announcement to 13 March 2019.
- [UCSD Superconducting Research Database](https://srd.physics.ucsd.edu/) (2026-11-01): Search-indexed primary interface exposes Name, Structure and Transition filters; direct requests returned HTTP 500 or timed out on the verification date. No current count or public bulk payload was verified.

### WebFF

- [WebFF Documentation — Introduction](https://webff-documentation.readthedocs.io/en/latest/Introduction.html) (2026-11-01): Describes the force-field repository, organic/soft-material scope, XML provenance, exploration/download route and account-controlled curation route.
