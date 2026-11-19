"""SQLite transaction feasibility only; not the packaged B04 handler/fixture."""
from contextlib import closing
from pathlib import Path
import re
import sqlite3
import tempfile
import unittest


SCRATCH = Path("/Volumes/AIWorkspace/caches/hooktrace/b01")


def connect(path):
    db = sqlite3.connect(path, isolation_level=None)
    db.execute("PRAGMA journal_mode=DELETE")
    db.execute("PRAGMA synchronous=FULL")
    return db


def reset(db):
    db.execute("BEGIN IMMEDIATE")
    try:
        db.execute("CREATE TABLE IF NOT EXISTS state (id TEXT PRIMARY KEY, access INTEGER NOT NULL CHECK(access IN (0,1)))")
        db.execute("CREATE TABLE IF NOT EXISTS tombstone (id TEXT PRIMARY KEY)")
        db.execute("CREATE TABLE IF NOT EXISTS processed (event_id TEXT PRIMARY KEY NOT NULL)")
        for table in ("state", "tombstone", "processed"):
            db.execute(f"DELETE FROM {table}")
        db.execute("COMMIT")
    except BaseException:
        db.execute("ROLLBACK")
        raise


def apply(db, event_id, canceled, fail_at=None):
    """One synthetic ID and policy; caller supplies no exported provider data."""
    if type(event_id) is not str or re.fullmatch(r"[A-Za-z0-9_.:-]{1,128}", event_id) is None:
        raise ValueError("invalid synthetic event ID")
    db.execute("BEGIN IMMEDIATE")
    try:
        if db.execute("SELECT 1 FROM processed WHERE event_id=?", (event_id,)).fetchone():
            db.execute("COMMIT")
            return "duplicate"
        tombstoned = db.execute("SELECT 1 FROM tombstone WHERE id='synthetic-sub'").fetchone()
        db.execute("INSERT OR REPLACE INTO state VALUES ('synthetic-sub', ?)",
                   (int(not canceled and not tombstoned),))
        if fail_at == "state":
            raise RuntimeError("injected failure")
        if canceled:
            db.execute("INSERT OR IGNORE INTO tombstone VALUES ('synthetic-sub')")
        if fail_at == "tombstone":
            raise RuntimeError("injected failure")
        db.execute("INSERT INTO processed VALUES (?)", (event_id,))
        if fail_at == "dedup":
            raise RuntimeError("injected failure")
        db.execute("COMMIT")
        return "committed"
    except BaseException:
        db.execute("ROLLBACK")
        raise


def snapshot(db):
    return tuple(db.execute(f"SELECT * FROM {table} ORDER BY 1").fetchall()
                 for table in ("state", "tombstone", "processed"))


class Transactions(unittest.TestCase):
    def setUp(self):
        SCRATCH.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(prefix="store-", dir=SCRATCH)
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / "synthetic.sqlite3"
        with closing(connect(self.path)) as db:
            reset(db)

    def read_back(self):
        # New connection, not cached values or a successful handler return.
        with closing(connect(self.path)) as db:
            self.assertEqual(db.execute("PRAGMA integrity_check").fetchone(), ("ok",))
            return snapshot(db)

    def test_commit_duplicate_and_reopen(self):
        with closing(connect(self.path)) as db:
            self.assertEqual(apply(db, "synthetic-update", False), "committed")
        self.assertEqual(self.read_back(), ([('synthetic-sub', 1)], [], [('synthetic-update',)]))
        with closing(connect(self.path)) as db:
            self.assertEqual(apply(db, "synthetic-cancel", True), "committed")
        expected = ([('synthetic-sub', 0)], [('synthetic-sub',)],
                    [('synthetic-cancel',), ('synthetic-update',)])
        self.assertEqual(self.read_back(), expected)
        with closing(connect(self.path)) as db:
            changes = db.total_changes
            self.assertEqual(apply(db, "synthetic-cancel", True), "duplicate")
            self.assertEqual(db.total_changes, changes)
        self.assertEqual(self.read_back(), expected)

    def test_invalid_ids_leave_state_and_transaction_unchanged(self):
        with closing(connect(self.path)) as db:
            apply(db, "synthetic-update", False)
            before = snapshot(db)
            changes = db.total_changes
            for active in (False, True):
                if active:
                    db.execute("BEGIN IMMEDIATE")
                for event_id in (None, None, "", " ", "bad id", "bad/id", "bad\n", "x" * 129,
                                 0, False, b"synthetic-update", {}):
                    with self.subTest(active=active, event_id=event_id):
                        with self.assertRaisesRegex(ValueError, "invalid synthetic event ID"):
                            apply(db, event_id, False)
                        self.assertEqual(db.in_transaction, active)
                        self.assertEqual(db.total_changes, changes)
                        self.assertEqual(snapshot(db), before)
                if active:
                    db.execute("ROLLBACK")
        self.assertEqual(self.read_back(), before)

    def test_database_rejects_null_processed_id(self):
        with closing(connect(self.path)) as db:
            apply(db, "synthetic-update", False)
            before = snapshot(db)
            changes = db.total_changes
            with self.assertRaisesRegex(sqlite3.IntegrityError, "NOT NULL"):
                db.execute("INSERT INTO processed VALUES (?)", (None,))
            self.assertFalse(db.in_transaction)
            self.assertEqual(db.total_changes, changes)
            self.assertEqual(snapshot(db), before)
        self.assertEqual(self.read_back(), before)

    def test_atomic_rollback_at_each_write_and_retry(self):
        for boundary in ("state", "tombstone", "dedup"):
            with self.subTest(boundary=boundary):
                with closing(connect(self.path)) as db:
                    reset(db)
                    apply(db, "synthetic-update", False)
                before = self.read_back()
                with closing(connect(self.path)) as db:
                    with self.assertRaisesRegex(RuntimeError, "injected failure"):
                        apply(db, "synthetic-cancel", True, fail_at=boundary)
                    self.assertFalse(db.in_transaction)
                self.assertEqual(self.read_back(), before)
                with closing(connect(self.path)) as db:
                    self.assertEqual(apply(db, "synthetic-cancel", True), "committed")
                self.assertEqual(self.read_back(), ([('synthetic-sub', 0)], [('synthetic-sub',)],
                                                    [('synthetic-cancel',), ('synthetic-update',)]))

    def test_tombstone_survives_reopen_and_reset_clears_every_table(self):
        with closing(connect(self.path)) as db:
            apply(db, "synthetic-cancel", True)
        with closing(connect(self.path)) as db:
            apply(db, "synthetic-later-update", False)
        self.assertEqual(self.read_back(), ([('synthetic-sub', 0)], [('synthetic-sub',)],
                                            [('synthetic-cancel',), ('synthetic-later-update',)]))
        with closing(connect(self.path)) as db:
            reset(db)
        self.assertEqual(self.read_back(), ([], [], []))
        with closing(connect(self.path)) as db:
            self.assertEqual(apply(db, "synthetic-later-update", False), "committed")
        self.assertEqual(self.read_back(), ([('synthetic-sub', 1)], [], [('synthetic-later-update',)]))


if __name__ == "__main__":
    print(f"SQLite {sqlite3.sqlite_version}; journal=DELETE; synchronous=FULL; scratch={SCRATCH}", flush=True)
    unittest.main(verbosity=2)
