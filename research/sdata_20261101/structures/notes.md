# Scientific Data: structures and computational corpora

Status: **complete and stable for integration**, verified 2026-11-01. `additions.json` contains 24 schema-valid records; `leads.json` contains 69 scoped paper rows: 24 added, 29 existing, 16 deferred. Canonical catalog, application source and Git were not edited.

## Research questions and method

RQ1: Which Scientific Data releases provide reusable periodic crystal structures or atomistic calculations beyond the current catalog? RQ2: What does each reported size count, and which atomic structures are actually downloadable? RQ3: How do parent-database overlap, release versions and external data terms constrain reuse?

This perspective screened the centrally harvested complete journal metadata (`../journal_works.json`, 9,304 works through 2026-11-01) and its expanded title-keyword shortlist. Primary web discovery supplemented older `sdata.*` descriptors, MOF/framework collections, 2D/bilayer/MAX phases, alloys, charge-density corpora, crystal prediction and atomistic trajectories. No OpenAlex bulk calls were made. The journal census is complete at its metadata cutoff; title-based relevance screening and release verification are not a proof that every materials-related supplemental dataset was found.

Primary publisher full text was downloaded for scoped candidates, and release metadata was inspected on Figshare, Zenodo, Materials Cloud, Dryad, NOMAD, MPContribs and Dataverse. External data licences were read independently from article licences. Raw responses and downloaded payloads remain exclusively under `research/cache/sdata_structures/`; public receipts retain URLs, statuses, bytes and hashes. Unknown counts/licences remain explicit. No agents were spawned within this perspective.

## Coverage and comparison

The additions span 2016–2026 and address different data objects:

| Group | Added releases | Meaning of the principal count |
|---|---|---|
| Porous/experimental crystal derivatives | CRAFTED, MOFSimplify, AlPO | Parent MOFs, label-specific MOF subsets, or experimental CIF structures |
| Crystal prediction/reference | HEX, CAMD, multinary perovskites, historical PBEsol/SCAN cohort | Element-pressure cases, candidate configurations or functional-specific materials |
| Electronic-structure corpora | Layered intercalation, all-electron HSE06, MIP-3d, HOIP, PAH101, TBHubbard | Crystal/property records, molecular-crystal cases or Hamiltonian cases |
| Atomistic training/dynamics | Nb–Ta–V, Ti/Ti64, ElectroFace | Starting configurations, selected training frames or trajectory packages |
| Surfaces and 2D | Elemental surface energies, bimetallic adsorption, MAX precursors, BMDS, Si chain surfaces | Polymorphs, DFT calculations, bulk precursor configurations, bilayers or slab configurations |
| Charge-density layers | ECD-cubic, MP/pyrho | Density-bearing periodic records; MP live corpus count remains unknown |

Cu dislocation–grain-boundary interactions add a further periodic-defect benchmark (5,234 outcomes over 587 structures). This table describes coverage branches, not a sum of unique materials.

Unlike CAMD's many generated crystal candidates, the 175k PBEsol/SCAN cohort re-calculates a stable/metastable selection using matched functionals. Its two functional files represent the same materials. Similarly, the all-electron HSE06 collection adds a different electronic-structure reference layer without establishing novel chemical identities. The charge-density datasets add volumetric fields on existing MP structures; counting them as newly discovered crystals would be misleading.

The two MLIP configuration releases sample a different object from a crystal catalog. Ti/Ti64 includes crystalline and liquid configurations; Nb–Ta–V contains randomized arrangements at shared compositions and their relaxation steps. ElectroFace additionally mixes AIMD and MLMD. These sampling and provenance distinctions matter more than comparing raw row counts. PAH101 supplies higher-level GW+BSE labels for 101 periodic molecular crystals, whereas isolated-molecule datasets derived from crystal-forming compounds remain adjacent leads.

## Independent payload checks and version reconciliations

