# B01a acquisition-safety prerequisite

Status: **Research NO-GO accepted**, [PR #11](https://github.com/Himanshu-singh04/hooktrace/pull/11)
merged at `529f8d5e06601def268828eaad993111987c9a76`; main
[CI 44510104992](https://github.com/Himanshu-singh04/hooktrace/actions/runs/44510104992) passed.
Acceptance does not authorize acquisition implementation or producer-created intake;
that workflow remains an unaccepted proposal. The original evidence and limits below
are retained; no new native enforcement or runtime validation is claimed.
The founder subsequently authorized the separate [B01c design study](b01c-producer-intake.md)
under issue #14, not acceptance of a workflow, threat-model change or implementation.

Original handoff status: **Decision ready for coordinator review**, [issue #10](https://github.com/Himanshu-singh04/hooktrace/issues/10),
2026-11-19. **NO-GO for arbitrary-export acquisition** on the observed host or
proposed product stack. Native nodev has a useful, narrower device-open guarantee
in the reviewed source; it does not establish the whole acquisition boundary.
No acquisition policy is approved or implemented by this record.

## Assignment and bounds

Original founder instruction: “ok then proceed with the further tasks”, after the
three first research PRs merged. The coordinator selected B01's unresolved
device-node/mount gate before B02. Issue #10 preserves the full assignment and
fixed A1–A6 acceptance criteria. This persistent worker uses GPT-6 Astra / OpenCode;
no subagents or product implementation are involved.

Base: clean fetched main `97f1669ddd92a510f7d637429b1c21f53713ae40`.
Compare at most two strategies: descriptor-bound local mount policy (including
native nodev), and a genuinely trusted input/staging boundary. Preserve HT-08 and
descriptor-relative/no-follow acquisition. Investigate exact Darwin source/API
and installed SDK evidence before deciding whether a native probe adds evidence.
Never infer prevention from post-open rejection, a mount listing, or injected flags.

Executable research is limited to generated regular files/directories,
symlinks and FIFO in task-owned cache paths. No devices, mount changes, arbitrary
exports, runtime installation, customer data, privileges or permissions changes.
Primary evidence establishes counterexamples to mount-observation-only and
copy-to-staging guarantees below. No new native acquisition executable or mock
enforcement was needed: SDK preprocessing and existing synthetic tests suffice
for this negative decision, not for approving either strategy.

## B01 approval and correction history

[Coordinator merge verification](https://github.com/Himanshu-singh04/hooktrace/pull/9#issuecomment-7002315562)
records founder approval of reviewed head `493027222584493d9722ec2dbfbba39043b53310`,
distinct from the earlier authorization to perform R7. PR #9 merged as the base
above; conditional Python/Acacia/SQLite direction is accepted for a separately
authorized next investigation, not runtime installation or B02 implementation.

R1/R3 validation corrections passed 11 acquisition and 5 store tests. R2's
device/mount limitation remains real. R4/R5 were fixed-literal SQL false positives;
R7 made the statements explicit for static review, preserving behavior. The fresh
Sourcery check passed before the replacement approval; prior failed checks and
superseded unapproved snapshots remain historical. The literal SQL and all B01
research source are preserved. Candidate runtime/build, fixtures, device/mount
and product isolation gates remain open.

## Threat model and decision (A1, A5)

**Decision:** keep arbitrary exports blocked. The smallest next decision is whether
to authorize investigation of **producer-created trusted intake** (strategy 2),
not to turn the workspace's observed nodev flag into an import permission. Strategy
1 remains a conditional mechanism worth retaining, not a certified supported mode.
HT-08 and the [contract](evidence-contract.md) remain unchanged; no path-check/reopen
fallback, weakened device rule, or new public input format is introduced.

Actors and objects must be distinguished:

- **Untrusted producer / namespace writer:** may supply malicious JSON, names,
  symlinks, hard links, pre-existing special nodes and directories; may rename,
  replace or mutate entries while capture runs. Lack of permission to create new
  devices does not prove none were already supplied. No trust comes from a manifest,
  filename, file owner, hash, or operator selecting a directory.
- **Trusted OS, kernel and filesystem implementation:** required for either strategy.
  A compromised kernel or malicious filesystem implementation is excluded, not
  detected by fstatfs. Only a version-reviewed local filesystem could be supported;
  `MNT_LOCAL` alone does not identify a trusted implementation.
- **Mount authority:** includes administrators, mount-owning users where permitted,
  automounters and privileged services acting for a user. Strategy 1 requires trusted
  cooperation: no mount/remount/unmount, flag change, replacement, trigger or nested
  foreign mount on the acquisition route for the entire operation. This is a trust
  assumption, **not** something the proposed descriptor checks enforce. An arbitrary
  export cannot assert it. An unprivileged importer does not constrain other actors.
- **Same-user writers / privileged operators:** private directory mode is not a
  boundary against the same UID or an administrator; `noowners` is not permission
  isolation. Strategy 2 must exclude their interference through an actually reviewed
  creation/handoff boundary. Neither strategy promises snapshot consistency against
  an authorized in-place writer; metadata/hash failures only detect some changes.
- **Hard links:** no-follow blocks symlinks, not additional names for the same inode.
  A regular file beneath the root may alias data outside it on the same filesystem.
  Proposed intake disallows imported hard links and requires newly created files.
  `st_nlink == 1` is only a post-open observation: an outside name can be removed
  while an outside writer retains a descriptor. It proves neither origin nor absence
  of writers. No new hard-link policy is silently added to the normative contract.

Supported **research use** remains B01's own synthetic trees. Unsupported for product
acquisition: arbitrary operator paths, unknown filesystems, network/user-space or
triggered mounts, nested mounts, mutable mount policy, unreviewed aliases/hard links,
or a staging directory filled by an unaudited copy/extractor. A failure to establish
the required boundary must eventually return `PLATFORM_UNSUPPORTED` before source
leaf opens, not try a weaker fallback. That product gate is still unimplemented.

## Primary Darwin and SDK evidence (A2, A3)

Read 2026-11-19. Apple source is cited, not vendored or executed. Pinned source:
**xnu-12377.121.6**, commit **ac9718fb1af618d5ce8678d0dc6e8a58f252216f**.
It was the first tag returned by the upstream tags query. It is **not** the running
kernel: `uname -a` reports Darwin **27.2.0**, **xnu-13432.41.4~25**, arm64;
`sw_vers` reports macOS **27.2.1**, build **26B131**. This mismatch is an explicit
verification gap, not permission to transfer an old implementation guarantee.
The reviewed XNU paths also do not constitute a review of the shipped APFS driver's
complete compound-open behavior. Local APFS is a proposed allowlist condition, not
a filesystem certification derived from its name.

| Evidence | Exact location and finding | Limit |
| --- | --- | --- |
| D1: device dispatch | [spec_vnops.c, spec_open](https://github.com/apple-oss-distributions/xnu/blob/ac9718fb1af618d5ce8678d0dc6e8a58f252216f/bsd/miscfs/specfs/spec_vnops.c#L352-L480): checks the **device vnode's own mount** for MNT_NODEV and returns ENXIO at lines 364–365, before character/block driver `d_open` | Strong evidence for this code path, not proof for every filesystem or the running build; flags must still hold at dispatch |
| D2: open before user validation | [vfs_vnops.c, vn_open_auth](https://github.com/apple-oss-distributions/xnu/blob/ac9718fb1af618d5ce8678d0dc6e8a58f252216f/bsd/vfs/vfs_vnops.c#L595-L737): compound-open path or VNOP_OPEN runs inside open | A later Python fstat or C fstatfs cannot undo driver/filesystem effects, even if open ultimately fails |
| D3: directory/type guard | [vfs_subr.c, vn_authorize_open_existing](https://github.com/apple-oss-distributions/xnu/blob/ac9718fb1af618d5ce8678d0dc6e8a58f252216f/bsd/vfs/vfs_subr.c#L8340-L8378): O_DIRECTORY rejects non-directories; O_NOFOLLOW rejects a symlink | Supports directory traversal guard, not a regular-file-only leaf open; filesystem compound operations also require supported-platform review |
| D4: descriptor statistics | [vfs_syscalls.c, fstatfs64](https://github.com/apple-oss-distributions/xnu/blob/ac9718fb1af618d5ce8678d0dc6e8a58f252216f/bsd/vfs/vfs_syscalls.c#L3906-L3955): gets vnode from FD, obtains its mount, copies statistics, releases references | An observation of that descriptor, no policy lease across the next syscall |
| D5: mutable flags | [mount_common](https://github.com/apple-oss-distributions/xnu/blob/ac9718fb1af618d5ce8678d0dc6e8a58f252216f/bsd/vfs/vfs_syscalls.c#L1290-L1467): authorized update can clear/set MNT_NODEV; non-root mounts/updates force nodev/nosuid | Do not claim an ordinary unprivileged writer can clear nodev; the counterexample needs authorized mount control |
| D6: mount traversal | [lookup_traverse_mountpoints](https://github.com/apple-oss-distributions/xnu/blob/ac9718fb1af618d5ce8678d0dc6e8a58f252216f/bsd/vfs/vfs_lookup.c#L1922-L2041): follows v_mountedhere, calls VFS_ROOT; conditional trigger resolution happens during lookup | No-follow is not no-cross-mount. fstatfs on the returned directory is too late to prevent entry/trigger activity |
| D7: public open semantics | [open(2)](https://github.com/apple-oss-distributions/xnu/blob/ac9718fb1af618d5ce8678d0dc6e8a58f252216f/bsd/man/man2/open.2#L146-L270): NONBLOCK is a waiting policy; EVTONLY is for notifications; BENEATH prevents escape; UNIQUE checks hard links | None of those descriptions promises an immutable nodev mount policy. EVTONLY is not a safe metadata-open/read-upgrade substitute |
| D8: hard-link semantics | [link(2)](https://github.com/apple-oss-distributions/xnu/blob/ac9718fb1af618d5ce8678d0dc6e8a58f252216f/bsd/man/man2/link.2#L54-L88): two names share one object; unlinking one decrements count; same filesystem required | Path containment and inode/link-count checks are not content provenance or writer isolation |
| D9: API/error contract | Apple's [statfs/fstatfs manual](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/statfs.2.html): descriptor form, 0 success / -1 with errno, EBADF/EFAULT/EIO | Archived page includes historical layouts; use the installed SDK for ABI, not a handwritten FFI structure |

Installed-tool observations (no binary built/run): Apple clang **21.0.0**
(`clang-2100.4.1.1`), target `arm64-apple-darwin27.2.0`; SDK **27.2**, build **26B118**
at `/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk`. Compiler preprocessing of
`<sys/mount.h>` and `<fcntl.h>` returned these declarations/macros:

- `int fstatfs(int, struct statfs *)`, symbol `_fstatfs`; `int openat(int, const char *,
  int, ...)`, symbol `_openat`, macOS availability 10.10. An FD is a C `int`, not a path.
- SDK `sys/mount.h:133` expands `struct statfs` with **uint32_t f_flags**, **fsid_t
  f_fsid**, **char f_fstypename[16]**; `sys/_types/_fsid_t.h:31` defines `fsid_t` as
  `struct fsid { int32_t val[2]; }`. Names/mountpoint strings are descriptive, not
  identity or authority. Do not serialize the native struct or infer padding.
- `MNT_NODEV=0x10`, `MNT_LOCAL=0x1000`, `MNT_UNION=0x20`,
  `MNT_IGNORE_OWNERSHIP=0x00200000`, `MNT_AUTOMOUNTED=0x00400000`.
  `O_DIRECTORY=0x00100000`, `O_NOFOLLOW=0x100`, `O_NONBLOCK=0x4`,
  `O_EVTONLY=0x8000`, `O_NOFOLLOW_ANY=0x20000000`,
  `O_RESOLVE_BENEATH=0x1000`, `O_UNIQUE=0x2000`.
  The last two **are declared** in this SDK; don't assume older Darwin limitations.
  BENEATH still allows downward mount traversal (D6); UNIQUE does not rule out
  retained writer handles. Neither was exercised. No private resolve flags are used.
- Installed Python **3.13.4** exposes O_DIRECTORY/O_NOFOLLOW and fstatvfs, but not
  fstatfs, O_RESOLVE_BENEATH or O_UNIQUE. No hardcoded flag or ctypes workaround was
  added. The candidate CPython **3.13.18** / SQLite **3.54.1** build remains unvalidated;
  current SQLite is **3.49.1**. SDK declarations do not establish Python exposure or
  runtime support on another OS/build.

Any later reviewed native probe would use the compiler's SDK types directly, check
every syscall result before accessing output, keep the directory FD alive through
the dependent open, and close each owned FD once on every exit. fstatfs borrows the
FD; it neither closes it nor freezes the mount. Errors/unknown flags/identity must
reject before a leaf open; no retry by pathname, private syscall, or generic FFI.
There is no new ABI/helper surface in this task.

## Two strategies and their failure boundaries (A1–A4)

### 1. Descriptor-bound local nodev policy

Conditional proposal, not implemented: reach a declared trusted local root using
the existing component-wise directory/no-follow procedure. Trusted system ancestors
may be non-nodev directories; do not open source leaves there. On the pinned input
root and **every retained source parent**, require SDK-native fstatfs success,
allowlisted APFS implementation, local + nodev, no union/automount, and matching
root filesystem identity. Use same-descriptor fstat identities as well. A mismatch
or unavailable observation stops **before the next source leaf open**. The manifest
is a leaf too. A root-only check or fstatvfs flag check alone is insufficient.

For one validated basename on that stable, trusted filesystem, the nodev check in
D1 rejects a device at kernel dispatch before its driver open. It applies to device
hard links too: the vnode's mount, not its name, is checked. Regular bytes are still
read only after same-FD type checks, then counted/hashed with before/after metadata.
FIFO nonblocking open/type rejection is separate, not evidence for devices. A
directory mounted at a leaf is not accepted as a regular source. This argument
depends on trusted directory-root/type semantics, not arbitrary filesystem behavior.

**Retained descriptor cases:** replacing the pathname of an already pinned parent
does not turn its FD into a new pathname lookup. B01 demonstrates rename/symlink
substitution only. A mount attached to a *child not yet opened* can still be traversed
by the next openat; gate the newly returned parent before opening its leaf. A mount
attached over an already-open directory does not rewrite that FD into the covering
mount; subsequent children and forced-unmount errors still need evaluation. Neither
FD identity nor filesystem ID locks flags or freezes the descendant namespace.
Never reopen a mountpoint string to try to recover the selected descriptor.

**Concrete counterexamples / no-go:**

1. **Flags change after observation.** Parent FD P observes nodev at time t0. An
   authorized mount actor clears nodev on that same mount at t1 (D5). P still refers
   to the same directory/filesystem. At t2, openat(P, device-leaf, READ|NOFOLLOW|
   NONBLOCK) reaches D1 without nodev and may call the driver. fstat/fstatfs after t2
   cannot undo that call. Repeating the pre-check just moves the race. This refutes
   safety *with mount-changing actors*, not the conditional stable-mount argument.
2. **Foreign mount before child open.** A pinned local root contains an unopened
   child with a foreign/triggered mount. openat(root, child, DIRECTORY|NOFOLLOW)
   traverses it and can call filesystem/trigger operations (D6) before user-space
   fstatfs can reject it. Checking each returned FD can prevent the subsequent
   device-leaf open but cannot guarantee zero foreign-filesystem/automount effects
   or outbound work during acquisition. No actual mount or network effect was tested.
   BENEATH/no-follow do not establish that stronger boundary.

Thus this policy could protect device dispatch **under separately enforced/trusted
stable-local-mount assumptions**, but does not admit unrestricted export trees under
HT-08/T08. Before using it, review actual kernel/filesystem behavior and establish
the mount/actor boundary, including root acquisition. `mount` currently reports
`/Volumes/AIWorkspace (apfs, local, nodev, nosuid, journaled, noowners)`; that is an
observation, not per-descriptor enforcement or proof that all descendants qualify.
No diskutil/listing, synthetic flag injection, or assertion of no root attacker
closes the pre-existing foreign/triggered-mount gap.

### 2. Genuinely trusted producer-created intake

Trust the **creation boundary**, never the payload. A separately approved producer
would emit bytes directly from its known application/export data into fresh regular
files it creates exclusively beneath retained descriptors in a reviewed local intake
root. All parents and names are controlled by that producer; it never recreates
input-supplied links, device nodes, mounts, metadata or archives. It closes writers
before handoff; untrusted actors cannot add mounts, replace entries or retain writer
access there. The reader still uses descriptor-relative/no-follow acquisition,
regular-file checks, immutable freezing and full untrusted-data validation.

Safe acquisition into staging must have an origin: the producer already holds its
own application data/known-safe descriptors, rather than walking an arbitrary
external tree. A future byte-stream handoff would need its own bounded format and
producer review; it is not a new importer interface authorized here. An existing
arbitrary path/export cannot be relabeled trusted by copying, hashing, dragging in
Finder, using an extractor, or asking an operator to vouch for it.

**Concrete no-go:** a copier opens an arbitrary source device before it can put
anything in staging. The source-side driver effect already happened; restricting
destination files cannot undo it. Copying also needs its own mount/symlink/hard-link
and concurrency guarantees. The trust-boundary solution must exclude that operation,
not move it into an undocumented preparation step. Same-user/noowners directory
creation on this pendrive alone cannot enforce the required handoff isolation.

This is the smaller **future workflow investigation**, but would narrow supported
inputs and therefore needs a separate founder decision and explicit contract review.
It is not approved security, implemented staging or permission to import customer data.

### Prevention, exclusion, and detection are different

| Condition | Classification in the evaluated designs |
| --- | --- |
| Invalid root/relative syntax | Rejected before any B01 opens; existing regression checks zero calls |
| Symlink at a directory/leaf component | No-follow rejects that lookup; retained parents avoid reopening replaced ancestors |
| Known parent policy missing/nodev off/wrong filesystem/error | Proposed descriptor gate rejects before **leaf** open; no gate implemented/tested here |
| Device on the same stable trusted nodev mount | D1 rejects in kernel before **driver** open; not a user-space pre-open test; current-host enforcement unverified |
| Mount changer, hostile/triggered filesystem or unknown root-acquisition route | Excluded by conditional strategy assumptions, not blocked by fstatfs; unsupported absent a trusted boundary |
| Newly crossed child mount | Only detected after child directory open by proposed gate; too late for lookup/trigger effects |
| Nonregular leaf, link count, changed size/metadata/hash | Detected after leaf open; before byte acceptance where implemented; no undo of open effects |
| In-place writer / earlier outside hard link | No snapshot/origin guarantee; trusted staging must establish writer exclusion before handoff |

## Safety verdict and next decision (A5)

| Claim | Observed host | Proposed product platform |
| --- | --- | --- |
| Synthetic descriptor/no-follow acquisition, retained identity and cleanup | **Met**, 11 B01 tests rerun | **Unverified** on future approved build/volume |
| Native device dispatch blocked by nodev | **Unverified** on running xnu-13432.41.4; mechanism supported by pinned older source | **Unverified** until exact supported kernel/filesystem reviewed and enforcement tested |
| Arbitrary exports cannot cross unsafe mounts or invoke pre-rejection device effects | **Unmet / NO-GO** for the observation-only design; counterexamples above | **Unmet / NO-GO** without a separately established input/mount boundary |
| Trusted producer/staging handoff | **Unverified**, no implementation or isolated intake | **Unverified**, founder scope decision and enforceable actor boundary required |
| HT-08/T08 and Q4 overall | **Unverified**, no product or network-denied acquisition test | **Unverified**, no supported-platform release claim |

Proposed founder question (not an approval request from this worker): **authorize a
separate bounded design for producer-created intake only, with arbitrary-directory
import remaining unsupported?** The coordinator should expose the workflow cost:
existing exports need a genuinely safe producer path, not a convenience copy step.
If that narrowing is rejected, retain no-go and separately investigate a verified
atomic/kernel-enforced boundary; do not weaken HT-08 or silently select strategy 1.

Still required: current-kernel/SDK/filesystem conformance; actual pre-driver rejection
and mount-substitution coverage in a separately authorized safe environment; same-FD
policy/error/cleanup tests if a gate is built; hard-link/writer handoff tests; root
bootstrap and no-network enforcement. Any injected mount/device observations would
test control flow only and must not substitute for those real enforcement tests.
This task adds none because no enforcement implementation is proposed for acceptance.

Other B02 gates remain: approved runtime build/SQLite linkage and reproducible lock,
full Acacia created/updated/deleted and unsupported-version/scope fixtures, schema
and RFC8785 conformance, safe freeze/publication and limits, isolation, and a separate
bounded B02 issue. No runtime installation, mount/permissions change, importer,
customer input, or product execution is authorized by B01/B01a research acceptance.

## Rerunnable evidence and outcomes (A6)

From the repository root, existing synthetic scripts create and clean only their
own fresh paths under `/Volumes/AIWorkspace/caches/hooktrace/b01`. No new temporary
tree, native binary, FFI, dependency, or runtime artifact is introduced by B01a.

| Exact command/check | Outcome |
| --- | --- |
| `python3 experiments/b01/acquisition.py` | Exit 0; **11 passed**: manifest/nested positive controls, root/ancestor/leaf substitution, retained identity/hash, invalid roots with zero opens, nonregular/FIFO rejection, mutation, injected failure and EBADF cleanup |
| `python3 experiments/b01/store.py` | Exit 0; **5 passed** on Python 3.13.4 / SQLite 3.49.1; final R7 literal SQL preserved |
| `uname -a`; `sw_vers`; `mount` (each read-only) | Exit 0; host/kernel/build and workspace mount observation recorded above; no device nodes opened by research code |
| `xcrun clang --version`; `xcrun --show-sdk-path`; `xcrun --show-sdk-version`; `xcrun --show-sdk-build-version` | Exit 0; installed tool/SDK versions above |
| Compiler preprocessing below | Exit 0 for declaration and macro passes; **not** runtime enforcement |
| `python3 scripts/check_repository.py` | Exit 0; tracked formatting and relative Markdown file links passed |
| `python3 -m unittest discover -s scripts -p 'test_*.py'` | Exit 0; **25 policy tests passed** |
| `/Volumes/AIWorkspace/caches/actionlint/1.7.12/actionlint -shellcheck= -pyflakes=` | Exit 0 |
| `git diff --check 97f1669ddd92a510f7d637429b1c21f53713ae40` | Exit 0; full PR diff |
| Inline Python SDD comparison against base and skill template | **55 identical headings**, no clarification placeholders |
| `git diff 97f1669ddd92a510f7d637429b1c21f53713ae40 -- experiments/b01` | Empty: B01 source including final literal SQL unchanged |

SDK inspection can be rerun without creating or executing a binary:

```sh
python3 - <<'PY'
import subprocess
source = '#include <sys/mount.h>\n#include <fcntl.h>\n'
for flags in ([], ['-dM']):
    print(subprocess.check_output(
        ['xcrun', 'clang', '-E', *flags, '-x', 'c', '-'],
        input=source, text=True))
PY
```

Research retrieval used `curl --fail --silent --show-error --max-time 40` on the
immutable raw GitHub URLs corresponding to D1–D8; Apple's archived D9 manual was
retrieved with the read-only web fetch tool.
Upstream tag was checked with scoped `gh api repos/apple-oss-distributions/xnu/tags?per_page=5`.
Direct SDK-header grep was denied by the tool's external-directory permission;
installed compiler preprocessing supplied declarations instead. No permission or
trust setting was changed. The early draft's bot summary displaced final attribution,
causing `pr-record` failure; its summary was preserved and the final trailer restored.
Checkpoint and final live CI/attribution results are recorded in PR #11.

**Not run:** real devices, device creation, mounts/remounts, privileged APIs,
hard-link creation, ACL/ownership changes, disconnect/crash tests, native fstatfs
execution or combined policy enforcement, mock mount/device scenarios, producer
staging, customer/arbitrary exports, candidate runtime/builds, schema/JCS installation,
network-denied product tests, T01–T11/Q1–Q5. Unchanged Node negative control and snapshot
sample retain B01 evidence; they were not rerun for this policy research.

Acceptance mapping: A1 threat/ordering table; A2 two strategies and D1–D9/SDK evidence;
A3 no native executable needed; A4 concrete source-grounded no-go plus rerun existing
synthetic controls, **not** an enforcement pass; A5 explicit verdicts/gates; A6 B01
history and exact checks. Coordinator reproduction and founder exact-revision
approval were pending at the original handoff; the subsequent accepted merge is
recorded above.
