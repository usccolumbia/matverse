# Hennig superconductivity dataset audit

Verified 2026-11-01. Four proposed catalog records: three direct Hennig releases and one explicitly attributed upstream archive reused by BEE-NET. Canonical datasets/resources and UI were not edited.

## Release and denominator findings

| Release | Catalog denominator | Scientific scope | Public access |
|---|---:|---|---|
| BETE-NET | 806 released CIFs / composition rows | Computed EPC and Tc; paper describes 818 accepted materials | Database and CIFs public; Apache-2.0 repository declaration |
| BEE-NET | 5,241 public CIFs | Ambient-pressure structures and splits; targets are upstream computed values | Structure/split release; full target JSON and model files absent |
| Hennig–Xie 2021 archive / 2022 paper | 3,046 rows in five CSVs | Synthetic plus physical Eliashberg cases, resampling and comparison baseline | Small actual data-table ZIP; archive Apache-2.0 |
| Cerqueira upstream | Approximately 7,000 model-data calculations | Broader archive and paper include more total EPC calculations | Open batch archives; CC BY 4.0 |

The [BETE-NET paper](https://doi.org/10.1038/s41524-024-01475-4) reports 818 dynamically stable materials. Its [pinned release](https://github.com/henniggroup/BETE-NET/tree/56bc783908a60e8a15e31b60018e6f3c3e48f593) contains 806 CIFs; the complete `comp` JSON column independently has 806 keys. This mismatch is retained rather than reconciled by assumption. Training/test files contain 651/173 labels; 18 labels do not occur among current JSON row labels. This is a version-matching warning, not a demonstrated model-reproduction failure.

The [BEE-NET README](https://raw.githubusercontent.com/henniggroup/BEE-NET/f21c260a9117830f2d74f2c5ac844ab671c0c606/README.md) explicitly says `database.json` and model ensembles are not tracked. Public tree enumeration confirms 5,241 CIFs and no target JSON; GitHub Releases is empty. Its 4,192/1,049 split is documented by the authors. This record covers public structures and splits, not a verified complete ready-to-train download. [Paper](https://doi.org/10.1038/s41524-026-01964-8).

The [2021 Hennig–Xie archive](https://archive.materialscloud.org/records/skdzy-kyx54) contains real numerical CSVs, not merely a model repository. Direct row counts: `data_artificial.csv` 2,819; `data_calculated.csv` 30; `data_literature.csv` 149; `data_hydrides.csv` 19; `data_AD29.csv` 29. Total 3,046, or 3,017 excluding the overlapping 29-row comparison table. The paper's 2,874 spectral cases instead comprise 55 physical cases and 2,819 artificial ones. The 55 physical cases comprise 13 calculated, 29 classic literature and 13 hydride cases. Resampling the Coulomb pseudopotential expands numerical rows. [2022 paper](https://doi.org/10.1038/s41524-021-00666-7).

The [earlier analytical-form paper](https://doi.org/10.1103/PhysRevB.100.174513) was published in 2019. The accessible 2021 archive includes an Allen–Dynes comparison table; no separate 2018 public release was verified. It is retained within the related benchmark record rather than duplicated as an independent crystal corpus.

## Tc, pressure and validation boundaries

BETE-NET and BEE-NET predict conventional electron–phonon quantities. Their ML targets are DFT/spectral-theory estimates, not measured Tc. Experimental confirmation of two BEE workflow examples does not establish experimental superconductivity for its full structural training set. BEE's [author preprint](https://arxiv.org/html/2503.20005v1) states ambient-pressure training and a 100 meV spectral ceiling; high-pressure hydrides are outside that stated domain. A pressure-resolved metadata field was not verified in the inspected BETE release.

For the Hennig–Xie benchmark, 13 hydride cases yield 19 rows; those theoretical targets and pressure contexts come from referenced calculations. The public tables do not preserve a uniform pressure field or full atomic structures. They should not be advertised as a comprehensive high-pressure hydride structure database.

The [Cerqueira archive](https://archive.materialscloud.org/records/3kbt5-r3n56) is authored by Cerqueira, Sanna and Marques. BEE reuses a subset. Its [paper](https://doi.org/10.1002/adma.202307085) reports over 8,250 ab initio EPC calculations and a 191,528-candidate ML screen; neither number equals BEE's public structure count. Archive description approximately 7,000 is a model-data denominator. Large archive payloads were not downloaded.

## Attribution and exclusions

- SuperBand, JARVIS 3D/2D, 3DSC and MDR SuperCon were checked against canonical data and not duplicated.
- [Superhydra](https://doi.org/10.1103/PhysRevMaterials.7.054806) is a Saha/Di Cataldo/Giannessi/Cucciari/von der Linden/Boeri project, not a Hennig release. Its paper distinguishes 880 hypothetical structures at 200 GPa from a 139-member superconductivity subset. It is contextual hydride coverage and was not misattributed or added here.
- Screening pools, predicted positive hits, experimentally synthesized examples, bootstrap draws and unique release structures are distinct quantities.
- Article licences are separate from repository/deposit data licences. BETE repository declares Apache-2.0. BEE had no licence file in the audited tree. Materials Cloud API explicitly records Apache-2.0 for Hennig–Xie and CC BY 4.0 for Cerqueira.

## Read-only verification receipts

Only the two requested research deliverables were written in this audit; no raw payload files were saved.

| Artifact | Immutable identifier / receipt | Audit |
|---|---|---|
| BETE Git commit | `56bc783908a60e8a15e31b60018e6f3c3e48f593` | Commit dated 2024-08-20; API tree `truncated=false` |
| BETE database blob | Git blob `81098b335be1e1bb1b3cce45d1c516701582810b` | 89,104,840 bytes declared; only first 262,144 bytes inspected; complete first `comp` field ends at byte position 11,408 and contains 806 keys |
| BETE CIFs | Same non-truncated tree | 806 `.cif` paths |
| BEE Git commit | `f21c260a9117830f2d74f2c5ac844ab671c0c606` | Commit dated 2026-10-05; API tree `truncated=false`; 5,241 `.cif` paths |
| Xie `data_tables.zip` | MD5 `86c68504d1780b6fc7eaccbd4116706c` | 429,059 bytes; digest matches published archive checksum; CSVs parsed in memory |
| Cerqueira README | Published MD5 `593fb5c38cb89d64380331107af19a5d` | Describes file contents; no multi-gigabyte batches retrieved |

Primary metadata APIs: [BETE tree](https://api.github.com/repos/henniggroup/BETE-NET/git/trees/56bc783908a60e8a15e31b60018e6f3c3e48f593?recursive=1), [BEE tree](https://api.github.com/repos/henniggroup/BEE-NET/git/trees/f21c260a9117830f2d74f2c5ac844ab671c0c606?recursive=1), [Hennig–Xie archive](https://archive.materialscloud.org/api/records/skdzy-kyx54), [Cerqueira archive](https://archive.materialscloud.org/api/records/3kbt5-r3n56).
