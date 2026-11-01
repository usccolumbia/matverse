# Specialized functional and low-dimensional datasets: additional catalog audit

Checked 2026-11-01. This is a local staging package; no canonical catalog, UI, Git commit, or remote repository was changed by this pass.

## Abstract

The specialized search supports 13 additional release records. The strongest new coverage is the NIMS Heusler magnetic-material release family, C1DB periodic chains, relativistic monolayer spin transport, magnetic exchange/spectra, and a generated ferroelectric-search cohort. Direct payload inspection also recovers several older CMR semiconductor/optical campaigns that broad modern-database surveys can miss. Counts refer to explicit files, database rows, or provider compound denominators; they do not assert cross-catalog unique materials.

## Research questions and method

The parent [brief](../BRIEF.md) freezes RQ1 (missing datasets), RQ2 (domain, unit and lineage), and RQ3 (release, coordinates, access and rights). This pass applied the deep-research workflow in a catalog-audit form. Search perspectives were run serially: low-dimensional/provider discovery; specialized magnetic/electronic/optical campaigns; and adversarial verification of source lineage, counting units and licenses. The parent coordinated the broader domain searches; this agent did not spawn further agents.

The 304 baseline IDs/names were checked before promotion. Searches covered provider databases, primary papers, official repositories, Zenodo and Materials Cloud, not only Scientific Data. The 28 compact query receipts are in `query_receipts.json`. Raw HTML, API payloads, SQLite databases, spreadsheets and archives are confined to ignored `research/cache/additional_20261101/functional/`; their public source URLs, sizes and SHA-256 hashes are in `evidence_manifest.json` and fetch receipts. The browser/API routes are public and require no supplied credentials.

The verification ladder was: provider/project description; named public release route; independent metadata or payload check; explicit count denominator; and dataset-rights check. Article open access was never substituted for a dataset license.

## Verified release taxonomy

| Release | Ranked denominator | Independent check and interpretation |
|---|---:|---|
| DXMag ternary DFT Heuslers | 106,235 calculation rows | Complete public CSV independently counted; every row has cell, positions and atomic numbers. Provider 27,864-compound denominator and 18,792 literal composition strings remain separate. |
| DXMag quaternary ML Heuslers | 131,544 compounds | Separate dated CSV; `ML_cell`, energy, magnetic, phonon and anisotropy prediction columns checked. |
| DXMag all-d ML Heuslers | 105,763 compounds | Separate dated CSV; same predicted-label distinction; all-d refers to element family and can include binary/ternary chemistries. |
| C1DB current browser | 3,157 database rows | Live browser reports 3,144 found out of 3,157 total. A sample generated chain has a working coordinate-bearing CIF export. |
| CMR ABSe3 | 5,976 ASE rows | Downloaded SQLite `systems` table, with atomic-coordinate blobs on every row. |
| CMR A2BCX4 | 1,368 ASE rows | Same payload check; multiple crystal prototypes are separate rows. |
| CMR ABX2 | 123 ASE rows | Same payload check; band gaps, effective masses and stability labels. |
| CMR optical perovskites | 79 ASE rows | Same payload check; frequency-dependent spectra live within records and are not counted as extra materials. |
| CMR C2DM (2015) | 494 calculation rows | 216 distinct name/phase keys across PBE, LDA and GLLB-SC. This old GW campaign is distinct from the later C2DB release but strongly overlaps its chemistry. |
| Zhou–Poncé–Charlier 2D spin-Hall v2 | 426 monolayers | Independent released README confirms 210 metals plus 216 insulators, with coordinate-bearing QE input and Wannier-Hamiltonian files. |
| FerroGen generated cohort | 12,800 CIF files | Downloaded tar archive has exactly 12,800 regular `.cif` members; MD5 matches Zenodo. |
| MINT-ATLAS | 209 API structure records | Unfiltered `meta.data_available`; sample contains cells and site coordinates and advertises interaction/structure/HDF5 downloads with checksums. |
| Sufyan altermagnetic splitting | 171 ranked material records | Downloaded OOXML has 171 nonempty records in each of two sheets of the same cohort; second sheet is not added. |

`sqlite_counts.json` records the exact SQLite count queries' results and confirms populated coordinate/cell/element blobs. `altermagnet_counts.json` records nonempty worksheet denominators without copying record payloads.

## Cross-release findings and evidence limits

DXMag's DFT ternary calculations provide training/reference evidence for its ML-derived quaternary/all-d releases; unlike the DFT release, the two ML tables do not constitute new first-principles or experimental confirmation of their predicted magnetic properties. All three have explicit database CC BY 4.0 terms on the provider page. The full ternary CSV was downloaded and independently recounted: 106,235 UUID-distinct calculation rows with populated coordinate columns, and 18,792 distinct literal composition strings. The provider’s 27,864-compound denominator is not reconciled to these. Only the two ML-family CSVs use provider compound counts; 64 KiB HTTP-range samples verify their actual public structure/property columns.

