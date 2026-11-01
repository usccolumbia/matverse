# Specialized superconductivity audit — 2026-11-01

Completed ten dataset proposals and four existing-entry correction proposals. Only the three assigned research outputs were edited; canonical data and UI were left to the parent agent. Primary author repositories, data deposits, NIST documentation, archive metadata and author papers support these proposals. Cached raw responses remain under the ignored `research/cache/superconductivity-specialized/` directory; no full articles are mirrored in these tracked outputs.

## Follow-up correction

The original zero-Tc interpretation in the accompanying correction-proposal snapshot is superseded by the [later primary-source audit](resource_supplement_superconductivity_notes.md). The Stanev author maps unreported Tc to zero; the canonical catalog now qualifies inherited zero labels. The original proposal JSON remains a historical audit artifact.

## Integration format

`superconductivity_specialized_additions.json` is an array of full canonical dataset records. `superconductivity_existing_corrections.json` is a dictionary keyed by canonical ID; each value contains replacement field values suitable for a shallow update of the existing record. Existing source and caveat lists were retained and extended. Main counts and names were deliberately omitted from corrections, so the parent agent's naming/tag changes can be retained.

| Proposed family | Selected count | Unit and evidence boundary |
| --- | ---: | --- |
| MC3D superconductivity | 4,533 | Initial metal structures; current archive version 4 additionally has nested 250 isotropic and 140 anisotropic Eliashberg subsets. |
| Sampling conventional superconductors | ~7,000 | Approximate initial electron–phonon calculation cases, not the ~200,000 model-screened compounds. |
| Antiperovskite DFPT | 384 | Starting material calculation cases, including dynamically unstable structures. |
| Superhydra | 880 | Hypothetical binary-hydride structures; 139 calculated superconducting cases form a subset. |
| JARVIS high-pressure hydrides | >900 | Structure-pressure calculation cases from author paper v4, not unique compositions. |
| HTSC-2025 | 140 | Actual material keys with CIF text and Tc in official JSON; primarily compiled theoretical Tc. |
| SuperCon² | 18,943 | Cleaned v23.04.28 CSV rows; original v22.12.03 independently has 40,324 rows. |
| SuperMat | 1,305 | Public CSV 2.0 linked records; full copyrighted article corpus is not public. |
| SC-CoMIcs | 1,000 | Annotated abstracts, not compounds. |
| JARVIS supercon_chem | 16,414 | Independently parsed composition/Tc records; SuperCon-derived and composition-only. |

## Existing-entry findings

- **3DSC_MP**: preserve 5,773 structure matches and add 5,759 matched SuperCon composition/Tc labels as an additional count. Fourteen labels have two MP matches. Structures can be artificially doped proxies.
- **3DSC_ICSD**: preserve 86,490 matched structures and add 9,150 matched labels. The public CSV provides original ICSD identifiers and labels; reconstructing adapted coordinates requires licensed ICSD data. Multiple crystal measurements inflate structural matches, and the MP and ICSD cohorts overlap.
- **SuperBand**: retain 2,474 DFT band cases (1,362 superconductors plus 1,112 negatives). Independently counted 8,625 nonheader rows in the reference CSV, with 8,598 nonempty formulas and 27 blank formula fields. The reference catalogue is a different scope from the band-data cohort. Extreme-pressure hydrides can appear as catalogue references while being excluded from ambient-structure band calculations.
- **MDR SuperCon**: Ver.240322, its version-specific DOI, series DOI and CC BY 4.0 are corroborated by NIMS-registered DataCite metadata. Direct NIMS access timed out. Count remains null, and Ver.240322 is not represented as the latest release.

## Interpretation and overlap limits

DFPT/EPC and Eliashberg labels are calculated quantities. They are separate from measured transition temperatures and from model-only predictions. None of the high-pressure or generated cohorts establishes experimental discovery. HTSC-2025 mainly compiles calculated literature values. SuperCon², SuperMat and SC-CoMIcs are text-information datasets: record/document totals cannot be ranked as numbers of experimentally confirmed compounds. JARVIS supercon_chem is experimental-label data, but includes zero-Tc entries and reuses the SuperCon lineage.

Integration duplicate identified by the parent: `sampling-conventional-superconductors` is the same Materials Cloud release as canonical `cerqueira-conventional-epc` and should be merged into that single record, not added separately. The parent also independently added the 3DSC label denominators; deduplicate equivalent additional counts when applying patches.

No totals across these families are proposed. Structural families, source literature, compositions and pressure cases overlap; the MC3D property release is a subset of the broader MC3D family. High-pressure JARVIS also reuses candidate structures from JARVIS, 3DSC and earlier hydride work. Hennig data, UCI/WebHTS/OSD/IEEE and existing JARVIS 3D/2D cohorts were assigned to other agents or already existed and were not duplicated here.

## License and access limits

Dataset-specific reuse rights remain **Not verified** for Superhydra and SuperCon². SC-CoMIcs deposit/abstract text is CC BY-NC 3.0; annotation-specific licensing was not independently verified. SuperMat publicly releases its CSV while withholding copyrighted full text. Materials Cloud deposits and the two cited JARVIS Figshare releases explicitly specify CC BY 4.0. ScienceDB V1 registrant metadata identifies MIT rights for HTSC-2025. Paper and software licenses were not substituted for unknown dataset licenses.

## Deferred candidates and bounded gaps

The following were inspected but not promoted: a Shipley/Needs high-pressure-hydride structure archive whose released subset was not recounted; an ambient-hydride screening paper whose ~150,000 figure is model screening; the HEX elemental high-pressure structural database without Tc labels; S2SNet without a fully audited dataset payload/license; and single-compound EPC/Hamiltonian deposits. A ternary-hydride literature workbook and large descriptor-screened ternary/quaternary composition pools also remain deferred. The latter are candidate enumerations, not measured or DFPT-validated Tc datasets. This audit does not claim exhaustive coverage of every superconductivity article or supplementary file.

## Small-file verification receipts

Counts were derived with Python CSV/JSON parsers excluding headers, without deduplicating or cleaning source rows. Relevant downloaded artifact SHA-256 hashes:

| Artifact | SHA-256 |
| --- | --- |
| SuperBand reference CSV | `0ab0d37a1dee14146b0d94daf4745df90d73122c6f34c3c2c7d65d8af57ccfb5` |
| SuperCon² cleaned CSV | `f7598571a59a35ae1ba281643f41f80248863f9e73e13b39e45659ea6170eb2d` |
| SuperCon² original CSV | `13a18935213c570bb06d1f7ba4aa209abe535b37eaae3c8dafa382b4bb8efc52` |
| SuperMat CSV 2.0 | `80e84ab67649a562a838c5a58fa8bb8025fe1e3225ad2eb664d9bcf3be8ed3ce` |
| HTSC-2025 JSON | `fba2681d115fcd131e0e09086bf0a271d6ecb5ef9e46f238be98d3faac0f92a3` |
| JARVIS supercon_chem ZIP | `14b7489822a1c25407cd6c83989dfca7f14263dfe6b5dc9f859969430c09e5b7` |

Official JARVIS documentation's `figshare.com/ndownloader` URL returned an empty response in this session; the deposit metadata's `ndownloader.figshare.com` download URL succeeded and yielded the expected 229,014-byte ZIP. This was a public endpoint change, with no login or access-control bypass.
