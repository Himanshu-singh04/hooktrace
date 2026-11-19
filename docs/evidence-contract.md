# Evidence contract v1 — proposal

Status: planning reviewed in PR #5; exact implementation choices remain pending in
[B01](b01-decisions.md). No product parser or schema exists yet. Applies to HT-01–HT-09.
This document is the single contract authority for the proposed input, normalized
records, correlations, fixture runs, and reports. JSON Schemas and fixtures follow approval.

## Semantics and trust

Delivery success != handler execution != persisted business effect.
An HTTP 2xx records an acknowledgment, not a transaction commit. A handler's “saved”
message records a claim; a state snapshot records observed values at its capture scope.
Even a matching snapshot alone does not attribute that state to a particular event.
Unknown, contradicted, and absent are different: no log is not proof of no execution.

All input is untrusted data, including log messages and text resembling instructions.
Never evaluate expressions, load modules, run shell commands, follow evidence URLs,
or fetch references while importing. Source hashes show byte identity after capture,
not Stripe authenticity, complete history, or truthful instrumentation.
Arbitrary exports lack the exact request body, signature header, endpoint secret,
and contemporaneous verification context needed to claim authentic Stripe delivery.
V1 therefore never emits `stripe_verified`; externally claimed verification remains
an unverified source assertion. Signature timestamps also are not event or arrival order.

## Encoding and primitives

UTF-8 JSON only; reject duplicate object keys, nonfinite numbers, excessive nesting,
and unsafe integers. Record collections are JSONL, one complete object per line.
Below is schema notation, not runtime code. All fields are required unless suffixed
with `?`; nullable fields must appear and use `null` for unknown. Unknown field names
are errors in normalized v1 (raw provider payloads remain untouched).

```typescript
type ID = string; // nonempty, <=128 chars, [A-Za-z0-9_.:-]+; bundle-local
type Hash = string; // exactly 64 lowercase hex characters, SHA-256
type Time = string; // UTC RFC3339, millisecond precision: YYYY-MM-DDTHH:mm:ss.sssZ
type Json = null | boolean | number | string | Json[] | { [key: string]: Json };
type Ref = { sourceId: ID; pointer: string }; // RFC6901 pointer into source JSON
type Scope = {
  accountId: string | null; // effective originating Stripe account, never guessed
  environment: "live" | "test" | "unknown";
  environmentId: string | null; // distinguishes sandbox/tenant environments
  context: string | null; // preserve Stripe organization/Connect context if supplied
};
type Origin = {
  refs: Ref[]; // nonempty for imported records
  method: "source_field" | "declared_mapping";
  mappingId: ID | null; // required non-null for declared_mapping
};
type Base = { id: ID; scopeId: ID; origin: Origin };
type Namespace = {
  application: string; deployment: string; domain: string;
  basis: "source_asserted" | "operator_mapping"; refs: Ref[];
};
type LocalId = { value: string; namespace: Namespace | null };
```

Source pointers address the parsed source: for JSONL, prefix with `/line/<1-based>`
then the RFC6901 pointer into that line. Whole-file evidence uses the empty pointer.
All refs resolve inside this bundle; IDs are unique per collection and references
carry collection-specific fields. Empty arrays mean “none supplied,” never “none occurred.”
Strings have a proposed 16 KiB limit except raw files; size/depth limits are in testing.
Namespace strings and LocalId values are nonempty; unknown namespace is `null`, not
an empty/shared default. Namespace refs must cite captured application/deployment and
identifier-domain metadata, not merely the repeated identifier or namespace label.

## Frozen input bundle and provenance

