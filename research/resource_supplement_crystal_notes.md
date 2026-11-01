# Crystal platform and legacy-route supplement — 2026-11-01

Completed a bounded primary-source audit of CMR, OMDB, MaterialsWeb and the NIMS Inorganic Material Database, plus the requested legacy aliases. Deliverables contain **one named dataset addition** and **three missing portal resources**. Existing C2DB/2DHub cohorts, OMDB-GAP1, AtomWork/AtomWork-Adv, ICSD, CSD, AFLOW, JARVIS, NOMAD and MOFX-DB were checked for overlap and not duplicated. No canonical JSON, UI or publication files were edited.

## New record and platform coverage

- **OMDB COD predictions v1.1**: official table and the 2019 primary paper agree on **260,092** crystal prediction records. These are SOAP/kernel-ridge, SchNet and ensemble predictions for COD-derived organics, not an enlarged DFT training set. The 12,500-record OMDB-GAP1 dataset already exists. Download requires login; no payload recount or redistribution license was established. Structure linkage is conservative, because the current payload was not inspected.
- **CMR**: a portal of project ASE databases rather than one additional unique-crystal corpus. Its provider page supplies browse/download instructions and an OPTIMADE link, and expressly states **CC BY-SA 4.0** for CMR databases. Named 2DHub datasets are already represented; no child-family sum was invented.
- **OMDB**: add the portal for electronic and magnetic crystal data. Public pages remain accessible, but the browser is limited and downloads are gated by free registration. The browser reports a page-local “all 781 materials” message while historical literature describes much broader cohorts; neither number is promoted as a verified current full-family total. Magnetic-property content is advertised, but a new audited named magnetic bulk release/count was not established.
- **MaterialsWeb**: retain as a legacy portal resource with a current access-failure note. The provider lab still links 2D and bulk sections. The 2017 author paper reports 826 monolayers, with 681 below its comparison exfoliation-energy thresholds, and says structures were posted at MaterialsWeb. These historical cohort figures are not current site-wide totals. A current downloadable payload and rights were not verified, so this audit does not create a separately ranked MaterialsWeb dataset.
- **“NMIS Inorganic Materials Database”**: correct organization/name to **NIMS AtomWork**, already in the catalog. It is distinct from paid **AtomWork-Adv**.

## Existing-record evidence upgrades for parent integration

These are recommendations in notes, not canonical edits or additional datasets:

