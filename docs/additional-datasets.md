# Additional materials dataset discoveries

[Back to MatVerse](../README.md) · [Search these additions](https://usccolumbia.github.io/matverse/?q=%22additional-materials-20261101%22) · [All source links](../sources.md)

Checked 2026-11-01. This targeted extension adds **50 dataset/release records** beyond the 304-record baseline. The maintained catalog now contains **548 records**. New records include independently useful property layers and named derived releases; they are not all disjoint material populations.

## Questions and search method

The search asked which relevant releases remained absent after the journal/property surveys, what their independent counting units and parent lineages were, and which primary sources established scope, access and rights. Independent passes covered defects/disorder, porous materials/adsorption and specialized functional/low-dimensional materials. A coordinating pass examined atomistic reference sets and experimental transport/alloy properties.

Searches followed papers to provider pages, author repositories, release APIs and selected payloads. A title hit or downloadable model alone was insufficient. This is a targeted extension across missing domains, not a census of every materials dataset online. Failed requests, deferred leads and alternative versions remain in the research trail.

[Frozen brief](../research/additional_20261101/BRIEF.md) · [Research package](../research/additional_20261101/README.md) · [Integration receipt and source hashes](../research/additional_20261101/integration_receipt.json) · [Source-entry dispositions](../research/collection_additional_20261101.json)

## What is newly covered

The structural additions extend dimensionality and order: C1DB covers one-dimensional systems, SACADA indexes carbon allotropes, and defect/grain-boundary/irradiation releases describe departures from perfect bulk crystals. Porous collections supply hypothetical coordinates, adsorption data and thermal or diffusion labels. Specialized functional releases add Heusler, altermagnetic, spin-Hall, optical and ferroelectric-search data.

These objects require different reuse strategies. A grain-boundary minimum is distinct from every candidate searched to obtain it; a defect-site calculation is distinct from its host crystal. A generated ferroelectric-search CIF is a model proposal, while measured thermoelectric observations and DFT-derived transport targets have different provenance. The DXMag ternary CSV counts calculation rows, whereas the other two Heusler releases report compound populations with ML-derived ground-state/property labels.

For atomistic learning, SoLiD26 adds explicit solid–liquid environments and SevenNet DBS adds harmonized single-point labels over existing parent geometries. The smaller GAP/MACE/ACE reference cohorts span particular chemistries and sampling schemes. SiOx reuses Si and silica references; original and revised carbon datasets overlap. Synthetic a-Si and amorphous-graphene labels come from trained potentials and must not be treated as fresh DFT observations.

## Verified release table

Reported sizes descend within each category. Units, access, licenses and caveats remain explicit in the linked cards. Unknown sizes are unranked; counts are not added across parents, derivatives, frames, specimens or property observations.

### Computed bulk inorganic crystals

| Release | Reported volume | Label provenance | Access |
|---|---:|---|---|
| [DXMag Computational HeuslerDB — quaternary ML](catalog/bulk_computed.md#dxmag-heusler-quaternary) | 131,544 provider-reported compounds | MLIP structure optimization and transfer-learned property estimates; trained on ternary Heusler DFT | open |
| [DXMag Computational HeuslerDB — ternary DFT](catalog/bulk_computed.md#dxmag-heusler-ternary) | 106,235 DFT calculation rows | DFT (PBE), multiple structural and magnetic configurations | open |
| [DXMag Computational HeuslerDB — all-d ML](catalog/bulk_computed.md#dxmag-heusler-alld) | 105,763 provider-reported compounds | MLIP structure optimization and transfer-learned property estimates; trained on ternary Heusler DFT | open |
| [SACADA three-periodic carbon allotropes](catalog/bulk_computed.md#sacada) | 1,661 carbon allotrope table entries | computed | open |
| [NIST MRAS amorphous structural models](catalog/bulk_computed.md#nist-mras-amorphous) | 50 final amorphous structure files | Worden–Cockayne–Garrity random-arrangement relaxation workflows at NIST | open |

### Bulk and mixed-domain MLIP configurations

| Release | Reported volume | Label provenance | Access |
|---|---:|---|---|
| [SoLiD26 solid–liquid interface configurations](catalog/mlip_configurations.md#solid26) | 15,379,823 atomic configuration frames | computed | open |
| [SevenNet-Omni domain-bridging set (DBS)](catalog/mlip_configurations.md#sevennet-omni-dbs) | ~125,000 cross-domain DFT configuration records | computed | open |
| [IAEA CascadesDB collision-cascade simulations](catalog/mlip_configurations.md#iaea-cascadesdb) | 17,024 collision-cascade simulations | IAEA-curated contributions from independently published molecular-dynamics radiation-damage studies | open |
| [Carbon GAP-20 DFT reference database](catalog/mlip_configurations.md#carbon-gap20) | ~17,000 DFT atomic configurations | computed | open |
| [SiOx-ACE-24 silicon–oxygen reference configurations](catalog/mlip_configurations.md#siox-ace24) | 11,428 normalized training configurations | computed | open |
| [Carbon GAP-20U revised training configurations](catalog/mlip_configurations.md#carbon-gap20u) | 6,088 DFT reference configurations | computed | open |
| [Materials Project non-crystalline AIMD and diffusivity database](catalog/mlip_configurations.md#mp-noncrystalline-aimd) | 5,120 5000 K AIMD parent systems | MPMorph AIMD workflows seeded from Materials Project compositions; non-crystalline trajectories are new calculations | open |
| [P-GAP-20 phosphorus reference configurations](catalog/mlip_configurations.md#p-gap20) | 4,798 normalized training configurations | computed | open |
| [MACE-MP-MOF0 DFT training configurations](catalog/mlip_configurations.md#mace-mp-mof0-training) | 4,311 DFT configuration frames | computed | open |
| [GO-MACE-23 graphene-oxide reference cohort](catalog/mlip_configurations.md#go-mace23) | 3,816 normalized training configurations | computed | open |
| [SiO2-GAP-22 silica training cohort](catalog/mlip_configurations.md#sio2-gap22) | 3,074 normalized training configurations | computed | open |
| [Paracrystalline/amorphous silicon structural models](catalog/mlip_configurations.md#asi-paracrystalline-models) | 3,069 final melt–quench configuration frames | model-generated; MTP-labeled | open |
| [GST-GAP-22 PBE reference cohort](catalog/mlip_configurations.md#gst-gap22-pbe) | 2,692 normalized training configurations | computed | open |
| [Si-GAP-18 silicon training cohort](catalog/mlip_configurations.md#si-gap18) | 2,475 normalized training configurations | computed | open |
| [Chalcogenide vacancy structure-reconstruction dataset](catalog/mlip_configurations.md#chalcogenide-vacancy-reconstructions) | ~130 neutral cation-vacancy defects | ShakeNBreak structure searches and VASP DFT relaxations; processed M3GNet training/validation configurations derived from the same trajectories | open |
| [Fe–Ni–Cr irradiated and relaxed atomistic configurations](catalog/mlip_configurations.md#fenicr-irradiated-relaxed-md) | 2 released atomistic sample configurations | Molecular-dynamics configurations supporting the atomistic radiation-induced ductile-to-brittle transition study | open |
| [Amorphous alumina bulk/surface DFT training release](catalog/mlip_configurations.md#amorphous-alumina-deep-potential) | Unranked DFT reference configurations | Active learning for amorphous Al2O3 bulk and surfaces with crystalline seed configurations | open |

### Two-dimensional and layered materials

| Release | Reported volume | Label provenance | Access |
|---|---:|---|---|
| [CMR C2DM transition-metal monolayer electronic structures (2015)](catalog/two_dimensional.md#cmr-c2dm-2015) | 494 ASE calculation/structure rows | DFT / first-principles calculations | open |
| [Zhou–Poncé–Charlier 2D spin-Hall / Wannier dataset](catalog/two_dimensional.md#zhou-2d-spin-hall-426) | 426 nonmagnetic monolayers | First-principles DFT and Wannier interpolation; monolayers drawn from existing 2D collections | open |
| [AC-2D-22 amorphous graphene benchmark subset](catalog/two_dimensional.md#ac2d-amorphous-graphene) | 150 selected 200-atom configurations | model-generated; C-GAP-17-labeled | open |

### MOFs, COFs and zeolites

| Release | Reported volume | Label provenance | Access |
|---|---:|---|---|
| [PORMAKE hypothetical MOFs for MOFTransformer](catalog/porous_frameworks.md#pormake-moftransformer-1m) | 1,118,074 hypothetical MOF structures | generated | open |
| [MOFX-DB computational adsorption database](catalog/porous_frameworks.md#mofx-db) | 168,534 parent-database structure records | computed | open |
| [SymGNN aluminum-substituted zeolite adsorption dataset](catalog/porous_frameworks.md#symgnn-zeolite-adsorption) | 57,084 substitution/property cases | computed | open |
| [ToBaCCo hypothetical MOF structure database](catalog/porous_frameworks.md#tobacco-mofs) | 13,511 valid hypothetical MOF structures | generated | open |

### Surfaces, interfaces and catalysis

| Release | Reported volume | Label provenance | Access |
|---|---:|---|---|
| [Homer aluminum grain-boundary structures across 5D space](catalog/surfaces_catalysis.md#homer-aluminum-gb-7304) | 7,304 minimum-energy grain-boundary structures | EAM-conjugate-gradient optimization of aluminum bicrystals over many microscopic initial configurations | open |
| [GBDB elemental-metal grain-boundary DFT database](catalog/surfaces_catalysis.md#gbdb-elemental-metals) | 327 grain-boundary structures | High-throughput scaled-template DFT calculations by Zheng and collaborators; distributed through Materials Project and Crystalium | open |

### Computed properties and prediction benchmarks

| Release | Reported volume | Label provenance | Access |
|---|---:|---|---|
| [Quantum Defects Database — semiconductor point defects](catalog/property_benchmarks.md#quantumdefects-semiconductor) | ≥50,000 point-defect calculations | High-throughput first-principles semiconductor defect calculations by Ivanov and collaborators | open |
| [PhononMOFdb](catalog/property_benchmarks.md#phononmofdb) | 11,900 MOF thermal-property records | MLIP-computed | open |
| [CMR ABSe3 ternary selenides](catalog/property_benchmarks.md#cmr-abse3) | 5,976 ASE calculation/structure rows | DFT / first-principles calculations | open |
| [ZeoDiff zeolite diffusion structure-property dataset](catalog/property_benchmarks.md#zeodiff-diffusion) | 4,194 zeolite descriptor/diffusion rows | computed | open |
| [Computational 1D Materials Database (C1DB)](catalog/property_benchmarks.md#c1db) | 3,157 browser database rows | DFT, exfoliated experimental-parent crystals and machine-generated chains | open |
| [OQMD-derived oxygen-vacancy formation energies](catalog/property_benchmarks.md#oqmd-oxygen-vacancy-sites-2023) | 2,677 oxygen-site property rows | Baldassarri–He–Wolverton high-throughput vacancy calculations on OQMD oxide hosts | open |
| [CMR A2BCX4 quaternary chalcogenides](catalog/property_benchmarks.md#cmr-a2bcx4) | 1,368 ASE calculation/structure rows | DFT / first-principles calculations | open |
| [Kumagai oxygen-vacancy database](catalog/property_benchmarks.md#kumagai-oxygen-vacancies) | 937 oxide hosts | New PBEsol(+U) and non-self-consistent dielectric-dependent hybrid calculations; hosts selected from Materials Project | open |
| [Nanoporous-material heat-capacity DFT and prediction dataset](catalog/property_benchmarks.md#porous-heat-capacity-2022) | 232 DFT-labelled parent structures | computed and model-predicted | open |
| [MINT-ATLAS atomistic magnetic interactions](catalog/property_benchmarks.md#mint-atlas) | 209 OPTIMADE structure records | Compiled atomistic magnetic-interaction calculations with per-record method and literature provenance | open |
| [Bond-focused grain-boundary solute interaction spectra](catalog/property_benchmarks.md#gb-solute-interaction-spectra) | ~200 binary alloy systems | EAM calculations of grain-boundary segregation and interaction spectra; not DFT or experimental measurements | open |
| [Sufyan altermagnetic spin-splitting screening release](catalog/property_benchmarks.md#altermagnet-spin-splitting-2026) | 171 ranked material records | DFT screening of MAGNDATA-derived magnetic structures; some candidates use forced-collinear variants | open |
| [CMR ABX2 photovoltaic polytypes](catalog/property_benchmarks.md#cmr-abx2) | 123 ASE calculation/structure rows | DFT / first-principles calculations | open |
| [CMR perovskite optical-absorption spectra](catalog/property_benchmarks.md#cmr-perovskite-absorption) | 79 ASE calculation/structure rows | DFT / first-principles calculations | open |

### Crystal generation and discovery benchmarks

| Release | Reported volume | Label provenance | Access |
|---|---:|---|---|
| [FerroGen MatterGen generated crystal cohort](catalog/generation_benchmarks.md#ferrogen-mattergen-12800) | 12,800 generated CIF files | MatterGen diffusion-model generation | open |

### Experimental properties and literature extraction

| Release | Reported volume | Label provenance | Access |
|---|---:|---|---|
| [NIST/ARPA-E adsorption isotherm database (NIST-ISODB)](catalog/experimental_properties.md#nist-isodb) | 37,703 adsorption isotherms | experimental | open |
| [ULTERA high-entropy-alloy property database](catalog/experimental_properties.md#ultera-2025) | ≥12,540 experimental HEA/MEA property observations | experimental; literature-curated | restricted |
| [sysTEm systematically verified experimental thermoelectrics](catalog/experimental_properties.md#system-thermoelectric) | 8,650 composition–temperature observations | experimental; literature-curated | open |
| [Literature-curated complex-oxide thermal expansion](catalog/experimental_properties.md#complex-oxide-cte-2026) | 204 composition–temperature-range records | experimental; literature-curated | open |

## Release and denominator findings

SoLiD26’s September preprint described access by request. Its October revision and actual Materials Cloud deposit establish an open CC BY 4.0 release. The 15,379,823-frame count is source-reported; the 63.8 GiB compressed payload was not downloaded. The public README warns that ASE constraints can alter returned forces, so raw force labels must be read appropriately.

SACADA’s live read-only response contains 1,661 unique IDs, even though its HTML displays an older update label. A sample ZIP contains ideal-net and optimized CIFs for one entry; these are not two new allotropes. Complete coordinate/property coverage and redistribution rights remain unverified.

The MACE-MP-MOF0 downloadable v2 archive contains 4,311 complete frames across train/validation/test files, differing from the article’s 4,764 DFT points. PhononMOFdb’s inspected thermal archive contains 11,900 records. The Heusler ternary table has 106,235 UUID-distinct calculation rows; the provider’s 27,864-compound figure is a different unreconciled denominator. The ranked altermagnet table has 171 rows, compared with 180 discussed by the paper/current application. Each discrepancy is qualified in its card.

The current sysTEm workbook contains 8,650 observations and 1,437 standardized composition strings, spanning 10–1275 K. It overlaps ESTM and extended MRL. The complex-oxide thermal-expansion table supplies 204 composition/temperature-range records. ULTERA’s May 2025 metadata reports 12,540+ HEA/MEA property points, but its files remain restricted and no data license was established.

## Limits and follow-up

Public metadata, downloadable coordinates, a declared license and a documentation check are separate signals. Some CMR pages have conflicting license statements; MINT’s client-code license does not establish its data rights; some defect archives have unverified rights. NIST adsorption’s historical count is explicitly dated and not presented as a live counter. Dataset cards preserve these distinctions.

Selected small/medium payloads were independently counted or sampled. Larger corpora retain provider-reported counts. No blanket claim of numerical accuracy, unbiased sampling, deduplicated material identities or complete bulk-transfer success follows. Split related source papers, trajectories, hosts and parent structures together where needed to reduce leakage.

The local preview exposed a previous source-year parsing error: **23 records** had been assigned 2002. Those values were corrected to the journal publication years using the retained DOI/date metadata. The integration receipt preserves each before/after value and source; historical staging files remain unchanged.

The search answers the first question with the verified additions above, the second through the category/unit/provenance crosswalk, and the third through release-specific sources and access/rights fields. Deferred candidates remain discoverable without being promoted into the ranked catalog. All changes remain local pending the user’s publication instruction.
