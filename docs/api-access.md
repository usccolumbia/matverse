# API-accessible / Agent-ready data sources

Checked 2026-11-01. [Search the API directory](https://usccolumbia.github.io/matverse/?view=apis) · [Machine-readable route registry](../data/api_sources.json) · [JARVIS coverage audit](jarvis-coverage.md) · [All source links](../sources.md)

Here, **Agent-ready** means a documented path that software can use to search metadata, retrieve records or download structured files. It is an interface classification, not a certification of scientific quality, complete labels, schema uniformity, autonomous-use permission or unrestricted licensing. The 20 routes below distinguish remote query APIs from bulk SDKs and static downloads. Authentication and the observed verification level remain explicit.

## OPTIMADE: one standard across materials databases

**Try it in a browser:** [Materials Cloud OPTIMADE Client](https://optimadeclient.materialscloud.io/) · [Official OPTIMADE clients directory](https://www.optimade.org/clients).

The Materials Cloud client lets you choose a provider and a child database, filter structures, and inspect or download results. It queries a selected database at a time. The official clients directory also describes tools for searching across providers, including `optimade.science` and `optimade-python-tools`. These clients are access tools for existing databases; they do not add independent structure counts. [Official client comparison](https://www.optimade.org/clients).

### Providers visible in the supplied screenshot

The following 17 provider options are visible in your screenshot and matched to the official registry. Index links lead to provider directories, from which clients discover child database endpoints. This list records advertised providers; individual endpoint availability, authentication and API version still require checking. [Provider registry](https://providers.optimade.org/v1/links).

| Provider ID | Database / provider index |
|---|---|
| `alexandria` | [Alexandria](https://providers.optimade.org/index-metadbs/alexandria) |
| `cod` | [Crystallography Open Database](https://providers.optimade.org/index-metadbs/cod) |
| `cmr` | [Computational materials repository (CMR)](https://providers.optimade.org/index-metadbs/cmr) |
| `mcloud` | [Materials Cloud](https://www.materialscloud.org/optimade/main) |
| `mcloudarchive` | [Materials Cloud Archive](https://www.materialscloud.org/optimade/archive) |
| `mp` | [The Materials Project](https://providers.optimade.org/index-metadbs/mp) |
| `mpdd` | [Material-Property-Descriptor Database](https://providers.optimade.org/index-metadbs/mpdd) |
| `matterverse` | [Matterverse](https://providers.optimade.org/index-metadbs/matterverse) |
| `nmd` | [novel materials discovery (NOMAD)](https://providers.optimade.org/index-metadbs/nmd) |
| `odbx` | [open database of xtals](https://optimade-index.odbx.science) |
| `omdb` | [Open Materials Database](https://optimade-index.openmaterialsdb.se) |
| `oqmd` | [The Open Quantum Materials Database (OQMD)](https://providers.optimade.org/index-metadbs/oqmd) |
| `jarvis` | [Joint Automated Repository for Various Integrated Simulations (JARVIS)](https://providers.optimade.org/index-metadbs/jarvis) |
| `psdi` | [Physical Sciences Data Infrastructure (PSDI)](https://metadata.psdi.ac.uk/optimade-index-metadb) |
| `tcod` | [Theoretical Crystallography Open Database](https://providers.optimade.org/index-metadbs/tcod) |
| `twodmatpedia` | [2DMatpedia](https://providers.optimade.org/index-metadbs/twodmatpedia) |
| `atomgpt` | [AtomGPT.org](https://atomgpt.org/index/optimade) |

`matterverse` names the separate Matterverse database. `omdb` here names Open Materials Database, distinct from the Organic Materials Database at `omdb.mathub.io`. The screenshot is a snapshot; the [live provider registry](https://providers.optimade.org/) can change.

**OPTIMADE — Open Databases Integration for Materials Design** defines a common HTTP API, filter language and structure representation across participating providers. The consortium lists specification **v1.3.0 (December 2025)** as its latest release at this check. Individual servers may implement other compatible versions or only a subset of optional fields. [Consortium overview](https://www.optimade.org/), [specification](https://www.optimade.org/api-specification).

Start with the machine-readable [provider index](https://providers.optimade.org/v1/links), follow each provider's index `/links` to its child databases, then inspect the child's versioned `/info` and `/info/structures`. Query `/v1/structures` with `filter`, `response_fields` and `page_limit`, and follow the returned `links.next` for pagination. A provider index is a directory; it is not itself a structure database. [Registry documentation](https://providers.optimade.org/), [API specification](https://www.optimade.org/api-specification).

The standard describes chemical formulas, elements, lattice vectors, Cartesian site positions, species and periodic dimensions. Properties such as band gaps or critical temperatures may be provider extensions; their names, units and provenance still need inspection. OPTIMADE does not harmonize DFT functionals, remove duplicate structures, grant a data license or bypass authentication. [Specification](https://www.optimade.org/api-specification).

For example, this small COD query requests binary Si–O records and only a few fields. It is an illustrative standard query; the COD request timed out during this audit, while several other registered providers returned records.

```bash
curl --fail --get 'https://www.crystallography.net/cod/optimade/v1/structures' \
  --data-urlencode 'filter=elements HAS ALL "Si","O" AND nelements=2' \
  --data-urlencode 'response_fields=chemical_formula_descriptive,nelements' \
  --data-urlencode 'page_limit=1'
```

To request coordinates, include `lattice_vectors,cartesian_site_positions,species_at_sites,species,dimension_types` when supported. Keep provider IDs, query text, API/database versions and retrieval date with each result. A server's `meta.data_available` and matched-result count refer to its served subset; neither automatically replaces a separately versioned catalog count. [Official query example and field explanation](https://www.optimade.org/), [specification](https://www.optimade.org/api-specification).

## Access routes and observed verification

| Source / interface | Interface type | Authentication | Verification on 2026-11-01 |
|---|---|---|---|
| [JARVIS-DFT · OPTIMADE](#jarvis-optimade) | OPTIMADE | Anonymous public route | JSON response; empty sample |
| [Materials Project · OPTIMADE](#mp-optimade) | OPTIMADE | Anonymous public route | Small record sample verified |
| [OQMD · OPTIMADE](#oqmd-optimade) | OPTIMADE | Anonymous public route | Small record sample verified |
| [AFLOW · OPTIMADE](#aflow-optimade) | OPTIMADE | Anonymous public route | Small record sample verified |
| [Crystallography Open Database · OPTIMADE](#cod-optimade) | OPTIMADE | Anonymous public route | Probe unsuccessful |
| [Alexandria PBE · OPTIMADE](#alexandria-optimade) | OPTIMADE | Anonymous public route | Small record sample verified |
| [Materials Cloud MC3D PBE · OPTIMADE](#mcloud-optimade) | OPTIMADE | Anonymous public route | Small record sample verified |
| [DTU Computational Materials Repository · OPTIMADE](#cmr-optimade) | OPTIMADE | Anonymous public route | Probe unsuccessful |
| [Materials Project · native API](#mp-native) | Native API | API key | Authentication required |
| [OQMD · native REST API](#oqmd-native) | Native API | Anonymous public route | Small record sample verified |
| [AFLOW · AFLUX search API](#aflow-aflux) | Native API | Anonymous public route | Documented; not queried |
| [NOMAD · entries and archives API](#nomad-native) | Native API | Depends on operation or dataset | Small record sample verified |
| [MPDS / PAULING FILE · native API](#mpds-native) | Native API | API key | Documented; not queried |
| [JARVIS · Figshare bulk SDK](#jarvis-sdk) | Bulk SDK | Anonymous public route | Documented; not queried |
| [Materials Data Facility / Foundry · discovery SDK](#mdf-sdk) | Bulk SDK | Account / authorization | Documented; not queried |
| [Hugging Face · materials dataset Hub / SDK](#huggingface) | Bulk SDK | Depends on operation or dataset | Metadata response verified |
| [Figshare · deposits and file metadata API](#figshare) | Native API | Depends on operation or dataset | Metadata response verified |
| [Zenodo · records and files REST API](#zenodo) | Native API | Depends on operation or dataset | Metadata response verified |
| [Starrydata · published bulk files](#starrydata-bulk) | Bulk files | Anonymous public route | Documented; not queried |
| [NIST SRD 81 insulation measurement API](#nist-insulation) | Native API | Anonymous public route | Small record sample verified |

**Small record sample verified** means an unauthenticated bounded request returned at least one data record. **Metadata response verified** means only repository/deposit metadata was checked. An empty JSON response does not establish working record retrieval. Authentication failures, timeouts and unavailable registered endpoints are retained. **Documented; not queried** means official documentation was read, but the API, SDK or complete payload was not exercised. No keys or private accounts were used. [Probe receipts](../research/provenance/api_probes_20261101.json).

## Reproducible access examples

Materials Project's native API requires a key; its separately registered OPTIMADE endpoint returned a small public sample. The official client can obtain its key from `MP_API_KEY` in the environment:

```python
from mp_api.client import MPRester

with MPRester() as mpr:
    records = mpr.materials.summary.search(
        material_ids=["mp-149"], fields=["material_id", "structure"]
    )
```

This snippet follows the [official client documentation](https://docs.materialsproject.org/downloading-data/using-the-api/getting-started); authenticated execution was not tested here.

JARVIS's bulk SDK is a different access pattern:

```python
from jarvis.db.figshare import data

records = data("dft_3d")  # Downloads/loads a complete named release.
```

Use the [JARVIS audit](jarvis-coverage.md) to choose a named snapshot and distinguish special helper functions. This is not a remote filtered property query. Inspect the [pinned registry](../research/collection_jarvis_databases.json) before downloading large archives.

For an automated workflow, select the required structure/property scope, inspect authentication and reuse terms, pin the served release or file revision, request a small sample, then paginate or download with the provider's supported client. Preserve IDs, units, method provenance and file checksums alongside the data. Bulk files on Figshare, Zenodo or Hugging Face remain dataset-specific formats even when their metadata API is uniform.

<a id="jarvis-optimade"></a>
## JARVIS-DFT · OPTIMADE

Standard structure search and retrieval; provider-specific property fields and coverage vary.

**Interface:** OPTIMADE. **Entrypoint:** [https://jarvis.nist.gov/optimade/jarvisdft](https://jarvis.nist.gov/optimade/jarvisdft).

**Authentication:** Public route advertised by the provider registry; current availability is reported separately.

**Formats:** JSON:API-style JSON.

**Verification:** JSON response; empty sample (2026-11-01). json_response; returned 0 records.

Probe: [https://jarvis.nist.gov/optimade/jarvisdft/v1/structures?page_limit=1&response_fields=chemical_formula_descriptive%2Cnelements](<https://jarvis.nist.gov/optimade/jarvisdft/v1/structures?page_limit=1&response_fields=chemical_formula_descriptive%2Cnelements>); HTTP 200.

**Catalog coverage:** [JARVIS-DFT 3D](catalog/bulk_computed.md#jarvis-dft-3d) · [JARVIS-DFT 2D snapshot](catalog/two_dimensional.md#jarvis-2d)

**Limits and interpretation:**

- The small unauthenticated request returned JSON with zero entries; successful structure retrieval was not established. Web portal registration is a separate route.
- A listed endpoint is not a guarantee of uptime or full conformance. API counts may cover a different release or subset than the ranked catalog.

**Official evidence:**

- [Provider index: JARVIS-DFT](https://providers.optimade.org/index-metadbs/jarvis/v1/links) (checked 2026-11-01): Lists this child database base URL.
- [OPTIMADE specification](https://www.optimade.org/api-specification) (checked 2026-11-01): Defines common endpoints, structure attributes, filtering and pagination.

<a id="mp-optimade"></a>
## Materials Project · OPTIMADE

Standard structure search and retrieval; provider-specific property fields and coverage vary.

**Interface:** OPTIMADE. **Entrypoint:** [https://optimade.materialsproject.org](https://optimade.materialsproject.org).

**Authentication:** Public route advertised by the provider registry; current availability is reported separately.

**Formats:** JSON:API-style JSON.

**Verification:** Small record sample verified (2026-11-01). json_response; returned 1 records.

Probe: [https://optimade.materialsproject.org/v1/structures?page_limit=1&response_fields=chemical_formula_descriptive%2Cnelements](<https://optimade.materialsproject.org/v1/structures?page_limit=1&response_fields=chemical_formula_descriptive%2Cnelements>); HTTP 200.

**Catalog coverage:** [Materials Project](catalog/bulk_computed.md#materials-project)

**Limits and interpretation:**

- The OPTIMADE sample worked without credentials; the separate native Materials Project API requires an API key.
- A listed endpoint is not a guarantee of uptime or full conformance. API counts may cover a different release or subset than the ranked catalog.

**Official evidence:**

- [Provider index: Materials Project](https://providers.optimade.org/index-metadbs/mp/v1/links) (checked 2026-11-01): Lists this child database base URL.
- [OPTIMADE specification](https://www.optimade.org/api-specification) (checked 2026-11-01): Defines common endpoints, structure attributes, filtering and pagination.

<a id="oqmd-optimade"></a>
## OQMD · OPTIMADE

Standard structure search and retrieval; provider-specific property fields and coverage vary.

**Interface:** OPTIMADE. **Entrypoint:** [https://oqmd.org/optimade](https://oqmd.org/optimade).

**Authentication:** Public route advertised by the provider registry; current availability is reported separately.

**Formats:** JSON:API-style JSON.

**Verification:** Small record sample verified (2026-11-01). json_response; returned 1 records.

Probe: [https://oqmd.org/optimade/v1/structures?page_limit=1&response_fields=chemical_formula_descriptive%2Cnelements](<https://oqmd.org/optimade/v1/structures?page_limit=1&response_fields=chemical_formula_descriptive%2Cnelements>); HTTP 200.

**Catalog coverage:** [OQMD](catalog/bulk_computed.md#oqmd)

**Limits and interpretation:**

- A listed endpoint is not a guarantee of uptime or full conformance. API counts may cover a different release or subset than the ranked catalog.

**Official evidence:**

- [Provider index: OQMD](https://providers.optimade.org/index-metadbs/oqmd/v1/links) (checked 2026-11-01): Lists this child database base URL.
- [OPTIMADE specification](https://www.optimade.org/api-specification) (checked 2026-11-01): Defines common endpoints, structure attributes, filtering and pagination.

<a id="aflow-optimade"></a>
## AFLOW · OPTIMADE

Standard structure search and retrieval; provider-specific property fields and coverage vary.

**Interface:** OPTIMADE. **Entrypoint:** [https://aflow.org/API/optimade](https://aflow.org/API/optimade).

**Authentication:** Public route advertised by the provider registry; current availability is reported separately.

**Formats:** JSON:API-style JSON.

**Verification:** Small record sample verified (2026-11-01). json_response; returned 1 records.

Probe: [https://aflow.org/API/optimade/v1/structures?page_limit=1&response_fields=chemical_formula_descriptive%2Cnelements](<https://aflow.org/API/optimade/v1/structures?page_limit=1&response_fields=chemical_formula_descriptive%2Cnelements>); HTTP 200.

**Catalog coverage:** [AFLOW](catalog/bulk_computed.md#aflow)

**Limits and interpretation:**

- AFLOW data terms restrict use to scientific, academic and non-commercial purposes.
- A listed endpoint is not a guarantee of uptime or full conformance. API counts may cover a different release or subset than the ranked catalog.

**Official evidence:**

- [Provider index: AFLOW](https://providers.optimade.org/index-metadbs/aflow/v1/links) (checked 2026-11-01): Lists this child database base URL.
- [OPTIMADE specification](https://www.optimade.org/api-specification) (checked 2026-11-01): Defines common endpoints, structure attributes, filtering and pagination.

<a id="cod-optimade"></a>
## Crystallography Open Database · OPTIMADE

Standard structure search and retrieval; provider-specific property fields and coverage vary.

**Interface:** OPTIMADE. **Entrypoint:** [https://www.crystallography.net/cod/optimade](https://www.crystallography.net/cod/optimade).

**Authentication:** Public route advertised by the provider registry; current availability is reported separately.

**Formats:** JSON:API-style JSON.

**Verification:** Probe unsuccessful (2026-11-01). request_failed.

Probe: [https://www.crystallography.net/cod/optimade/v1/structures?page_limit=1&response_fields=chemical_formula_descriptive%2Cnelements](<https://www.crystallography.net/cod/optimade/v1/structures?page_limit=1&response_fields=chemical_formula_descriptive%2Cnelements>); no HTTP response recorded.

**Catalog coverage:** [Crystallography Open Database (COD)](catalog/experimental_crystallography.md#cod)

**Limits and interpretation:**

- The audit request timed out; retain the documented route with availability unconfirmed.
- A listed endpoint is not a guarantee of uptime or full conformance. API counts may cover a different release or subset than the ranked catalog.

**Official evidence:**

- [Provider index: Crystallography Open Database](https://providers.optimade.org/index-metadbs/cod/v1/links) (checked 2026-11-01): Lists this child database base URL.
- [OPTIMADE specification](https://www.optimade.org/api-specification) (checked 2026-11-01): Defines common endpoints, structure attributes, filtering and pagination.

<a id="alexandria-optimade"></a>
## Alexandria PBE · OPTIMADE

Standard structure search and retrieval; provider-specific property fields and coverage vary.

**Interface:** OPTIMADE. **Entrypoint:** [https://alexandria.icams.rub.de/pbe](https://alexandria.icams.rub.de/pbe).

**Authentication:** Public route advertised by the provider registry; current availability is reported separately.

**Formats:** JSON:API-style JSON.

**Verification:** Small record sample verified (2026-11-01). json_response; returned 1 records.

Probe: [https://alexandria.icams.rub.de/pbe/v1/structures?page_limit=1&response_fields=chemical_formula_descriptive%2Cnelements](<https://alexandria.icams.rub.de/pbe/v1/structures?page_limit=1&response_fields=chemical_formula_descriptive%2Cnelements>); HTTP 200.

**Catalog coverage:** [Alexandria](catalog/bulk_computed.md#alexandria)

**Limits and interpretation:**

- PBEsol is another child endpoint in the provider index; do not combine its structures with PBE without checking functional lineage.
- A listed endpoint is not a guarantee of uptime or full conformance. API counts may cover a different release or subset than the ranked catalog.

**Official evidence:**

- [Provider index: Alexandria PBE](https://providers.optimade.org/index-metadbs/alexandria/v1/links) (checked 2026-11-01): Lists this child database base URL.
- [OPTIMADE specification](https://www.optimade.org/api-specification) (checked 2026-11-01): Defines common endpoints, structure attributes, filtering and pagination.

<a id="mcloud-optimade"></a>
## Materials Cloud MC3D PBE · OPTIMADE

Standard structure search and retrieval; provider-specific property fields and coverage vary.

**Interface:** OPTIMADE. **Entrypoint:** [https://optimade.materialscloud.org/main/mc3d-pbe-v1](https://optimade.materialscloud.org/main/mc3d-pbe-v1).

**Authentication:** Public route advertised by the provider registry; current availability is reported separately.

**Formats:** JSON:API-style JSON.

**Verification:** Small record sample verified (2026-11-01). json_response; returned 1 records.

Probe: [https://optimade.materialscloud.org/main/mc3d-pbe-v1/v1/structures?page_limit=1&response_fields=chemical_formula_descriptive%2Cnelements](<https://optimade.materialscloud.org/main/mc3d-pbe-v1/v1/structures?page_limit=1&response_fields=chemical_formula_descriptive%2Cnelements>); HTTP 200.

**Catalog coverage:** [Materials Cloud 3D (MC3D)](catalog/bulk_computed.md#mc3d)

**Limits and interpretation:**

- This is one child dataset; Materials Cloud exposes other child endpoints through its index.
- A listed endpoint is not a guarantee of uptime or full conformance. API counts may cover a different release or subset than the ranked catalog.

**Official evidence:**

- [Provider index: Materials Cloud MC3D PBE](https://www.materialscloud.org/optimade/main/v1/links) (checked 2026-11-01): Lists this child database base URL.
- [OPTIMADE specification](https://www.optimade.org/api-specification) (checked 2026-11-01): Defines common endpoints, structure attributes, filtering and pagination.

<a id="cmr-optimade"></a>
## DTU Computational Materials Repository · OPTIMADE

Standard structure search and retrieval; provider-specific property fields and coverage vary.

**Interface:** OPTIMADE. **Entrypoint:** [https://cmr-optimade.fysik.dtu.dk](https://cmr-optimade.fysik.dtu.dk).

**Authentication:** Public route advertised by the provider registry; current availability is reported separately.

**Formats:** JSON:API-style JSON.

**Verification:** Probe unsuccessful (2026-11-01). http_error.

Probe: [https://cmr-optimade.fysik.dtu.dk/v1/structures?page_limit=1&response_fields=chemical_formula_descriptive%2Cnelements](<https://cmr-optimade.fysik.dtu.dk/v1/structures?page_limit=1&response_fields=chemical_formula_descriptive%2Cnelements>); HTTP 404.

**Catalog coverage:** [Computational 2D Materials Database (C2DB)](catalog/two_dimensional.md#c2db)

**Limits and interpretation:**

- The registered endpoint returned HTTP 404 for the versioned structure request. It is a discovery lead, not verified access to the complete current C2DB.
- A listed endpoint is not a guarantee of uptime or full conformance. API counts may cover a different release or subset than the ranked catalog.

**Official evidence:**

- [Provider index: DTU Computational Materials Repository](https://providers.optimade.org/index-metadbs/cmr/v1/links) (checked 2026-11-01): Lists this child database base URL.
- [OPTIMADE specification](https://www.optimade.org/api-specification) (checked 2026-11-01): Defines common endpoints, structure attributes, filtering and pagination.

<a id="mp-native"></a>
## Materials Project · native API

Query material summaries and specialized property collections with the official MPRester client.

**Interface:** Native API. **Entrypoint:** [https://api.materialsproject.org](https://api.materialsproject.org).

**Authentication:** Account and API key required; mp-api can read MP_API_KEY from the environment.

**Formats:** JSON, pymatgen structures.

**Verification:** Authentication required (2026-11-01). http_error.

Probe: [https://api.materialsproject.org/materials/summary/?_limit=1&_fields=material_id](<https://api.materialsproject.org/materials/summary/?_limit=1&_fields=material_id>); HTTP 401.

**Catalog coverage:** [Materials Project](catalog/bulk_computed.md#materials-project)

**Limits and interpretation:**

- Unauthenticated sample returned HTTP 401 as expected; authenticated payload retrieval was not tested. Property collections have different coverage and licensing.

**Official evidence:**

- [Materials Project API getting started](https://docs.materialsproject.org/downloading-data/using-the-api/getting-started) (checked 2026-11-01): Documents the API key, MPRester and material/property endpoints.

<a id="oqmd-native"></a>
## OQMD · native REST API

Query formation-energy and related calculated-material entries with filters and pagination.

**Interface:** Native API. **Entrypoint:** [https://oqmd.org/oqmdapi](https://oqmd.org/oqmdapi).

**Authentication:** Public queries do not require credentials.

**Formats:** JSON.

**Verification:** Small record sample verified (2026-11-01). json_response; returned 1 records.

Probe: [https://oqmd.org/oqmdapi/formationenergy?limit=1](<https://oqmd.org/oqmdapi/formationenergy?limit=1>); HTTP 200.

**Catalog coverage:** [OQMD](catalog/bulk_computed.md#oqmd)

**Limits and interpretation:**

- Follow the returned pagination metadata. Formation-energy records are not necessarily unique compositions.

**Official evidence:**

- [OQMD REST API documentation](https://static.oqmd.org/static/docs/restful.html) (checked 2026-11-01): Documents native filters, responses and OPTIMADE access.

<a id="aflow-aflux"></a>
## AFLOW · AFLUX search API

Search AFLOW by material properties using AFLUX summons and paging directives.

**Interface:** Native API. **Entrypoint:** [https://aflow.org/API/aflux/](https://aflow.org/API/aflux/).

**Authentication:** Public HTTP query interface.

**Formats:** JSON.

**Verification:** Documented; not queried (2026-11-01). Official documentation inspected; no end-to-end API or SDK query executed for this route..

**Catalog coverage:** [AFLOW](catalog/bulk_computed.md#aflow)

**Limits and interpretation:**

- Native AFLUX syntax differs from OPTIMADE. Provider data terms restrict reuse; a public API does not imply an unrestricted data license.

**Official evidence:**

- [AFLOW AFLUX documentation](https://aflow.org/documentation/) (checked 2026-11-01): Documents the search interface, JSON responses and data-use restrictions.

<a id="nomad-native"></a>
## NOMAD · entries and archives API

Search calculation/experimental metadata, processed archives and raw files; query endpoints support read-only POST searches.

**Interface:** Native API. **Entrypoint:** [https://nomad-lab.eu/prod/v1/api/v1](https://nomad-lab.eu/prod/v1/api/v1).

**Authentication:** Published public entries can be read anonymously; private or embargoed data require authorization.

**Formats:** JSON, raw files, ZIP.

**Verification:** Small record sample verified (2026-11-01). json_response; returned 1 records.

Probe: [https://nomad-lab.eu/prod/v1/api/v1/entries?page_size=1](<https://nomad-lab.eu/prod/v1/api/v1/entries?page_size=1>); HTTP 200.

**Catalog coverage:** [NOMAD Repository & Archive — bulk crystals](catalog/bulk_computed.md#nomad-bulk)

**Limits and interpretation:**

- The sampled production route responded, but newer documentation also shows /backend/api/v1. Read the target installation API docs rather than substituting versions blindly. Entries and calculations are not a deduplicated material count.
- The linked catalog record counts the public bulk-crystal subset; the API also searches non-bulk and experimental entries. Its record count is not the size of the entire repository.

**Official evidence:**

- [NOMAD programmatic API guide](https://docs.nomad-lab.eu/2.0/howto/manage/program/api.html) (checked 2026-11-01): Documents entry queries and structured results; base URLs depend on the installation/version.
- [NOMAD download guide](https://docs.nomad-lab.eu/2.0/howto/manage/program/download.html) (checked 2026-11-01): Documents raw and processed archive downloads by query.

<a id="mpds-native"></a>
## MPDS / PAULING FILE · native API

Retrieve experimental structures, physical properties and phase-diagram entries in machine-readable formats.

**Interface:** Native API. **Entrypoint:** [https://api.mpds.io](https://api.mpds.io).

**Authentication:** API key and subscription/SLA for the full curated database; some data classes are freely available.

**Formats:** JSON, CIF.

**Verification:** Documented; not queried (2026-11-01). Official documentation inspected; no end-to-end API or SDK query executed for this route..

**Catalog coverage:** [Materials Platform for Data Science (MPDS / PAULING FILE)](catalog/experimental_crystallography.md#mpds-pauling-file)

**Limits and interpretation:**

- No authenticated query executed. Experimental structures, physical-property and phase-diagram records have different denominators.

**Official evidence:**

- [MPDS API documentation](https://developer.mpds.io/) (checked 2026-11-01): Documents the API key/subscription, open subsets and S/P/C entry types.

<a id="jarvis-sdk"></a>
## JARVIS · Figshare bulk SDK

Use jarvis.db.figshare.data(name) for named bulk releases; dedicated helpers retrieve STM and Wannier payloads.

**Interface:** Bulk SDK. **Entrypoint:** [https://pages.nist.gov/jarvis/databases/](https://pages.nist.gov/jarvis/databases/).

**Authentication:** Public named files do not require a JARVIS web account.

**Formats:** JSON, ZIP, JARVIS Atoms.

**Verification:** Documented; not queried (2026-11-01). Official documentation inspected; no end-to-end API or SDK query executed for this route..

**Catalog coverage:** [JARVIS-DFT 3D](catalog/bulk_computed.md#jarvis-dft-3d) · [JARVIS-DFT 2D snapshot](catalog/two_dimensional.md#jarvis-2d) · [JARVIS-QETB / TB3PY DFT database](catalog/bulk_computed.md#jarvis-qetb) · [JARVIS-FF classical force-field calculations](catalog/property_benchmarks.md#jarvis-ff) · [JARVIS InterfacDB / InterMat interface release](catalog/surfaces_catalysis.md#jarvis-interfacedb) · [JARVIS vacancy formation-energy release](catalog/property_benchmarks.md#jarvis-vacancydb) · [JARVIS / InterMat surface release](catalog/surfaces_catalysis.md#jarvis-surfacedb) · [JARVIS-WTBH electron Hamiltonians](catalog/property_benchmarks.md#jarvis-wtbh-electron) · [JARVIS-WTBH phonon Hamiltonians](catalog/property_benchmarks.md#jarvis-wtbh-phonon)

**Limits and interpretation:**

- Bulk SDK, not a remote property-query API: data(name) can download and load the entire archive. Documentation, registry progress messages and newer deposit files can describe different releases.

**Official evidence:**

- [Pinned JARVIS download registry](https://github.com/usnistgov/jarvis/blob/3b0c9d0f0c15759135de857dbc93e010db01eb29/jarvis/db/figshare.py) (checked 2026-11-01): Defines 66 named downloads plus special helpers.
- [JARVIS database documentation](https://pages.nist.gov/jarvis/databases/) (checked 2026-11-01): Lists 65 named table entries and the public bulk-loader usage.

<a id="mdf-sdk"></a>
## Materials Data Facility / Foundry · discovery SDK

Discover deposited datasets and use Foundry to load structured ML datasets by DOI.

**Interface:** Bulk SDK. **Entrypoint:** [https://www.materialsdatafacility.org/](https://www.materialsdatafacility.org/).

**Authentication:** Globus/Foundry account or authorization may be required depending on discovery, transfer and dataset access.

**Formats:** metadata JSON, dataset-dependent arrays/files.

**Verification:** Documented; not queried (2026-11-01). Official documentation inspected; no end-to-end API or SDK query executed for this route..

**Limits and interpretation:**

- Repository/SDK coverage spans many materials domains. A DOI lookup does not ensure all files are anonymously downloadable or expose crystal coordinates.

**Official evidence:**

- [MDF provider guide](https://www.materialsdatafacility.org/) (checked 2026-11-01): Describes discovery, Globus transfer and Foundry loading by DOI.
- [Foundry official client](https://github.com/MLMI2-CSSI/foundry) (checked 2026-11-01): Provides a dataset discovery and access SDK.

<a id="huggingface"></a>
## Hugging Face · materials dataset Hub / SDK

Load or stream dataset files with datasets and huggingface_hub; includes LeMat and MateriaViva releases.

**Interface:** Bulk SDK. **Entrypoint:** [https://huggingface.co/api/datasets](https://huggingface.co/api/datasets).

**Authentication:** Public repository metadata can be anonymous; gated/private files require the appropriate account/token and agreement.

**Formats:** JSON metadata, Parquet, JSON, dataset-dependent files.

**Verification:** Metadata response verified (2026-11-01). json_response.

Probe: [https://huggingface.co/api/datasets/AI4QC/MateriaViva-Open](<https://huggingface.co/api/datasets/AI4QC/MateriaViva-Open>); HTTP 200.

**Catalog coverage:** [LeMat-Bulk](catalog/aggregated_crystals.md#lemat-bulk) · [LeMat-Traj](catalog/mlip_configurations.md#lemat-traj) · [MateriaViva Open](catalog/aggregated_crystals.md#materiaviva-open)

**Limits and interpretation:**

- Only the public MateriaViva repository metadata was probed here. Loadable files, streaming support and licenses must be checked per dataset; pin the repository commit.

**Official evidence:**

- [Hugging Face dataset loading](https://huggingface.co/docs/datasets/loading) (checked 2026-11-01): Documents loading from the Hub and pinning a revision.
- [MateriaViva-Open dataset card](https://huggingface.co/datasets/AI4QC/MateriaViva-Open) (checked 2026-11-01): Dataset-specific schema and access evidence.

<a id="figshare"></a>
## Figshare · deposits and file metadata API

Resolve deposit versions, license fields, file sizes, checksums and download links for JARVIS and other releases.

**Interface:** Native API. **Entrypoint:** [https://api.figshare.com/v2](https://api.figshare.com/v2).

**Authentication:** Public deposit metadata is anonymous; private account endpoints need authentication.

**Formats:** JSON metadata, deposited files.

**Verification:** Metadata response verified (2026-11-01). json_response.

Probe: [https://api.figshare.com/v2/articles/25832614](<https://api.figshare.com/v2/articles/25832614>); HTTP 200.

**Limits and interpretation:**

- A deposit is a container, not a crystal structure database. Files use author-defined schemas; version selection and payload parsing are separate steps.

**Official evidence:**

- [Figshare API v2](https://docs.figshare.com/v2/) (checked 2026-11-01): Documents public deposit and authenticated account APIs.

<a id="zenodo"></a>
## Zenodo · records and files REST API

Retrieve versioned record metadata and download/checksum manifests for published materials datasets.

**Interface:** Native API. **Entrypoint:** [https://zenodo.org/api](https://zenodo.org/api).

**Authentication:** Public records and open files can be anonymous; restricted files require permission.

**Formats:** JSON metadata, deposited files.

**Verification:** Metadata response verified (2026-11-01). json_response.

Probe: [https://zenodo.org/api/records/10703249](<https://zenodo.org/api/records/10703249>); HTTP 200.

**Catalog coverage:** [Work function and cleavage energy surface database](catalog/surfaces_catalysis.md#work-function-cleavage-surfaces)

**Limits and interpretation:**

- Record metadata is not a uniform crystal-property schema. Pin the record version and apply its dataset license.

**Official evidence:**

- [Zenodo developer documentation](https://developers.zenodo.org/) (checked 2026-11-01): Documents records, file metadata, access and API pagination.

<a id="starrydata-bulk"></a>
## Starrydata · published bulk files

Machine-readable paper, sample and curve files; 14 project subsets are separately cataloged.

**Interface:** Bulk files. **Entrypoint:** [https://starrydata.github.io/starrydata_datasets/](https://starrydata.github.io/starrydata_datasets/).

**Authentication:** Public release asset downloads.

**Formats:** CSV.gz.

**Verification:** Documented; not queried (2026-11-01). Official documentation inspected; no end-to-end API or SDK query executed for this route..

**Limits and interpretation:**

- Downloadable files, not a documented remote structure-query API. Samples and digitized curves generally lack complete crystal coordinates.

**Official evidence:**

- [Starrydata dataset releases](https://starrydata.github.io/starrydata_datasets/) (checked 2026-11-01): Lists combined and project-specific CSV assets.

<a id="nist-insulation"></a>
## NIST SRD 81 insulation measurement API

Historical guarded-hot-plate measurement rows with material, specimen, apparatus and conditioning fields.

**Interface:** Native API. **Entrypoint:** [https://srdata.nist.gov/insulation/api/TableAllData](https://srdata.nist.gov/insulation/api/TableAllData).

**Authentication:** Anonymous public JSON route; no key used for the verified response.

**Formats:** JSON.

**Verification:** Small record sample verified (2026-11-01). Retrieved complete response: 2,175 objects with 2,175 unique record IDs. Numeric units require the linked SI/IP field definitions; 1,667 records lack uncertainty..

Probe: [https://srdata.nist.gov/insulation/api/TableAllData](<https://srdata.nist.gov/insulation/api/TableAllData>); HTTP 200.

**Catalog coverage:** [NIST Heat Transmission Properties of Insulating and Building Materials (SRD 81)](catalog/experimental_properties.md#nist-srd81-insulation)

**Limits and interpretation:**

- 2,175 counts measurement rows, not distinct materials or specimens; API snapshot was checked 2026-11-01.
- API fields do not encode units. Values appear to use inch-pound conventions; confirm each unit/conversion against the UI before quantitative reuse, and do not label API values SI by default.
- 1,667 of 2,175 API rows have null uncertainty. Provider default uncertainty guidance does not supply measured row-specific uncertainty.
- Apparent thermal transmission properties can combine conduction, radiation and convection; they are not intrinsic lattice thermal conductivity.
- Historical data content ends in 1983; current site accessibility and the 2015 software release are separate from measurement freshness.
- Public access does not establish an open redistribution license.

**Official evidence:**

- [SRD 81 live public JSON API](https://srdata.nist.gov/insulation/api/TableAllData) (checked 2026-11-01): Downloaded 2,175 objects with 2,175 distinct id values. Fields include material/manufacturer, specimen, density, thickness, mean temperature, temperature difference, conductivity, uncertainty, apparatus, method and conditioning; 1,667 rows have null unc.
- [SRD 81 scope and measurement method](https://srdata.nist.gov/insulation/Home/Intro) (checked 2026-11-01): Describes historical 200-mm guarded-hot-plate measurements, over 2,000 observations, most near 24 °C, with broad specimen-density coverage.
- [SRD 81 definitions and uncertainty](https://srdata.nist.gov/insulation/Home/DataFieldDef) (checked 2026-11-01): Defines SI/IP property units, specimen and pre-test conditions, apparatus and test mode; describes relative expanded uncertainty conventions. API numeric fields do not embed units.
- [SRD 81 release history](https://srdata.nist.gov/insulation/Home/VersionHistory) (checked 2026-11-01): Web version 2.0 released December 2015, superseding version 1.0 released January 2000.
- [SRD 81 landing page and rights](https://srdata.nist.gov/insulation/) (checked 2026-11-01): Current public page identifies data content last updated 1983 and copyright U.S. Department of Commerce with all rights reserved.


[Back to MatVerse](../README.md)
