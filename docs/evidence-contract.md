# Evidence contract v1 — proposal

Status: draft, no parser or schema exists yet. Applies to HT-01–HT-09.
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
```

Source pointers address the parsed source: for JSONL, prefix with `/line/<1-based>`
then the RFC6901 pointer into that line. Whole-file evidence uses the empty pointer.
All refs resolve inside this bundle; IDs are unique per collection and references
carry collection-specific fields. Empty arrays mean “none supplied,” never “none occurred.”
Strings have a proposed 16 KiB limit except raw files; size/depth limits are in testing.

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
  id: ID; path: string; sha256: Hash; bytes: number;
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
paths, `..`, symlinks, devices, archives, and path escapes. File names in the frozen
store are generated from hashes, never copied from executable/path-bearing payloads.
Freeze exact bytes before parsing; verify declared byte counts/hashes against the frozen
copies. Hash the exact manifest bytes separately. References refer to these copies.
The frozen-manifest file's own SHA-256 is stored in the report, avoiding a self-hash.
Capture timestamps are exporter assertions; import wall-clock time belongs in a run log.
Any redaction creates a new source and hash; do not mutate the frozen original.
Reject inconsistent scope assignments rather than silently overriding raw `livemode`,
`account`, or `context`. Missing account/environment identity stays unknown and prevents
cross-source confirmed links unless an explicitly evidenced scope mapping resolves it.

## Normalized input records

Stripe payloads use a version-pinned reviewed adapter; other input kinds supply the
same normalized fields below through `normalized_v1`. Importer assigns `id`, `origin`,
and validated scope references; it must retain every contributing source ref.
The aggregate record file has the following exact root shape:

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
  eventId: string | null; endpointId: string | null; providerAttemptId: string | null;
  requestId: string | null; sentAt: Time | null; receivedAt: Time | null;
  arrival: { streamId: ID; index: number } | null; // observed receiving-stream ordinal
  httpStatus: number | null; // integer 100..599
  transport: "response" | "timeout" | "connection_error" | "unknown";
  retryOfAttemptId: ID | null; // only an explicit source relationship
};
type Handler = Base & {
  executionId: string | null; eventId: string | null; attemptId: ID | null;
  requestId: string | null; subscriptionId: string | null;
  observedAt: Time | null;
  phase: "started" | "completed" | "failed" | "write_claimed";
  transactionId: string | null; errorCode: string | null;
};
type Snapshot = Base & {
  subscriptionId: string; capturedAt: Time | null; storeId: string;
  readKind: "persisted_read" | "transactional_read" | "unknown";
  transactionId: string | null; executionId: string | null;
  values: { [field: string]: Json }; // explicit captured subset, not a full DB claim
  absentFields: string[]; // explicit observed absence; missing key otherwise unknown
};
```

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
Snapshots permit an allowlisted domain subset and must exclude credentials.
Imported schema support is not a general payment-policy validation.

## Relationships and ordering

```typescript
type Node = { collection: "events" | "attempts" | "handlers" | "snapshots"; id: ID };
type Link = {
  id: ID; from: Node; candidates: Node[];
  relation: "delivery_of" | "execution_for" | "state_for" | "retry_of" | "possible_duplicate";
  confidence: "explicit" | "candidate" | "ambiguous" | "unresolved";
  basis: ("event_id" | "attempt_id" | "execution_id" | "request_id" |
    "transaction_id" | "object_type" | "subscription_id" | "scope_unknown")[];
  refs: Ref[]; reason: string;
};
type Order = {
  id: ID; members: Node[];
  basis: "observed_arrival" | "fixture_permutation";
  streamId: ID; refs: Ref[];
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

Arrival order exists only within one observed receiving stream; unique nonnegative
indices define it, gaps remain visible. Never synthesize indices from file order,
`created`, signature time, or timestamps from unsynchronized clocks. Separate streams
form partial orders. Stable ID sorting is permitted only for display, labeled as such.
A fixture permutation is an explicitly selected model input, never observed production order.

## Output records and reports

```typescript
type Finding = {
  id: ID; ruleId: string; ruleVersion: string;
  kind: "observation" | "gap" | "conflict" | "hypothesis";
  severity: "info" | "review"; summary: string;
  nodes: Node[]; linkIds: ID[]; refs: Ref[];
  limitations: string[]; // required; nonempty for hypotheses/gaps
};
type Assertion = {
  id: ID; snapshotId: ID; field: string; expected: Json; actual: Json;
  result: "pass" | "fail"; // actual is a captured value, never fabricated for unknown
};
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
synthetic fixture/run artifacts, never imported customer evidence. Assertions can
only evaluate supplied fields; missing read-back yields `incomplete`, no assertion
with fabricated `actual`. Fixture event IDs in permutations may repeat for duplicate
tests. Reports cannot imply one failed assertion describes a production root cause.
Artifact IDs must be globally unique across the report (prefix with fixture run ID);
artifact paths resolve beneath that run's output directory with the same path rules
as Source. Retain definition, handler, initial-state, and read-back artifacts matching
the declared hashes; every fixture Ref must resolve there. Snapshot `scopeId` must
equal that run's `scope.id`. Imported and synthetic records cannot be correlation targets
for one another. Seeds are nonnegative safe integers; permutation IDs must belong to
the packaged fixture definition. Empty permutation is invalid.
All findings cite source refs or declare an evidence gap with refs to the bounded
input being searched. Aggregate counts count records, not unique incidents or failures.
No global “business success” boolean is inferred from this model.

Canonical derived JSON uses RFC8785 serialization and sorted set-like collections by
stable ID; ordered permutations remain ordered. IDs derive from source hash/pointer
plus record kind (or rule/version + sorted evidence IDs for findings), with collision
checks. Identical frozen input, tool/rules versions, fixture inputs, and limits must
produce byte-identical JSON and Markdown; durations/host paths/run timestamps stay
in separate local logs. Markdown renders the JSON, escapes input HTML/links, and
contains a source-hash/pointer index usable without network access.

## Evolution, errors, and retention

Reject unknown major schema versions; no implicit migrations. A future migration
creates a new derived bundle with parent hash and tool version, preserving originals.
Proposed diagnostics: `INPUT_INVALID`, `VERSION_UNSUPPORTED`, `SCOPE_CONFLICT`,
`REFERENCE_INVALID`, `HASH_MISMATCH`, `LIMIT_EXCEEDED`, `IO_FAILED`,
`FIXTURE_INCOMPLETE`, and `INTERNAL_ERROR`. Unsupported Stripe interpretation is
retained with a finding; unsupported HookTrace schema is a fatal validation error.
Use redacted messages with record refs, never dump payloads or credentials.
Fatal validation prevents publishing a report; an incomplete fixture may appear in
a complete investigation report with its explicit incomplete outcome.
Store bundles outside Git; retain until the operator deletes them. No background
upload, retention daemon, telemetry, or guarantee of secure deletion on flash media.
See [operations](operations.md) for interruption, recovery, and sharing procedures.
