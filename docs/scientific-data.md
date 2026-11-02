# Materials datasets in Scientific Data

[Back to MatVerse](../README.md) · [Journal](https://www.nature.com/sdata/) · [Search catalog additions](https://usccolumbia.github.io/matverse/?q=%22Scientific-Data-survey-20261101%22)

Checked 2026-11-02. This pass adds **90 dataset/release records**. The catalog now links **131 records to 128 distinct Scientific Data descriptors**. A descriptor can cover several releases or subsets; these are not independent material totals.

## Search scope and audit trail

The [Crossref journal endpoint](https://api.crossref.org/journals/2052-4463/works) was paginated to its reported total: **9,304 indexed records** for ISSN 2052-4463 through 2026-11-01. A broad, preserved title-keyword screen flagged **1,514 candidates**. Searches of publisher pages, linked references and dataset repositories supplemented that screen. Three independent topical passes covered structures/computation, physical properties/synthesis, and characterization/processing.

Complete API pagination means complete retrieval of this indexed response, not complete publisher indexing or full-text review of every article. Title matches include unrelated biomedical and environmental papers. Most candidates remain unreviewed discovery leads. Only primary-source-verified releases enter the ranked catalog. This is a broad journal search with a documented verification boundary, not an exhaustive census of all materials data published by Scientific Data.

[Full journal metadata](../research/sdata_20261101/journal_works.json) · [Title candidates](../research/sdata_20261101/journal_candidates.json) · [Query/page receipts and hashes](../research/sdata_20261101/journal_harvest_receipts.json) · [Reproducible harvest script](../research/sdata_20261101/harvest_journal.py) · [Source-entry dispositions](../research/collection_sdata_20261101.json) · [Descriptor-to-catalog index](../data/scientific_data_index.json) · [Frozen research brief](../research/sdata_20261101/BRIEF.md) · [Integration receipt](../research/sdata_20261101/integration_receipt.json)

The source-entry inventory retains every title candidate, its DOI and its review treatment, plus verified descriptor matches missed by title keywords. Existing catalog matches and verified new additions are distinguished from unresolved leads and corrections. Local research notes and compact repository receipts are retained in the three topical folders under [the audit directory](../research/sdata_20261101/README.md). Large retrieved article bodies and payloads remain in ignored local caches.

## What the collections enable

Crystal/DFT collections provide coordinates and calculated labels, but often share parent structures with Materials Project, COD, CoRE MOF or PhononDB. Property tables capture measurements or calculations under specific temperatures, processing histories, functionals or pressure ranges. Images, spectra, simulated diffraction patterns and atomistic trajectories add other observations of materials; they are not interchangeable with unique equilibrium crystals.

For training, split related structures, source papers, specimens and trajectories together where appropriate. Literature-extracted values can repeat observations from parent databases. Simulation grids over functionals or charge models expand label coverage without creating the same number of independent structures. Report the release, counted unit, conditions and lineage used for each experiment.

Dataset rights were checked separately from article rights. A CC BY article does not automatically license a linked archive. Missing rights or sizes remain explicit; unknown sizes are unranked. Selected small-file recounts and repository metadata inspections are documented in the cards. Full bulk transfers, numerical replication and comprehensive row-level quality audits were not performed.

## Verified catalog coverage

Sizes descend within each category; unknown sizes appear last. “New” identifies this search pass. Counts are not summed across units, parents, derivatives or releases.

### Computed bulk inorganic crystals

| Dataset / release | Reported volume | Structure level | Descriptor | Pass |
|---|---:|---|---|---|
| [PBEsol/SCAN 175k crystalline-material reference cohort](catalog/bulk_computed.md#pbesol-scan-175k-2022) | ~175,000 crystalline material records | `periodic_atomic` | [paper 1](https://doi.org/10.1038/s41597-022-01177-w) | New |
| [CAMD autonomous crystal discovery corpus](catalog/bulk_computed.md#camd-crystal-discoveries-2022) | 96,640 crystal structure records | `periodic_atomic` | [paper 1](https://doi.org/10.1038/s41597-022-01438-8) | New |
| [Theoretical multinary perovskite oxides](catalog/bulk_computed.md#multinary-perovskite-66516) | 66,516 optimized oxide entries | `periodic_atomic` | [paper 1](https://doi.org/10.1038/s41597-023-02127-w) | New |
| [MIP-3d materials informatics release](catalog/bulk_computed.md#mip3d-release) | 33,078 metadata/property records | `periodic_atomic` | [paper 1](https://doi.org/10.1038/s41597-021-01022-6) | New |
| [Layered intercalation crystal band structures](catalog/bulk_computed.md#layered-intercalation-bandstructures) | 9,024 intercalated crystal records | `periodic_atomic` | [paper 1](https://doi.org/10.1038/s41597-024-04008-2) | New |
| [Double-transition-metal MAX-phase precursors](catalog/bulk_computed.md#dtm-max-phases-8712) | 8,712 MAX-phase configuration records | `periodic_atomic` | [paper 1](https://doi.org/10.1038/s41597-023-02755-2) | New |
| [All-electron hybrid-functional materials database](catalog/bulk_computed.md#all-electron-hybrid-7024) | 7,024 inorganic material records | `periodic_atomic` | [paper 1](https://doi.org/10.1038/s41597-025-05867-z) | New |
| [Hybrid organic–inorganic perovskite DFT dataset](catalog/bulk_computed.md#hoip-2017) | 1,346 optimized hybrid-perovskite compounds | `periodic_atomic` | [paper 1](https://doi.org/10.1038/sdata.2017.57) | New |
| [HEX high-pressure elemental crystals](catalog/bulk_computed.md#hex-high-pressure-elements) | 228 element-pressure ground-state cases | `periodic_atomic` | [paper 1](https://doi.org/10.1038/s41597-024-03447-1) | New |

### Bulk and mixed-domain MLIP configurations

| Dataset / release | Reported volume | Structure level | Descriptor | Pass |
|---|---:|---|---|---|
| [Polyanion sodium cathode atomic structure and dynamics](catalog/mlip_configurations.md#polyanion-sodium-cathode-2025) | 298,144 periodic atomic configurations | `periodic_atomic` | [paper 1](https://doi.org/10.1038/s41597-025-05799-8) | Existing |
| [Massive Atomic Diversity](catalog/mlip_configurations.md#mad-original-2025) | 95,595 configurations | `mixed` | [paper 1](https://doi.org/10.1038/s41597-025-06109-y) | Existing |
| [Nb–Ta–V BCC solid-solution DFT configurations](catalog/mlip_configurations.md#nb-ta-v-bcc-dft) | 19,800 sampled starting alloy configurations | `periodic_atomic` | [paper 1](https://doi.org/10.1038/s41597-024-03720-3) | New |
| [Multiphase Ti and Ti-6Al-4V MLIP configurations](catalog/mlip_configurations.md#ti-ti64-multiphase) | 15,563 selected training configurations | `periodic_atomic` | [paper 1](https://doi.org/10.1038/s41597-025-05302-3) | New |
| [ElectroFace electrochemical interface trajectories](catalog/mlip_configurations.md#electroface-trajectories) | 71 trajectory archive packages | `periodic_atomic` | [paper 1](https://doi.org/10.1038/s41597-025-05338-5) | New |

### Two-dimensional and layered materials

| Dataset / release | Reported volume | Structure level | Descriptor | Pass |
|---|---:|---|---|---|
| [2DMatPedia](catalog/two_dimensional.md#2dmatpedia) | 6,351 monolayer structures | `periodic_atomic` | [paper 1](https://doi.org/10.1038/s41597-019-0097-3) | Existing |
| [BMDS bilayer electronic and transport dataset](catalog/two_dimensional.md#bmds-bilayers-760) | 760 bilayer materials | `structure_linked` | [paper 1](https://doi.org/10.1038/s41597-023-02146-7) | New |

### MOFs, COFs and zeolites

| Dataset / release | Reported volume | Structure level | Descriptor | Pass |
|---|---:|---|---|---|
| [Zeo-1](catalog/porous_frameworks.md#zeo-1) | 32,550 geometry-optimization frames | `periodic_atomic` | [paper 1](https://doi.org/10.1038/s41597-022-01160-5) | Existing |
| [TBHubbard MOF Hamiltonians](catalog/porous_frameworks.md#tbhubbard-mofs) | 10,000 MOF tight-binding cases | `periodic_atomic` | [paper 1](https://doi.org/10.1038/s41597-025-06054-w) | New |
| [AdsZeo equilibrium methane adsorption configurations](catalog/porous_frameworks.md#adszeo-equilibrium-configurations) | 4,775 zeolite framework realizations | `periodic_atomic` | [paper 1](https://doi.org/10.1038/s41597-026-08392-9) | New |
| [MOFSimplify stability-labelled MOFs](catalog/porous_frameworks.md#mofsimplify-stability) | 3,132 thermal-stability-labelled MOFs | `structure_linked` | [paper 1](https://doi.org/10.1038/s41597-022-01181-0) | New |
| [CRAFTED MOF adsorption isotherms](catalog/porous_frameworks.md#crafted-mof-isotherms) | 690 parent MOF structures | `periodic_atomic` | [paper 1](https://doi.org/10.1038/s41597-023-02116-z) | New |
| [Open-framework aluminophosphate structure database](catalog/porous_frameworks.md#alpo-open-framework) | 312 crystal structures | `periodic_atomic` | [paper 1](https://doi.org/10.1038/s41597-020-0452-4) | New |

### Molecular crystals and ice

| Dataset / release | Reported volume | Structure level | Descriptor | Pass |
|---|---:|---|---|---|
| [Open Molecular Crystals 2025 (OMC25)](catalog/molecular_crystals.md#omc25) | 26,257,042 DFT configuration frames | `periodic_atomic` | [paper 1](https://doi.org/10.1038/s41597-026-06628-2) | Existing |
| [PAH101 molecular-crystal GW+BSE dataset](catalog/molecular_crystals.md#pah101-gwbse) | 101 molecular crystal records | `periodic_atomic` | [paper 1](https://doi.org/10.1038/s41597-025-04959-0) | New |

### Surfaces, interfaces and catalysis

| Dataset / release | Reported volume | Structure level | Descriptor | Pass |
|---|---:|---|---|---|
| [SUNCAT bimetallic adsorption calculations](catalog/surfaces_catalysis.md#bimetallic-catalysis-2019) | ≥90,000 DFT calculations | `periodic_atomic` | [paper 1](https://doi.org/10.1038/s41597-019-0080-z) | New |
| [Organic chains chemisorbed on silicon surfaces](catalog/surfaces_catalysis.md#si-organic-chain-slab-2026) | ≥700 optimized adsorbate–slab configurations | `periodic_atomic` | [paper 1](https://doi.org/10.1038/s41597-026-07766-3) | New |
| [Elemental crystal surface energies and Wulff shapes](catalog/surfaces_catalysis.md#elemental-surface-energy-2016) | ≥100 elemental crystal polymorphs | `periodic_atomic` | [paper 1](https://doi.org/10.1038/sdata.2016.80) | New |

### Computed properties and prediction benchmarks

| Dataset / release | Reported volume | Structure level | Descriptor | Pass |
|---|---:|---|---|---|
| [Materials Project / Ricci electronic transport database](catalog/property_benchmarks.md#mp-boltztrap-transport) | ~48,000 materials | `periodic_atomic` | [paper 1](https://doi.org/10.1038/sdata.2017.85) | Existing |
| [ECD-cubic electronic charge-density database](catalog/property_benchmarks.md#ecd-cubic) | 17,418 cubic material charge-density records | `periodic_atomic` | [paper 1](https://doi.org/10.1038/s41597-022-01158-z) | New |
| [JARVIS electric-field-gradient tensor release](catalog/property_benchmarks.md#jarvis-efg-2020) | 15,202 material EFG records | `periodic_atomic` | [paper 1](https://doi.org/10.1038/s41597-020-00707-8) | New |
| [SPSE hierarchical solid-electrolyte ion transport](catalog/property_benchmarks.md#spse-ion-transport-2020) | 11,989 BVSE transport entries | `structure_linked` | [paper 1](https://doi.org/10.1038/s41597-020-0474-y) | New |
| [SNUMAT hybrid-functional band-gap dataset](catalog/property_benchmarks.md#snumat-hybrid-gap) | 10,481 materials | `periodic_atomic` | [paper 1](https://doi.org/10.1038/s41597-020-00723-8) | Existing |
| [Fang Wannier optical and transport tensors](catalog/property_benchmarks.md#fang-wannier-optical-transport-2025) | 7,301 material entries | `periodic_atomic` | [paper 1](https://doi.org/10.1038/s41597-025-05396-9) | Existing |
| [FCC Cu dislocation–grain-boundary interactions](catalog/property_benchmarks.md#cu-dislocation-grain-boundary) | 5,234 dislocation–grain-boundary interaction outcomes | `periodic_atomic` | [paper 1](https://doi.org/10.1038/s41597-025-05256-6) | New |
| [SuperBand electronic-band / superconductivity dataset](catalog/property_benchmarks.md#superband) | 2,474 materials | `periodic_atomic` | [paper 1](https://doi.org/10.1038/s41597-025-05015-7) | Existing |
| [Materials Project / Petretto DFPT phonons (2018)](catalog/property_benchmarks.md#mp-dfpt-phonons-2018) | 1,521 materials | `periodic_atomic` | [paper 1](https://doi.org/10.1038/sdata.2018.65) | Existing |
| [Quantum-Chemical Bonding Database for Solid-State Materials (2023)](catalog/property_benchmarks.md#lobster-bonding-2023) | 1,520 compounds | `structure_linked` | [paper 1](https://doi.org/10.1038/s41597-023-02477-5) | Existing |
| [JARVIS-WTBH electron Hamiltonians](catalog/property_benchmarks.md#jarvis-wtbh-electron) | 1,440 electron Hamiltonian entries | `structure_linked` | [paper 1](https://doi.org/10.1038/s41597-021-00885-z) | Existing |
| [Materials Project elastic tensor release (2015)](catalog/property_benchmarks.md#mp-elastic-2015) | 1,181 materials | `periodic_atomic` | [paper 1](https://doi.org/10.1038/sdata.2015.9) | Existing |
| [Materials Project dielectric tensor release (2017)](catalog/property_benchmarks.md#mp-dielectric-2017) | 1,056 materials | `periodic_atomic` | [paper 1](https://doi.org/10.1038/sdata.2016.134) | Existing |
| [Materials Project piezoelectric tensor release (2015)](catalog/property_benchmarks.md#mp-piezo-2015) | 941 materials | `periodic_atomic` | [paper 1](https://doi.org/10.1038/sdata.2015.53) | Existing |
| [Ternary fluoride-ion battery electrode reaction pairs](catalog/property_benchmarks.md#ternary-fluoride-electrode-pairs) | 807 fluorinated/defluorinated reaction pairs | `structure_linked` | [paper 1](https://doi.org/10.1038/s41597-023-01954-1) | Existing |
| [Literature-derived battery ionic migration barriers](catalog/property_benchmarks.md#migration-barriers-literature-2025) | 621 ionic migration pathways | `periodic_atomic` | [paper 1](https://doi.org/10.1038/s41597-025-06196-x) | Existing |
| [Trinquet nonlinear-optical SHG tensor dataset](catalog/property_benchmarks.md#trinquet-shg-2024) | 579 inorganic semiconductor structures | `periodic_atomic` | [paper 1](https://doi.org/10.1038/s41597-024-03590-9) | Existing |
| [Predicted high-dielectric ternary oxide structures](catalog/property_benchmarks.md#predicted-high-dielectric-oxides) | 441 computed ternary-oxide structures | `periodic_atomic` | [paper 1](https://doi.org/10.1038/s41597-020-0418-6) | New |
| [MAST-ML dilute-solute diffusion educational slice](catalog/property_benchmarks.md#mastml-dilute-diffusion-education) | 408 host–solute feature/property rows | `composition_only` | [paper 1](https://doi.org/10.1038/sdata.2016.54) | Existing |
| [UW CMG dilute-solute diffusion database](catalog/property_benchmarks.md#uw-cmg-dilute-solute-diffusion) | ≥400 host-solute diffusion systems | `structure_linked` | [paper 1](https://doi.org/10.1038/sdata.2016.54) | Existing |
| [Smidt first-principles ferroelectric candidate database](catalog/property_benchmarks.md#smidt-ferroelectric-2020) | 255 completed polar–nonpolar structure pairs | `periodic_atomic` | [paper 1](https://doi.org/10.1038/s41597-020-0407-9) | Existing |
| [INS-derived magnetic exchange and Monte Carlo dataset](catalog/property_benchmarks.md#ins-exchange-magnetic-2025) | Unranked magnetic compounds with exchange models | `periodic_atomic` | [paper 1](https://doi.org/10.1038/s41597-025-06099-x) | New |
| [Materials Project representation-independent charge densities](catalog/property_benchmarks.md#mp-charge-density-pyrho) | Unranked charge-density records | `periodic_atomic` | [paper 1](https://doi.org/10.1038/s41597-022-01746-z) | New |

### Experimental properties and literature extraction

| Dataset / release | Reported volume | Structure level | Descriptor | Pass |
|---|---:|---|---|---|
| [ChemDataExtractor stress-strain property database](catalog/experimental_properties.md#cde-stress-strain-2024) | 720,308 extracted property records | `composition_only` | [paper 1](https://doi.org/10.1038/s41597-024-03979-6) | New |
| [ChemDataExtractor battery materials database (2020)](catalog/experimental_properties.md#cde-battery-2020) | 292,313 property records | `composition_only` | [paper 1](https://doi.org/10.1038/s41597-020-00602-2) | Existing |
| [JCAP metal-oxide synthesis, imaging and UV–Vis cohort](catalog/experimental_properties.md#jcap-metal-oxide-optical-179k) | 179,072 synthesized metal-oxide samples | `composition_only` | [paper 1](https://doi.org/10.1038/s41597-019-0019-4) | New |
| [Text-mined sol-gel synthesis and phase-purity outcomes](catalog/experimental_properties.md#solgel-phase-purity-2026) | ~148,000 synthesis protocol records | `composition_only` | [paper 1](https://doi.org/10.1038/s41597-026-08492-6) | New |
| [High Throughput Experimental Materials Database (HTEM)](catalog/experimental_properties.md#htem) | ≥140,000 entries | `structure_linked` | [paper 1](https://doi.org/10.1038/sdata.2018.53) | Existing |
| [ChemDataExtractor refractive-index and dielectric database](catalog/experimental_properties.md#cde-refractive-dielectric-2022) | 109,880 optical/dielectric literature records | `composition_only` | [paper 1](https://doi.org/10.1038/s41597-022-01295-5) | Existing |
| [ChemDataExtractor semiconductor band-gap database](catalog/experimental_properties.md#cde-bandgaps-2022) | 100,236 band-gap literature records | `composition_only` | [paper 1](https://doi.org/10.1038/s41597-022-01294-6) | Existing |
| [ChemDataExtractor yield-strength and grain-size databases](catalog/experimental_properties.md#cde-yield-grainsize) | 94,554 extracted property records | `composition_only` | [paper 1](https://doi.org/10.1038/s41597-022-01301-w) | New |
| [3DSC_ICSD — superconductors linked to ICSD structures](catalog/experimental_properties.md#3dsc-icsd) | 86,490 matched crystal structures | `structure_linked` | [paper 1](https://doi.org/10.1038/s41597-023-02721-y) | Existing |
| [Solid-state synthesis recipes with impurity phases](catalog/experimental_properties.md#solid-state-synthesis-impurities) | 80,806 synthesis reactions | `composition_only` | [paper 1](https://doi.org/10.1038/s41597-025-06222-y) | Existing |
| [ChemDataExtractor/Snowball Curie–Néel dataset (2025)](catalog/experimental_properties.md#cde-curie-neel-2025) | 56,037 property records | `composition_only` | [paper 1](https://doi.org/10.1038/s41597-025-06244-6) | Existing |
| [ChemDataExtractor dye-sensitized solar-cell devices](catalog/experimental_properties.md#cde-dye-sensitized-solar-devices) | 41,860 device-report JSON documents | `composition_only` | [paper 1](https://doi.org/10.1038/s41597-022-01355-w) | New |
| [ChemDataExtractor Curie and Néel database (2018)](catalog/experimental_properties.md#cde-curie-neel-2018) | 39,822 property records | `composition_only` | [paper 1](https://doi.org/10.1038/sdata.2018.111) | Existing |
| [Text-mined solution-based inorganic synthesis procedures](catalog/experimental_properties.md#text-mined-solution-synthesis) | 35,675 synthesis procedures | `composition_only` | [paper 1](https://doi.org/10.1038/s41597-022-01317-2) | Existing |
| [ChemDataExtractor thermoelectric materials database](catalog/experimental_properties.md#cde-thermoelectric) | 22,805 property records | `composition_only` | [paper 1](https://doi.org/10.1038/s41597-022-01752-1) | Existing |
| [Text-mined inorganic solid-state synthesis recipes](catalog/experimental_properties.md#text-mined-solid-state-synthesis) | 19,488 synthesis entries | `composition_only` | [paper 1](https://doi.org/10.1038/s41597-019-0224-1) | Existing |
| [ChemDataExtractor perovskite solar-cell devices](catalog/experimental_properties.md#cde-perovskite-solar-devices) | 15,818 device-report JSON documents | `composition_only` | [paper 1](https://doi.org/10.1038/s41597-022-01355-w) | New |
| [ChemDataExtractor water-splitting photocatalysis](catalog/experimental_properties.md#cde-photocatalysis-water-splitting) | 15,755 extracted photocatalytic activity records | `composition_only` | [paper 1](https://doi.org/10.1038/s41597-023-02511-6) | New |
| [Aluminum alloy composition and mechanical-property literature datasets](catalog/experimental_properties.md#aluminum-alloy-literature-2022) | 14,884 alloy composition entries | `composition_only` | [paper 1](https://doi.org/10.1038/s41597-022-01215-7) | New |
| [LLM high-entropy alloy phase and processing database](catalog/experimental_properties.md#hea-llm-2026) | 12,427 literature-derived alloy entries | `composition_only` | [paper 1](https://doi.org/10.1038/s41597-026-06930-z) | New |
| [FePTP iron-containing phase-transformation pathways](catalog/experimental_properties.md#feptp-iron-phase-pathways) | 11,241 phase-transformation pathways | `composition_only` | [paper 1](https://doi.org/10.1038/s41597-026-07067-9) | New |
| [CO2 electrocatalysis and catalyst synthesis corpora](catalog/experimental_properties.md#co2-electrocatalyst-llm-corpus) | 6,985 human-annotated benchmark records | `composition_only` | [paper 1](https://doi.org/10.1038/s41597-024-03180-9) | New |
| [Welded-joint fatigue property database](catalog/experimental_properties.md#weld-fatigue-2025) | 5,797 fatigue condition/parameter records | `composition_only` | [paper 1](https://doi.org/10.1038/s41597-025-06067-5) | New |
| [3DSC_MP — superconductors with Materials Project structures](catalog/experimental_properties.md#3dsc-mp) | 5,773 matched crystal structures | `periodic_atomic` | [paper 1](https://doi.org/10.1038/s41597-023-02721-y) | Existing |
| [Text-mined layered sodium cathode synthesis and performance](catalog/experimental_properties.md#layered-na-cathode-textmine) | 5,265 extracted experimental records | `composition_only` | [paper 1](https://doi.org/10.1038/s41597-024-03196-1) | New |
| [Text-mined gold nanoparticle synthesis and morphology](catalog/experimental_properties.md#aunp-textmined-synthesis) | 5,154 publication-level synthesis records | `composition_only` | [paper 1](https://doi.org/10.1038/s41597-022-01321-6) | New |
| [Nuclear structural material Charpy impact tests](catalog/experimental_properties.md#nuclear-charpy-impact) | 4,961 Charpy impact test records | `composition_only` | [paper 1](https://doi.org/10.1038/s41597-025-04823-1) | New |
| [Refractiveindex.info optical constants](catalog/experimental_properties.md#refractiveindex-info) | 3,328 published optical data records | `mixed` | [paper 1](https://doi.org/10.1038/s41597-023-02898-2) | Existing |
| [Text-mined perovskite solar-device fabrication attributes](catalog/experimental_properties.md#psc-fabrication-textmine-2025) | 3,164 article-linked fabrication records | `composition_only` | [paper 1](https://doi.org/10.1038/s41597-025-04566-z) | New |
| [Cu-Cr-X mechanical and electrical property dataset](catalog/experimental_properties.md#cu-cr-x-figure-extraction) | 3,018 alloy composition-processing-property records | `composition_only` | [paper 1](https://doi.org/10.1038/s41597-025-06295-9) | Existing |
| [FatigueData-AM2022 additively manufactured alloys](catalog/experimental_properties.md#fatiguedata-am2022) | 2,460 fatigue test-condition datasets | `composition_only` | [paper 1](https://doi.org/10.1038/s41597-023-02150-x) | New |
| [AlloyData-2024LT low-temperature alloy mechanics](catalog/experimental_properties.md#alloydata-lowtemp) | 1,913 experimental test-condition records | `composition_only` | [paper 1](https://doi.org/10.1038/s41597-025-05512-9) | New |
| [Copper-alloy mechanical properties and electrical conductivity (Gorsse 2023)](catalog/experimental_properties.md#cu-alloys-mechanical-2023) | 1,831 composition-processing-property-reference records | `composition_only` | [paper 1](https://doi.org/10.1038/s41597-023-02411-9) | Existing |
| [Nuclear structural material creep tests](catalog/experimental_properties.md#nuclear-creep-properties) | 1,583 creep test/specimen records | `composition_only` | [paper 1](https://doi.org/10.1038/s41597-026-07563-y) | New |
| [L-PBF commercial alloy relative-density dataset](catalog/experimental_properties.md#lpbf-relative-density) | 1,579 literature processing-condition observations | `composition_only` | [paper 1](https://doi.org/10.1038/s41597-025-04576-x) | New |
| [Borg expanded MPEA mechanical properties and phases](catalog/experimental_properties.md#mpea-borg-expanded) | 1,545 composition–condition–reference records | `composition_only` | [paper 1](https://doi.org/10.1038/s41597-020-00768-9) | New |
| [HYPOD-X: quasicrystals and approximants](catalog/experimental_properties.md#hypod-x) | 1,448 composition/sample instances | `structure_linked` | [paper 1](https://doi.org/10.1038/s41597-024-04043-z) | Existing |
| [Experimental interfacial thermal resistance and descriptors](catalog/experimental_properties.md#itr-interface-descriptors) | 1,318 interface–temperature observations | `mixed` | [paper 1](https://doi.org/10.1038/s41597-020-0373-2) | New |
| [Calorimetric inorganic formation enthalpies](catalog/experimental_properties.md#experimental-formation-enthalpy-2017) | 1,276 experimental formation-enthalpy entries | `structure_linked` | [paper 1](https://doi.org/10.1038/sdata.2017.162) | New |
| [EKHI optical and thermal radiative properties](catalog/experimental_properties.md#ekhi-radiative-2026) | 1,251 experimental property curves | `composition_only` | [paper 1](https://doi.org/10.1038/s41597-026-07083-9) | Existing |
| [Sub-sized nuclear structural material tensile tests](catalog/experimental_properties.md#nuclear-subsize-tensile) | 1,050 tensile test records | `composition_only` | [paper 1](https://doi.org/10.1038/s41597-024-04329-2) | New |
| [Metallic-material combustion property database](catalog/experimental_properties.md#metal-combustion-properties) | 725 combustion measurement records | `composition_only` | [paper 1](https://doi.org/10.1038/s41597-026-06862-8) | Existing |
| [China Space Station levitation thermophysical dataset](catalog/experimental_properties.md#css-levitation-thermophysical) | 565 levitation experimental records | `mixed` | [paper 1](https://doi.org/10.1038/s41597-025-06428-0) | New |
| [Oxygen-ion conductor Arrhenius property dataset](catalog/experimental_properties.md#oxygen-ion-conductor-2026) | 483 oxide measurement-condition entries | `composition_only` | [paper 1](https://doi.org/10.1038/s41597-026-07100-x) | New |
| [DAX-Ti experimental Ti-alloy mechanical-property compilation](catalog/experimental_properties.md#dax-ti-experimental) | 282 alloy entries | `composition_only` | [paper 1](https://doi.org/10.1038/s41597-022-01283-9) | Existing |
| [Mechanically deformed ferritic-steel XCT defect database](catalog/experimental_properties.md#ferritic-steel-xct-defects) | 276 sample-condition XCT datasets | `composition_only` | [paper 1](https://doi.org/10.1038/s41597-025-06141-y) | New |
| [Fe/MgO soft magnetic composite processing properties](catalog/experimental_properties.md#softmag-fe-mgo) | 274 corrected processing-condition samples | `composition_only` | [paper 1](https://doi.org/10.1038/s41597-024-04286-w) | New |
| [FatigueData-CMA2022 complex metallic-alloy fatigue database](catalog/experimental_properties.md#fatiguedata-cma2022) | 272 fatigue test-condition datasets | `composition_only` | [paper 1](https://doi.org/10.1038/s41597-023-02354-1) | Existing |
| [HEA fracture and impact toughness dataset](catalog/experimental_properties.md#hea-fracture-impact-2023) | 245 metallurgical-condition property records | `composition_only` | [paper 1](https://doi.org/10.1038/s41597-022-01911-4) | New |
| [Multinary alloy HER catalyst performance](catalog/experimental_properties.md#her-multinary-alloys-2026) | 180 experimental catalyst/performance records | `composition_only` | [paper 1](https://doi.org/10.1038/s41597-026-07856-2) | New |
| [Optical emissivity curves for heterogeneous engineered designs](catalog/experimental_properties.md#optical-emissivity-designs-2022) | 153 emissivity curve records | `composition_only` | [paper 1](https://doi.org/10.1038/s41597-022-01699-3) | New |
| [Trace-IN625 source-aware tensile properties](catalog/experimental_properties.md#trace-in625-tensile) | 149 tensile-property records | `composition_only` | [paper 1](https://doi.org/10.1038/s41597-026-08585-2) | New |
| [AISI52100 grease-lubricated rolling-contact fatigue benchmark](catalog/experimental_properties.md#aisi52100-rolling-contact-fatigue) | 63 four-ball tribometer trials | `composition_only` | [paper 1](https://doi.org/10.1038/s41597-026-08057-7) | New |
| [Aggregated oxide synthesis parameter distributions](catalog/experimental_properties.md#oxide-synthesis-aggregates-2017) | 30 oxide material-system summaries | `composition_only` | [paper 1](https://doi.org/10.1038/sdata.2017.127) | New |
| [Correlative chemical, crystallographic and magnetic iron-oxide grains](catalog/experimental_properties.md#hawaii-ironoxide-correlative-grains) | 23 deposited component datasets | `composition_only` | [paper 1](https://doi.org/10.1038/sdata.2018.162) | New |
| [BAM temperature-dependent elastic alloy reference data](catalog/experimental_properties.md#bam-temperature-elastic-alloys) | 3 alloy systems with paired manufacturing routes | `composition_only` | [paper 1](https://doi.org/10.1038/s41597-023-02387-6) | New |
| [304L stainless-steel full-field DIC and infrared thermography](catalog/experimental_properties.md#steel304l-dic-ir-fullfield) | Unranked specimen-test measurement records | `composition_only` | [paper 1](https://doi.org/10.1038/s41597-024-03949-y) | New |
| [Corrosion-resistant alloy electrochemical metrics](catalog/experimental_properties.md#corrosion-resistant-alloy-metrics) | Unranked corrosion metric/condition records | `composition_only` | [paper 1](https://doi.org/10.1038/s41597-021-00840-y) | New |
| [Inconel718 correlative 3D microstructure and deformation fields](catalog/experimental_properties.md#in718-correlative-3d-ebsd-dic) | Unranked registered multimodal specimen datasets | `mixed` | [paper 1](https://doi.org/10.1038/s41597-022-01525-w) | New |
| [Self-cleaning coating material and property corpora](catalog/experimental_properties.md#self-cleaning-coating-literature) | Unranked material/property/source group records | `composition_only` | [paper 1](https://doi.org/10.1038/s41597-024-02983-0) | New |

### Diffraction, spectroscopy and characterization

| Dataset / release | Reported volume | Structure level | Descriptor | Pass |
|---|---:|---|---|---|
| [Materials Project K-edge XANES release](catalog/diffraction_spectroscopy.md#mp-kedge-xanes-2018) | ≥500,000 site-resolved K-edge XANES spectra | `structure_linked` | [paper 1](https://doi.org/10.1038/sdata.2018.151) | New |
| [SIMPOD simulated powder X-ray diffraction benchmark](catalog/diffraction_spectroscopy.md#simpod-powder-xrd) | 467,861 COD structure/diffractogram pairs | `periodic_atomic` | [paper 1](https://doi.org/10.1038/s41597-025-05534-3) | New |
| [Materials Project L-edge XANES release](catalog/diffraction_spectroscopy.md#mp-ledge-xanes-2021) | ~140,000 site-wise L2 or L3 XANES spectra | `structure_linked` | [paper 1](https://doi.org/10.1038/s41597-021-00936-5) | New |
| [Synthetic inelastic-neutron spectra — inorganic crystal subset](catalog/diffraction_spectroscopy.md#ins-crystals-10023) | 10,023 inorganic crystal models with simulated INS | `periodic_atomic` | [paper 1](https://doi.org/10.1038/s41597-022-01926-x) | New |
| [Oulu computational Raman database](catalog/diffraction_spectroscopy.md#raman-oulu-5099) | 5,099 materials with calculated Raman properties | `periodic_atomic` | [paper 1](https://doi.org/10.1038/s41597-023-01988-5) | New |
| [Quaternary-phosphonium-salt image-to-molecule morphology benchmark](catalog/diffraction_spectroscopy.md#qps-morphology-images) | 4,037 SEM and optical images | `mixed` | [paper 1](https://doi.org/10.1038/s41597-026-06941-w) | New |
| [Two-dimensional materials ab initio Raman spectra](catalog/diffraction_spectroscopy.md#raman-2d-3504) | 3,504 two-dimensional materials | `periodic_atomic` | [paper 1](https://doi.org/10.1038/s41597-025-04593-w) | New |
| [Lithium-thiophosphate sulfur K-edge XAS](catalog/diffraction_spectroscopy.md#lps-sulfur-kedge-xas) | 2,681 site-resolved sulfur K-edge spectra | `mixed` | [paper 1](https://doi.org/10.1038/s41597-023-02262-4) | New |
| [Aachen-Heerlen annotated steel microstructures](catalog/diffraction_spectroscopy.md#aachen-heerlen-steel-sem) | 2,580 SEM images | `composition_only` | [paper 1](https://doi.org/10.1038/s41597-021-00926-7) | New |
| [Pd-on-carbon SEM ordering benchmark](catalog/diffraction_spectroscopy.md#pd-carbon-sem-ordering) | 1,000 SEM images | `composition_only` | [paper 1](https://doi.org/10.1038/s41597-020-0439-1) | New |
| [JARVIS-STM computational scanning-tunneling microscopy](catalog/diffraction_spectroscopy.md#jarvis-stm) | 716 exfoliable two-dimensional materials | `structure_linked` | [paper 1](https://doi.org/10.1038/s41597-021-00824-y) | New |
| [AmalgaMatch correlative materials microscopy benchmark](catalog/diffraction_spectroscopy.md#amalgamatch-microscopy) | 187 annotated image pairs | `mixed` | [paper 1](https://doi.org/10.1038/s41597-026-07961-2) | New |
| [Hybrid-functional inorganic-crystal Raman database](catalog/diffraction_spectroscopy.md#hybrid-raman-crystal-2024) | 161 inorganic compounds | `structure_linked` | [paper 1](https://doi.org/10.1038/s41597-024-02924-x) | New |
| [DL-ADD MoS2/WS2 atomic-defect STM benchmark](catalog/diffraction_spectroscopy.md#dl-add-tmd-stm-defects) | 105 original STM benchmark images | `composition_only` | [paper 1](https://doi.org/10.1038/s41597-023-02004-6) | New |
| [MicroLib SliceGAN microstructure library](catalog/diffraction_spectroscopy.md#microlib-slicegan) | 87 source microstructure entries | `composition_only` | [paper 1](https://doi.org/10.1038/s41597-022-01744-1) | New |
| [Materials Project Raman tensor and RRUFF matching benchmark](catalog/diffraction_spectroscopy.md#mp-raman-2019) | 55 computed inorganic compounds | `periodic_atomic` | [paper 1](https://doi.org/10.1038/s41597-019-0138-y) | New |
| [Battery-interphase IR/Raman/XRD reference library](catalog/diffraction_spectroscopy.md#battery-interphase-ir-raman-xrd) | 10 reference compounds | `composition_only` | [paper 1](https://doi.org/10.1038/s41597-024-04236-6) | New |
| [Nanomaterial STEM tomography reference collection](catalog/diffraction_spectroscopy.md#stem-nanomaterial-tomography-2016) | 5 tomographic material systems | `mixed` | [paper 1](https://doi.org/10.1038/sdata.2016.41) | New |
| [Zn-doped zeolite13X multimodal synchrotron benchmark](catalog/diffraction_spectroscopy.md#zeolite13x-multimodal-tomography) | 1 bespoke two-phase sample | `mixed` | [paper 1](https://doi.org/10.1038/s41597-025-04605-9) | New |
| [BraggNN high-energy diffraction microscopy training/validation data](catalog/diffraction_spectroscopy.md#braggnn-hedm-datasets) | Unranked diffraction frame/Bragg-peak records | `mixed` | [paper 1](https://doi.org/10.1038/s41597-022-01712-9) | New |
| [Graphene/black-phosphorus ARPES simulation and HOPG reference data](catalog/diffraction_spectroscopy.md#arpes-graphene-bp-2016) | Unranked simulation/spectral records | `mixed` | [paper 1](https://doi.org/10.1038/sdata.2016.31) | New |