1. **`omdb-gap1`**: preserve v1.1 and 12,500 DFT-labelled crystals. The actual [download route](https://omdb.mathub.io/dataset/download/gap1_v1.1) currently redirects to [login](https://omdb.mathub.io/login), which offers free registration. Change access from `open` to `registration` (or explain mixed limited public browsing versus registered download). Keep license `Not verified`; [terms](https://omdb.mathub.io/page/terms) discuss quotas but not a general reuse license. Do not substitute a software or paper license.
2. **`atomwork`**: the [current provider homepage](https://crystdb.nims.go.jp/) itself still explicitly displays **82,000 crystal structures**, **55,000 property records**, and **15,000 phase diagrams**, and identifies the underlying data as **release 2010/06**. This upgrades the source from a secondary historical table, without changing the 82,000 value or claiming a new November data release. The page requires DICE/MatNavi registration, prohibits mass acquisition and scraping, and says reproduction/republication/third-party distribution requires written NIMS permission. Preserve registered access and note proprietary reuse limits. Prefer `https://crystdb.nims.go.jp/` as the direct dataset homepage; MatNavi is its platform parent.
3. **`atomwork-adv`**: the [provider service page](https://atomwork-adv.nims.go.jp/en/service.html?lan=en) directly corroborates **409,723 structures**, plus 746,888 XRD records, 568,195 property records and 49,650 phase diagrams. Preserve the verified structure count. The page identifies a paid license, **5,000 downloads/year**, and a **72-hour/1,000-page-view trial without downloads**. Trial access is not an open bulk release. These denominators are different units and must not be summed as materials.
4. **`c2db`**: the old CMR page explicitly says it moved to 2DHub. Existing canonical 2DHub routes are already appropriate; this does not create another C2DB record.
5. Existing ICSD, CSD, AFLOW, JARVIS and NOMAD counts remain unchanged. User-provided historical figures are not replacements for verified release-scoped counters.

## Original and current routes

All checks dated 2026-11-01. “Current” identifies observed provider routes, not guaranteed permanent availability. Session-bearing redirect values are deliberately omitted.

| Target | Original / historical route | Current route or observed behavior | Count/access interpretation |
| --- | --- | --- | --- |
| CMR | https://cmr.fysik.dtu.dk/ | Same portal, public | Project databases; no independent portal total. |
| CMR OPTIMADE | Linked from CMR | https://cmr-optimade.fysik.dtu.dk/ | Provider-listed API; endpoint payload/counters not audited. |
| C2DB | https://cmr.fysik.dtu.dk/c2db/c2db.html | Page announces move to https://2dhub.org/; current C2DB portal https://2dhub.org/c2db/c2db.html | Existing dataset, not a new release count. |
| OMDB | https://omdb.mathub.io/ | Same portal; https://omdb.mathub.io/dataset/ lists named releases | Limited anonymous browsing; registered downloads. |
| OMDB older branding | https://omdb.diracmaterials.org/ | Old address still mentioned in the OMDB About page; route itself not independently tested | Do not replace verified current mathub route from a stale textual link. |
| OMDB-GAP1 v1.1 | https://omdb.mathub.io/dataset/download/gap1_v1.1 | Redirects to https://omdb.mathub.io/login | 12,500 DFT-labelled structures; existing record. |
| OMDB COD predictions v1.1 | https://omdb.mathub.io/dataset/download/gap1-cod_v1.1 | Redirects to https://omdb.mathub.io/login | 260,092 model-predicted COD entries; proposed new derivative record. |
| MaterialsWeb | https://www.materialsweb.org/ and https://materialsweb.org/ | Both HTTPS hosts fail normal TLS access in this session | Current count, bulk availability and rights unknown. |
| MaterialsWeb 2D | https://materialsweb.org/twodmaterials | Lab-provider link remains; web fetch times out | Historical 826-monolayer paper cohort only. |
| MaterialsWeb bulk | https://materialsweb.org/bulkmaterials | Lab-provider link remains; web fetch fails | No bulk size adopted. |
| AtomWork | https://crystdb.nims.go.jp/en/ | Redirects to https://crystdb.nims.go.jp/ | NIMS registered service, 82,000 displayed structures from legacy release. |
| AtomWork-Adv | https://atomwork-adv.nims.go.jp/ | https://atomwork-adv.nims.go.jp/en/service.html?lan=en | Separate paid product; 409,723 structures, download quota. |
| ICSD search | https://icsd.fiz-karlsruhe.de/ | ICSD Web login at same host; version 5.7.0, Data Release 2026.2 displayed | Keep existing licensed ICSD record; do not store generated session IDs. |
| ICSD product description | Existing https://icsd.products.fiz-karlsruhe.de/en | Current catalog provider route retained | No new numeric claim from login page. |
| CSD old component | https://www.ccdc.cam.ac.uk/solutions/csd-system/components/csd/ | Redirects to https://www.ccdc.cam.ac.uk/solutions/software/csd/ | Existing CSD product route is already current. |
| CSD/ICSD individual access | https://www.ccdc.cam.ac.uk/structures/ | Current Access Structures service | Free individual viewing/retrieval; advanced curated CSD-Core and ICSD access requires licenses. |
| AFLOWlib | https://aflowlib.org/ | Both it and https://aflow.org/ return identical homepage HTML; neither redirected during the check | Treat as a coexisting legacy alias, not a separate database. |
| JARVIS old JVASP | https://www.ctcms.nist.gov/~knc6/JVASP.html | Redirect target https://jarvis.nist.gov/login?next=/jarvisdft/ observed; final page inaccessible through web tool | Current front-end login does not invalidate separately verified public Figshare bulk releases. |
| JARVIS documentation/data list | https://pages.nist.gov/jarvis/ and https://pages.nist.gov/jarvis/databases/ | Public provider documentation and downloader routes | Existing dataset release counts stay version-scoped. |
| NOMAD old repository | https://repository.nomad-coe.eu/ | Redirects to https://nomad-lab.eu/nomad-lab/ | Repository/platform, not another dataset. |
| NOMAD “Open NOMAD” | Link on current NOMAD page | https://nomad-lab.eu/prod/v1/gui/search/entries then https://nomad-lab.eu/select-gui?destination=entries | GUI selection route; retain existing platform resource. |
| User MOFDB | https://mof.tech.northwestern.edu/ | Current page brands itself **MOFX DB**; https://mof.tech.northwestern.edu/databases lists bulk downloads | Same existing MOFX-DB portal; no duplicate record. |

## Additional primary-source receipts and cautions

- [CMR](https://cmr.fysik.dtu.dk/) and [2DHub](https://2dhub.org/) supply the repository relationship and CC BY-SA 4.0 statement.
- [OMDB official download table](https://omdb.mathub.io/dataset/) and [primary paper](https://doi.org/10.1002/qute.201900023) distinguish 12,500 training structures from 260,092 model predictions. No quoted current family total is substituted for these versioned releases.
- [Hennig lab resources](https://hennig.mse.ufl.edu/resources/) supplies exact MaterialsWeb 2D/bulk paths; the [author paper](https://arxiv.org/abs/1610.07673) supports historical 826/681 figures. Standard urllib checks of bare/www HTTP/HTTPS routes returned `TLSV1_UNRECOGNIZED_NAME`; certificate checks were not bypassed.
- [AtomWork](https://crystdb.nims.go.jp/) supplies base-service counts, data release, registration and copyright limits; [AtomWork-Adv service](https://atomwork-adv.nims.go.jp/en/service.html?lan=en) supplies its separate counts and paid/trial limits. No database records were scraped.
- [CCDC Access Structures](https://www.ccdc.cam.ac.uk/structures/) explicitly separates free individual retrieval from advanced licensed access; individual access is not a bulk redistribution license.
- AFLOW bare homepages each returned HTTP 200 and 2,025 bytes, SHA-256 `fc4c10e6771f25c3581ce8959ac42796a91eecacbf884654106f8a4596525500`. This supports alias equivalence for the inspected homepage only, not identical release histories.
- [MOFX-DB downloads](https://mof.tech.northwestern.edu/databases) advertises CIFs plus isotherms for CoREMOF 2014/2019, hMOF, IZA, PCOD-syn and ToBaCCo. Current page version is `dc8a0295db`. These source families already overlap catalog records; adsorption condition rows and unique frameworks must remain separate. The site footer's image CC BY 3.0 credit is not a dataset license.

The extraction boundary was the named entrypoints, their immediate provider pages/download links, the requested alias routes and the cited author paper. The audit did not recursively enumerate CMR projects or retrieve gated datasets.
