# B01 runtime, contract and store decision frontier

Status: **Frontier-ready** research for [issue #8](https://github.com/Himanshu-singh04/hooktrace/issues/8), 2026-11-19.
Owner confirmation of ADR-1–4 remains pending; this is not an accepted ADR or product.

## Assignment and bounds

Original founder instruction: “ok proceed”, responding to the first bounded decision
tasks including runtime and payload/storage choices for HookTrace. The full refined
assignment and A1–A6 acceptance criteria are preserved in issue #8.

Bound: compare Node/TypeScript with a simpler runtime; exercise descriptor-relative
no-follow acquisition and transactional synthetic storage on this Mac/pendrive;
review two version-grounded Stripe snapshot samples; return exact proposed pins,
tradeoffs, limitations and B02 prerequisites. No importer, product CLI, packaged
handler, live Stripe integration or optional AI implementation belongs in this spike.

Planning/rename PR #5 and provisioning issue #7 are complete. Handoff main was
`87f64dd1fd0840c4567e5476d89c8ca31ff7bc93`; fetched main matched it at research start.
Worker history/OAuth is on pendrive; coordinator history/App key remains on Mac,
per [coordinator verification](https://github.com/Himanshu-singh04/hooktrace/issues/7#issuecomment-6999734294).
Worker inference is development assistance, not product-local AI.

## Decision frontier (A1, A5)

| Decision | Proposed direction | Status / consequence |
| --- | --- | --- |
| ADR-1 runtime | Python modular CLI instead of the original TypeScript/Node proposal | **Proposed**, owner pending. Standard-library descriptor acquisition and SQLite avoid a second runtime/native acquisition addon |
| ADR-2 evidence bundles | Retain frozen files, JSON Schema 2020-12 and RFC8785; Python descriptor-relative acquisition | **Proposed**, owner pending. Synthetic substitution tests pass on Mac/APFS; device-node/mount safety is **unverified/blocking for B02**. Node path-only acquisition is **blocked/no-go** |
| ADR-3 adapter | Interpret only exact `2025-02-24.acacia` subscription snapshots initially | **Proposed**, owner pending. Basil is version-grounded but deliberately unsupported in the first slice |
| ADR-4 synthetic store | SQLite, explicit transactions, rollback journal, close/reopen assertions | **Proposed**, owner pending. Store feasibility passes; packaged handler, isolation and B04 assertions are future work |

ADR-5 optional product AI remains deferred. No runtime switch or new dependency is
accepted by this record. Coordinator review and an explicit owner decision route
these recommendations to B02; green research tests alone do not authorize it.

### Observed environment versus proposed pins

Observed: CPython **3.13.4** at
`/Library/Frameworks/Python.framework/Versions/3.13/bin/python3`, linked SQLite
**3.49.1**; Node **26.13.0** at `/opt/homebrew/bin/node`, npm **11.20.0**;
`tsc` absent from PATH. Mac reports **macOS 27.2.1, arm64**. `diskutil info
/Volumes/AIWorkspace` reports external USB **APFS**, volume UUID
`EAD8504C-B540-47B5-95EA-FBA54591ACAC`, owners disabled. These are observations,
not a supported-platform matrix, permission isolation, or durability certification.

Exact candidate pins below are recommendations for approval, **not installed or
tested stacks**. The older installed Python/SQLite were sufficient for isolated
synthetic feasibility, not recommended as a new product distribution baseline.

| Layer | Preferred Python path | Credible TypeScript/Node alternative |
| --- | --- | --- |
| Runtime | CPython **3.13.18**, same minor as tested, security-only maintenance through October 2028; source-only release | Node **26.13.1 LTS**; also reviewed **24.11.1 LTS** as an older comparison baseline, not recommended over the current security release |
| Tooling | pip **26.3** for a future isolated venv; `unittest`, `venv`, `zipapp` from **3.13.18**; no compiler/test framework dependency | TypeScript **5.9.3**, npm **11.20.0**, `node:test` from **26.13.1**; compile with tsc, distribute JS rather than depend on implicit type stripping |
| Schema | JSON Schema **2020-12**, `jsonschema` **4.25.1**, no optional format extras | JSON Schema **2020-12**, Ajv **8.17.1**, explicit 2020 constructor, no coercion/default insertion/removal of additional fields |
| Canonicalization | RFC **8785**, `rfc8785` **0.1.4** (no runtime dependencies) | RFC **8785**, `canonicalize` **2.1.0** (no runtime dependencies) |
| Fixture store | SQLite **3.54.1** via CPython `sqlite3`; explicitly pin/verify linked library in the future runtime build | Same SQL policy via Node's bundled SQLite; exact linked version and Node API behavior must be recorded and rerun if selected |
| Provider SDK | **None**; versioned stripe-node declarations are research evidence only | **None**; don't install an API client to parse offline files |

Python wins at the Store seam: `os.open(..., dir_fd=parent)` gives the required
native primitive directly, and `sqlite3` supplies transactions without an addon.
Importer/Analyzer/Reporter contracts stay language-neutral. TypeScript offers
stronger compile-time JSON models and familiar JS handler examples, but neither
types nor Ajv supplies secure acquisition. A reviewed C/Rust addon would introduce
ABI/build distribution; a packaged Python helper would introduce two runtimes and
an IPC contract. Neither helper was built or approved. Do not replace it with
`realpath`, `lstat`/reopen, `/dev/fd` path tricks, or just leaf `O_NOFOLLOW`.

Python costs: 3.13.18 has no official binary installer, so its runtime build and
SQLite linkage require a reviewed, unprivileged packaging task; no such build ran.
A plain zipapp cannot contain native wheels such as jsonschema's transitive
`rpds-py`; prefer a venv plus an offline wheelhouse for B02 development. B06 owns
distributable packaging. Node has an official darwin-arm64 archive, but a secure
addon/helper would complicate that simpler installation. Neither path needs hosting.

Reproducibility: experiments use installed standard libraries only, so there is no
new dependency manifest or lockfile. After approval, lock every direct/transitive
wheel and SHA-256, runtime artifact, SQLite build configuration and license; use a
project-isolated venv and pip `--require-hashes --only-binary=:all: --no-index
--find-links` against the reviewed wheelhouse. No sdists/build hooks or installer
scripts. For Node, lock exact package versions/integrities and use `npm ci
--ignore-scripts --offline`. Populate any approved download cache only under
`/Volumes/AIWorkspace/caches/hooktrace`; missing wheels/runtime artifacts block
installation rather than trigger an unreviewed build. Runtime construction itself
needs explicit review. These are future procedures, not an installation claim.

Schema libraries do not replace duplicate-key, byte/depth, safe-number, scope or
cross-reference checks. Python's `json.dumps(sort_keys=True)` is **not RFC8785**:
number formatting and UTF-16 property ordering differ. B02 must verify JCS vectors
(negative zero, exponents, non-BMP keys, invalid surrogates), reject nonfinite/unsafe
numbers and duplicate keys before information is lost, and prohibit remote `$ref`
retrieval. Schema format assertions need explicit activation or local validation.

### Primary version-specific sources and licenses

Read 2026-11-19; references are evidence, not executable instructions. No dependency
archive, SDK, model, runtime or global tool was installed. Package metadata is not
a completed transitive-license/security audit.

- CPython [3.13.18 release](https://www.python.org/downloads/release/python-31318/),
  [versioned os API](https://github.com/python/cpython/blob/v3.13.18/Doc/library/os.rst),
  [tested-version openat implementation](https://github.com/python/cpython/blob/v3.13.4/Modules/posixmodule.c):
  `os.open` dispatches `dir_fd` calls to `openat`; availability is platform-specific.
  [PSF license and historical notices](https://github.com/python/cpython/blob/v3.13.18/LICENSE).
- Node [26.13.1 release](https://nodejs.org/en/blog/release/v26.13.1),
  [versioned fs API](https://nodejs.org/download/release/v26.13.1/docs/api/fs.html#fsopensyncpath-flags-mode),
  [24.11.1 comparison](https://nodejs.org/en/blog/release/v24.11.1): public open
  signatures take path/flags/mode, not a parent directory descriptor.
  [MIT plus bundled third-party notices](https://github.com/nodejs/node/blob/v26.13.1/LICENSE).
- Registry release metadata: [TypeScript 5.9.3, Apache-2.0](https://registry.npmjs.org/typescript/5.9.3),
  [npm 11.20.0, Artistic-2.0](https://registry.npmjs.org/npm/11.20.0),
  [Ajv 8.17.1, MIT](https://registry.npmjs.org/ajv/8.17.1),
  [canonicalize 2.1.0, Apache-2.0](https://registry.npmjs.org/canonicalize/2.1.0).
  Ajv's [versioned 2020 constructor](https://github.com/ajv-validator/ajv/blob/v8.17.1/lib/2020.ts)
  explicitly loads the 2020-12 vocabulary and metaschema.
  Ajv adds fast-uri, fast-deep-equal, require-from-string and json-schema-traverse;
  exact transitive lock/license review remains a B02 prerequisite if selected.
- [pip 26.3, MIT](https://pypi.org/pypi/pip/26.3/json),
  [jsonschema 4.25.1, MIT](https://pypi.org/pypi/jsonschema/4.25.1/json) and its
  [2020-12/format documentation](https://github.com/python-jsonschema/jsonschema/blob/v4.25.1/README.rst).
  Base dependencies: attrs, jsonschema-specifications, referencing, rpds-py;
  pin/license-check these in B02, not optional network/format extras.
- [rfc8785 0.1.4 release metadata](https://pypi.org/pypi/rfc8785/0.1.4/json),
  [implementation contract](https://github.com/trailofbits/rfc8785.py/blob/v0.1.4/README.md),
  [Apache-2.0 license](https://github.com/trailofbits/rfc8785.py/blob/v0.1.4/LICENSE),
  [RFC8785 sections 3.1–3.2 and Appendix B](https://www.rfc-editor.org/rfc/rfc8785).
- SQLite [observed 3.49.1](https://www.sqlite.org/releaselog/3_49_1.html),
  [proposed 3.54.1](https://www.sqlite.org/releaselog/3_54_1.html),
  [transaction guarantees](https://www.sqlite.org/transactional.html),
  [public-domain dedication](https://www.sqlite.org/copyright.html). Upstream
  crash-test claims are not evidence that this USB device survives power loss.

## Acquisition experiment (A2)

[acquisition.py](../experiments/b01/acquisition.py) is restricted to its built-in
tests and their own generated synthetic trees, not customer/arbitrary trees or a
reusable acquisition API. It rejects nonabsolute roots and any root `..` component
before opening descriptors; it does not normalize or resolve those inputs.
It opens `/` as the trusted anchor,
walks every root component with `O_DIRECTORY|O_NOFOLLOW` relative to retained
directory descriptors, then traverses the source identically. It applies the same
leaf procedure to `manifest.json` and nested source bytes. `fstat` verifies directory
and regular-file types; device/inode identities match synthetic setup oracles.
Read/hash/size/metadata checks use that same descriptor, and `ExitStack` owns closure.
`O_NONBLOCK` allows the generated FIFO to be rejected before a blocking read, but
does not make device-node opens harmless: opening occurs before `fstat` rejection.

Eleven passing tests cover positive controls, invalid roots with zero `os.open`
calls/recorded descriptors, root/ancestor symlinks introduced before
and after pinning, leaf swaps before/after opening, in-place mutation, FIFO/directory
rejection, invalid relative paths and four injected failure boundaries. Every opened
descriptor is checked for `EBADF` after success or exception. Post-open renames may
change ctime; the acceptable outcomes are original pinned bytes or mutation rejection,
never acceptance of outside-sentinel bytes. Schedules are deterministic hooks, not
probabilistic racing threads. Ordinary path writes are only synthetic test setup.

[node-path-control.cjs](../experiments/b01/node-path-control.cjs) provides a negative
control on Node 26.13.0: normal read returns `original`, leaf symlink fails `ELOOP`,
but substituting the ancestor redirects an `O_NOFOLLOW` path open to
`outside-sentinel`. `fs.openat` is undefined. This rejects the path-only design, not
every possible Node native helper. Python is the explicit alternative recommendation.

**Unverified/blocking B02 prerequisite:** establish and review an enforceable
device-node/mount threat policy before using acquisition on arbitrary exports.
The research assumes only its generated regular files, directories, symlinks and
FIFO, with no device nodes, hostile mounts or external tree mutation except test
hooks. A device open may have side effects before rejection; mount substitution
is not addressed. No safe production policy was established by this spike.
Pre-`lstat` followed by opening is not a race-safe remedy. No device creation,
privileged tests, mount changes or customer trees were used. These results do not
establish full secure acquisition readiness.

Other limits: this is acquisition feasibility, not immutable freezing/publication. It
does not implement declared-source hash validation, full importer limits, hard-link
policy, a filesystem snapshot, protection from an authorized in-place writer,
mount replacement, permission sandboxing, crash, unplug or power-loss tests. Owners
disabled on this volume is not changed. Rerun on the approved runtime/build/volume;
unavailable primitives must fail closed with `PLATFORM_UNSUPPORTED` in B02.

## Stripe snapshot boundary and provenance (A3)

Two primary, generated-from-OpenAPI declaration sets were reviewed:

| API version | Exact primary version binding | Subscription and item evidence |
| --- | --- | --- |
| `2025-02-24.acacia` | [stripe-node v17.7.0 apiVersion](https://github.com/stripe/stripe-node/blob/v17.7.0/src/apiVersion.ts) | [Subscription](https://github.com/stripe/stripe-node/blob/v17.7.0/types/Subscriptions.d.ts) has top-level `current_period_start/end`; [SubscriptionItem](https://github.com/stripe/stripe-node/blob/v17.7.0/types/SubscriptionItems.d.ts) does not |
| `2025-03-31.basil` | [stripe-node v18.0.0 apiVersion](https://github.com/stripe/stripe-node/blob/v18.0.0/src/apiVersion.ts) | [Subscription](https://github.com/stripe/stripe-node/blob/v18.0.0/types/Subscriptions.d.ts) removes these fields; [SubscriptionItem](https://github.com/stripe/stripe-node/blob/v18.0.0/types/SubscriptionItems.d.ts) adds them |

Stripe's [dated Basil breaking-change note](https://docs.stripe.com/changelog/basil/2025-03-31/deprecate-subscription-current-period-start-and-end)
independently describes that move and changed `previous_attributes` in updated
webhooks. A missing top-level period in Basil is not missing billing activity;
multiple items cannot be collapsed to one subscription period by guessing.

Hand-authored [Acacia](../experiments/b01/acacia.snapshot.json) and
[Basil](../experiments/b01/basil.snapshot.json) samples retain only the fields needed
to illustrate this difference and common identity/status context. All IDs and values
are invented; samples are intentionally partial, not complete Stripe response schemas,
real deliveries, or a test of SDK/provider compatibility. `snapshots.py` checks the
reviewed period locations and types in these examples, not an importer. The API version
labels are grounded in the tagged primary schemas above, not inferred from fixtures.

| Input | Proposed B02 interpretation |
| --- | --- |
| Exact `2025-02-24.acacia`, snapshot `customer.subscription.created/updated/deleted`, embedded `object=subscription` | Supported narrow identity extraction: event ID/type/version/created, object/subscription ID, customer ID (string or expanded object's ID), trigger request/idempotency key and evidenced scope; raw bytes preserved |
| Exact `2025-03-31.basil` | `unsupported_version`; retained inert context, no Acacia field-path fallback |
| Other, missing or unrecognized API versions | `unsupported_version`; never silently treat as latest |
| Thin events | Outside initial interpretation boundary, retained unsupported context; no resource fetch |
| Other event types, including invoices | `unsupported_type`; no invoice/access policy inference |
| Recognized version/type but missing required identity data | `insufficient`; no invented values or provider authenticity claim |

This is proposed support, not shipped compatibility. Acacia periods/status are raw
provider evidence, not new normalized application-state fields or an access rule.
Created/deleted variants, expanded/deleted customer shapes and missing-field/scope
cases need reviewed B02 fixtures. Unknown account stays unknown; `pending_webhooks=0`
and `status=active` prove neither local handler execution nor persisted access.

Provenance/license: source declarations are Stripe/Ask Bjørn Hansen MIT-licensed
([v18.0.0 license](https://github.com/stripe/stripe-node/blob/v18.0.0/LICENSE)); no SDK
or declaration text is vendored. Stripe website documentation is cited, not relicensed
as MIT. Our samples are original research artifacts in this repository, not copied
provider fixtures; this task grants no package/public fixture distribution license.
No Stripe keys, account, CLI or live API call was used.

## Transactional store experiment (A4)

[store.py](../experiments/b01/store.py) uses the observed SQLite 3.49.1 through
stdlib `sqlite3`: explicit `BEGIN IMMEDIATE`/`COMMIT`/`ROLLBACK`, `isolation_level=None`,
`journal_mode=DELETE`, `synchronous=FULL`. State, cancellation tombstone and processed
event ID occupy three tables in one transaction. A `NOT NULL` primary key enforces
non-null deduplication; the experiment boundary accepts only string IDs of 1–128
ASCII letters/digits or `_.:-`, rejecting invalid IDs before any transaction begins.
Every operation uses one synthetic subscription; no imported payload or handler runs.

Five passing tests demonstrate: active state read after close/reopen; cancellation
and dedup recorded together; duplicate causes zero additional writes; injected faults
after each of the three writes roll everything back to the prior reopened state;
retry succeeds; tombstone survives reopen and prevents a later synthetic update from
restoring access; transactional reset empties all tables and permits reuse of event IDs.
Invalid IDs (including repeated nulls) leave state, write count and existing/absent
transaction state unchanged. A direct null insertion also fails the database's
`NOT NULL` constraint, with unchanged reopened state. These are fresh disposable
databases; no product migration is introduced.
Each read-back uses a fresh connection and `integrity_check=ok`; returns/logs alone
are not the oracle. Temporary databases and generated payloads live in a fresh owned
cache directory outside Git and are cleaned after each test.

Alternative: one JSON document containing state/tombstones/event IDs could be written
to a temporary file then renamed atomically. It is inspectable and dependency-free,
but requires us to implement locking, full-file rewrites, rollback, uniqueness and
recovery discipline. SQLite supplies those invariants and bounded single-writer
transactions without a server. WAL is unnecessary for this isolated single-writer
experiment and adds sidecar/checkpoint handling. Neither JSON-store nor WAL was tested.

Limits: no concurrent-reader/writer stress, process-kill recovery, full disk, corrupt
DB, USB unplug, power loss or future SQLite 3.54.1 build was tested. Database inputs
are always created by the experiment, never customer-provided SQLite files. This is
local storage feasibility, not B04, a universal cancellation rule, delivery evidence,
production execution evidence or production causality.

## Independent reruns and outcomes (A6)

Run from `/Volumes/AIWorkspace/projects/hooktrace` on the observed Mac. Scripts create
only fresh directories under `/Volumes/AIWorkspace/caches/hooktrace/b01`, remove their
own temporary files, and make no network calls. No install step is required.

```sh
python3 experiments/b01/acquisition.py
node experiments/b01/node-path-control.cjs
python3 experiments/b01/store.py
python3 experiments/b01/snapshots.py
python3 scripts/check_repository.py
python3 -m unittest discover -s scripts -p 'test_*.py'
/Volumes/AIWorkspace/caches/actionlint/1.7.12/actionlint -shellcheck= -pyflakes=
git diff --check
```

Observed experiment exits: **0** for all four; acquisition **11 tests passed**,
Node **expected path-only NO-GO confirmed**, store **5 tests passed**, samples
**1 test passed**. After staging all new files: repository formatting/links **passed**,
policy unit tests **25 passed**, actionlint **exit 0**, `git diff --check` and
`git diff --cached --check` **exit 0**. SDD comparison against both handoff main and
the required template found **55 identical headings**, no clarification placeholders.
Remote PR-record and CI outcomes are recorded in the PR timeline. Mac research is manually rerunnable;
existing GitHub CI checks repository/policy, not these Mac/APFS claims.

Coordinator correction round R1–R3: the reviewed baseline had 10 acquisition and
3 store tests passing, but missed relative-root misinterpretation and nullable
dedup IDs. The added regressions now bring those suites to 11 and 5 passing tests.
Repository check, 25 policy tests, actionlint, diff checks and SDD heading preservation
were rerun successfully. Unchanged Node/sample results above are retained from the
initial worker run and coordinator verification, not claimed as new reruns. R2's
device/mount risk remains an explicit unverified B02 blocker, not a fixed mechanism.

Research retrieval failures: Python urllib failed certificate verification against
PyPI; used curl with verification enabled instead, without modifying trust settings.
One multi-source curl inspection hit the 120-second command timeout; bounded retries
retrieved the relevant primary sources. Initial PR title used unsupported `research:`
and was corrected to `chore:`. Sourcery appended a summary after the co-author trailer,
causing `pr-record` failures; its summary was retained and the final trailer restored.
No product T01–T11, Q1–Q5, clean-machine install, dependency-library conformance suite,
network-isolation test or pilot was run. This record does not claim those results.

## B02 prerequisites and next route

1. Coordinator independently reruns the research and reviews each A1–A6 criterion;
   owner confirms or rejects ADR-1–4 recommendations for the reviewed revision.
2. Approve the exact runtime build and SQLite linkage; prepare a reproducible local
   runtime/dependency lock with licenses, then rerun acquisition/store and schema/JCS
   vectors on it. Future candidate pins have not inherited the installed-stack results.
3. Review the explicit Acacia-only support matrix and full narrow-slice fixtures,
    including created/deleted, unsupported Basil, thin/unknown versions and missing scope.
4. Resolve the unverified device-node/mount acquisition policy above before arbitrary
   export-tree acquisition; synthetic FIFO and symlink tests do not satisfy this gate.
5. Open a bounded B02 issue/branch for one manifest, two events, one attempt, one
   handler observation and one state snapshot. Implement freeze/validate/normalize
   with located errors, declared hash/size checks, invariant enforcement and interruption
   tests. No report generation, networking, AI or fixture execution in that slice.

The expensive-to-reverse choice is the secure Store/runtime boundary. Python removes
the helper seam; Node remains viable only after a separately reviewed secure helper.
Runtime artifacts, dependency locks and B02 implementation remain blocked on that
owner choice. The source experiments are disposable research, not production modules.