```typescript
type Manifest = {
  schemaVersion: "hooktrace.input/1"; bundleId: ID;
  sources: Source[]; scopes: ScopeRecord[]; mappings: Mapping[];
};
type ScopeRecord = {
  id: ID; value: Scope; origin: Origin;
  coverage: { start: Time | null; end: Time | null;
    completeness: "partial" | "source_claimed_complete" | "unknown"; refs: Ref[] };
};
type Source = {
  id: ID; path: string; sha256: Hash; bytes: number; // id assigned before file hashing
  kind: "stripe_events" | "delivery_attempts" | "handler_observations" |
    "state_snapshots" | "scope_metadata";
  format: "json" | "jsonl"; capturedAt: Time | null;
  producer: string; // exporter/instrumentation description, not an authenticity claim
  provenance: "synthetic" | "operator_export";
  redacted: boolean; parentSha256?: Hash; // only supplied if actual prior bytes were hashed
  signatureEvidence: "unavailable" | "external_claim_only";
};
type Mapping = {
  id: ID; sourceId: ID; scopeId: ID; adapter: "stripe_snapshot_v1" | "normalized_v1";
  recordsPointer: string; // JSON array pointer or empty for JSONL
  declaredApiVersion: string | null;
};
type FrozenManifest = {
  schemaVersion: "hooktrace.frozen/1"; inputManifestSha256: Hash;
  manifest: Manifest; normalizerVersion: string; normalizedSha256: Hash;
};
```

Paths are relative regular files beneath the selected input root: reject absolute
paths, `..`, symlinks, devices, archives, and path escapes. Proposed acquisition pins
the operator-selected root as an open directory descriptor, reached component-by-component
from a trusted directory anchor with symlink following disabled. Validate its directory
type/identity with descriptor metadata. Resolve each source component relative to retained
directory descriptors using no-follow directory opens, then open the leaf no-follow and
require a regular file via `fstat`. Apply this to the manifest too; never validate a path
and subsequently reopen it by name. Freeze, count, and hash bytes read from that same
validated descriptor into an exclusively created owned temporary file; parse only the
frozen copy. A replaced path must not redirect the read to a new symlink target.
Close descriptors on success/failure; check metadata before/after reading and reject
detected concurrent mutation or declared size/hash mismatch. This is not a guarantee
of a filesystem-wide snapshot or protection against an authorized in-place writer.
File names in the frozen store are generated from hashes, never from payload paths.
Hash the exact manifest bytes separately. References refer to the frozen copies.
The OS/runtime must provide verified descriptor-relative/no-follow semantics: B01 must
prove feasibility on the supported Mac/runtime/filesystem, including parent/leaf swaps.
Do not assume ordinary Node path APIs or final-component `O_NOFOLLOW` secure ancestors.
Any required native helper/runtime change needs review; unsupported platforms fail closed
with `PLATFORM_UNSUPPORTED`, without a realpath/lstat-then-open fallback.
The frozen-manifest file's own SHA-256 is stored in the report, avoiding a self-hash.
Capture timestamps are exporter assertions; import wall-clock time belongs in a run log.
Any redaction creates a new source and hash; do not mutate the frozen original.
Reject inconsistent scope assignments rather than silently overriding raw `livemode`,
`account`, or `context`. Missing account/environment identity stays unknown and prevents
cross-source confirmed links unless an explicitly evidenced scope mapping resolves it.
Source IDs are stable operator-assigned labels, unique in the manifest and independent
of content hashes. Separately declared byte-identical exports retain distinct Source
entries, original paths/provenance, and record origins. Frozen storage may share a
physical hash-addressed byte copy, but must not merge those logical observations.
Each data source has exactly one mapping in v1; metadata sources need none. Declare
another source ID to represent a separate export, not overlapping mappings of one row.
For coverage, validate parsed UTC instants: when both endpoints are non-null require
`start <= end`; equality is allowed, inversion is `INPUT_INVALID`. A null endpoint
remains unknown (not infinity or a bound inferred from event times). Even a valid range
and `source_claimed_complete` describe a source assertion, not proven complete coverage.

## Normalized input records

Stripe payloads use a version-pinned reviewed adapter. The `normalized_v1` adapter
accepts the source-local input rows defined after the output types below, not copies
of derived records. Importer assigns `id`, `origin`, and validated scope references;
it retains every contributing source ref. The derived aggregate has this exact shape:

