# Defects, disorder and irradiation extension

Checked 2026-11-01. Twelve staged records; no canonical catalog edits, commits or pushes were performed by this worker. This is a scoped evidence report under the parent frozen brief, not an assertion that all defect data have been exhaustively discovered. Core Obsidian notes were read; the project index did not identify a dedicated MatVerse note. No memory was written.

## Method and research questions

RQ1 (missing releases) was investigated through serial point-defect, amorphous, grain-boundary/segregation, and irradiation perspectives. RQ2 (units and lineage) distinguishes parent compounds, sites/charge states, frames, final structures and simulation archives. RQ3 (release and rights) uses provider pages, live APIs, author repositories and primary papers; dataset rights remain separate from article rights. The deep-research skill was applied as a dataset-oriented investigation; perspectives ran serially in this delegated worker and no additional agents were spawned.

Search was broader than Scientific Data: primary APS, ACS, Acta Materialia, npj Computational Materials, IAEA, NIST, Mendeley Data, Zenodo, GitHub, RepOD, Materials Project and Fairdata sources. Compact reproducible query URLs are in queries.json. Bodies and payloads are confined to ignored research/cache/additional_20261101/defects/. receipts.json, oxygen_receipts.json, final_receipts.json, sample_receipts.json and quantum_example_receipt.json preserve response hashes and access outcomes. Failed or misidentified retrievals remain auditable and are not used as evidence (oxygen-paper was an unverified arXiv lead and nist-mras-paper was an unsuccessful speculative DOI lookup; neither informs promoted records).

## Evidence synthesis

| Branch | Promoted corpora | Independent denominator | Coordinate evidence |
|---|---|---|---|
| Point defects | Quantum Defects Database; Kumagai oxygen vacancies; OQMD-derived vacancy labels; chalcogenide reconstruction landscapes | >50,000 calculations; 937 host oxides; 2,677 site-property rows; ~130 defect types | Live quantum example supplies POSCAR; Kumagai release describes CIF/CONTCAR; OQMD CSV links entry IDs only; reconstruction release names POSCAR/CONTCAR/vasprun.xml |
| Amorphous | MP non-crystalline AIMD; NIST MRAS; amorphous alumina training | 5,120 5000 K parent systems; 50 final models; alumina frame count unknown | Provider structure/trajectory downloads; downloaded NIST archive inspected; author alumina XYZ tree |
| Grain boundaries | Homer 5D Al; elemental GBDB; solute interaction spectra | 7,304 minimized GB structures; 327 DFT GBs; ~200 binary systems | Homer truncated LAMMPS dumps; live Fe GBDB lattice/sites sampled; spectrum coordinates not established |
| Irradiation | IAEA CascadesDB; Fe–Ni–Cr release | 17,024 simulations; two sample configurations | XYZ simulation archives; RepOD LAMMPS positions/velocities/box metadata |

The defect datasets add labels beyond their parent Materials Project or OQMD crystals, whereas downstream alignment transformations of existing oxygen-vacancy data do not establish an independent corpus. The Homer release supplies one minimized structure per macroscopic GB, whereas the paper's 43,009,236 optimization trials measure computation and should not become the public release size. Similarly, MP's 5,120 systems cover 4,849 compositions, and CascadesDB's 320 archives hold 17,024 simulations; neither archive count nor trajectory frame count can be substituted for unique materials.

The strongest verified rights are CC BY 4.0 on Homer, segregation spectra, IAEA data/metadata, Kumagai data, OQMD-vacancy Zenodo metadata and RepOD files. NIST supplies its own Open License URL. Alumina's author README explicitly applies GPL v3 to the repository containing the data. Quantum defect rights, GBDB data rights and chalcogenide reconstruction rights remain Not verified. MPContribs shows CCA4, but file-level release terms were not independently confirmed, so the record retains that limitation.

## Direct count checks

- OQMD Data.csv SHA-256 is recorded in oxygen_receipts.json. It contains 2,677 data rows; pristine IDs include `_vN` site suffixes. Removing those suffixes yields 1,157 distinct pristine parents. Merely taking unique raw ID strings would incorrectly report 2,677 parent materials.
- Kumagai charge0/charge1/charge2 CSVs contain 1,745/1,689/1,613 rows respectively (5,047 total filtered labels); the ranked 937 count is host oxides reported by the primary paper. These are different scopes, not conflicting totals.
- NIST archive SHA-256 matches the publisher metadata value. Each of Si_Final, SiO2_Final, HfO2_Final, ZrCu_Final and Al2O3_Final has 10 CONTCAR files, yielding 50 final models. Another 240 CONTCAR files under Si_Base are exploratory settings and are excluded.
- Quantum Defects public Si query returned 400 entries. That is a query result count, not the live database total. Record c103 and its public structure-download route were verified. The 2023 paper's >50,000 calculation claim supplies the lower bound.
- A live GBDB Fe response includes ten GB records with lattice/site coordinates and properties alongside surface data. The ranked 327 is the documented publication cohort, not a current full enumeration.

## Open problems and limits

No external dataset was mirrored into the published catalog tree. Public web pages and selected small payloads were fetched for verification; large 20.7 GB defect and multi-GB trajectory releases were not downloaded. Unknown alumina frame count stays null. Separate nickel irradiation data may overlap CascadesDB, and downstream charged-defect alignment data may reuse Kumagai's oxygen corpus; both remain deferred. PRAM amorphous nanoporous materials was routed to the porous perspective. Parent agent owns broad GAP/ACE/MACE and atomistic-training releases, preventing cross-worker duplication.

Evidence-first answers to the brief: RQ1 yields twelve distinct candidate releases missing from the starting 304; RQ2 yields explicit non-additive units and parent lineage for every candidate; RQ3 has named public release routes for every promotion while leaving unverified licences and coordinate limits visible. A final curator should check cross-worker identifiers before merging.
