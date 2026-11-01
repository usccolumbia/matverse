# API-accessible / Agent-ready data sources

Checked 2026-11-01. [Search the API directory](https://usccolumbia.github.io/matverse/?view=apis) · [Machine-readable route registry](../data/api_sources.json) · [JARVIS coverage audit](jarvis-coverage.md) · [All source links](../sources.md)

Here, **Agent-ready** means a documented path that software can use to search metadata, retrieve records or download structured files. It is an interface classification, not a certification of scientific quality, complete labels, schema uniformity, autonomous-use permission or unrestricted licensing. The 35 routes below distinguish remote query APIs from bulk SDKs and static downloads. Authentication and the observed verification level remain explicit.

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
| [Matterverse · OPTIMADE](#matterverse-optimade) | OPTIMADE | Anonymous public route | Small record sample verified |
| [Theoretical Crystallography Open Database (TCOD) · OPTIMADE](#tcod-optimade) | OPTIMADE | Anonymous public route | Small record sample verified |
| [Open Materials Database · OPTIMADE](#omdb-optimade) | OPTIMADE | Anonymous public route | Small record sample verified |
| [Open Database of Xtals (odbx) · OPTIMADE provider index](#odbx-optimade) | OPTIMADE | Depends on operation or dataset | Probe unsuccessful |
| [Physical Sciences Data Infrastructure (PSDI) · OPTIMADE provider index](#psdi-optimade) | OPTIMADE | Anonymous public route | Metadata response verified |
| [Material-Property-Descriptor Database (MPDD) · OPTIMADE](#mpdd-optimade) | OPTIMADE | Anonymous public route | Small record sample verified |
| [MatCloud · OPTIMADE provider index](#matcloud-optimade) | OPTIMADE | Depends on operation or dataset | Metadata response verified |
| [Material Properties Open Database (MPOD) · OPTIMADE](#mpod-optimade) | OPTIMADE | Depends on operation or dataset | Probe unsuccessful |
| [AtomGPT.org · OPTIMADE](#atomgpt-optimade) | OPTIMADE | Anonymous public route | Small record sample verified |
| [Anyterial · OPTIMADE](#anyterial-optimade) | OPTIMADE | Anonymous public route | Small record sample verified |
| [NIMS MDR · JSON API and OAI-PMH](#nims-mdr-native) | Native API | Anonymous public route | Probe unsuccessful |
| [Materials Commons · CLI / API](#materials-commons-native) | Bulk SDK | API key | Documented; not queried |
| [MPContribs · projects and contributions API](#mpcontribs-native) | Native API | Depends on operation or dataset | Small record sample verified |
| [NIST PhaseData · CDCS API documentation](#nist-phasedata-native) | Native API | Account / authorization | Authentication required |
| [NIST TRC Alloy Data · API access by request](#nist-trc-alloy-native) | Native API | Account / authorization | Documented; not queried |

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

<a id="matterverse-optimade"></a>
## Matterverse · OPTIMADE

M3GNet-predicted structures and properties of hypothetical materials and Materials Project materials; predictions require physical validation. Unrelated to this MatVerse directory.

**Interface:** OPTIMADE. **Entrypoint:** [https://optimade.matterverse.ai](https://optimade.matterverse.ai).

**Authentication:** Anonymous read-only sample verified.

**Formats:** OPTIMADE JSON.

**Verification:** Small record sample verified (2026-11-01). One public structure record retrieved; no full-corpus validation..

Probe: [https://optimade.matterverse.ai/v1/structures?page_limit=1](<https://optimade.matterverse.ai/v1/structures?page_limit=1>); HTTP 200.

**Catalog coverage:** [Matterverse](catalog/bulk_computed.md#matterverse)

**Limits and interpretation:**

- One public structure record retrieved; no full-corpus validation.
- Index and child databases have different scopes. Public access does not establish redistribution rights; inspect dataset terms.
- Property coverage varies by record; metadata totals are provider-reported and are not independently deduplicated.

**Official evidence:**

- [Matterverse provider documentation](https://matterverse.ai/about) (checked 2026-11-01): M3GNet-predicted structures and properties of hypothetical materials and Materials Project materials; predictions require physical validation. Unrelated to this MatVerse directory.
- [Official OPTIMADE provider registry](https://providers.optimade.org/v1/links) (checked 2026-11-01): Lists provider identity and index URL; listing alone does not establish live data access.
- [Matterverse bounded API sample](https://optimade.matterverse.ai/v1/structures?page_limit=1) (checked 2026-11-01): Anonymous JSON query returned 1 record(s); exact response and hash retained in research/repository_audit_20261101. Only the sample was inspected.

<a id="tcod-optimade"></a>
## Theoretical Crystallography Open Database (TCOD) · OPTIMADE

Theoretically calculated or refined periodic structures with computational provenance; distinct from experimental COD.

**Interface:** OPTIMADE. **Entrypoint:** [https://www.crystallography.net/tcod/optimade](https://www.crystallography.net/tcod/optimade).

**Authentication:** Anonymous read-only sample verified.

**Formats:** OPTIMADE JSON.

**Verification:** Small record sample verified (2026-11-01). One public structure record retrieved; no full-corpus validation..

Probe: [https://www.crystallography.net/tcod/optimade/v1/structures?page_limit=1](<https://www.crystallography.net/tcod/optimade/v1/structures?page_limit=1>); HTTP 200.

**Catalog coverage:** [Theoretical Crystallography Open Database (TCOD)](catalog/bulk_computed.md#tcod)

**Limits and interpretation:**

- One public structure record retrieved; no full-corpus validation.
- Index and child databases have different scopes. Public access does not establish redistribution rights; inspect dataset terms.
- Property coverage varies by record; metadata totals are provider-reported and are not independently deduplicated.

**Official evidence:**

- [Theoretical Crystallography Open Database (TCOD) provider documentation](https://www.crystallography.net/tcod/) (checked 2026-11-01): Theoretically calculated or refined periodic structures with computational provenance; distinct from experimental COD.
- [Official OPTIMADE provider registry](https://providers.optimade.org/v1/links) (checked 2026-11-01): Lists provider identity and index URL; listing alone does not establish live data access.
- [Theoretical Crystallography Open Database (TCOD) bounded API sample](https://www.crystallography.net/tcod/optimade/v1/structures?page_limit=1) (checked 2026-11-01): Anonymous JSON query returned 1 record(s); exact response and hash retained in research/repository_audit_20261101. Only the sample was inspected.

<a id="omdb-optimade"></a>
## Open Materials Database · OPTIMADE

Computational crystal structures and related calculations served through httk. Distinct from Organic Materials Database (omdb.mathub.io), despite the shared OMDB abbreviation.

**Interface:** OPTIMADE. **Entrypoint:** [http://optimade.openmaterialsdb.se](http://optimade.openmaterialsdb.se).

**Authentication:** Anonymous read-only sample verified.

**Formats:** OPTIMADE JSON.

**Verification:** Small record sample verified (2026-11-01). One public structure record retrieved; no full-corpus validation..

Probe: [http://optimade.openmaterialsdb.se/v1/structures?page_limit=1](<http://optimade.openmaterialsdb.se/v1/structures?page_limit=1>); HTTP 200.

**Catalog coverage:** [Open Materials Database](catalog/bulk_computed.md#open-materials-database)

**Limits and interpretation:**

- One public structure record retrieved; no full-corpus validation.
- Index and child databases have different scopes. Public access does not establish redistribution rights; inspect dataset terms.
- Property coverage varies by record; metadata totals are provider-reported and are not independently deduplicated.

**Official evidence:**

- [Open Materials Database provider documentation](https://openmaterialsdb.se/) (checked 2026-11-01): Computational crystal structures and related calculations served through httk. Distinct from Organic Materials Database (omdb.mathub.io), despite the shared OMDB abbreviation.
- [Official OPTIMADE provider registry](https://providers.optimade.org/v1/links) (checked 2026-11-01): Lists provider identity and index URL; listing alone does not establish live data access.
- [Open Materials Database bounded API sample](http://optimade.openmaterialsdb.se/v1/structures?page_limit=1) (checked 2026-11-01): Anonymous JSON query returned 1 record(s); exact response and hash retained in research/repository_audit_20261101. Only the sample was inspected.

<a id="odbx-optimade"></a>
## Open Database of Xtals (odbx) · OPTIMADE provider index

OPTIMADE-listed crystal database. Provider index retrieval failed during this check; current release volume, license and payload availability remain unverified.

**Interface:** OPTIMADE. **Entrypoint:** [https://optimade-index.odbx.science](https://optimade-index.odbx.science).

**Authentication:** Provider index may be public; child access requirements are unverified. No credentials used.

**Formats:** OPTIMADE JSON.

**Verification:** Probe unsuccessful (2026-11-01). Advertised route could not be verified: <urlopen error [SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c:1032)>.

Probe: [https://optimade-index.odbx.science/v1/links](<https://optimade-index.odbx.science/v1/links>); no HTTP response recorded.

**Catalog coverage:** [Open Database of Xtals (odbx)](catalog/bulk_computed.md#odbx)

**Limits and interpretation:**

- Advertised route could not be verified: <urlopen error [SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c:1032)>
- Index and child databases have different scopes. Public access does not establish redistribution rights; inspect dataset terms.
- Property coverage varies by record; metadata totals are provider-reported and are not independently deduplicated.

**Official evidence:**

- [Open Database of Xtals (odbx) provider documentation](https://providers.optimade.org/v1/links) (checked 2026-11-01): OPTIMADE-listed crystal database. Provider index retrieval failed during this check; current release volume, license and payload availability remain unverified.
- [Official OPTIMADE provider registry](https://providers.optimade.org/v1/links) (checked 2026-11-01): Lists provider identity and index URL; listing alone does not establish live data access.

<a id="psdi-optimade"></a>
## Physical Sciences Data Infrastructure (PSDI) · OPTIMADE provider index

Federated discovery and community collections across physical sciences. Its index links multiple child services; metadata counts are not independent crystal counts.

**Interface:** OPTIMADE. **Entrypoint:** [https://index.psdi.ac.uk/optimade/afmdb](https://index.psdi.ac.uk/optimade/afmdb).

**Authentication:** Provider index may be public; child access requirements are unverified. No credentials used.

**Formats:** OPTIMADE JSON.

**Verification:** Metadata response verified (2026-11-01). Index JSON returned ten child collections spanning data and publication metadata. Child payloads not queried..

Probe: [https://metadata.psdi.ac.uk/optimade-index-metadb/v1/links](<https://metadata.psdi.ac.uk/optimade-index-metadb/v1/links>); HTTP 200.

**Limits and interpretation:**

- Index JSON returned ten child collections spanning data and publication metadata. Child payloads not queried.
- Index and child databases have different scopes. Public access does not establish redistribution rights; inspect dataset terms.
- Property coverage varies by record; metadata totals are provider-reported and are not independently deduplicated.

**Official evidence:**

- [Physical Sciences Data Infrastructure (PSDI) provider documentation](https://www.psdi.ac.uk/) (checked 2026-11-01): Federated discovery and community collections across physical sciences. Its index links multiple child services; metadata counts are not independent crystal counts.
- [Official OPTIMADE provider registry](https://providers.optimade.org/v1/links) (checked 2026-11-01): Lists provider identity and index URL; listing alone does not establish live data access.

<a id="mpdd-optimade"></a>
## Material-Property-Descriptor Database (MPDD) · OPTIMADE

Atomic structures organized for high-throughput material featurizers and machine-learning models, maintained by the Phases Research Lab.

**Interface:** OPTIMADE. **Entrypoint:** [https://optimade.mpdd.org](https://optimade.mpdd.org).

**Authentication:** Anonymous read-only sample verified.

**Formats:** OPTIMADE JSON.

**Verification:** Small record sample verified (2026-11-01). One public structure record retrieved; no full-corpus validation..

Probe: [https://optimade.mpdd.org/v1/structures?page_limit=1](<https://optimade.mpdd.org/v1/structures?page_limit=1>); HTTP 200.

**Catalog coverage:** [Material-Property-Descriptor Database (MPDD)](catalog/aggregated_crystals.md#mpdd)

**Limits and interpretation:**

- One public structure record retrieved; no full-corpus validation.
- Index and child databases have different scopes. Public access does not establish redistribution rights; inspect dataset terms.
- Property coverage varies by record; metadata totals are provider-reported and are not independently deduplicated.

**Official evidence:**

- [Material-Property-Descriptor Database (MPDD) provider documentation](https://optimade.mpdd.org/) (checked 2026-11-01): Atomic structures organized for high-throughput material featurizers and machine-learning models, maintained by the Phases Research Lab.
- [Official OPTIMADE provider registry](https://providers.optimade.org/v1/links) (checked 2026-11-01): Lists provider identity and index URL; listing alone does not establish live data access.
- [Material-Property-Descriptor Database (MPDD) bounded API sample](http://mpddoptimade.phaseslab.org/v1/structures?page_limit=1) (checked 2026-11-01): Anonymous JSON query returned 1 record(s); exact response and hash retained in research/repository_audit_20261101. Only the sample was inspected.
- [MPDD HTTPS structure API](https://optimade.mpdd.org/v1/structures?page_limit=1) (checked 2026-11-01): One anonymous structure record retrieved via the current HTTPS deployment; meta.data_available=4,457,640.

<a id="matcloud-optimade"></a>
## MatCloud · OPTIMADE provider index

High-throughput platform integrating data, simulation and supercomputing. The registry child has a null base_url: no operational structure endpoint was supplied.

**Interface:** OPTIMADE. **Entrypoint:** [https://providers.optimade.org/index-metadbs/matcloud](https://providers.optimade.org/index-metadbs/matcloud).

**Authentication:** Provider index may be public; child access requirements are unverified. No credentials used.

**Formats:** OPTIMADE JSON.

**Verification:** Metadata response verified (2026-11-01). Registry index retrieved, but child base_url is null. This is a discovery index, not an operational data API..

Probe: [https://providers.optimade.org/index-metadbs/matcloud/v1/links](<https://providers.optimade.org/index-metadbs/matcloud/v1/links>); HTTP 200.

**Limits and interpretation:**

- Registry index retrieved, but child base_url is null. This is a discovery index, not an operational data API.
- Index and child databases have different scopes. Public access does not establish redistribution rights; inspect dataset terms.
- Property coverage varies by record; metadata totals are provider-reported and are not independently deduplicated.

**Official evidence:**

- [MatCloud provider documentation](https://providers.optimade.org/v1/links) (checked 2026-11-01): High-throughput platform integrating data, simulation and supercomputing. The registry child has a null base_url: no operational structure endpoint was supplied.
- [Official OPTIMADE provider registry](https://providers.optimade.org/v1/links) (checked 2026-11-01): Lists provider identity and index URL; listing alone does not establish live data access.

<a id="mpod-optimade"></a>
## Material Properties Open Database (MPOD) · OPTIMADE

Quantitative physical-property data for crystalline materials. The advertised OPTIMADE structure endpoint timed out; data availability and licensing require provider confirmation.

**Interface:** OPTIMADE. **Entrypoint:** [http://mpod_optimade.cimav.edu.mx](http://mpod_optimade.cimav.edu.mx).

**Authentication:** Provider index may be public; child access requirements are unverified. No credentials used.

**Formats:** OPTIMADE JSON.

**Verification:** Probe unsuccessful (2026-11-01). Advertised route could not be verified: <urlopen error timed out>.

Probe: [http://mpod_optimade.cimav.edu.mx/v1/structures?page_limit=1](<http://mpod_optimade.cimav.edu.mx/v1/structures?page_limit=1>); no HTTP response recorded.

**Catalog coverage:** [Material Properties Open Database (MPOD)](catalog/experimental_properties.md#mpod)

**Limits and interpretation:**

- Advertised route could not be verified: <urlopen error timed out>
- Index and child databases have different scopes. Public access does not establish redistribution rights; inspect dataset terms.
- Property coverage varies by record; metadata totals are provider-reported and are not independently deduplicated.

**Official evidence:**

- [Material Properties Open Database (MPOD) provider documentation](https://providers.optimade.org/v1/links) (checked 2026-11-01): Quantitative physical-property data for crystalline materials. The advertised OPTIMADE structure endpoint timed out; data availability and licensing require provider confirmation.
- [Official OPTIMADE provider registry](https://providers.optimade.org/v1/links) (checked 2026-11-01): Lists provider identity and index URL; listing alone does not establish live data access.

<a id="atomgpt-optimade"></a>
## AtomGPT.org · OPTIMADE

Materials-data service whose current OPTIMADE index exposes JARVIS-DFT. Linked to the existing JARVIS dataset rather than counted as a new independent corpus.

**Interface:** OPTIMADE. **Entrypoint:** [https://atomgpt.org/optimade/v1](https://atomgpt.org/optimade/v1).

**Authentication:** Anonymous read-only sample verified.

**Formats:** OPTIMADE JSON.

**Verification:** Small record sample verified (2026-11-01). One public structure record retrieved; no full-corpus validation..

Probe: [https://atomgpt.org/optimade/v1/structures?page_limit=1](<https://atomgpt.org/optimade/v1/structures?page_limit=1>); HTTP 200.

**Catalog coverage:** [JARVIS-DFT 3D](catalog/bulk_computed.md#jarvis-dft-3d)

**Limits and interpretation:**

- One public structure record retrieved; no full-corpus validation.
- Index and child databases have different scopes. Public access does not establish redistribution rights; inspect dataset terms.
- Property coverage varies by record; metadata totals are provider-reported and are not independently deduplicated.

**Official evidence:**

- [AtomGPT.org provider documentation](https://atomgpt.org/index/optimade/v1/links) (checked 2026-11-01): Materials-data service whose current OPTIMADE index exposes JARVIS-DFT. Linked to the existing JARVIS dataset rather than counted as a new independent corpus.
- [Official OPTIMADE provider registry](https://providers.optimade.org/v1/links) (checked 2026-11-01): Lists provider identity and index URL; listing alone does not establish live data access.
- [AtomGPT.org bounded API sample](https://atomgpt.org/optimade/v1/structures?page_limit=1) (checked 2026-11-01): Anonymous JSON query returned 1 record(s); exact response and hash retained in research/repository_audit_20261101. Only the sample was inspected.

<a id="anyterial-optimade"></a>
## Anyterial · OPTIMADE

httk ecosystem gateway to altermagnet, defect, hard-coating alloy and Open Materials databases. Child databases overlap other catalog providers.

**Interface:** OPTIMADE. **Entrypoint:** [https://altermagnets.anyterial.se/optimade/amdb](https://altermagnets.anyterial.se/optimade/amdb).

**Authentication:** Anonymous read-only sample verified.

**Formats:** OPTIMADE JSON.

**Verification:** Small record sample verified (2026-11-01). One public structure record retrieved; no full-corpus validation..

Probe: [https://altermagnets.anyterial.se/optimade/amdb/v1/structures?page_limit=1](<https://altermagnets.anyterial.se/optimade/amdb/v1/structures?page_limit=1>); HTTP 200.

**Catalog coverage:** [Anyterial — altermagnet database (AMDB)](catalog/property_benchmarks.md#anyterial-amdb)

**Limits and interpretation:**

- One public structure record retrieved; no full-corpus validation.
- Index and child databases have different scopes. Public access does not establish redistribution rights; inspect dataset terms.
- Property coverage varies by record; metadata totals are provider-reported and are not independently deduplicated.

**Official evidence:**

- [Anyterial provider documentation](https://www.anyterial.se/) (checked 2026-11-01): httk ecosystem gateway to altermagnet, defect, hard-coating alloy and Open Materials databases. Child databases overlap other catalog providers.
- [Official OPTIMADE provider registry](https://providers.optimade.org/v1/links) (checked 2026-11-01): Lists provider identity and index URL; listing alone does not establish live data access.
- [Anyterial bounded API sample](https://altermagnets.anyterial.se/optimade/amdb/v1/structures?page_limit=1) (checked 2026-11-01): Anonymous JSON query returned 1 record(s); exact response and hash retained in research/repository_audit_20261101. Only the sample was inspected.

<a id="nims-mdr-native"></a>
## NIMS MDR · JSON API and OAI-PMH

Research data and publications with materials-specific metadata, including SuperCon, phonon and spectroscopy collections. Distinct from NIST MDR.

**Interface:** Native API. **Entrypoint:** [https://mdr.nims.go.jp/api/v1/datasets](https://mdr.nims.go.jp/api/v1/datasets).

**Authentication:** Public metadata JSON, individual work metadata and ZIP downloads; OAI-PMH at https://mdr.nims.go.jp/oai. Beta API may change without notice. Probe failed: The read operation timed out

**Formats:** JSON, OAI-PMH XML, ZIP.

**Verification:** Probe unsuccessful (2026-11-01). Public metadata JSON, individual work metadata and ZIP downloads; OAI-PMH at https://mdr.nims.go.jp/oai. Beta API may change without notice. Probe failed: The read operation timed out.

Probe: [https://mdr.nims.go.jp/api/v1/datasets?q=phonon](<https://mdr.nims.go.jp/api/v1/datasets?q=phonon>); no HTTP response recorded.

**Limits and interpretation:**

- Public metadata JSON, individual work metadata and ZIP downloads; OAI-PMH at https://mdr.nims.go.jp/oai. Beta API may change without notice. Probe failed: The read operation timed out
- Metadata access does not imply permission to reuse every attached file; check individual dataset licenses.

**Official evidence:**

- [NIMS MDR · JSON API and OAI-PMH documentation](https://dice.nims.go.jp/services/MDR/manual/html/api.html) (checked 2026-11-01): Public metadata JSON, individual work metadata and ZIP downloads; OAI-PMH at https://mdr.nims.go.jp/oai. Beta API may change without notice. Probe failed: The read operation timed out

<a id="materials-commons-native"></a>
## Materials Commons · CLI / API

Collaborative research-data storage, metadata, versioning and publication with DOI assignment. Public datasets and private workspaces have different permissions.

**Interface:** Bulk SDK. **Entrypoint:** [https://materialscommons.org/mcdocs2/getting_started/cli.html](https://materialscommons.org/mcdocs2/getting_started/cli.html).

**Authentication:** Documentation entrypoint. materials-commons-cli uses an API key and project permissions; no authenticated request was made.

**Formats:** CLI, files, metadata.

**Verification:** Documented; not queried (2026-11-01). Documentation entrypoint. materials-commons-cli uses an API key and project permissions; no authenticated request was made..

**Limits and interpretation:**

- Documentation entrypoint. materials-commons-cli uses an API key and project permissions; no authenticated request was made.
- Metadata access does not imply permission to reuse every attached file; check individual dataset licenses.

**Official evidence:**

- [Materials Commons · CLI / API documentation](https://materialscommons.org/mcdocs2/getting_started/cli.html) (checked 2026-11-01): Documentation entrypoint. materials-commons-cli uses an API key and project permissions; no authenticated request was made.

<a id="mpcontribs-native"></a>
## MPContribs · projects and contributions API

Community-contributed experimental and computational projects linked to Materials Project materials or compositions. Selected hosted projects are already cataloged.

**Interface:** Native API. **Entrypoint:** [https://contribs-api.materialsproject.org](https://contribs-api.materialsproject.org).

**Authentication:** Public project sample retrieved anonymously; private projects and write operations require authorization. Python package: mpcontribs-client.

**Formats:** JSON, tables, structures, attachments.

**Verification:** Small record sample verified (2026-11-01). Public project sample retrieved anonymously; private projects and write operations require authorization. Python package: mpcontribs-client..

Probe: [https://contribs-api.materialsproject.org/projects/?_limit=1](<https://contribs-api.materialsproject.org/projects/?_limit=1>); HTTP 200.

**Limits and interpretation:**

- Public project sample retrieved anonymously; private projects and write operations require authorization. Python package: mpcontribs-client.
- Metadata access does not imply permission to reuse every attached file; check individual dataset licenses.

**Official evidence:**

- [MPContribs · projects and contributions API documentation](https://docs.materialsproject.org/services/mpcontribs) (checked 2026-11-01): Public project sample retrieved anonymously; private projects and write operations require authorization. Python package: mpcontribs-client.

<a id="nist-phasedata-native"></a>
## NIST PhaseData · CDCS API documentation

Phase-based experimental and computational materials data, including diffusion, transition temperatures and composition-dependent properties; also indexes historical diffusion literature.

**Interface:** Native API. **Entrypoint:** [https://phasedata.nist.gov/docs/api/](https://phasedata.nist.gov/docs/api/).

**Authentication:** API documentation link returned HTTP 401. Account access and dataset permissions must be resolved with the provider.

**Formats:** CDCS structured data.

**Verification:** Authentication required (2026-11-01). API documentation link returned HTTP 401. Account access and dataset permissions must be resolved with the provider..

**Limits and interpretation:**

- API documentation link returned HTTP 401. Account access and dataset permissions must be resolved with the provider.
- Metadata access does not imply permission to reuse every attached file; check individual dataset licenses.

**Official evidence:**

- [NIST PhaseData · CDCS API documentation documentation](https://phasedata.nist.gov/) (checked 2026-11-01): API documentation link returned HTTP 401. Account access and dataset permissions must be resolved with the provider.

<a id="nist-trc-alloy-native"></a>
## NIST TRC Alloy Data · API access by request

Experimental thermophysical properties of unary, binary and ternary metallic systems with original-publication provenance and uncertainty.

**Interface:** Native API. **Entrypoint:** [https://www.nist.gov/mgi/materials-data-resources](https://www.nist.gov/mgi/materials-data-resources).

**Authentication:** Provider explicitly states API access is available upon request. This is the access-information page, not a callable API endpoint; no data API tested.

**Formats:** Provider-defined API data.

**Verification:** Documented; not queried (2026-11-01). Provider explicitly states API access is available upon request. This is the access-information page, not a callable API endpoint; no data API tested..

**Catalog coverage:** [NIST TRC Alloy Data](catalog/experimental_properties.md#nist-trc-alloy)

**Limits and interpretation:**

- Provider explicitly states API access is available upon request. This is the access-information page, not a callable API endpoint; no data API tested.
- Metadata access does not imply permission to reuse every attached file; check individual dataset licenses.

**Official evidence:**

- [NIST TRC Alloy Data · API access by request documentation](https://www.nist.gov/mgi/materials-data-resources) (checked 2026-11-01): Provider explicitly states API access is available upon request. This is the access-information page, not a callable API endpoint; no data API tested.


[Back to MatVerse](../README.md)