```typescript
type Evidence = {
  schemaVersion: "hooktrace.evidence/1";
  events: Event[]; attempts: Attempt[]; handlers: Handler[]; snapshots: Snapshot[];
};
type Event = Base & {
  eventId: string; eventType: string; apiVersion: string | null;
  format: "snapshot" | "thin" | "unknown";
  createdUnixSeconds: number | null; // nonnegative safe integer; never arrival
  objectId: string | null; objectType: string | null;
  subscriptionId: string | null; customerId: string | null;
  triggerRequestId: string | null; idempotencyKey: string | null;
  payloadHash: Hash; // hash of canonical parsed event JSON; distinct from raw source hash
  interpretation: "supported" | "unsupported_version" | "unsupported_type" | "insufficient";
};
type Attempt = Base & {
  producerNamespace: Namespace | null;
  eventId: string | null; endpointId: string | null; providerAttemptId: string | null;
  requestId: LocalId | null; sentAt: Time | null; receivedAt: Time | null;
  arrival: { streamId: LocalId; index: number } | null; // observed receiving-stream ordinal
  httpStatus: number | null; // integer 100..599
  transport: "response" | "timeout" | "connection_error" | "unknown";
  retryOfAttemptId: ID | null; // only an explicit source relationship
};
type Handler = Base & {
  producerNamespace: Namespace | null;
  executionId: LocalId | null; eventId: string | null; attemptId: ID | null;
  requestId: LocalId | null; subscriptionId: string | null;
  observedAt: Time | null;
  phase: "started" | "completed" | "failed" | "write_claimed";
  transactionId: LocalId | null; errorCode: string | null;
};
type SnapshotFields = { // closed allowlist for hooktrace.subscription-state/1
  access: boolean;
  status: "incomplete" | "incomplete_expired" | "trialing" | "active" |
    "past_due" | "canceled" | "unpaid" | "paused";
  cancellationTombstone: boolean;
  processedEventCount: number; // nonnegative safe integer
  mutationCount: number; // nonnegative safe integer
};
type SnapshotField = keyof SnapshotFields;
type Snapshot = Base & {
  producerNamespace: Namespace | null;
  subscriptionId: string; capturedAt: Time | null; storeId: LocalId;
  readKind: "persisted_read" | "transactional_read" | "unknown";
  transactionId: LocalId | null; executionId: LocalId | null;
  valuesSchema: "hooktrace.subscription-state/1";
  values: Partial<SnapshotFields>; // optional captured fields; no other keys
  absentFields: SnapshotField[]; // explicit observed absence; otherwise unknown
};
```

The values schema is proposed for imported and fixture snapshots alike. Reject unknown
schema versions, unapproved keys (including credential/free-text/metadata fields), nested
objects/arrays, nulls, and wrong field types before normalization or report publication.
Booleans cannot be strings or 0/1; status is exactly the enum above; counts are integers
0–9007199254740991. Do not coerce, silently drop, or automatically rename fields. New
fields require a reviewed schema version. Empty `values` is allowed for partial evidence.
`absentFields` must contain unique allowlisted names and be disjoint from `values` keys;
overlap or duplicates are `INPUT_INVALID`. A field in neither is unknown. Recorded false,
zero, and an explicit absence have different meanings; absence is not a default value.

Raw application rows use these types; all omitted Base/output fields are forbidden:

```typescript
type InputRowRef = {
  sourceId: ID; collection: "attempts" | "handlers" | "snapshots"; rowId: ID;
};
type InputAttempt = Omit<Attempt, keyof Base | "retryOfAttemptId"> & {
  rowId: ID; retryOfAttemptRef: InputRowRef | null;
};
type InputHandler = Omit<Handler, keyof Base | "attemptId"> & {
  rowId: ID; attemptRef: InputRowRef | null;
};
type InputSnapshot = Omit<Snapshot, keyof Base> & { rowId: ID };
```

`rowId` is a source-local operator/exporter label, unique within that source. JSON
array/JSONL rows use the type matching Source.kind. Both reference fields must target
`attempts`; source-qualified references are required even within the same file.
`normalized_v1` accepts only delivery_attempts/handler_observations/state_snapshots;
stripe_events uses `stripe_snapshot_v1`, and scope_metadata is citation-only metadata.
For example, handler row `h1` can carry
`attemptRef: {sourceId: "deliveries", collection: "attempts", rowId: "a1"}`.
Neither file contains a derived record ID or its own hash. Raw Stripe events remain
unmodified; their provider event IDs are not these row IDs. The snapshot adapter
assigns observation IDs by source/pointer; application rows associate events by `eventId`.

