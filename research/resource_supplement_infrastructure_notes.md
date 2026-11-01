# Infrastructure and adjacent-polymer resource supplement

Audit date: 2026-11-01. Seven proposed new resources are in `resource_supplement_infrastructure_resources.json`. One full replacement record for an existing duplicate is in `resource_supplement_infrastructure_patches.json`. These are resource arrays using the existing canonical schema. No canonical data or UI files were edited.

## Scope and integration

- Add the seven new resources once each. These are directories, polymer properties, interatomic models, force-field parameters or curation tools; none adds a unique-crystal count.
- The user supplied CDCS twice. Both refer to one curation-software resource.
- Merge existing `Materials Data Facility` and `Materials Data Facility / Foundry` into the single replacement record. Their non-www and www homepage routes resolve to the same service and response. Do not append a third MDF record.
- Keep the existing `NIST Materials Data Repository` resource. The MGI directory, resource registry, data repository and CDCS software have different functions; this supplement does not create another copy of the data repository.
- Do not infer unrestricted reuse from publicly viewable data. No blanket data license was verified for OpenKIM, PPPDB or WebFF. PoLyInfo has explicit access and redistribution restrictions. The CDCS/MDCS software statement does not license data stored in individual deployments.

## Endpoint and access findings

| Resource | Primary route and observed state | Access / interpretation |
|---|---|---|
| NIST MGI directory | [Materials Data Resources](https://www.nist.gov/mgi/materials-data-resources), HTTP 200 | Public directory. Provider-specific access and terms. |
| Materials Resource Registry route | [materials.registry.nist.gov](https://materials.registry.nist.gov/) resolves to [MGI landing page](https://www.nist.gov/mgi), HTTP 200 | Redirect reproduced through independent fetch methods. No formal service-termination notice verified. Retained as a source route within the directory record. |
| OpenKIM | [About](https://openkim.org/about/), [model download instructions](https://openkim.org/doc/usage/obtaining-models/) and [query API](https://query.openkim.org/) accessible | Public model discovery/download/query documentation. Some web-extractor requests returned 444, while independent direct requests succeeded with HTTP 200; this is not evidence of service unavailability. Models and model predictions differ from DFT or experimental datasets. |
| PoLyInfo | [Canonical homepage](https://polymer.nims.go.jp/); supplied [/en/ route](https://polymer.nims.go.jp/en/) also returns PoLyInfo | DICE registration, email-domain eligibility and MatNavi application required. Bulk acquisition, including scraping, prohibited. Redistribution requires written NIMS permission. Separate paid-dataset service. Polymer chemical structures are not necessarily periodic atomic structures. |
| PPPDB | [HTTP route](http://pppdb.uchicago.edu/) upgrades to [HTTPS](https://pppdb.uchicago.edu/), HTTP 200 | Public chi, Tg and cloud-point tables inspected without login; no dataset-wide license found. Phase/property and chemical identity information does not establish atomic crystal structures. |
| WebFF | [Documentation](https://webff-documentation.readthedocs.io/en/latest/Introduction.html), HTTP 200 | Documents [exploration](https://webff.nist.gov/explore) and [curation](https://webff.nist.gov/curate); authorized account required for curation. Direct live-portal checks returned 502 for root/explore and 400 for curate. Availability of live data access remains unconfirmed; no end-of-service conclusion. |
| CDCS / MDCS | Supplied [older NIST path](https://www.nist.gov/itl/ssd/information-systems-group/configurable-data-curation-system-cdcs/about-cdcs) resolves to [current NIST path](https://www.nist.gov/itl/ai/applied-ai-research-group/configurable-data-curation-system-cdcs/about-cdcs) | Software infrastructure; deployment access and data licenses vary. [Official MDCS source](https://github.com/usnistgov/MDCS) and [software license](https://github.com/usnistgov/MDCS/blob/develop/LICENSE.md) verified. |
| PolymerDatabase.com | [Requested page](https://polymerdatabase.com/home.html), HTTP 200 | Hosting-provider temporary-unavailability page rather than data. [HTTP](http://polymerdatabase.com/home.html), [root](https://polymerdatabase.com/) and [www](https://www.polymerdatabase.com/home.html) variants had the same response hash. No formal end-of-service notice, original dataset terms or registration conditions verified. |
| MDF | [Non-www](https://materialsdatafacility.org/) redirects to [www](https://www.materialsdatafacility.org/), HTTP 200 | Same final body. [Foundry README](https://github.com/MLMI2-CSSI/foundry) independently verified; consolidate the two existing catalog resources. The inherited guide source is preserved in the patch but was not independently re-audited in this supplement. |

No numerical polymer, model, parameterization or property-table totals are promoted to crystal counts. Literature DOI references visible inside property tables also do not create independent dataset records.

## Response provenance

SHA-256 values below identify response bodies fetched during this audit. HTML can vary with server state; hashes establish the observed responses, not permanent content identity. Only public stable URLs are retained; no credentials or access-bearing signed URLs were recorded. Raw source pages are not embedded in these tracked outputs.

| Requested public URL | Final route / status when relevant | Response-body SHA-256 |
|---|---|---|
| https://www.nist.gov/mgi/materials-data-resources | HTTP 200 | `e0fc59ea1831c1a02501de909ce5a60e73615aad7d40b76cf4138b75c5313028` |
| https://materials.registry.nist.gov/ | https://www.nist.gov/mgi; HTTP 200 | `1bfa9fc8bb82f580e6788926c1f1f973a8be72c4e2c0db22063e87c2613fe2d5` |
| https://openkim.org/ | HTTP 200 direct fetch | `2adfa834e2212acba0abd4c64aac8b8d0a7260c52c69d2719cf82bd733b44d51` |
| https://openkim.org/about/ | HTTP 200 direct fetch | `383781548f4b8d3f982feb40c511b7e45fb6659b53879e29654cdc581500d429` |
| https://openkim.org/doc/usage/obtaining-models/ | HTTP 200 direct fetch | `7cb69ba015cbc39be7d29a8e1d0b90d78897319b5f0a3619af073141e4fc7070` |
| https://openkim.org/doc/schema/kimspec/ | HTTP 200 direct fetch | `89b5e0112f0e1af4687c56fc99d662054110387204dd4b46133f43ed10fe86aa` |
| https://polymer.nims.go.jp/en/ | HTTP 200 direct fetch | `3a6131d0af01a17e424976a056f29020302d0d9cc4ffbe20e2e07448e253b56f` |
| https://pppdb.uchicago.edu/ | HTTP 200 | `ad307b79dce66345528798f39eb577ecb8cd50c6c79b098ffaa9ed2583b6d407` |
| https://pppdb.uchicago.edu/chi | HTTP 200 | `07d441923488380db6a151489547fe7bf4e271fbbede103458e6eb465eb8a331` |
| https://pppdb.uchicago.edu/tg | HTTP 200 | `61bfa642dc878e18b798644b68fa688fff8c936081d8fe3c02f88fb2062cd17b` |
| https://pppdb.uchicago.edu/cloud_points | HTTP 200 | `477ad504f1973b53002ef8e0dd97587e03cb8023c18b84317425c86d0671326b` |
| https://webff-documentation.readthedocs.io/en/latest/Introduction.html | HTTP 200 | `47fcf109a76573ce1e9929ac63261f050e497c70f0d07d8fdcd96ccadc7386be` |
| https://www.nist.gov/itl/ssd/information-systems-group/configurable-data-curation-system-cdcs/cdcs-downloads | HTTP 200; links official software repositories | `811479319fb89529e1fb5ac5d9cfd076f21119544c23034a95c4232553b670df` |
| https://api.github.com/repos/usnistgov/MDCS/license | HTTP 200; API response identifies develop/LICENSE.md | `78d6ae4791b403db97766533974bf8bac7290eb27a9d26d9bf485e3c38a99ee1` |
| https://polymerdatabase.com/home.html | HTTP 200; hosting-provider page | `41a8d311437f6f9c55b29159974c4292212eb1d06ea64c3fde5c96039a08148c` |
| https://materialsdatafacility.org/ | https://www.materialsdatafacility.org/; HTTP 200 | `92cb5dde07d05760ab9d3716e4c022c996b4bd2052ab0e48dca2e0e3c763c6b5` |
| https://raw.githubusercontent.com/MLMI2-CSSI/foundry/main/README.md | HTTP 200 | `5244cf343f99aba56abeb5a154beefff6661c2b1df032e8fcf8c78cd0acfcd64` |

The public MDCS license API response was inspected for its actual content, rather than treating GitHub's generic license classification as authoritative. The NIST statement allows software reuse and redistribution with notice, change marking and acknowledgment conditions; third-party component licenses remain separate.
