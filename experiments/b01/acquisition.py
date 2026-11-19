"""Run only the built-in tests against their own generated synthetic trees.

Not an acquisition API for customer/arbitrary trees: device-node opens can have
side effects before fstat rejection. Device/mount safety remains unverified and
blocks production acquisition; O_NONBLOCK only addresses the synthetic FIFO test.
"""
from contextlib import ExitStack
import errno
import hashlib
import os
from pathlib import Path
import platform
import stat
import tempfile
import unittest
from unittest.mock import patch


SCRATCH = Path("/Volumes/AIWorkspace/caches/hooktrace/b01")
GOOD = b'{"synthetic":"pinned-original"}\n'
OUTSIDE = b'{"synthetic":"outside-sentinel"}\n'


def identity(info):
    return info.st_dev, info.st_ino


def metadata(info):
    return identity(info), info.st_size, info.st_mtime_ns, info.st_ctime_ns


def capture(root, relative, hook, opened):
    """Test helper for generated trees only; pin from / without resolving paths."""
    if not root.is_absolute() or ".." in root.parts:
        raise ValueError("invalid root")
    if os.open not in os.supports_dir_fd or not hasattr(os, "O_NOFOLLOW"):
        raise RuntimeError("PLATFORM_UNSUPPORTED")
    parts = relative.split("/")
    if any(part in ("", ".", "..") for part in parts):
        raise ValueError("invalid relative path")
    directory_flags = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW
    with ExitStack() as stack:
        def acquire(name, flags, parent=None):
            fd = os.open(name, flags, dir_fd=parent)
            opened.append(fd)
            stack.callback(os.close, fd)
            return fd

        parent = acquire("/", directory_flags)
        hook("before-root")
        for part in root.parts[1:]:
            parent = acquire(part, directory_flags, parent)
            if not stat.S_ISDIR(os.fstat(parent).st_mode):
                raise ValueError("not a directory")
        pinned_root = identity(os.fstat(parent))
        hook("after-root")
        for part in parts[:-1]:
            hook("before-ancestor")
            parent = acquire(part, directory_flags, parent)
            if not stat.S_ISDIR(os.fstat(parent).st_mode):
                raise ValueError("not a directory")
            hook("after-ancestor")
        hook("before-leaf")
        # NONBLOCK avoids waiting on our synthetic FIFO, not device-open effects.
        leaf = acquire(parts[-1], os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, parent)
        before = os.fstat(leaf)
        if not stat.S_ISREG(before.st_mode):
            raise ValueError("not a regular file")
        hook("after-leaf")
        chunks = []
        total = 0
        while chunk := os.read(leaf, 64):
            total += len(chunk)
            if total > 1024:
                raise ValueError("synthetic size limit")
            chunks.append(chunk)
        hook("after-read")
        if metadata(before) != metadata(os.fstat(leaf)):
            raise ValueError("concurrent mutation")
        data = b"".join(chunks)
        if len(data) != before.st_size:
            raise ValueError("size changed")
        return data, pinned_root, identity(before), hashlib.sha256(data).hexdigest()