Normalization has two passes over frozen sources:
1. Validate row shapes/unique labels and manifest scope assignments. Assign each output
   ID from the source identity/hash/pointer/kind rule below; build the qualified-row
   lookup. Preserve the original row (including rowId/ref fields) in raw evidence.
2. Resolve all qualified refs, including forward/cross-file refs; require the named
   source, row and collection to exist, then rewrite to `attemptId`/`retryOfAttemptId`.
   Validate target type, matching supplied event IDs, scope/endpoint/producer compatibility,
   namespace citation targets, and retry self-links or cycles. Reject dangling/wrong-type
   refs, known incompatible boundaries/identities, and cycles
   with located diagnostics before publishing. Unknown boundaries retain the declared
   reference with a gap/candidate link, never an explicit correlation.

The output ID rule never depends on rewritten links or another derived ID. Merely
resolving a syntactic reference does not establish its truth or correlation confidence.

All imported rows remain distinct observations, including repeated event exports.
`eventId` is the provider event identifier; `id` identifies an observation in this bundle.
Matching event IDs with different payload hashes create a conflict, not an overwrite.
Matching object/type on different event IDs suggests possible semantic duplication,
not equivalence or permission to discard. Explicit retry links must be acyclic and
within compatible scope/endpoint; multiple deliveries alone do not prove retry intent.
Handler completion does not prove a write; transaction IDs remain source assertions.
Event `triggerRequestId` is Stripe's originating API request, not a webhook receipt.
Attempt/Handler `requestId` means the instrumented receiving HTTP request ID; only
those matching namespaces may use the `request_id` correlation basis.
Local execution, transaction, store, and arrival-stream IDs use LocalId too. Namespace
`domain` identifies the actual uniqueness boundary: e.g. instrumentation boot/session,
database/store incarnation for transactions, or receiving-stream epoch. A producer
namespace identifies the emitting application/deployment/instrumentation domain. Reused
IDs across domains are not equivalent, even with identical account and event IDs.
The closed values schema limits normalized state content; it does not certify arbitrary
raw input, identifiers, other string fields, or reports as secret-free. Frozen raw files
can still contain sensitive rejected content; operators must minimize exports and review
redaction before sharing. Do not render rejected field values in diagnostics/reports.
Imported schema support is not a general payment-policy validation.

## Relationships and ordering

```typescript
type Node = { collection: "events" | "attempts" | "handlers" | "snapshots"; id: ID };
type Link = {
  id: ID; from: Node; candidates: Node[];
  relation: "delivery_of" | "execution_for" | "state_for" | "retry_of" | "possible_duplicate";
  confidence: "explicit" | "candidate" | "ambiguous" | "unresolved";
  basis: ("event_id" | "attempt_id" | "execution_id" | "request_id" |
    "transaction_id" | "object_type" | "subscription_id" | "scope_unknown" |
    "namespace_unknown")[];
  refs: Ref[]; reason: string; limitations: string[];
};
type Order = {
  id: ID; members: Node[];
  basis: "observed_arrival";
  streamId: LocalId; refs: Ref[];
};
```

`explicit` requires a unique compatible target and an observed identifier relationship,
not a probability score or causality guarantee. `candidate` means one indirect match;
`ambiguous` means multiple possible targets or conflicting direct identifiers;
`unresolved` has zero candidates. Do not choose the closest timestamp as a winner.
Exact account and environment boundaries are mandatory for explicit cross-source
links. Unknown scope can produce candidates only. Same account with incompatible
context needs reviewed mapping, not string similarity. API versions partition payload
interpretation; joining a known event ID does not authorize cross-version field assumptions.