C1DB extends coverage to periodic chains, whereas the existing C2DB and most cataloged low-dimensional resources emphasize sheets. Its live rows include parent-bulk, functional and generated-chain variants, so the current total cannot be read as 3,157 independent 1D materials. The historical 820-material paper count is a different denominator. The bulk `c1db.db` link returned 404; per-entry CIF export worked. The current search includes machine-generated entries absent from the original paper.

The CMR campaigns expose small, well-defined method-specific releases that large aggregate structure counts obscure. C2DM's 494 functional calculations are not 494 distinct monolayers, just as the optical perovskite spectra are not independently counted spectral points. Because the CMR index declares CC BY-SA 4.0 while its database-browser footers declare CC BY-NC 4.0, the six CMR/C1DB records conservatively use **Not verified** rights wording pending dataset-specific clarification.

The 426-monolayer spin-Hall release has a newer v2 (June 18, 2026), independently resolved from the old 2024 deposit. Its API explicitly says CC BY 4.0. The released README distinguishes the full Wannier cohort from detailed EPW/transport folders for selected materials; the record does not claim 426 complete EPC datasets. Its approximately 390 MiB main archive was not downloaded.

FerroGen's archive is a generated-structure cohort. It does not supply evidence that all 12,800 outputs are ferroelectric, stable, novel or experimentally realizable. The deposit itself, independently of the associated article, declares CC BY 4.0 through the Zenodo API.

MINT-ATLAS provides actual exchange parameters and magnetic spectra, unlike composition-only experimental transition-temperature tables. It compiles diverse calculations and uses periodic simulation cells even for lower-dimensional systems. Its mean-field temperature is explicitly a scalar-exchange q=0 estimate. The client has an MIT **software** license; a dataset license was not established, so the record remains **Not verified**. The live API's first response inconsistently labels `data_returned=209` for a one-entry page; the catalog uses `data_available=209` and discloses the anomaly.

The altermagnet release illustrates why paper counts need payload checks: its paper/current application discusses 180 materials, but the deposited ranked spreadsheet contains 171 rows per duplicate-cohort sheet. The broader candidate spreadsheet has 295 nonempty material rows (one extra styled/blank worksheet row was excluded). It is a MAGNDATA-derived property dataset, not 171 new parent structures. MAGNDATA/ICSD identifiers establish structure linkage; the small Zenodo deposit does not independently establish the release of all coordinates or raw DFT files claimed in its description. The deposit API declares CC BY 4.0.

## Open leads and stopping boundary

`leads.json` retains all 13 promoted records and 10 other dispositions. CPMDB and the NJU phonon-emergent-particle portal are promising chiral/topological-phonon expansions: public provider search pages work, but their independently verified release counts, coordinate exports and data rights remain unresolved. Novamag's Zenodo deposit is a mixed software/input package; its advertised full property-database count was not imported without inventorying that package. Further leads include bulk/2D spin-Hall screening, 1D exciton calculations, XTANT-3 coupling curves and other CMR projects.

Existing MAGNDATA/NEMAD/C2DB/ferroelectric/optical releases and parent JARVIS property slices were not treated as new independent corpora merely because another article or landing page was found. The search is broad and provenance-preserving, not an exhaustive claim about every specialized dataset. Deferred items are not counted as promoted records.

## Answers and validation

RQ1: 13 distinct release/property records are staged. RQ2: the additional coverage spans magnetic alloy families, chains, optical semiconductors, spin transport, magnetic interactions, generated ferroelectric candidates and altermagnetic bands, with parent lineage and count units explicit. RQ3: public release/provider evidence supports access and structure availability at the declared level; rights are verified only where deposit/provider terms establish them, and uncertain/conflicting rights remain marked.

Both JSON Schema validation and the existing `scripts/build_catalog.py:validate` function passed on the staged records plus all 304 baseline records. There are zero overlapping IDs. See `validation.json`. This invokes the project's validator without editing or regenerating canonical outputs. The parent can review/import `additions.json`; this agent performed no Git commit or push.

## Primary evidence routes

The `sources` arrays in `additions.json` provide claim-specific links, verification dates and evidence summaries. Especially useful audit anchors are the [NIMS provider](https://www.nims.go.jp/group/spintheory/database/), [CMR](https://cmr.fysik.dtu.dk/), [C1DB browser](https://cmrdb.fysik.dtu.dk/c1db/), [spin-Hall v2 metadata](https://archive.materialscloud.org/api/records/rfcdy-wcy32), [FerroGen deposit metadata](https://zenodo.org/api/records/17223175), [MINT structure API](https://mintatlas.org/optimade/v1/structures?page_limit=1) and [altermagnet deposit metadata](https://zenodo.org/api/records/19109715).
