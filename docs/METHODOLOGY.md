# Scope, evidence and counting method

This is a living research catalog, first assembled on 2026-11-01. It answers three questions: what crystal-related datasets exist, how much data each contains under an explicit denominator, and what conditions govern useful reuse.

## Coverage and search

Independent research perspectives covered general inorganic databases and MLIP data; experimental crystallography and literature extraction; 2D, framework, molecular and surface systems; and property, generation and discovery benchmarks. Searches used the named provider sites, author repositories, Hugging Face release cards and APIs, Figshare/Zenodo/Materials Cloud metadata, primary papers, and Scientific Data descriptors. Two rounds of searches followed names and references into newer releases, restricted collections and lesser-covered domains. The requested ACS Perspective supplied a separate coverage crosswalk.

Source priority is versioned release metadata or files, official current documentation, and primary dataset papers. A review is a discovery and interpretation source; its approximate scale figures are not automatically treated as live database statistics. A successful webpage fetch does not independently validate a dataset's scientific quality. Search-index-only evidence and direct access failures are identified where relevant.

The source fields in every record are the claim-level audit trail. Scout query summaries are retained in `research/`; these are working research snapshots, while `data/datasets.json` is the maintained catalog. Selected public-document fetches have URL, response status, timestamp, byte length and SHA-256 in `research/source_fetch_manifest.json`. Downloaded source pages and PDFs in `research/cache/` are excluded from Git. Some other research evidence records retain only hashes, snippets or file inventories; their scope is described locally. No claim is made that every cited document has a saved snapshot or that every link is currently downloadable.

## Inclusion and boundaries

Include publicly documented datasets with periodic crystal coordinates, structure-linked computed labels, experimental crystallography or crystal-related experimental properties. Include commercial/reference databases to map access limitations, but do not redistribute their payloads. Include specialized benchmark derivatives when they have a documented task or release; record overlap explicitly. A primary category identifies the main use, and tags capture additional domains. For example, ODAC is filed with frameworks and OMC25 with molecular crystals even though both contain training frames.

Standalone molecular datasets such as QM9, SPICE and OMol25 are outside the crystal ranking. Mixed-domain MLIP data can include molecules if periodic systems are a substantial part of the documented release; the structure level is `mixed`. Battery cycling portals, interoperability APIs, archives, collection repositories and model-only availability references belong in the resource directory. There is no additive grand total of materials. Dataset/release record counts measure this catalog's coverage, not the number of independent experimental corpora.

## Ordering and uncertainty

Rows descend numerically within each primary category by `count`, with unknown sizes last and ties broken by name. Different units remain visible; the sort is a volume convenience, not a quality or chemical-diversity score. `~` marks approximate source figures, `≥` a source lower bound, and `Unranked` an unverified count. A lower-bound position is provisional because the true count may be greater than the listed minimum. Historical counts remain tied to their release or paper, never silently relabeled as current.

The selected size is defined by `count_scope`. Other denominators appear in caveats or `additional_counts`; they are not added to the size column. Arithmetic counts use an explicit `count_derivation`. Full trajectories and end-point structures, unique geometries and repeated labels, source inputs and converged results, training/validation and overlapping subsplits are kept distinct. Counting a small structure archive verifies file/row volume only, not crystallographic uniqueness or validity.

## Data dictionary

| Field | Meaning |
|---|---|
| `id`, `name` | Stable slug and display name |
| `category`, `tags` | One primary category; optional cross-cutting tags |
| `version`, `year` | Exact release/snapshot or publication context; year can be null |
| `count`, `count_display` | Positive integer sort value or null; source wording retained separately |
| `count_unit`, `count_scope` | What is counted and which release/subset it describes |
| `count_precision` | `exact`, `approximate`, `lower_bound`, `unknown`; exact describes reported precision, not a full independent audit |
| `structure_level` | `periodic_atomic`: atomic coordinates; `structure_linked`: structural links/identifiers; `composition_only`: composition/property without full atomic geometry; `mixed`: heterogeneous availability or domains |
| `provenance` | Experimental, computed, generated, literature or mixed origin; read the release caveats |
| `properties` | Documented labels/content, without implying complete row coverage |
| `access` | Open, registration, restricted, commercial or mixed distribution |
| `license` | Dataset-specific terms and uncertainty, independent of paper/model/code licenses |
| `links` | Official homepage, release/data, paper and code routes when verified |
| `sources` | URL, title, evidence paraphrase and verification date |
| `caveats` | Overlap, coverage, uncertainty, availability and scientific interpretation limits |
| `additional_counts`, `count_derivation` | Optional alternate denominators and reproducible arithmetic |

The [JSON Schema](../data/dataset.schema.json) describes the format. The standard-library validator checks required fields, enums, positive counts, unknown-count handling, source URLs, identifier uniqueness, sum derivations and deterministic generated views. It cannot automatically certify the scientific content of a source or legal interpretation of license terms.

## Update protocol

Keep old release context when changing a count; add the new source and explain a changed denominator. Cite original datasets when reusing data. Submit corrections through issues or pull requests with a primary evidence link and a clear scope. See [CONTRIBUTING.md](../CONTRIBUTING.md).