For a link relying on local identity, require compatible evidenced producer namespaces
and the namespace of every compared LocalId; compare only the same identifier family.
Compatibility means matching application/deployment/domain tuples supported by source
metadata for both sides or an explicit operator mapping citing both sides. Equal
unauthenticated strings alone, even inside one source, do not establish that boundary.
Cross-source mappings must explain the shared domain in captured metadata. Unknown
namespaces yield candidates/gaps, never explicit links; incompatible ones exclude a
match. Qualified row references do not bypass this rule. Different known producers
need an evidenced mapping of the shared instrumentation domain, not a guessed join.
Store identity and transaction-domain evidence must prevent treating equal transaction
IDs in different stores as the same commit. Unknown stream namespace cannot form Order.

`explicit` means a direct association supported **within the supplied evidence**.
Namespace/scope metadata and operator mappings are still unauthenticated assertions;
they cannot prove real application identity, authenticity, or causality. Link limitations
must state this, including for same-source matches. Preserve supporting refs and any
conflict; neither namespace equality nor a source hash upgrades trust. Stripe `eventId`
is a provider identifier, separate from local identifier families: linking to an Event
by it still requires compatible evidenced Stripe scope, but does not itself select a
particular application execution, attempt, store, or stream.

Arrival order exists only within one observed receiving stream; unique nonnegative
indices and a compatible evidenced stream namespace define it, gaps remain visible.
Order.members contain only imported Attempt nodes from that stream and compatible scope/
producer; retain unknown-namespace arrival claims as observations without constructing Order.
Never synthesize indices from file order,
`created`, signature time, or timestamps from unsynchronized clocks. Separate streams
form partial orders. Stable ID sorting is permitted only for display, labeled as such.
A fixture sequence exists only in FixtureRun.permutation, never in imported Order.

## Output records and reports

```typescript
type Finding = {
  id: ID; ruleId: string; ruleVersion: string;
  kind: "observation" | "gap" | "conflict" | "hypothesis";
  severity: "info" | "review"; summary: string;
  nodes: Node[]; linkIds: ID[]; refs: Ref[];
  limitations: string[]; // required; nonempty for hypotheses/gaps
};
type Assertion = { [K in SnapshotField]: {
  id: ID; snapshotId: ID; field: K;
  expected: SnapshotFields[K]; actual: SnapshotFields[K];
  result: "pass" | "fail"; // derived, never an independently trusted flag
} }[SnapshotField];
type FixtureRun = {
  schemaVersion: "hooktrace.fixture-run/1"; id: ID;
  fixtureId: ID; fixtureVersion: string; fixtureSha256: Hash;
  handlerVariant: "buggy" | "fixed"; handlerSha256: Hash;
  initialStateSha256: Hash; permutation: ID[]; seed: number;
  scope: ScopeRecord; // synthetic scope, separate from imported scope IDs
  artifacts: { id: ID; path: string; sha256: Hash; bytes: number }[];
  snapshots: Snapshot[]; assertions: Assertion[];
  outcome: "passed" | "failed" | "incomplete";
  limitation: "modeled_scenario_not_production_cause";
};
type Report = {
  schemaVersion: "hooktrace.report/1"; bundleId: ID; frozenManifestSha256: Hash;
  evidenceSha256: Hash; toolVersion: string; rulesVersion: string;
  links: Link[]; orders: Order[]; findings: Finding[]; fixtureRuns: FixtureRun[];
  summary: { events: number; attempts: number; handlers: number; snapshots: number;
    findingsByKind: { observation: number; gap: number; conflict: number; hypothesis: number } };
  limitations: string[];
};
type Diagnostic = {
  schemaVersion: "hooktrace.diagnostic/1"; code: string;
  message: string; refs: Ref[]; retryable: boolean;
};
```

