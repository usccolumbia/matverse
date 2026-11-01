# NOMAD: dataset coverage and counting scope

NOMAD was listed as a repository platform and an API provider in MatVerse. Its public bulk-crystal archive is now also an independent searchable dataset entry, under **Computed bulk inorganic crystals**.

[Open the dataset entry](catalog/bulk_computed.md#nomad-bulk) · [NOMAD homepage](https://nomad-lab.eu/nomad-lab/) · [Search the public archive](https://nomad-lab.eu/prod/v1/gui/search/entries) · [API guide](https://docs.nomad-lab.eu/2.0/howto/manage/program/api.html)

## Counts checked on November 1, 2026

| Scope | Count | Meaning |
|---|---:|---|
| Public bulk-crystal query, used in MatVerse's ranking | 15,065,560 | Public archive entries with `results.material.structural_type=bulk` |
| Public, unfiltered API query | 19,419,851 | Public entries across all structural types |
| Official homepage uploaded-entry counter | 19,425,275 | Provider-reported repository-wide uploads |
| Official homepage represented-material counter | 4,346,100 | Provider-reported material identities across the broader repository |

These scopes must not be interchanged. None of the entry counts is a count of independent crystal structures, unique materials or trajectory frames. The [official FAQ](https://nomad-lab.eu/nomad-lab/faqs.html) explains that entries correspond essentially to code runs and that NOMAD imports records from AFLOW, OQMD and Materials Project. Those sources and their derivatives overlap this archive.

The bulk query's method aggregation reports 14,988,740 DFT-labeled entries; other method labels and missing method metadata remain in the bulk total. The catalog therefore describes a predominantly computed archive, with heterogeneous property and quality coverage. A single sampled CaFe2Re entry returned normalized lattice vectors, four atomic positions and full three-dimensional periodicity. This verifies an access path, not every archived payload.

## Reproduce the query

The queried legacy production deployment still exposes `structural_type`; newer NOMAD documentation can show `type_structural` and a different base path. Use the recorded deployment and its API documentation together rather than substituting endpoint versions blindly.

```python
import json
from urllib.request import Request, urlopen

body = {
    "owner": "public",
    "query": {"results.material.structural_type": "bulk"},
    "pagination": {"page_size": 1},
    "required": {"include": ["entry_id", "results.material.*"]},
}
request = Request(
    "https://nomad-lab.eu/prod/v1/api/v1/entries/query",
    data=json.dumps(body).encode(),
    headers={"Content-Type": "application/json"},
)
with urlopen(request, timeout=40) as response:
    payload = json.load(response)
print(payload["pagination"]["total"])
```

This is a read-only POST search. A later execution can return a different count. Exact query bodies, bounded metadata responses, a single structure sample and SHA-256 values are retained in [the audit folder](../research/nomad_20261101/). No full-corpus download or independent deduplication was performed.

[NOMAD terms](https://nomad-lab.eu/nomad-lab/terms.html) specify CC BY 4.0 for open-access content and CC0 for metadata unless otherwise specified. Attribute original contributors, references and data sources when reusing data. Private or embargoed content remains outside this public-query scope.
