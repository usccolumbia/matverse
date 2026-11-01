# JARVIS database coverage audit

Checked 2026-11-01. **All 13 homepage database rows, all 65 linked Figshare table entries and all 66 current downloader names are included.** The homepage numbers its rows 1–7 and 9–14; there is no row 8.

Before this audit, MatVerse covered selected JARVIS releases and the notebook collection, but not the complete database directory. The current inventory preserves every requested row and the linked download inventory. Seven additional ranked dataset releases fill major gaps; search tools, APIs, literature portals and alternate front ends remain resources.

[Search all JARVIS source entries](https://usccolumbia.github.io/matverse/?view=sources&collection=jarvis_databases) · [Inventory JSON](../research/collection_jarvis_databases.json) · [API access guide](api-access.md)

## Homepage Databases: complete crosswalk

| Original database row | Catalog / resource representation | Note |
|---|---|---|
| [1. JARVIS-DFT](https://jarvis.nist.gov/jarvisdft) | [JARVIS-DFT 3D](catalog/bulk_computed.md#jarvis-dft-3d) · [JARVIS-DFT 2D snapshot](catalog/two_dimensional.md#jarvis-2d) | Represented as a catalog release or explicitly identified navigation resource. |
| [2. JARVIS-FF](https://jarvis.nist.gov/jarvisff) | [JARVIS-FF classical force-field calculations](catalog/property_benchmarks.md#jarvis-ff) | Represented as a catalog release or explicitly identified navigation resource. |
| [3. JARVIS-QETB](https://jarvis.nist.gov/jarvisqetb) | [JARVIS-QETB / TB3PY DFT database](catalog/bulk_computed.md#jarvis-qetb) | Represented as a catalog release or explicitly identified navigation resource. |
| [4. JARVIS-ChemNLP](https://jarvis.nist.gov/jarvischemnlp) | [Resource](https://jarvis.nist.gov/jarvischemnlp) | Represented as a catalog release or explicitly identified navigation resource. |
| [5. JARVIS-Leaderboard](https://pages.nist.gov/jarvis_leaderboard/) | [Resource](https://pages.nist.gov/jarvis_leaderboard/) | Represented as a catalog release or explicitly identified navigation resource. |
| [6. JARVIS-Tools-Notebooks](https://github.com/JARVIS-Materials-Design/jarvis-tools-notebooks) | [Resource](https://github.com/JARVIS-Materials-Design/jarvis-tools-notebooks) | Represented as a catalog release or explicitly identified navigation resource. |
| [7. JARVIS-OPTIMADE](https://jarvis.nist.gov/optimade/jarvisdft/) | [Resource](https://jarvis.nist.gov/optimade/jarvisdft/) | Represented as a catalog release or explicitly identified navigation resource. |
| [9. JARVIS-SuperConDB](https://jarvis.nist.gov/supercon) | [JARVIS superconductivity 3D DFT cohort](catalog/property_benchmarks.md#jarvis-supercon-3d) · [JARVIS superconductivity 2D DFT cohort](catalog/property_benchmarks.md#jarvis-supercon-2d) · [Stanev SuperCon subset / JARVIS supercon_chem composition–Tc benchmark](catalog/experimental_properties.md#jarvis-supercon-chem) | Represented as a catalog release or explicitly identified navigation resource. |
| [10. JARVIS-InterfacDB](https://jarvis.nist.gov/interfacedb) | [JARVIS InterfacDB / InterMat interface release](catalog/surfaces_catalysis.md#jarvis-interfacedb) | Represented as a catalog release or explicitly identified navigation resource. |
| [11. JARVIS-Universal Search](https://jarvis.nist.gov/jarvisus) | [Resource](https://jarvis.nist.gov/jarvisus) | Represented as a catalog release or explicitly identified navigation resource. |
| [12. JARVIS-DMFT](https://jarvis.nist.gov/jarvisbdft) | [Resource](https://jarvis.nist.gov/jarvisbdft) | Represented as a catalog release or explicitly identified navigation resource. |
| [13. FigShare curated datasets](https://pages.nist.gov/jarvis/databases/) | [Resource](https://pages.nist.gov/jarvis/databases/) | Represented as a catalog release or explicitly identified navigation resource. |
| [14. JARVIS-DFT2](https://jarvis.nist.gov/jarvisdft2) | [JARVIS-DFT 3D](catalog/bulk_computed.md#jarvis-dft-3d) · [Resource](https://jarvis.nist.gov/jarvisdft2) | Alias of the DFT family; not counted again. |

## Figshare documentation: every named entry

The numbers below preserve documentation wording. They mix materials, configurations, property records, papers, files and Hamiltonians; they are not a size ranking or an additive crystal total. Third-party mirrors retain their source identities. “Inventory only” means the route is searchable and sourced, while that specific release has not been promoted to an independently checked ranked dataset card.

| Original name / download route | Documented data points | Catalog treatment |
|---|---:|---|
| [AGRA_CHO](https://figshare.com/ndownloader/files/41923275) | 214 | Inventory only; mirror / adjacent / release lead |
| [AGRA_COOH](https://figshare.com/ndownloader/files/41923281) | 280 | Inventory only; mirror / adjacent / release lead |
| [AGRA_CO](https://figshare.com/ndownloader/files/41923278) | 193 | Inventory only; mirror / adjacent / release lead |
| [AGRA_OH](https://figshare.com/ndownloader/files/41923287) | 875 | Inventory only; mirror / adjacent / release lead |
| [AGRA_O](https://figshare.com/ndownloader/files/41923284) | 1000 | Inventory only; mirror / adjacent / release lead |
| [aflow2](https://ndownloader.figshare.com/files/25453265) | 400k | Inventory only; mirror / adjacent / release lead |
| [alex_pbe_1d_all](https://figshare.com/ndownloader/files/49622991) | 100k | Inventory only; mirror / adjacent / release lead |
| [alex_pbe_2d_all](https://figshare.com/ndownloader/files/49622988) | 200k | Inventory only; mirror / adjacent / release lead |
| [alex_pbe_3d_all](https://figshare.com/ndownloader/files/49622946) | 5 million | Inventory only; mirror / adjacent / release lead |
| [alex_pbe_hull](https://figshare.com/ndownloader/files/49622718) | 116k | Inventory only; mirror / adjacent / release lead |
| [alex_pbesol_3d_all](https://figshare.com/ndownloader/files/49623096) | 500k | Inventory only; mirror / adjacent / release lead |
| [alex_scan_3d_all](https://figshare.com/ndownloader/files/49623090) | 500k | Inventory only; mirror / adjacent / release lead |
| [alignn_ff_db](https://ndownloader.figshare.com/files/38522315) | 307113 | [ALIGNN-FF training dataset](catalog/mlip_configurations.md#alignn-ff) |
| [arXiv](https://ndownloader.figshare.com/files/26804795) | 1796911 | Inventory only; mirror / adjacent / release lead |
| [arxiv_summary](https://figshare.com/ndownloader/files/40566137) | 137927 | Inventory only; mirror / adjacent / release lead |
| [c2db](https://ndownloader.figshare.com/files/28682010) | 3514 | [Computational 2D Materials Database (C2DB)](catalog/two_dimensional.md#c2db) |
| [cccbdb](https://figshare.com/ndownloader/files/47283808) | 1333 | Inventory only; mirror / adjacent / release lead |
| [cfid_3d](https://ndownloader.figshare.com/files/29205201) | 55723 | Inventory only; mirror / adjacent / release lead |
| [cod](https://ndownloader.figshare.com/files/28715301) | 431778 | [Crystallography Open Database (COD)](catalog/experimental_crystallography.md#cod) |
| [dft_2d_2021](https://ndownloader.figshare.com/files/26808917) | 1079 | Inventory only; mirror / adjacent / release lead |
| [dft_2d](https://ndownloader.figshare.com/files/38521268) | 1109 | [JARVIS-DFT 2D snapshot](catalog/two_dimensional.md#jarvis-2d) |
| [dft_3d_2021](https://ndownloader.figshare.com/files/29204826) | 55723 | Inventory only; mirror / adjacent / release lead |
| [dft_3d](https://ndownloader.figshare.com/files/38521619) | 75993 | [JARVIS-DFT 3D](catalog/bulk_computed.md#jarvis-dft-3d) |
| [edos_pdos](https://ndownloader.figshare.com/files/29216859) | 48469 | Inventory only; mirror / adjacent / release lead |
| [halide_peroskites](https://figshare.com/ndownloader/files/44619562) | 229 | Inventory only; mirror / adjacent / release lead |
| [hmof](https://figshare.com/ndownloader/files/30972655) | 137651 | [Wilmer hypothetical MOF database (hMOF)](catalog/porous_frameworks.md#hmof-wilmer) |
| [hopv](https://ndownloader.figshare.com/files/28814184) | 4855 | Inventory only; mirror / adjacent / release lead |
| [interfacedb](https://figshare.com/ndownloader/files/46355692) | 593 | [JARVIS InterfacDB / InterMat interface release](catalog/surfaces_catalysis.md#jarvis-interfacedb) |
| [jff](https://ndownloader.figshare.com/files/28937793) | 2538 | [JARVIS-FF classical force-field calculations](catalog/property_benchmarks.md#jarvis-ff) |
| [m3gnet_mpf_1.5mil](https://figshare.com/ndownloader/files/47281519) | 1.5 million | Inventory only; mirror / adjacent / release lead |
| [m3gnet_mpf](https://figshare.com/ndownloader/files/41009036) | 168k | Inventory only; mirror / adjacent / release lead |
| [megnet2](https://ndownloader.figshare.com/files/28332741) | 133k | Inventory only; mirror / adjacent / release lead |
| [megnet](https://ndownloader.figshare.com/files/26724977) | 69239 | Inventory only; mirror / adjacent / release lead |
| [mlearn](https://figshare.com/ndownloader/files/40357663) | 1730 | Inventory only; mirror / adjacent / release lead |
| [mp_3d_2020](https://ndownloader.figshare.com/files/26791259) | 127k | Inventory only; mirror / adjacent / release lead |
| [mp_3d](https://ndownloader.figshare.com/files/24979850) | 84k | Inventory only; mirror / adjacent / release lead |
| [mxene275](https://figshare.com/ndownloader/files/41266233) | 275 | Inventory only; mirror / adjacent / release lead |
| [ocp100k](https://figshare.com/ndownloader/files/40902845) | 149886 | Inventory only; mirror / adjacent / release lead |
| [ocp10k](https://figshare.com/ndownloader/files/40566122) | 59886 | Inventory only; mirror / adjacent / release lead |
| [ocp_all](https://figshare.com/ndownloader/files/40974599) | 510214 | Inventory only; mirror / adjacent / release lead |
| [omdb](https://ndownloader.figshare.com/files/28501761) | 12500 | [OMDB-GAP1](catalog/property_benchmarks.md#omdb-gap1) |
| [oqmd_3d_no_cfid](https://ndownloader.figshare.com/files/26790182) | 817636 | Inventory only; mirror / adjacent / release lead |
| [oqmd_3d](https://ndownloader.figshare.com/files/24981170) | 460k | Inventory only; mirror / adjacent / release lead |
| [pdbbind_core](https://ndownloader.figshare.com/files/28874802) | 195 | Inventory only; mirror / adjacent / release lead |
| [pdbbind](https://ndownloader.figshare.com/files/28816368) | 11189 | Inventory only; mirror / adjacent / release lead |
| [polymer_genome](https://ndownloader.figshare.com/files/26809907) | 1073 | Inventory only; mirror / adjacent / release lead |
| [qe_tb](https://ndownloader.figshare.com/files/29070555) | 829574 | [JARVIS-QETB / TB3PY DFT database](catalog/bulk_computed.md#jarvis-qetb) |
| [qm9_dgl](https://ndownloader.figshare.com/files/28541196) | 130829 | Inventory only; mirror / adjacent / release lead |
| [qm9_std_jctc](https://ndownloader.figshare.com/files/28715319) | 130829 | Inventory only; mirror / adjacent / release lead |
| [qmof](https://figshare.com/ndownloader/files/30972640) | 20425 | [Quantum MOF Database (QMOF)](catalog/porous_frameworks.md#qmof) |
| [raw_files](https://ndownloader.figshare.com/files/25295732) | 144895 | Inventory only; mirror / adjacent / release lead |
| [snumat](https://ndownloader.figshare.com/files/38521736) | 10481 | [SNUMAT hybrid-functional band-gap dataset](catalog/property_benchmarks.md#snumat-hybrid-gap) |
| [ssub](https://figshare.com/ndownloader/files/40084921) | 1726 | Inventory only; mirror / adjacent / release lead |
| [stm](https://github.com/usnistgov/jarvis/blob/3b0c9d0f0c15759135de857dbc93e010db01eb29/jarvis/db/figshare.py) | 1132 | [JARVIS-STM computational scanning-tunneling microscopy](catalog/diffraction_spectroscopy.md#jarvis-stm) |
| [supercon_2d](https://figshare.com/ndownloader/files/38950433) | 161 | [JARVIS superconductivity 2D DFT cohort](catalog/property_benchmarks.md#jarvis-supercon-2d) |
| [supercon_3d](https://figshare.com/ndownloader/files/38307921) | 1058 | [JARVIS superconductivity 3D DFT cohort](catalog/property_benchmarks.md#jarvis-supercon-3d) |
| [supercon_chem](https://figshare.com/ndownloader/files/40719260) | 16414 | [Stanev SuperCon subset / JARVIS supercon_chem composition–Tc benchmark](catalog/experimental_properties.md#jarvis-supercon-chem) |
| [surfacedb](https://figshare.com/ndownloader/files/46355689) | 607 | [JARVIS / InterMat surface release](catalog/surfaces_catalysis.md#jarvis-surfacedb) |
| [tinnet_N](https://figshare.com/ndownloader/files/40934285) | 329 | Inventory only; mirror / adjacent / release lead |
| [tinnet_OH](https://figshare.com/ndownloader/files/40978949) | 748 | Inventory only; mirror / adjacent / release lead |
| [tinnet_O](https://figshare.com/ndownloader/files/40978943) | 747 | Inventory only; mirror / adjacent / release lead |
| [twod_matpd](https://ndownloader.figshare.com/files/26789006) | 6351 | [2DMatPedia](catalog/two_dimensional.md#2dmatpedia) |
| [vacancydb](https://figshare.com/ndownloader/files/40750811) | 464 | [JARVIS vacancy formation-energy release](catalog/property_benchmarks.md#jarvis-vacancydb) |
| [wtbh_electron](https://github.com/usnistgov/jarvis/blob/3b0c9d0f0c15759135de857dbc93e010db01eb29/jarvis/db/figshare.py) | 1440 | [JARVIS-WTBH electron Hamiltonians](catalog/property_benchmarks.md#jarvis-wtbh-electron) |
| [wtbh_phonon](https://github.com/usnistgov/jarvis/blob/3b0c9d0f0c15759135de857dbc93e010db01eb29/jarvis/db/figshare.py) | 15502 | [JARVIS-WTBH phonon Hamiltonians](catalog/property_benchmarks.md#jarvis-wtbh-phonon) |

## Registry-only entries

These names occur in pinned `get_db_info()` but not in the documentation table. Progress-message numbers are not promoted to exact dataset counts.

- [qm9](https://ndownloader.figshare.com/files/27627596)
- [cord19](https://ndownloader.figshare.com/files/26804798)
- [foundry_ml_exp_bandgaps](https://figshare.com/ndownloader/files/40557743)
- [mag2d_chem](https://figshare.com/ndownloader/files/40720004)

## Access, versions and checks

- `stm`, `wtbh_electron` and `wtbh_phonon` have dedicated helpers. They are documentation entries but not current `data(name)` keys. Wannier helpers use `WANN` and `FD-ELAST` groups in `raw_files`.
- The selected `dft_3d` mirror is the December 2022 release with 75,993 documented entries. The homepage statistics show 77,096, descriptive text says 80,000+, and Figshare lists a newer September 2025 file. These sources do not identify one interchangeable release.
- The parsed interface archive contains 593 records; the selected vacancy archive contains 464. Other sizes are documentation-reported unless a dataset card states otherwise. Deposit metadata confirms CC BY 4.0 for QETB, FF, interface/surface and vacancy deposits. Hamiltonian payload rights remain unverified.
- JARVIS-DFT2 is an alternate route to the DFT family. Universal Search, ChemNLP, Leaderboard, Notebooks and OPTIMADE do not add independent crystal structure counts.
- Portal login requirements are distinct from public Figshare downloads. The JARVIS OPTIMADE probe returned JSON with an empty sample; this does not establish working structure retrieval.

## Source provenance

- [JARVIS homepage](https://jarvis.nist.gov/#Databases) and [Figshare documentation](https://pages.nist.gov/jarvis/databases/).
- [Pinned downloader](https://github.com/usnistgov/jarvis/blob/3b0c9d0f0c15759135de857dbc93e010db01eb29/jarvis/db/figshare.py), revision `3b0c9d0f0c15759135de857dbc93e010db01eb29`. Parsed as syntax; not executed.
- [Document response hashes](../research/provenance/jarvis_api_inputs_20261101.json)
- [Deposit metadata and file identities](../research/provenance/jarvis_release_metadata_20261101.json)
- [Provider discovery and bounded archive checks](../research/provenance/optimade_discovery_20261101.json)
- [Small API probe receipts](../research/provenance/api_probes_20261101.json)

[Back to MatVerse](../README.md)