Fixture snapshots use a separate run namespace; their refs resolve into retained
synthetic fixture/run artifacts, never imported customer evidence. Assertions use the
packaged fixture's expected field/value and the named run-local snapshot's `values[field]`
from persisted read-back with verified artifact hashes. Both must satisfy that field's
values-schema type. Derive `pass` iff they are exactly equal: boolean identity, exact
case-sensitive enum string, or equal safe-integer numeric value (1 and 1.0 are equal;
0 and -0 are equal). No coercion, truthiness, tolerance, or arbitrary JSON comparison.
Derive `fail` only for two available valid values that differ. Missing/absent field,
unknown/non-persisted read, invalid read-back type, or unverifiable artifact yields
`incomplete` with a diagnostic; never invent actual=false/null/0 or emit a pass/fail
assertion for that missing check. Invalid read-back bytes may be retained as a run
artifact, but must not appear as a schema-invalid Snapshot in the report. Before
publishing, validate actual against the cited
snapshot, expected against the fixture, and result against this comparison; inconsistent
serialized assertions are invalid, not trusted output. A run is `incomplete` if any
required check lacks evidence; otherwise `failed` if any assertion fails, and `passed`
only if every required fixture assertion exists and passes (no vacuous empty success).
Fixture event IDs in permutations may repeat for duplicate
tests. Reports cannot imply one failed assertion describes a production root cause.
Artifact IDs must be globally unique across the report (prefix with fixture run ID)
and disjoint from every imported Source.id; reject collisions rather than resolving
them across registries. A fixture Ref.sourceId resolves only in that run's artifacts;
an imported Ref resolves only in the frozen manifest. Node, Link, Order, and Finding
never address fixture snapshots. Assertions resolve snapshotId only within their run;
artifact paths resolve beneath that run's output directory with the same path rules
as Source. Retain definition, handler, initial-state, and read-back artifacts matching
the declared hashes; every fixture Ref must resolve there. Snapshot `scopeId` must
equal that run's `scope.id`. Imported and synthetic records cannot be correlation targets
for one another. Proposed fixture `subscription-ordering-v1` defines event tokens U/D;
permutation is an ordered list of 2–8 tokens containing both U and D, repeats allowed.
Default is [D,U]. Seed is an integer 0–4294967295, default 0; this deterministic fixture
does not randomize anything, so seed is recorded but has no behavioral effect. Reject
other fixture IDs/tokens, empty or oversized lists, missing U/D, and invalid seeds.
These limits/defaults apply equally to CLI and internal runFixture calls; the report
records the fully resolved permutation and seed, not omitted option values.
All findings cite source refs or declare an evidence gap with refs to the bounded
input being searched. Aggregate counts count records, not unique incidents or failures.
No global “business success” boolean is inferred from this model.

Canonical derived JSON uses RFC8785 serialization and sorted set-like collections by
stable ID; ordered permutations remain ordered. An imported observation ID is `obs:`
plus SHA-256 of RFC8785 JSON `[Source.id, Source.sha256, rowPointer, collection]`.
Thus separate byte-identical sources produce separate observations with their own
origin refs, while re-importing the same manifest/bytes produces identical IDs.
Reject duplicate source IDs and unexpected derived collisions; never merge rows.
Finding IDs derive from rule/version plus sorted evidence IDs, with collision checks.
Identical frozen input, tool/rules versions, fixture inputs, and limits must
produce byte-identical JSON and Markdown; durations/host paths/run timestamps stay
in separate local logs. Markdown renders the JSON, escapes input HTML/links, and
contains a source-hash/pointer index usable without network access.

## Evolution, errors, and retention

Reject unknown major schema versions; no implicit migrations. A future migration
creates a new derived bundle with parent hash and tool version, preserving originals.
Proposed diagnostics: `INPUT_INVALID`, `VERSION_UNSUPPORTED`, `SCOPE_CONFLICT`,
`REFERENCE_INVALID`, `HASH_MISMATCH`, `LIMIT_EXCEEDED`, `IO_FAILED`,
`PLATFORM_UNSUPPORTED`, `FIXTURE_INCOMPLETE`, and `INTERNAL_ERROR`. Unsupported Stripe interpretation is
retained with a finding; unsupported HookTrace schema is a fatal validation error.
Use redacted messages with record refs, never dump payloads or credentials.
Fatal validation prevents publishing a report; an incomplete fixture may appear in
a complete investigation report with its explicit incomplete outcome.
Store bundles outside Git; retain until the operator deletes them. No background
upload, retention daemon, telemetry, or guarantee of secure deletion on flash media.
See [operations](operations.md) for interruption, recovery, and sharing procedures.
