import hashlib
import json
import os
import sqlite3
import time
from contextlib import contextmanager

from . import config


@contextmanager
def connect():
    directory = config.ROOT / "state"
    directory.mkdir(parents=True, exist_ok=True)
    db = sqlite3.connect(directory / "jobs.sqlite3", timeout=30)
    db.row_factory = sqlite3.Row
    db.execute("PRAGMA journal_mode=WAL")
    try:
        yield db
        db.commit()
    except BaseException:
        db.rollback()
        raise
    finally:
        db.close()


def initialize():
    with connect() as db:
        db.executescript('''
        CREATE TABLE IF NOT EXISTS jobs (
          id TEXT PRIMARY KEY, query TEXT NOT NULL, status TEXT NOT NULL,
          created REAL NOT NULL, updated REAL NOT NULL, expires REAL,
          attempts INTEGER NOT NULL DEFAULT 0, progress TEXT, error TEXT,
          result TEXT, client TEXT, lease TEXT
        );
        CREATE INDEX IF NOT EXISTS job_status ON jobs(status,updated);
        CREATE TABLE IF NOT EXISTS submissions (client TEXT, created REAL);
        CREATE INDEX IF NOT EXISTS submissions_client ON submissions(client,created);
        CREATE TABLE IF NOT EXISTS metrics (key TEXT PRIMARY KEY, value INTEGER NOT NULL);
        ''')


def increment(key, value=1):
    with connect() as db:
        db.execute("INSERT INTO metrics VALUES (?,?) ON CONFLICT(key) DO UPDATE SET value=value+excluded.value", (key, value))


def submit(selection, client):
    query = json.dumps(selection.model_dump(), sort_keys=True, separators=(",", ":"))
    identity = hashlib.sha256(("export-v1:" + query).encode()).hexdigest()[:32]
    client = hashlib.sha256(client.encode()).hexdigest()
    now = time.time()
    with connect() as db:
        db.execute("BEGIN IMMEDIATE")
        existing = db.execute("SELECT * FROM jobs WHERE id=?", (identity,)).fetchone()
        if existing and (existing["status"] in ("queued", "running") or
                         (existing["status"] == "complete" and existing["expires"] > now)):
            return dict(existing), True
        db.execute("DELETE FROM submissions WHERE created < ?", (now - 86400,))
        if db.execute("SELECT count(*) FROM submissions WHERE client=? AND created>?", (client, now-3600)).fetchone()[0] >= 12:
            raise ValueError("Hourly export limit reached; reuse existing downloads or retry later")
        if db.execute("SELECT count(*) FROM jobs WHERE client=? AND status IN ('queued','running')", (client,)).fetchone()[0] >= 4:
            raise ValueError("Four exports are already pending for this client")
        if db.execute("SELECT count(*) FROM jobs WHERE status IN ('queued','running')").fetchone()[0] >= 32:
            raise ValueError("Export queue is full; retry later")
        db.execute("INSERT INTO submissions VALUES (?,?)", (client, now))
        db.execute("INSERT OR REPLACE INTO jobs(id,query,status,created,updated,client) VALUES (?,?,'queued',?,?,?)", (identity,query,now,now,client))
        return dict(db.execute("SELECT * FROM jobs WHERE id=?", (identity,)).fetchone()), False


def get(identity):
    with connect() as db:
        row = db.execute("SELECT * FROM jobs WHERE id=?", (identity,)).fetchone()
        return dict(row) if row else None


def claim():
    now = time.time()
    lease = os.urandom(16).hex()
    with connect() as db:
        db.execute("BEGIN IMMEDIATE")
        db.execute("UPDATE jobs SET status='queued', lease=NULL, progress='Requeued after worker restart' WHERE status='running' AND updated<? AND attempts<3", (now-180,))
        db.execute("UPDATE jobs SET status='failed', error='Worker stopped repeatedly',lease=NULL WHERE status='running' AND updated<? AND attempts>=3", (now-180,))
        row = db.execute("SELECT id FROM jobs WHERE status='queued' ORDER BY created LIMIT 1").fetchone()
        if not row:
            return None
        db.execute("UPDATE jobs SET status='running',updated=?,attempts=attempts+1,lease=?,error=NULL WHERE id=?", (now,lease,row['id']))
        return dict(db.execute("SELECT * FROM jobs WHERE id=?", (row['id'],)).fetchone())


def update(identity, lease, **fields):
    allowed = {"status", "progress", "error", "result", "expires"}
    if not set(fields) <= allowed:
        raise ValueError("Unknown state field")
    fields["updated"] = time.time()
    with connect() as db:
        cur = db.execute("UPDATE jobs SET " + ",".join(f"{k}=?" for k in fields) + " WHERE id=? AND lease=? AND status='running'", (*fields.values(),identity,lease))
        return cur.rowcount == 1
