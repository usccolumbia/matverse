# Materials repository coverage audit

Checked 2026-11-01 against catalog `a9bb2ca`: 524 dataset records, 88 resources and 20 API routes.

Selected major materials repositories/databases plus adjacent OPTIMADE providers; not an exhaustive global registry or uptime audit. Dataset mappings are representative, not every child release.

## Finding

Coverage is substantial but incomplete. A source-list occurrence or an upstream citation is not a standalone searchable repository/dataset entry. Portals such as MDF appropriately belong in the resource view; individual deposits belong in the dataset view. The initial audit was read-only. The subsequent integration adds all 15 missing providers; see integration.json for exact new IDs and counts.

## Coverage matrix

Dataset mappings below are representative releases. A blank API cell means no dedicated MatVerse API card, not that the provider lacks an API.

| Repository / database | Main dataset IDs | Repository card | API card | Finding |
|---|---|---|---|---|
| NOMAD | nomad-bulk | Yes | nomad-native | Represented as a first-class entry |
| Materials Project | materials-project | — | mp-native, mp-optimade | Represented as a first-class entry |
| AFLOW | aflow | — | aflow-aflux, aflow-optimade | Represented as a first-class entry |
| OQMD | oqmd | — | oqmd-native, oqmd-optimade | Represented as a first-class entry |
| Alexandria | alexandria | — | alexandria-optimade | Represented as a first-class entry |
| JARVIS | jarvis-dft-3d, jarvis-qetb | Yes | jarvis-optimade, jarvis-sdk | Represented as a first-class entry |
| Materials Cloud | mc3d, mc2d | Yes | mcloud-optimade | Represented as a first-class entry |
| Materials Data Facility | — | Yes | mdf-sdk | Represented as a first-class entry |
| NIST Materials Data Repository | — | Yes | — | Represented as a first-class entry |
| DTU CMR / C2DB | c2db | Yes | cmr-optimade | Represented as a first-class entry |
| NIMS MatNavi / AtomWork | atomwork, atomwork-adv | Yes | — | Represented as a first-class entry |
| NIMS MDR | — | — | — | Source-list entry and selected MDR-hosted datasets exist; missing a standalone repository card. NIMS MDR is distinct from NIST MDR. |
| Materials Commons | — | — | — | No first-class dataset, repository or API record found; collaboration and data-publication repository. |
| MPContribs | — | — | — | Selected contributed datasets exist; missing a platform card and dedicated API route. |
| COD | cod | — | cod-optimade | Represented as a first-class entry |
| ICSD | icsd | — | — | Represented as a first-class entry |
| CSD | csd | — | — | Represented as a first-class entry |
| MPDS / PAULING FILE | mpds-pauling-file | — | mpds-native | Represented as a first-class entry |
| Pearson's Crystal Data | pearsons-crystal-data | — | — | Represented as a first-class entry |
| SpringerMaterials | — | Yes | — | Represented as a first-class entry |
| Organic Materials Database | omdb-gap1, omdb-cod-bandgap-predictions | Yes | — | Represented as a first-class entry |
| Open Materials Database | — | — | — | Source-entry-only provider; distinct from the Organic Materials Database (both use OMDB). |
| Matterverse | — | — | — | Source-entry-only provider. Official about page reports 31,791,192 ML-predicted materials; these are not experimental or DFT-validated discoveries. |
| TCOD | — | — | — | Source-list and upstream-property mentions only; missing standalone crystal database card. |
| odbx | — | — | — | Source-list and upstream-property mentions only; provider homepage could not be read by web tool in this audit. |
| PSDI | — | — | — | Provider source entry exists; missing discovery-infrastructure card. Do not treat its federated holdings as an independent additive corpus. |
| MPDD | — | — | — | Provider source entry exists; homepage could not be read by web tool. Registry evidence alone does not verify access or release size. |
| MatCloud | — | — | — | Listed in current OPTIMADE registry; no first-class MatVerse record found. Service availability and scope need verification. |
| MPOD | — | — | — | Listed in current OPTIMADE registry; no first-class record. Unrelated to SIMPOD powder diffraction dataset. |
| AtomGPT | — | — | — | Provider source entry and related JARVIS notebook links exist; no standalone database card. |
| Anyterial | — | — | — | Upstream MateriaViva property references exist; no standalone provider card. |
| HTEM | htem | — | — | Represented as a first-class entry |
| Carolina Materials Database | carolina | — | — | Represented as a first-class entry |
| NLR MatDB | nlr-matdb | — | — | Represented as a first-class entry |
| 2DMatPedia | 2dmatpedia | — | — | Represented as a first-class entry |
| Open Catalyst | oc20, oc22 | — | — | Represented as a first-class entry |
| Catalysis-Hub | — | Yes | — | Represented as a first-class entry |
| ColabFit Exchange | — | Yes | — | Represented as a first-class entry |
| OpenKIM | — | Yes | — | Represented as a first-class entry |
| Starrydata | starrydata2 | — | starrydata-bulk | Represented as a first-class entry |
| ULTERA | ultera-2025 | — | — | Represented as a first-class entry |
| NIST PhaseData | — | — | — | Source-list entry exists; no dedicated repository card. |
| NIST TRC Alloy Data | — | — | — | Source-list entry and a low-temperature dataset subset exist; no parent resource card. |

