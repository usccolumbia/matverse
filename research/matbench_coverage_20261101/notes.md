# Matbench Discovery dataset directory: complete coverage audit

Checked 2026-11-01. Source: [data/sets](https://matbench-discovery.materialsproject.org/data/sets). The rendered table has **46 rows** and agrees exactly with the46 keys of the [pinned dataset registry](https://github.com/janosh/matbench-discovery/blob/8869a883a5067015b815886d878bd7aaa3862d2d/data/datasets.yml).

## Answer before integration

No: the previous catalog covered23 rows through existing dataset families and2 through resources. It lacked13 named release/subset cards and8 adjacent or unreleased resources. Even some existing family mappings have different releases or counting denominators. This audit prepares the missing records and all46 searchable source entries for local integration; it does not claim that they were already published.

The13 new dataset cards distinguish specific training/validation sets, historical snapshots, recomputed phonon cohorts and the COSMOS umbrella. The8 new resource cards preserve molecular/polymer datasets and SMAX without counting them as public periodic-crystal corpora. MatterSim remains an existing unreleased-data resource.

## Important release distinctions

- Materials Project 2022 is a frozen154,718-entry training release; it does not replace the current Materials Project 271,325 structures.
- GNoME 89M and ELEMENTA 210.7M refer to partly unavailable full training corpora. The public catalog records are smaller released subsets.
- sAlex existing 11,000,983 counts training plus validation, while the page training row is 10,447,765; the 553,218 validation subset is separately prepared and overlaps that parent.
- Alexandria relaxation frames differ from equilibrium crystal populations; AFLOW/OQMD/QMOF repository snapshots also require version alignment.
- MatPES 2025.1 PBE/r2SCAN have separate target labels and overlapping geometries. The newer 2025.2 release removes duplicates and adds charge labels; a default SDK request may return it instead.
- MDR-PBE directory metadata contains9,958 distinct mp-ID YAML files, one fewer than the paper 9,959. PFT is a training subset with Hessians, separate from validation/test and the original MDR calculation convention.
- COSMOS combines 15 existing datasets plus DBS and is not a single 242.8M-frame deposited archive. DBS already has its own independent label-layer card.
- OC20NEB saves repeated fixed endpoints across optimization iterations; frame count does not equal independent transition states.
- OCx24 page material count 19,406 refers to computational candidates, while the existing experimental dataset card counts 5,412 measurement rows. These are distinct denominators within one project.

**MatPES license correction:** the current [Hugging Face data card](https://huggingface.co/datasets/materialyze/matpes/blob/main/README.md) declares BSD-3-Clause, while the benchmark registry lists MIT. New frozen2025.1 cards retain this unresolved mismatch; a code license badge is insufficient evidence for the data.

## All46 rows

| Original row | Table structures/configurations | Table material denominator | Representation | Catalog mapping / resource |
|---|---:|---:|---|---|
| [WBM](https://matbench-discovery.materialsproject.org/data/wbm) | 256,963 | 215,488 | existing dataset | [WBM / Matbench Discovery stability test set](../../docs/catalog/property_benchmarks.md#wbm-matbench-discovery) |
| [MP 2022](https://matbench-discovery.materialsproject.org/data/mp-2022) | 154,718 | 154,718 | new dataset | [MP v2022.10.28](../../docs/catalog/bulk_computed.md#mp-frozen-2022) |
| [MPtrj](https://matbench-discovery.materialsproject.org/data/mptrj) | 1,580,395 | 145,923 | existing dataset | [Materials Project Trajectory (MPtrj)](../../docs/catalog/mlip_configurations.md#mptrj) |
| [MPF](https://matbench-discovery.materialsproject.org/data/mpf) | 188,349 | 62,783 | existing dataset | [MPF.2021.2.8](../../docs/catalog/mlip_configurations.md#mpf2021) |
| [MP Graphs](https://matbench-discovery.materialsproject.org/data/mp-graphs) | 133,420 | 133,420 | new dataset | [Graphs of MP 2019](../../docs/catalog/property_benchmarks.md#mp-graphs-2019) |
| [GNoME](https://matbench-discovery.materialsproject.org/data/gnome) | 89,000,000 | 6,000,000 | existing dataset | [GNoME released stable-materials set](../../docs/catalog/bulk_computed.md#gnome) |
| [MatterSim](https://matbench-discovery.materialsproject.org/data/mattersim) | 17,000,000 | Not reported | existing resource | [Resource](https://github.com/microsoft/mattersim/blob/main/MODEL_CARD.md) |
| [Alex](https://matbench-discovery.materialsproject.org/data/alex) | 30,497,628 | 3,100,000 | existing dataset | [Alexandria](../../docs/catalog/bulk_computed.md#alexandria) |
| [OMat24](https://matbench-discovery.materialsproject.org/data/omat24) | 100,824,585 | 3,227,606 | existing dataset | [Open Materials 2024 (OMat24)](../../docs/catalog/mlip_configurations.md#omat24) |
| [sAlex](https://matbench-discovery.materialsproject.org/data/salex) | 10,447,765 | 3,227,606 | existing dataset | [sAlex (OMat24 distribution)](../../docs/catalog/mlip_configurations.md#salex-omat24) |
| [sAlex Validation](https://matbench-discovery.materialsproject.org/data/salex-validation) | 553,218 | 170,905 | new dataset | [Subsampled Alexandria Validation Set](../../docs/catalog/mlip_configurations.md#salex-omat24-validation) |
| [OpenLAM](https://matbench-discovery.materialsproject.org/data/openlam) | 162,507,178 | Not reported | existing dataset | [OpenLAM TrainingSet](../../docs/catalog/mlip_configurations.md#openlam-training) |
| [COSMOSDataset](https://matbench-discovery.materialsproject.org/data/cosmosdataset) | 242,788,218 | Not reported | new dataset | [COSMOSDataset](../../docs/catalog/mlip_configurations.md#cosmos-sevennet-omni) |
| [OC20](https://matbench-discovery.materialsproject.org/data/oc20) | 133,934,018 | 11,500 | existing dataset | [Open Catalyst 2020 (OC20)](../../docs/catalog/surfaces_catalysis.md#oc20) |
| [NOMAD](https://matbench-discovery.materialsproject.org/data/nomad) | 19,111,098 | 4,335,728 | existing resource | [Resource](https://nomad-lab.eu/) |
| [AFLOW](https://matbench-discovery.materialsproject.org/data/aflow) | 3,530,330 | 3,530,330 | existing dataset | [AFLOW](../../docs/catalog/bulk_computed.md#aflow) |
| [OQMD](https://matbench-discovery.materialsproject.org/data/oqmd) | 1,226,781 | 1,226,781 | existing dataset | [OQMD](../../docs/catalog/bulk_computed.md#oqmd) |
| [MatPES PBE](https://matbench-discovery.materialsproject.org/data/matpes-pbe) | 434,712 | 110,317 | new dataset | [MatPES 2025.1 — PBE](../../docs/catalog/mlip_configurations.md#matpes-pbe-2025-1) |
| [MatPES r2SCAN](https://matbench-discovery.materialsproject.org/data/matpes-r2scan) | 387,897 | 89,719 | new dataset | [MatPES 2025.1 — r2SCAN](../../docs/catalog/mlip_configurations.md#matpes-r2scan-2025-1) |
| [MDR Phonon PBE](https://matbench-discovery.materialsproject.org/data/mdr-phonon-pbe) | 9,958 | 9,958 | new dataset | [MDR Phonon PBE](../../docs/catalog/property_benchmarks.md#mdr-phonon-pbe-recalculation) |
| [MDR-MP PBE ω_q](https://matbench-discovery.materialsproject.org/data/mdr-mp-pbe-ω-q) | 8,510 | 8,510 | new dataset | [PFT MDR-PBE phonon training subset](../../docs/catalog/property_benchmarks.md#pft-mdr-pbe-training) |
| [ELEMENTA](https://matbench-discovery.materialsproject.org/data/elementa) | 210,656,285 | 9,781,175 | existing dataset | [ELEMENTA public core release](../../docs/catalog/mlip_configurations.md#elementa-public) · [ELEMENTA Spin](../../docs/catalog/mlip_configurations.md#elementa-spin) |
| [SMAX](https://matbench-discovery.materialsproject.org/data/smax) | 1,693,386 | Not reported | new resource | [Resource](https://arxiv.org/abs/2602.23489) |
| [OC22](https://matbench-discovery.materialsproject.org/data/oc22) | 9,854,504 | 4,286 | existing dataset | [Open Catalyst 2022 (OC22)](../../docs/catalog/surfaces_catalysis.md#oc22) |
| [OC25](https://matbench-discovery.materialsproject.org/data/oc25) | 7,801,261 | Not reported | existing dataset | [Open Catalyst 2025 (OC25)](../../docs/catalog/surfaces_catalysis.md#oc25) |
| [ODAC23](https://matbench-discovery.materialsproject.org/data/odac23) | 38,983,748 | 8,412 | existing dataset | [Open Direct Air Capture 2023 (ODAC23)](../../docs/catalog/porous_frameworks.md#odac23) |
| [ODAC25](https://matbench-discovery.materialsproject.org/data/odac25) | 70,000,000 | 15,000 | existing dataset | [Open Direct Air Capture 2025 (ODAC25)](../../docs/catalog/porous_frameworks.md#odac25) |
| [OMol25](https://matbench-discovery.materialsproject.org/data/omol25) | 101,666,280 | Not reported | new resource | [Resource](https://github.com/facebookresearch/fairchem/blob/main/docs/molecules/datasets/omol25.md) |
| [OMol25 Electronic](https://matbench-discovery.materialsproject.org/data/omol25-electronic) | 4,000,000 | Not reported | new resource | [Resource](https://github.com/facebookresearch/fairchem/blob/main/docs/molecules/datasets/omol25_elec.md) |
| [OMC25](https://matbench-discovery.materialsproject.org/data/omc25) | 26,257,042 | 218,841 | existing dataset | [Open Molecular Crystals 2025 (OMC25)](../../docs/catalog/molecular_crystals.md#omc25) |
| [OPoly26](https://matbench-discovery.materialsproject.org/data/opoly26) | 6,570,542 | Not reported | new resource | [Resource](https://arxiv.org/abs/2512.23117) |
| [OC20-mAds](https://matbench-discovery.materialsproject.org/data/oc20-mads) | 21,804,758 | Not reported | new dataset | [Open Catalyst 2020 Multiple Adsorbates](../../docs/catalog/surfaces_catalysis.md#oc20-mads) |
| [OC20-Slabs](https://matbench-discovery.materialsproject.org/data/oc20-slabs) | 18,323,074 | Not reported | new dataset | [Open Catalyst 2020 Clean Slabs](../../docs/catalog/surfaces_catalysis.md#oc20-slabs) |
| [OC20-Dense](https://matbench-discovery.materialsproject.org/data/oc20-dense) | 85,658 | 833 | new dataset | [Open Catalyst 2020 Dense Adsorbate Sampling](../../docs/catalog/surfaces_catalysis.md#oc20-dense) |
| [OC20NEB](https://matbench-discovery.materialsproject.org/data/oc20neb) | 1,375,930 | 821 | new dataset | [Open Catalyst 2020 Nudged Elastic Band Benchmark](../../docs/catalog/surfaces_catalysis.md#oc20-neb) |
| [OCx24](https://matbench-discovery.materialsproject.org/data/ocx24) | Not reported | 19,406 | existing dataset | [Open Catalyst Experiments 2024 (OCx24) experimental data](../../docs/catalog/experimental_properties.md#ocx24-experimental) |
| [MAD](https://matbench-discovery.materialsproject.org/data/mad) | 95,595 | Not reported | new dataset | [Massive Atomic Diversity](../../docs/catalog/mlip_configurations.md#mad-original-2025) |
| [MAD-1.5](https://matbench-discovery.materialsproject.org/data/mad-1.5) | 216,803 | Not reported | existing dataset | [Massive Atomic Diversity (MAD-1.5)](../../docs/catalog/mlip_configurations.md#mad15) |
| [MAD-1.6](https://matbench-discovery.materialsproject.org/data/mad-1.6) | 362,646 | Not reported | existing dataset | [Massive Atomic Diversity (MAD-1.6)](../../docs/catalog/mlip_configurations.md#mad16) |
| [MP-ALOE](https://matbench-discovery.materialsproject.org/data/mp-aloe) | 909,792 | Not reported | existing dataset | [MP-ALOE](../../docs/catalog/mlip_configurations.md#mp-aloe) |
| [SPICE 2](https://matbench-discovery.materialsproject.org/data/spice-2) | 2,000,000 | Not reported | new resource | [Resource](https://github.com/openmm/spice-dataset) |
| [QMOF](https://matbench-discovery.materialsproject.org/data/qmof) | 20,372 | 20,372 | existing dataset | [Quantum MOF Database (QMOF)](../../docs/catalog/porous_frameworks.md#qmof) |
| [rMD17](https://matbench-discovery.materialsproject.org/data/rmd17) | 999,988 | 10 | new resource | [Resource](https://figshare.com/articles/dataset/Revised_MD17_dataset_rMD17_/12672038) |
| [JARVIS-DFT](https://matbench-discovery.materialsproject.org/data/jarvis-dft) | 75,993 | 75,993 | existing dataset | [JARVIS-DFT 3D](../../docs/catalog/bulk_computed.md#jarvis-dft-3d) |
| [ANI-1x](https://matbench-discovery.materialsproject.org/data/ani-1x) | 5,000,000 | 64,000 | new resource | [Resource](https://github.com/aiqm/ANI1x_datasets) |
| [QM9](https://matbench-discovery.materialsproject.org/data/qm9) | 133,885 | 133,885 | new resource | [Resource](https://springernature.figshare.com/collections/Quantum_chemistry_structures_and_properties_of_134_kilo_molecules/978904) |

## Verification and limits

The page HTML and the exact GitHub metadata revision are hashed in receipts. Selected original provider guides and release APIs confirm data roles, licenses, schemas and release distinctions. The MDR-PBE directory was recounted by filename; no large training corpus was downloaded or independently deduplicated. Numerical values for the other additions are retained as provider/benchmark reports, not claimed as MatVerse row recounts.

Two failed/irrelevant exploratory routes are recorded honestly: a guessed root data-files.yml was 404, and a guessed PFT paper identifier was unrelated and excluded. The correct PFT paper 2601.07742 was established from the primary Figshare deposit. An attempted Figshare file API returned a payload; the read was bounded to 2 MB and was not used as metadata or a count. Nature article responses returned only challenge-sized HTML and are not used as fulltext evidence.

[Audit JSON](audit.json) · [Prepared dataset records](additions.json) · [Prepared resources](resources.json) · [Fetch receipts](receipts.json) · [MDR-PBEfilename count](mdr_directory_count.json) · [Full 46-row searchable inventory](../collection_matbench_discovery_20261101.json)

All edits remain local.