class Acquisition(unittest.TestCase):
    def setUp(self):
        SCRATCH.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(prefix="acquire-", dir=SCRATCH)
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.root = self.base / "input"
        self.outside = self.base / "outside"
        for directory, data in ((self.root, GOOD), (self.outside, OUTSIDE)):
            (directory / "nested").mkdir(parents=True)
            (directory / "manifest.json").write_bytes(data)
            (directory / "nested" / "source.json").write_bytes(data)
        self.opened = []
        self.root_id = identity(self.root.stat())

    def run_capture(self, relative, hook=lambda stage: None):
        try:
            return capture(self.root, relative, hook, self.opened)
        finally:
            # Every actual open, including the trusted anchor, must be closed on
            # both return and exception; no other opens occur during this check.
            for fd in self.opened:
                with self.assertRaises(OSError) as closed:
                    os.fstat(fd)
                self.assertEqual(closed.exception.errno, errno.EBADF)
            self.opened.clear()

    def replace_with_symlink(self, path, target):
        path.rename(path.with_name(path.name + ".original"))
        path.symlink_to(target)

    def assert_original(self, relative, hook=lambda stage: None):
        expected_leaf = identity((self.root / relative).stat())
        data, root_id, leaf_id, digest = self.run_capture(relative, hook)
        self.assertEqual(data, GOOD)
        self.assertNotEqual(data, OUTSIDE)
        self.assertEqual(root_id, self.root_id)
        self.assertEqual(leaf_id, expected_leaf)
        self.assertEqual(digest, hashlib.sha256(GOOD).hexdigest())

    def test_positive_manifest_and_nested_source(self):
        for relative in ("manifest.json", "nested/source.json"):
            self.assert_original(relative)

    def test_invalid_roots_rejected_without_opens(self):
        for root in (Path("ignored") / self.root.relative_to("/"),
                     self.root / ".." / "input"):
            with self.subTest(root=root), patch("os.open", wraps=os.open) as open_call:
                with self.assertRaisesRegex(ValueError, "invalid root"):
                    capture(root, "manifest.json", lambda stage: None, self.opened)
                open_call.assert_not_called()
                self.assertEqual(self.opened, [])

    def test_root_substitution_before_pin_rejected(self):
        def hook(stage):
            if stage == "before-root":
                self.replace_with_symlink(self.root, self.outside)
        with self.assertRaises(OSError) as rejected:
            self.run_capture("manifest.json", hook)
        self.assertIn(rejected.exception.errno, (errno.ELOOP, errno.ENOTDIR))

    def test_root_substitution_after_pin_keeps_original(self):
        def hook(stage):
            if stage == "after-root":
                self.replace_with_symlink(self.root, self.outside)
        self.assert_original("manifest.json", hook)

    def test_ancestor_substitution_before_open_rejected(self):
        def hook(stage):
            if stage == "before-ancestor":
                self.replace_with_symlink(self.root / "nested", self.outside / "nested")
        with self.assertRaises(OSError) as rejected:
            self.run_capture("nested/source.json", hook)
        self.assertIn(rejected.exception.errno, (errno.ELOOP, errno.ENOTDIR))

    def test_ancestor_substitution_after_open_keeps_original(self):
        def hook(stage):
            if stage == "after-ancestor":
                self.replace_with_symlink(self.root / "nested", self.outside / "nested")
        self.assert_original("nested/source.json", hook)

    def test_leaf_substitution_before_open_rejected(self):
        for relative in ("manifest.json", "nested/source.json"):
            with self.subTest(relative=relative):
                def hook(stage):
                    if stage == "before-leaf":
                        self.replace_with_symlink(self.root / relative, self.outside / relative)
                with self.assertRaises(OSError) as rejected:
                    self.run_capture(relative, hook)
                self.assertEqual(rejected.exception.errno, errno.ELOOP)

    def test_leaf_substitution_after_open_never_reads_target(self):
        for relative in ("manifest.json", "nested/source.json"):
            with self.subTest(relative=relative):
                def hook(stage):
                    if stage == "after-leaf":
                        self.replace_with_symlink(self.root / relative, self.outside / relative)
                # Rename can change ctime: either original descriptor or mutation rejection.
                try:
                    self.assert_original(relative, hook)
                except ValueError as rejected:
                    self.assertEqual(str(rejected), "concurrent mutation")

    def test_in_place_mutation_rejected(self):
        def hook(stage):
            if stage == "after-read":
                (self.root / "manifest.json").write_bytes(b"changed-size")
        with self.assertRaisesRegex(ValueError, "concurrent mutation"):
            self.run_capture("manifest.json", hook)

    def test_nonregular_and_invalid_paths_rejected(self):
        (self.root / "directory").mkdir()
        os.mkfifo(self.root / "fifo")
        for relative in ("directory", "fifo", "../outside/manifest.json", "/manifest.json", "nested//source.json"):
            with self.subTest(relative=relative), self.assertRaises(ValueError):
                self.run_capture(relative)

    def test_injected_failure_closes_descriptors(self):
        for boundary in ("after-root", "after-ancestor", "after-leaf", "after-read"):
            with self.subTest(boundary=boundary):
                def hook(stage):
                    if stage == boundary:
                        raise RuntimeError("injected failure")
                with self.assertRaisesRegex(RuntimeError, "injected failure"):
                    self.run_capture("nested/source.json", hook)


if __name__ == "__main__":
    print(f"Python {platform.python_version()}; {platform.platform()}; scratch={SCRATCH}", flush=True)
    unittest.main(verbosity=2)
