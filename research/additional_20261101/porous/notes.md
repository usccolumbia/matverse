# Porous-material additions: evidence and overlap audit

Date: 2026-11-01. Scope: local staged research only. Nine complete canonical-schema records are in `additions.json`. No canonical data, application code, Git commits or pushes were changed by this pass.

## Research questions and method

The parent `BRIEF.md` fixes three questions: missing relevant releases, their independent counting units and lineage, and evidence for release/access/coordinates/rights. This pass applies the deep-research workflow to porous frameworks and adsorption. Perspectives ran serially within this delegated task: (1) major structural/pretraining collections, (2) experimental adsorption and stability evidence, (3) phonon/MLIP and transport-property releases, and (4) skeptical release/count/licensing audit. Primary sources include ACS/Nature/RSC papers, NIST provider pages, Figshare/Zenodo/Materials Cloud metadata, and author GitHub repositories; Scientific Data was not the exclusive search venue.

Core Obsidian memory notes were read. No matching MatVerse project note was found by a focused vault filename search. No memory writes were made. The existing 304-record catalog was inspected before promotion; existing CoRE, QMOF, ODAC, ARC-MOF, ReDD-COFFEE, CURATED, hMOF and other parent records were excluded as duplicates.

## Promoted evidence

| Release | Count unit and scope | Evidence type / qualification |
|---|---|---|
| PORMAKE for MOFTransformer | 1,118,074 hypothetical CIF structures | Exact Figshare v2 provider release count; CC BY 4.0; 9.49 GB archive not downloaded |
| MOFX-DB | 168,534 parent-database structure records | Live `databases.json` sum; API sample has CIF and 7 isotherms; aggregates existing parents |
| ToBaCCo | 13,511 valid hypothetical frameworks | MOFX subset; original 13,512 includes one empty/null structure; overlaps MOFX and selected QMOF parents |
| NIST-ISODB | 37,703 measured isotherms | Explicit historical 2023-12-01 provider snapshot; 8,265 material identities are a different count; no live total claimed |
| PhononMOFdb | 11,900 thermal YAML records / unique QMOF IDs | Independently counted in downloaded Thermal.zip after excluding resource forks; model-computed parent-linked properties |
| MACE-MP-MOF0 | 4,311 DFT configuration frames | Complete extXYZ records parsed in current v2 archive, not the article's 4,764 claim |
| Nanoporous heat capacity | 232 DFT-labelled structures | CSV rows counted; 31,420 model-prediction rows and 17,619 atomic-site rows retained as separate units |
| SymGNN zeolites | 57,084 substitution/property cases | NumPy headers parsed without loading pickles; 227 shared topology folders, occupancy and heat-of-adsorption arrays |
| ZeoDiff | 4,194 descriptor/diffusion rows | XLSX XML parsed; 4,194 unique first-column names; nested RAR of CIFs present but not decompressed |

The strongest structural expansion is the PORMAKE release; NIST supplies experimentally measured curves, while MOFX supplies simulation outputs. Heat-capacity/phonon/transport additions primarily add labels to known parent geometries. Their totals must not be interpreted as numbers of newly discovered compounds or added to their parent catalogs.

## Corrections earned by payload inspection

* MACE-MP-MOF0 downloadable v2 has **3,611 train + 331 valid + 369 test = 4,311** extXYZ frames. The final article reports 4,764 DFT points. The record scopes the directly verified payload and preserves the mismatch instead of silently adopting the larger number.
* PhononMOFdb contains **11,900** `.yml` thermal files and unique QMOF IDs, despite a rounded approximately 12,000 provider description. The ZIP also contains `__MACOSX` resource forks; counting all entries would double the apparent size.
* Moosavi heat capacity uses **232** released DFT rows; the paper's approximate 230 is a rounded overview. Model tables span five parent collections and can overlap; their 31,420 rows are neither 31,420 DFT measurements nor 31,420 globally unique structures.
* ACS Figshare 19633101 (`ie2c00561_si_002.xlsx`) contains one `correlation_raw` sheet with 1,594 rows including the header. Its first column lists **descriptor names**, and the body is a correlation matrix. It was **not** promoted as 1,593 MOF measurements.
* SymGNN's downloaded archive directly verifies heat-of-adsorption arrays and geometry; it does not justify claiming all full isotherms described by the paper are present. The record deliberately limits its properties.
* ZeoDiff's article mentions approximately 100,000 screened frameworks. The released spreadsheet independently verified here has 4,194 rows, so the larger screen is not used as the released dataset count.

## Rights/access audit

Dataset-level CC BY 4.0 is explicit for PORMAKE, PhononMOFdb, Materials Cloud heat capacity, SymGNN and ZeoDiff. MACE's folder license explicitly covers the data. MOFX/ToBaCCo downloads are public, but no universal reuse license was verified; the archive GitHub metadata has `license: null`. NIST metadata links generic government open-data terms, yet its actual homepage requests consultation about data licensing/reproduction and includes third-party digitized/contributed data. NIST is therefore conservatively marked **Not verified**, with both pieces of evidence preserved.

NIST's JavaScript-served homepage/API documentation were retrieved through their read-only page rendering POST routes; direct JSON calls returned 403. Its count remains a clearly dated historical snapshot. RSC direct article requests returned 403 after relevant primary-page search retrieval; Zenodo payload/metadata were independently downloaded. Some PMC HTTP-200 responses were CAPTCHA pages, and the raw-response receipts explicitly mark them as challenges rather than verified article content. No challenge page supplies a numerical claim.

## Deferred and excluded coverage

`leads.json` records unresolved releases, existing-parent duplicates and out-of-scope artifacts, including uMOF, Genomic MOF/COF, COF source-data studies, water stability and MOFinder. No unverified candidate was promoted merely to satisfy a quota. Experimental stability remains partly covered by the existing MOFSimplify record; newly found narrow studies are preserved for follow-up rather than represented as large general corpora.

## Reproducibility and validation

* `fetch_receipts.json`: source URLs, status/failure, local ignored raw-body path, byte count and SHA-256. Raw responses and downloaded payloads stay under `research/cache/additional_20261101/porous/`.
* `payload_inspection.json`: structured count/field checks derived from downloaded archive members, NumPy array headers, extXYZ frame boundaries and XLSX XML.
* `queries.json`: compact search perspectives, exact queries and reproducible search URLs.
* `validation.json`: validation outcome and SHA-256 for staged additions. `build_catalog.validate(existing + additions, [])` passed with all nine new IDs unique against the existing 304 records. This does not run or mutate the site's generator.

Coverage limits: no complete CIF enumeration for the 9.49 GB PORMAKE tarball; no decompression of nested ZeoDiff RAR; no complete PhononMOFdb DOS/band/INS archive enumeration; no successful current NIST API inventory. These limits are reflected in each record's scope and caveats.
