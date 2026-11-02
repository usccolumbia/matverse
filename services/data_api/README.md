# MaterialsAtlas Data API

First collection: AI4QC/MateriaViva-Open revision
`6010a086ade47c2c99d1b2dca3a944c3996959a4`.
The service keeps an immutable compressed mirror, validates joins/counts, serves
publisher-labelled open property rows, labels predictions separately, and builds
bounded asynchronous CIF/table exports. Curves are retained but not exposed yet.

## Deployment

Code: `/home/jianjunh/materialsatlas-data-api` on the MaterialsAtlas host.
Data: `/data/materialsatlas-data`. nginx routes `/api/data/v1/`,
`/optimade/`, `/data-downloads/` to loopback port 8094. An internal nginx alias
serves authorized downloads with range requests. Direct access to that alias
is forbidden. Existing MaterialsAtlas apps remain on their original backend.

```
docker build -t materialsatlas-data-api:20261102 .
docker compose -f deploy/compose.yml up -d
```

The production compose file caps API at 2 CPUs/4 GiB and export workers together
at 2 CPUs/8 GiB. Two exports can run concurrently. Total storage budget is 100 GB,
cache 30 GB, temporary export space 20 GB, maximum job size 8 GB, timeout one hour,
minimum free disk 10 GB. Jobs beyond these limits fail with an actionable error.
Cache URLs remain valid for their advertised seven-day lifetime. Requests reuse
normalized-query hashes; failed jobs can be resubmitted. Worker leases recover
after a restart. Anonymous clients have four queued/running jobs and twelve new
exports per hour. nginx also rate-limits API queries. No throughput guarantee
is implied by these limits.

## Release pipeline

`python -m data_api.mirror --help`, `build_catalog --help`, and `build_optimade
--help` describe ingestion. Use a full upstream revision. Mirror integrity is
recorded in `mirror_receipt.json`. Catalog validation creates `READY.json` then
atomically activates `current`; normalization creates `OPTIMADE_READY.json`.
Never modify active source files or rebuild a live database in place. Build a new
release, validate it, then switch the current pointer. Keep the previous release
for rollback. Normalized receipts report every skipped CIF and reason.

Source filters have different meanings: property provider, structure membership,
and coordinate origin. Do not collapse them. Multiple values are preserved.
OPTIMADE normalizes CIF geometry, so its site counts may differ from source
metadata. Unsupported nested/correlated filters fail explicitly. The fixture
validator report is in `research/data_api_20261102`; live validation is required
before calling a deployment compliant. Passing the validator covers its tested
surface, not every possible query.

## Monitoring, backup and recovery

The five-minute systemd check writes `state/monitor.json` and exits nonzero on
health, stale-worker, or storage problems. Inspect `systemctl status
materialsatlas-data-monitor.service` and its journal. It provides local monitoring;
no email or external paging is configured. Daily backup copies immutable releases,
service code, and a consistent SQLite snapshot to the separate mounted backup
disk. Cache and working space are reproducible and omitted. The script refuses
to write to an unmounted backup path and preserves old state snapshots.

After recovery, restore the selected release and service code, restore a SQLite
snapshot, resubmit missing cached exports, and start Compose. To roll back this
installation, restore the saved nginx site file, run `nginx -t`, reload nginx,
and stop only this Compose project. Keep all data and source backups. To disable
timers: `systemctl disable --now materialsatlas-data-{monitor,backup}.timer`.

## Development

```
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 PYTHONPATH=services/data_api:python/materialsatlas/src \
  python -m pytest services/data_api/tests python/materialsatlas/tests -q
optimade-validator https://materialsatlas.org/optimade/v1 --json --random-seed 7
```

The client package lives at `python/materialsatlas`; PyPI uses the repository's
`publish-materialsatlas.yml` workflow and the `pypi` environment through trusted
publishing. No PyPI token belongs in this repository.
