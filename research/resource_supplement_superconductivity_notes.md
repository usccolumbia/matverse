# Superconductivity resource supplement — verified 2026-11-01

Completed: one new dataset proposal (corrected CompSC), three reference resources, and corrections to existing SuperCon-derived records. Only the three requested supplement files were edited. Canonical data and UI were not changed.

## UCSD Superconducting Research Database

The [owning Schuller group announcement](https://ischuller.ucsd.edu/timeline-post/foundation-of-new-superconducting-research-database/) describes a community database of materials tested for superconductivity and invites researcher uploads to avoid repeated experiments. The [group news archive](https://ischuller.ucsd.edu/) dates the announcement to 13 March 2019. The [database](https://srd.physics.ucsd.edu/) has a search-indexed interface with Name, Structure and Transition filters.

Direct HTTP/HTTPS requests returned HTTP 500; the web reader timed out. Consequently, **current material count = unknown; tested count = unknown; negative count = unknown; untested count = unknown**. No public bulk export or actual coordinate payload was verified. A Structure filter alone does not establish downloadable periodic coordinates. Uploader eligibility beyond the general researcher invitation, account requirements, moderation, download authentication and redistribution license remain unverified. The group statement establishes tested-material intent; it does not establish exact positive/negative/untested status definitions or detection limits. Do not convert missing transitions or untested materials into confirmed negatives.

UCSD is retained as a database reference resource, without claiming a verified full-structure release. **UCSD SRD is unrelated to NIST Standard Reference Database 62.** No historical secondary-source count is promoted to a current primary-verified total.

## Supplied APS/ADS abstract belongs to Clark OSD

The supplied [ADS identifier 2021APS..MARX61003G](https://ui.adsabs.harvard.edu/abs/2021APS..MARX61003G/abstract) returned HTTP 405. Its corresponding [official APS session X61.00003](https://meetings.aps.org/Meeting/MAR21/Session/X61.3) is **“The Organic Superconductor Database,” Owen Ganter and Charles C. Agosta, Clark University**, presented 19 March 2021. This is **OSD, already cataloged**, rather than UCSD SRD.

The abstract describes low-dimensional organic crystals, molecular arrangement, tight-binding band structures derived from Gaussian09 transfer integrals, density of states, Fermi surfaces, and experimental measurements. It provides no material count or dataset license. The APS source can be appended to the existing `osd-organic-superconductors` record. It must not be used to support UCSD’s uploader, coordinate or count claims.

## ACS review: identity, access and coverage

Verified citation: Huan Tran, Hieu-Chi Dam, Christopher Kuenneth, Vu Ngoc Tuoc, and Hiori Kino, **“Superconductor Discovery in the Emerging Paradigm of Materials Informatics,” Chemistry of Materials 36(22), 10939–10966 (2024), DOI [10.1021/acs.chemmater.4c01757](https://doi.org/10.1021/acs.chemmater.4c01757)**. [Publisher metadata](https://pubs.acs.org/cmatex/article/36/22/10939/154808/Superconductor-Discovery-in-the-Emerging-Paradigm) and [Crossref’s publisher-deposited record](https://api.crossref.org/works/10.1021/acs.chemmater.4c01757) agree on publication online 8 November 2024; issue date is 26 November. Publisher license is CC BY 4.0. Direct ACS requests returned 403, but indexed publisher text was accessible. The [author-posted full manuscript](https://arxiv.org/html/2510.25971v1) was read; its [29 October 2025 posting](https://arxiv.org/abs/2510.25971) explicitly identifies the 2024 journal article. Posting year is not the journal publication year.

The review distinguishes composition-only data, approximate structure matching, computed electron–phonon targets and text-extraction corpora. It stresses data scarcity and the need for trustworthy labels, structures and physical conditions. Its Table 2 routes to SuperCon/MDR, Stanev, 3DSC, JARVIS EPC, Cerqueira, CompSC, SC-CoMIcs, SuperMat and SuperCon². All are covered by the current catalog except CompSC. The Stanev table is already represented by JARVIS supercon_chem. [Three author CSV files](https://github.com/huantd/matsdata/tree/main/papers/supercond_2024_01) support review figures and are reference artifacts, not an independent new corpus. Review counts are discovery leads, not substitutes for release-level audits.

## New addition: CompSC corrected public release

[Author repository](https://github.com/huantd/matsdata/tree/main/CompSC/202305), revision `ec5411ca41a0726cad01324609ed34940c9e20ab`, supplies CSV and a 93,842-byte POSCAR archive. The [author README](https://raw.githubusercontent.com/huantd/matsdata/ec5411ca41a0726cad01324609ed34940c9e20ab/CompSC/202305/README) explicitly corrects the original 587-structure corpus after removal of a duplicate in August 2024: **586 structures, 583 lambda labels, 566 omega_log labels**. Direct parsing independently confirms 586 CSV rows and 586 regular archive members. There are 272 distinct literal composition strings; structures at different pressures are distinct cases, not 586 unique formulas.

The [2023 primary paper](https://journals.aps.org/prmaterials/abstract/10.1103/PhysRevMaterials.7.054805) is Huan Tran and Tuoc N. Vu, “Machine-learning approach for discovery of conventional superconductors,” Physical Review Materials 7, 054805, published 31 May 2023. Its abstract refers to a 584-case modeling set; that is not the denominator of the corrected public structural release. Targets are literature-computed electron–phonon parameters. Tc is derived afterward; no experimental-Tc column is present in this release.

The released `pressure` column has 584 numeric cells, ranging 0–800; IDs 567/568 contain `270Pa.vasp` / `300Pa.vasp`. Preserve those malformed source strings and consult original references for units/repair. The review’s historical up-to-500-GPa wording should not be imposed on this file. Data license was not verified: the public repository has no license file. The review’s CC BY license does not automatically license CompSC.

Receipts from in-memory parsing; no data mirrors written:

| File | Bytes | SHA-256 |
|---|---:|---|
| CompSC README | 821 | `9c6dad6c372901dd7fc40560f0b2ab21a479011224f3cfae168bc15bd36ff4c0` |
| CompSC supercond_May23.csv | 441200 | `4f24d0c9fd6f806410d80b1e25d434fa443daa559cb8a7fe82793f100f705b38` |
| CompSC poscar.tgz | 93842 | `364d8389c2c0f90a8c861f6c5e10683ba783255c78848b7e487a2b9ec00579f7` |
| Author arXiv review HTML | 664638 | `680326c56a8935c4eb895609304886344bdd98285b272c7c37bb12b617cee448` |

## Existing-record correction: JARVIS / Stanev identity and zero labels

The [Stanev author README](https://raw.githubusercontent.com/vstanev1/Supercon/6e56e577b2239ebb6bebdcaeefc9ba470a3d5ce5/README.md) states that materials **without reported critical temperature are assigned Tc=0**. The [author CSV](https://raw.githubusercontent.com/vstanev1/Supercon/6e56e577b2239ebb6bebdcaeefc9ba470a3d5ce5/Supercon_data.csv) contains 16,414 data rows and 3,966 numerical zeros. Its two columns are `name` and `Tc`; there is no pressure, lower-temperature detection bound or coordinate field.

The official [JARVIS Figshare ZIP](https://ndownloader.figshare.com/files/40719260), linked by [deposit metadata](https://api.figshare.com/v2/articles/22975787), contains 16,414 objects. **The multiset of (formula, numerical Tc) pairs is identical to the author CSV**, with zero extra or missing pairs. Row order differs; JARVIS adds identifiers. Therefore, no separate Stanev dataset is added.

Proposed reframe for existing `jarvis-supercon-chem` (retain its id and Figshare data link):

- Name: **Stanev SuperCon subset / JARVIS supercon_chem composition–Tc benchmark**.
- Description: **SuperCon-derived 2018 author composition/Tc table, redistributed in JARVIS JSON format. Missing reported critical temperatures are encoded as zero; no atomic coordinates are included.**
- Version: retain **Figshare v1, 2023-05-20**, adding **upstream author table 2018, revision 6e56e577b2239ebb6bebdcaeefc9ba470a3d5ce5**.
- Provenance: **literature** (experimental measurements plus author-coded missing targets); properties should distinguish **reported critical temperature** from **zero-coded missing target**.
- Add author repository and README/CSV sources above. Keep the Figshare CC BY 4.0 statement explicitly scoped to the deposit; the upstream repository has no explicit license.
- Add caveat: **Tc=0 includes values assigned when critical temperature was unreported; these rows are not automatically confirmed experimental negatives. The zero-coded count is 3,966 in both author CSV and JARVIS JSON.**
- Keep the original cohort count 16,414 and state that both formats represent the same cohort. Neither 16,414 nor 3,966 is a count of distinct verified crystal structures or confirmed negative experiments.

Stanev receipts:

| File | Bytes | SHA-256 |
|---|---:|---|
| README.md | 385 | `4830a3d3b50c25aa02ad39d048bb4d64509bba65f85ffaac902d84eab6c6beeb` |
| Supercon_data.csv | 357918 | `b34a955cc59f7a1556bc92c4b9db559bfd634c03227b7e95337a2e5d69227dd6` |
| JARVIS supercon_chem.json.zip | 229014 | `14b7489822a1c25407cd6c83989dfca7f14263dfe6b5dc9f859969430c09e5b7` |

## Existing-record correction: inherited 3DSC zero-label semantics

The [primary 3DSC descriptor](https://pmc.ncbi.nlm.nih.gov/articles/PMC10663493/) explicitly states that its SuperCon parent is Stanev’s published GitHub subset. Its cleaning section retains 15,758 entries, calls 3,854 zeros non-superconductors, and uses zero as its operational encoding. Those are the 3DSC authors’ labels; the upstream README, however, says missing reported Tc is mapped to zero. The descriptor does not supply an entry-level audit establishing that every inherited zero represents a measured negative within a documented temperature range.

For both `3dsc-mp` and `3dsc-icsd`, replace **“Tc = 0 denotes tested nonsuperconducting entries in the source labels”** with:

> **The 3DSC authors operationally label Tc=0 entries as nonsuperconductors. Their Stanev parent table also assigns zero to unreported Tc; a zero alone therefore does not verify a tested negative or establish a lower-temperature detection bound.**

This qualifies evidence strength without claiming that all zeros are missing, or that none are genuine experimental negatives. It also does not change 3DSC’s reported counts or structure-matching results.

## NIST 62 is documentation of the existing WebHTS / SRD 62 family

The supplied [NIST publication](https://www.nist.gov/publications/nist-62-nistnrim-high-temperature-superconductors-database-version-20), **“NIST 62. NIST/NRIM High Temperature Superconductors Database: Version 2.0,” R. G. Munro, 16 October 2008**, describes evaluated superconducting, thermal, mechanical and crystallographic data from 1987–1996 papers. It has no dataset count or independent downloadable release. The [1999 WebHTS Version 2.0 publication](https://www.nist.gov/publications/nist-www-high-temperature-superconducting-materials-database-webhts-version-20) by E. F. Begley and R. G. Munro describes the same property-database family.

The [live NIST portal](https://srdata.nist.gov/CeramicDataPortal/hit) provides the decisive identity link: its Introduction calls it **WebHTS**, its heading and citation call it **NIST Standard Reference Database 62**, and its DOI is **10.18434/T4KP8J**. It says the last data-content update was **1996**. Retain the existing `nist-webhts-srd62` record; append the 2008 NIST publication as documentation. Publication/page dates 1999, 2008 and metadata year 2015 do not imply three independent experimental corpora. No material count or broad open redistribution license is inferred.