- **CRAFTED 1.1.1:** checksum verified; tar listing confirms 4,140 CIFs, 49,680 adsorption-isotherm CSVs and 49,680 adsorption-enthalpy CSVs for 690 parent MOFs. The generated data use **CDLA-Sharing-1.0**, CIFs use CC BY 4.0, and two RASPA force-field definitions use MIT. The article's CC BY licence is not substituted for these terms. [Release](https://doi.org/10.5281/zenodo.7689919).
- **AlPO v6:** checksum verified and ZIP independently contains 312 CIFs. [Release](https://doi.org/10.6084/m9.figshare.7822574.v6).
- **HEX:** the ZIP has 457 real CIFs: 228 GS, 228 EA and one MISS. A naive `.cif` filename count gives 914 because of macOS `._` resource forks. GS/EA overlap and pressure repeats are retained explicitly; main count is 228 element-pressure GS cases. [Release](https://doi.org/10.6084/m9.figshare.25403968.v1).
- **Ti/Ti64:** the two selected, checksum-verified training payloads contain 6,640 and 8,923 frames, total 15,563. Earlier April08 Ti64 files and model files are overlapping variants and are excluded from that sum. [Release](https://doi.org/10.5281/zenodo.15114121).
- **MIP-3d v7:** checksum-verified JSON has 33,078 `RECORDS`. The companion tar was also verified and includes VASP POSCAR inputs; it is not necessary to equate the 652,044 archive members with unique crystals. No one-to-one join of the coordinate files to every JSON row was performed. [Release](https://doi.org/10.6084/m9.figshare.13655276.v7).
- **ElectroFace:** publication says 69 trajectories; inspected Dataverse v4.1 lists 71 `.traj.zip` and 71 structure packages. Count is deliberately **71 trajectory archive packages**, not unique materials or trajectory frames. [Release](https://doi.org/10.12463/AI4EC/8NPZZC).
- **Cu dislocation/GB interactions:** final paper and archive 2025.65 report 5,234 interactions and 587 grain-boundary structures, superseding old 2024 counts of 5,593/449. The final release is included as an addition; neither the old nor new outcome count describes unique bulk materials. [Final archive](https://archive.materialscloud.org/record/2025.65).
- **2D spin splitting:** primary paper reports 358 spin-splitting-positive materials, while the archive's DataCite description reports 315; 436 screened candidates form yet another scope. This remains deferred pending archive-version reconciliation rather than selecting whichever counter is largest. [Paper](https://doi.org/10.1038/s41597-022-01292-8).

## Licensing, access and remaining limits

TBHubbard's deposit registration identifies **custom dataset terms** for Dataverse v4.1. Its custom-licence detail endpoint returned 403; it is not labelled CC0. PAH101 and the MP charge-density endpoint have no separately verified external data licence in this audit. These unknowns are retained in their catalog records. Dryad metadata confirms CC0 for elemental surface energies and HOIP, but attempted surface-payload download returned 401. Public metadata availability and successful payload retrieval are distinct facts.

MOFSimplify's 35.7 MB archive was inspected and contains no CIF files; it is classified `structure_linked`. Its 3,132 thermal-label and 2,179 solvent-removal subsets overlap, so they are not summed. BMDS release inventory confirms property CSVs, band/transport figures and prototype stacking-generation code; complete ready-made coordinates for every one of the 760 bilayers were not verified, so it is also `structure_linked`.

The MPContribs multinary-oxide provider displays “CCA4”; the catalog records that provider declaration while disclosing that the linked legal text was not exposed in the parsed page. Its 66,516 optimized records overlap MP, and only 59,708 remain perovskites after relaxation. The historical 175k PBEsol/SCAN cohort overlaps Alexandria-family and MP/AFLOW source structures. Neither is additive to parent crystal totals.

Large Nb–Ta–V, ECD, PAH101 and electronic-structure payloads were not downloaded in full. Sizes/units are anchored to primary descriptor and deposit inventories; selected small/medium payload counts are clearly distinguished from those declarations. No test of physical synthesis, finite-temperature stability or experimental performance was performed.

## Deferred release details and handoff

**Si(110)/Si(111) organic-chain slab configurations** are included with a lower bound of >700 configurations, Materials Cloud 2026.111/v6 and verified CC BY 4.0 terms; the slab model approximates nanowire facets. **Cu dislocation–grain-boundary interactions** are also included using the final 5,234-outcome release. **2D spin splitting** remains deferred because of the version/count discrepancy above. Their evidence is retained in cached primary responses and lead rows. Pure molecule/reaction corpora, nanoclusters and platform/method papers were not promoted as independent periodic crystal releases. Existing MAD versions, JARVIS-FF, 2DMatPedia, phonons, tensors and other canonical families are linked as existing.

`additions.json` has no ID collisions against the inspected 214-record canonical catalog and passes `data/dataset.schema.json`. `manifest.json` hashes compact staging artifacts. `primary_receipts*.json`, `provider_receipts*.json`, payload receipts and `article_metadata.json` preserve public provenance. Source bodies and full data stay in the ignored cache. Counts across this survey must not be summed into a unique-material total.