## Primary sources and evidence limits

- [Official OPTIMADE provider registry](https://www.optimade.org/providers/) and [machine-readable index](https://providers.optimade.org/v1/links); exact response retained beside this report. Registration can include reserved prefixes, tools, examples, and unavailable services. It is not proof of a live, complete dataset.
- [NIST materials data resources](https://www.nist.gov/mgi/materials-data-resources): parent repository, PhaseData and TRC Alloy Data descriptions.
- [NIMS MDR provider description](https://dice.nims.go.jp/services/MDR/en/): materials research data and publication repository, separate from MatNavi.
- [Materials Commons documentation](https://materialscommons.org/mcdocs2/index.html): collaborative research data platform.
- [MPContribs documentation](https://docs.materialsproject.org/services/mpcontribs): contributed computational and experimental data with its own API.
- [Matterverse provider description](https://matterverse.ai/about): ML-predicted materials, provider-reported count 31,791,192.
- [TCOD](https://www.crystallography.net/tcod/): theoretical crystal structures, provider-reported 362,294 entries and CC0 terms.
- [Open Materials Database](https://openmaterialsdb.se/): computational materials database, distinct from Organic Materials Database. Homepage count not available in parsed text.
- [PSDI](https://www.psdi.ac.uk/): physical sciences infrastructure and cross-data search.
- [Materials Cloud](https://www.materialscloud.org/): archive plus curated discover/explore databases.
- [MDF](https://www.materialsdatafacility.org/): publish, discover and access data.

## Priority for closing gaps

1. Add repository cards for NIMS MDR, Materials Commons and MPContribs, with dataset links and dedicated API verification where supported.
2. Add independently searchable dataset records for Matterverse, TCOD, Open Materials Database and odbx after verifying count units, access and reuse terms. Preserve ML-predicted versus computed/experimental provenance.
3. Add PSDI as a search infrastructure resource; evaluate MPDD, MPOD, MatCloud, AtomGPT and Anyterial individually.
4. Add parent resources for NIST PhaseData and TRC Alloy Data.
5. Reconcile the complete OPTIMADE registry periodically, excluding examples/software-only entries from dataset totals. Avoid asserting live API support from registry membership alone.

## Boundary

“All major repositories” has no fixed authoritative denominator. This selected roster is a gap audit, not a completeness certification. Commercial engineering handbooks and molecular/biological repositories outside the crystal-materials focus are not comprehensively audited. Individual deposits in broad archives (including Zenodo, Figshare and Hugging Face) require separate dataset-level review.

## Integration completed

All 15 gaps above now have repository cards. Eight named data collections were added to the main dataset search; 15 API/access records document samples, index-only routes, authentication or unsuccessful probes. Totals are 532 datasets, 103 resources and 35 API/access routes. API route count includes documented access routes and indexes, not 35 independently verified operational data APIs. Five repository/search tools were added.

The table above preserves the pre-integration audit. Refer to [integration.json](integration.json), [index-probes.json](index-probes.json), [sample-probes.json](sample-probes.json), and [extra-probes.json](extra-probes.json) for the integration and access evidence.
