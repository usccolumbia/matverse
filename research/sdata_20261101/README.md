# Scientific Data materials-dataset audit

Checked November 1, 2026. Local research and catalog changes are complete; publication remains pending the user's explicit instruction.

The journal metadata harvest retrieved **9,304 indexed works** through the cutoff. Broad title screening flagged **1,514 candidates**. These are bibliographic leads, including false positives, not 1,514 verified materials datasets. The source inventory additionally retains **six verified descriptor matches missed by title keywords**. Complete cursor pagination does not establish complete publisher indexing or full-text review of every paper.

Three topical audits produced 91 staged records. One shared 30-system oxide-synthesis aggregate was merged, yielding **90 new catalog records** and **304 total records**. The generated journal index covers **130 catalog records / 127 distinct papers**, including older descriptor URLs previously omitted by the index. Parent and derivative datasets, structures and frames, sites and spectra, samples and measurements are not additive.

- [Search brief](BRIEF.md)
- [Full journal metadata](journal_works.json)
- [Broad title candidates](journal_candidates.json)
- [Query/page receipts and hashes](journal_harvest_receipts.json)
- [Refresh script](harvest_journal.py) — run manually from the repository root; performs network requests, never runs in CI
- [Integration receipt, IDs, aliases and input hashes](integration_receipt.json)
- [Searchable-source inventory and dispositions](../collection_sdata_20261101.json)
- [Generated survey](../../docs/scientific-data.md)
- [Descriptor/canonical-record index](../../data/scientific_data_index.json)

## Independent topical audits

| Perspective | Staged / integrated records | Notes and disposition ledger |
|---|---:|---|
| Structures and computational corpora | 27 / 27 | [Notes](structures/notes.md) · [Leads](structures/leads.json) · [Manifest](structures/manifest.json) |
| Physical properties and synthesis | 35 / 35 | [Notes](properties/notes.md) · [Leads](properties/leads.json) · [Cache hashes](properties/cache_manifest.json) |
| Characterization and processing | 29 / 28 | [Notes](characterization/notes.md) · [Leads](characterization/leads.json) · [Receipt](characterization/receipt.json) |

The staging files preserve the research handoff. `data/datasets.json` is the maintained source; normalized rights phrasing, merged metadata, tags and later corrections belong there. Staging is not an automatic replacement for canonical metadata.

Compact public response receipts identify URLs, statuses, versions, byte counts and hashes. Raw article bodies, API bodies and downloaded payloads remain in ignored local `research/cache/` folders. Some counts were independently checked in small/medium release files; others are explicitly provider-reported. Missing counts and external data rights remain explicit. Article licensing is not assigned to an external archive by inference.

The source inventory maps verified descriptors to canonical IDs, retains topical title dispositions and labels all remaining candidates unreviewed. Corrections/commentary are not new datasets. Adjacent imaging, liquid-phase, amorphous, processing and literature resources have their scope qualified in their cards. No claim of numerical replication, complete bulk accessibility, full coordinate coverage or universal data quality follows from documentation verification.

## Final coverage audit

A final primary-source pass added 12 more records from 11 papers and linked the existing JARVIS electron-Hamiltonian family to its Scientific Data descriptor. The table above includes these contributions. Original perspective staging remains unchanged; separate final-audit files preserve the additions and the evidence-only patch.

- Structures: [Additions](structures/final_audit_additions.json) · [Patch](structures/final_audit_patches.json) · [Notes](structures/final_audit_notes.md)
- Properties: [Additions](properties/final_audit_additions.json) · [Notes](properties/final_audit_notes.md)
- Characterization: [Additions](characterization/final_audit_additions.json) · [Notes](characterization/final_audit_notes.md)

The EFG deposit contains 15,202 unique JID records, differing from the paper's 15,187. Dye-sensitized device archives contain 41,860 distinct-ID JSON documents, differing from the reported 41,680. The JARVIS Hamiltonian documentation snapshot (1,440), original paper (1,771) and current original-collection archive inventory (1,772) are explicitly separated. These discrepancies are reported rather than silently reconciled by choosing the largest number.
