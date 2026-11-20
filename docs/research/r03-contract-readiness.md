# R03 deterministic contract readiness

Status: **Research ready for review; decide missing-event-ID disposition first**, [issue #22](https://github.com/Himanshu-singh04/hooktrace/issues/22).
Documentation-only gap analysis; proposed dispositions/numeric policies are unadopted.

## Authority and bounds

Founder requested ongoing business/development research during ReleaseLens build
priority and said **“resume everything”**. Coordinator dispatched fixed A1–A6 in issue
#22. Same persistent GPT-6 Astra / OpenCode worker; no subagents or portfolio-file reads.
Successful start **2026-11-20 05:59:23 UTC**; deadline **07:59:23 UTC**, earlier if ready.
One 200–260-line ordered readiness ledger, at most six external primary documents,
three missing-event-ID alternatives and eight paper oracle cases. No implementation.

Exact approved base: `457a84aec693c5ecb07a2ed32e8b0377c40186f0`.
Preserve R02 draft #21 at `737d828bed6af498a66ab961023d4559b633d197`, R01 draft #19
at `5669bacedd5c226dc631a3b76dd77848b886212f` and B01d draft #17 at
`65ecb026453e39f2f64692dafbec416ed5914439`, plus historical review checkouts.
R02/R01 passed coordinator review but remain founder-unapproved; B01d full source
audit remains pending. No pending direction or operator-trust proposal is adopted.

Question: which JSON/schema/numeric/JCS/hash/observation-ID decisions block an
independently checkable synthetic contract specification, and what is the smallest
next decision? Preserve approved Acacia scope, source-truth/correlation limits and
all normative/source/corpus/capture/lock/workflow bytes, including 55 SDD headings.
No executable schemas, goldens/fixtures/harness, SDK/library trials, native probes,
customer/API operations, accounts/outreach, installs/environment changes or spend.
Do not import ReleaseLens numeric policies/runtime results. Intake remains **NO-GO**;
P1–P4 and acquisition/runtime/schema/identity/publication/isolation/product gates persist.

## Recommendation and evidence limits

**Propose retaining an ID-less raw event as cited evidence, omitting its normalized
Event, and reporting the gap.** This is option M2 below, not current behavior. It
preserves useful partial evidence without inventing a provider ID or making every
Event caller handle null. It needs an explicit exception to row normalization and
a deterministic identity rule for source-only findings before implementation.

Confidence is high that the listed contract gaps need decisions; confidence in M2
as the best customer trade-off is conditional. No customer workflow, preparation
cost, incident frequency or willingness to pay was measured. R02's Q1 direction
remains a proposal; this ledger does not adopt it or accelerate the build sequence.

## Six primary documents

All retrieved **2026-11-20**; zero HTTP failures. No linked documents, schemas,
packages or sample programs fetched/executed. RFC8785 is Informational; JSON Schema
2020-12 documents are published draft specifications, not IETF standards-track RFCs.
The Python page identifies 3.13.18 at retrieval; documentation is not a runtime test.

| Source | Exact document and sections used | Relevance and boundary |
| --- | --- | --- |
| S1 | [RFC8259](https://www.rfc-editor.org/rfc/rfc8259.txt), §§2–9 | JSON grammar, duplicate-name interoperability, number precision/range, UTF-8/BOM and Unicode; HookTrace imposes stricter rejection requirements |
| S2 | [RFC8785](https://www.rfc-editor.org/rfc/rfc8785.txt), §§3.1–3.2.4, Appendix B/E | JCS input constraints, binary64 serialization, string preservation, UTF-16 key sorting, array-order preservation and UTF-8 bytes; not arbitrary decimal-lossless identity |
| S3 | [JSON Schema 2020-12 Core](https://json-schema.org/draft/2020-12/json-schema-core), §§4.2.1–4.2.2, 6.2–6.4, 7.6.1 | Mathematical instance equality, lexical information outside schema model, language limits and unanchored regex semantics; schema cannot recover duplicate keys discarded by parsing |
| S4 | [JSON Schema 2020-12 Validation](https://json-schema.org/draft/2020-12/json-schema-validation), §§4.2, 6.1–6.5, 7.1–7.3, 9.2 | Integer means zero fractional part; explicit bounds/required/type checks, string character counts and optional format assertion. An annotation/default is not authority to insert evidence |
| S5 | [RFC6901](https://www.rfc-editor.org/rfc/rfc6901.txt), §§3–7 | Decode `~1` then `~0`; zero-based array indexes with no leading zero, exact Unicode keys, unresolved-pointer error; HookTrace adds JSONL line addressing |
| S6 | [Python 3.13 json documentation](https://docs.python.org/3.13/library/json.html), load/loads/JSONDecoder and “Standard Compliance and Interoperability” | Default float/int conversion, pair/number hooks, permissive NaN/duplicate/lone-surrogate handling, non-UTF-8 byte input support and parser limits; exact selected build/configuration remains unverified |

Approved local sources: [contract](../evidence-contract.md) (**C**),
[B01](../b01-decisions.md) (**B**, especially lines 92–97, 209–222),
[B01b](../b01b-fixture-corpus.md) (**F**, lines 110–135, 171–194), and
[testing](../testing.md) (**T**). Line references below refer to the fixed approved
base above. F supplies field facts and bounded research predicates, not JCS goldens.
Pending [R02 at exact revision](https://github.com/Himanshu-singh04/hooktrace/blob/737d828bed6af498a66ab961023d4559b633d197/docs/research/r02-scope-fit.md)
is provisional context only. No ReleaseLens document, policy or runtime result used.

## Current authority and ordered gap ledger (A1/A5)

**Four separate tests:** schema validity checks allowed representation; provenance
locates captured bytes; correlation checks compatible observed relationships; source
truth remains an assertion. Passing any combination cannot prove authentic delivery,
execution, committed effect or cause. Acquisition must precede handling real inputs.

The order below is a decision dependency order, not a new execution pipeline. D1 can
be decided on paper while D2 remains open; any later parser must enforce D2 before
classification/normalization. “Blocking” means blocking the claimed deterministic
specification, not a newly authorized implementation milestone.

| Priority / decision | Existing authority | Concrete unresolved choice and consequence | Later exit evidence / solo-maintainer burden |
| --- | --- | --- | --- |
| **D1: output when provider ID is missing** | C156 requires `eventId: string`; B216 contemplates `insufficient`; F129–135 explicitly leaves disposition open; C253 preserves observations | A supported-type raw event lacks `id`: no valid Event can express that lack. Skipping silently loses evidence; a hash in `eventId` invents identity. M1–M3 below change different caller contracts | Founder-approved wording and report/caller/count semantics before schema authors encode one outcome; small decision now avoids pervasive nullable/sentinel handling |
| **D2: lossless boundary checks and numeric domain** | C28–32 UTF-8/duplicate/nonfinite/depth/unsafe rejection; C205–210 no coercion, safe counts; B92–97 pre-loss checks; T89–93 caps | `1.0000000000000001` is not an integer, but rounding could make it one; raw `1e-400` could collapse to zero. Clarify token-level checks, allowed raw decimals, BOM/line framing, depth counting and encoded-string byte measurement | Reviewed acceptance table for lexical tokens and parsed values; later bounded parser proof. Costs include retaining enough lexical information and preventing parser-dependent acceptance |
| **D3: schema versus semantic invariants** | C30–32 required/nullable/closed fields; C202–248 closed Snapshot, qualified refs/two passes; C129–141 scope/coverage; T R1/R7/R9/R11 | TypeScript notation is not a schema. `null` is not omission; bool is not count; `format` alone may not reject an invalid date. Row-label uniqueness, cross-file targets, coverage order and cycles need graph/application checks | Map each clause to parser/schema/semantic checker; pin local 2020-12 dialect/format handling, no remote `$ref` retrieval (B96–97). Maintain one trace table instead of inconsistent validators |
| **D4: canonical value and observation preimages** | C162 canonical event hash; C412–417 exact observation formula; B93–95 says sorted Python dumps is not JCS | Parsed strings/numbers must satisfy S2; raw field stripping, decimal rounding or Unicode normalization can change meaning. `rowId` is not the ID preimage's pointer; ref rewrites cannot feed observation IDs | Independent canonical bytes/preimages for admitted cases, exact UTF-8/no-extra-whitespace rules, future selected-library conformance; no library trial here |
| **D5: aggregate hashes, array order and other IDs** | C95–98/359–365 hash-bearing outputs; C412 says sort set-like collections by stable ID; C418 only sketches finding IDs | Which arrays are sets? `Origin.refs`, `absentFields` and `Link.basis` lack IDs; Order.members has arrival semantics. Source-only gaps have no evidence node ID. Link/Order/Assertion/FixtureRun ID recipes and finding collision tie-breaks are incomplete | Field-by-field order/duplicate policy and hash-preimage registry, including digest aliases and file framing. Otherwise two conforming-looking implementations can produce different bytes; largest ongoing spec surface |
| **D6: independent oracle qualification** | F120–127/187–194 limits corpus authority; T56–70 independent review; T Q1/T07 deterministic outputs | Re-importing one's own output or generating expected hashes with the normalizer does not independently check it. JSON determinism alone leaves Markdown escaping/order/newlines and diagnostics underdefined | Reviewer-owned expectations, separate byte/hash verification and traceable disagreements; only then authorize implementation/qualification. Extra review effort is real but unmeasured |

Acacia scope remains exact `2025-02-24.acacia` snapshot
`customer.subscription.created`, `customer.subscription.updated`,
`customer.subscription.deleted`, embedded subscription, narrow identity extraction.
Basil/other/missing versions, thin and other types retain existing unsupported limits.
Raw status/periods cannot become local access, payment or feature-policy conclusions.
Neither this ledger nor a schema validity result expands provider compatibility.

## Missing-event-ID frontier: exact wording proposals (A2)

Shared **old wording**: C156 `eventId: string;`; B216 “Recognized version/type but
missing required identity data” → “`insufficient`; no invented values or provider
authenticity claim”; C253 “All imported rows remain distinct observations, including
repeated event exports.” F131–133 says the variant does not emit an invalid Event and
“Retention/diagnostic/output disposition requires an explicit B02 contract clarification.”
These clauses establish the gap, not any of the following outcomes.

| Option | Exact proposed replacement/addition, **not adopted** | Raw evidence, normalized identity, reports and callers |
| --- | --- | --- |
| **M1 fatal missing ID** | Keep `eventId: string;`. Add: “A raw event without a provider event ID is `INPUT_INVALID`; emit a source-located diagnostic and publish no report. The `insufficient` classification applies only when a provider event ID is available.” | Original input bytes stay untouched; acquired failure artifacts follow separately specified retention/recovery policy. No Event/observation ID or report for the failed bundle; callers handle fatal validation. Lowest type burden, but one incomplete record blocks reporting otherwise useful evidence |
| **M2 raw evidence plus gap (recommended)** | Keep `eventId: string;`. Add: “For an otherwise admissible raw event whose provider event ID is absent, retain its raw source and pointer, emit no normalized Event for that row, and emit a source-cited gap finding. This is an explicit exception to normalized-row emission, not permission to drop raw observations or invent a provider ID.” | Retain each source/pointer separately; no Event ID or event-based link for omitted row. Gap cites Ref(s), not a fabricated Node; summary.events counts emitted Event records and limitations disclose omissions. Callers must distinguish normalized event count from captured rows. Requires source-based finding identity and report wording, but avoids nullable Event propagation |
| **M3 nullable event ID** | Replace `eventId: string;` with `eventId: string \| null;`. Add: “A missing provider event ID yields an Event with `eventId=null` and `interpretation=insufficient`; its observation ID still derives from source/hash/pointer/collection. Null IDs never match other null IDs or receive invented values.” | Raw and normalized observations remain; event count includes ID-less Event. All identity joins/conflicts/report renderers must handle null; observation ID remains distinct from provider identity. Widest schema/caller surface, needs version/compatibility review rather than silently weakening v1 |

M2 is a proposal for genuinely absent IDs, not permission to accept malformed ID
types, invalid JSON, scope contradictions or hash mismatches. Empty strings/null/wrong
types need explicit reconciliation; current field notation and provider expectations
do not fully specify that boundary. Valid IDs with other missing identity can retain
the existing `insufficient` category. Unsupported-version/type handling also needs an
explicit precedence decision when the ID is absent; do not silently apply M2 to it.

Before adoption, coordinator reviews one exact-revision decision PR and founder
approves it under development policy. Reconcile C Event/row preservation/findings/
counts/error clauses, B support matrix, F's unresolved note, T expected dispositions
and affected SDD interfaces/version policy. Keep F's historical research outcomes;
do not rewrite them as proof of the new behavior. Later implementation needs its own
authorization. M2's source-only finding recipe remains D5 work, not an invented hash.

## Numeric, Unicode and canonical identity controls (A3)

**Grammar and information loss:** S1 permits one JSON value with surrounding allowed
whitespace; it excludes `NaN`, `Infinity`, leading-zero numbers and trailing garbage.
C further rejects duplicate decoded keys, unsafe integers and non-UTF-8 input. Names
`"a"` and `"\u0061"` collide after decoding; reject before dictionary construction
loses either member. JSONL needs one complete object per line, not an empty record.
CRLF/final-newline conventions and whether depth counts the root need boundary rules.
S1 allows parsers to ignore BOM; C has not chosen that policy. No silent BOM stripping
or newline rewriting of the raw source used for byte count/hash is justified.

**Numbers:** S3/S4 model mathematical values; `integer` includes `1.0` and `1e0`.
C378–379 explicitly equates valid 1/1.0 and 0/-0 for fixture comparisons; boolean
identity stays separate. C's safe-count range is 0–9007199254740991; fractional, negative,
boolean or larger counts fail. The runtime must not round a noninteger into that range
before validation. Bare `number` fields such as Source.bytes also need field-specific
integer/nonnegative bounds reconciled with their byte-count meaning and global caps.

S2 uses binary64 and demonstrates rounding; JCS is not preservation of arbitrary
decimal lexemes. Its Appendix B includes numbers outside HookTrace's safe-integer
boundary, so passing JCS vectors does not mean admitting them as HookTrace input.
For raw fractional values, decide accepted precision/range, underflow and conversion
timing before claiming a canonical event hash preserves all mathematical distinctions.
`1e400` is JSON grammar-valid but outside finite binary64 and the safe-integer range;
reject under current limits. `1e-400` is finite mathematical nonzero: its treatment as
raw data needs a decision, not an assumption that zero faithfully represents it.
Do not apply an integer-only policy to every raw value or turn numbers into strings
without reviewed scope/schema changes. No ReleaseLens N1–N4 policy imported.

**Unicode/order:** S2 requires rejection of lone surrogates, unchanged decoded string
data, recursive property sorting by unsigned UTF-16 code units and UTF-8 output.
Escaped and literal forms of the same scalar may canonicalize equally; composed and
decomposed Unicode strings remain distinct. S2 does not perform NFC normalization.
Arrays retain order: only an explicitly approved derived set-normalization step may
reorder designated collections. Raw event arrays, fixture permutations and observed
arrival sequences cannot be sorted as generic sets. S4 maxLength counts characters;
C/T's proposed 16 KiB string cap needs an escaped-versus-decoded UTF-8 byte definition;
character maxLength alone cannot enforce it. No new unit policy is selected here.

**Runtime unknowns:** S6 documents duplicate-name last-wins, nonfinite constants,
default float conversion, acceptance of some lone surrogates and UTF-16/32 byte input.
`strict=True` governs control characters, not the full HookTrace contract. Pair and
numeric hooks offer control points, not proof of bounded lexical checks. B's preferred
runtime/library versions remain research choices. Exact decoding, overflow/underflow,
bool/integer handling, Unicode sort and resource behavior need later tests on the
reviewed build. No default parser or `sort_keys=True` output earns a JCS claim here.

## Hash domains and two-pass identities (A1/A3)

| Identity | Current preimage/meaning | What must not be conflated; remaining decision |
| --- | --- | --- |
| Source.sha256 / inputManifestSha256 | Exact captured source / input-manifest bytes, including whitespace/newlines (C109–115, F179–185) | Lexical identity only. A reformat or redaction changes the hash input even if parsed values match; no authenticity or completeness proof |
| Event.payloadHash | Canonical parsed event JSON (C162), read with RFC8785 commitment C412/B93–95 | Parsed event, not extracted normalized fields; later preimage registry should document the exact envelope/pointer boundary without filtering/mutation. Equal JCS values do not prove byte-identical delivery or truthful content |
| Imported observation ID | `obs:` plus SHA-256 of RFC8785 JSON `[Source.id, Source.sha256, rowPointer, collection]` (C413–417) | Tuple order fixed; source label and raw hash are inputs. Provider ID/rowId/rewritten links are not. Same source bytes/pointer re-import stably; separate logical sources remain distinct; reject unexpected collisions |
| normalizedSha256 / evidenceSha256 / frozenManifestSha256 | Named output hashes (C95–98, 359–365); frozen manifest's own hash lives in report (C126) | Need exact artifact/preimage and equality/alias rules, serialized-byte framing and stage boundaries. Do not assume normalizedSha256=evidenceSha256 or introduce a self-hash |
| Findings and other derived IDs | Finding uses rule/version plus sorted evidence IDs with collision checks (C418); other output types have `id` fields | Exact tuple/domain/order conventions remain incomplete, especially M2 source-only gaps or multiple findings over the same nodes; do not solve collisions by unstable counters |

C238–251 requires IDs before reference rewriting. Reordering traversal of unchanged
sources must not affect IDs. Editing source row order or just a row's ref text changes
the raw source hash, hence the ID preimage for **every row in that source**; moving
a row also changes its pointer. This is intended source-sensitive identity, not
semantic row identity. C's identical-input determinism promise does not promise IDs
survive re-export. Later oracles must distinguish these operations.

Pointers use decoded RFC6901 tokens, not URI fragments or filesystem paths. For JSONL,
C59's `/line/<1-based>` prefix is a HookTrace convention; a normal JSON array uses
zero-based indexes. `/a~1b` addresses key `a/b`; `/~01` addresses key `~1`, not `/`.
The empty pointer differs from `/` (empty-key member). A pointer can be well-formed
yet unresolved; references cannot create default values or fetch external resources.

## Eight representative paper oracle cases (A4)

These are prospective expectations, **not executed fixtures or verified hash goldens**.
Otherwise valid context is assumed where a single boundary is varied. “Decision needed”
is an explicit unresolved disposition; no acceptance is inferred from parser behavior.

| Case | Paper input / comparison | Expected result and independent basis |
| --- | --- | --- |
| O1 invalid JSON boundary | One object contains both `"a"` and `"\u0061"` as keys | Reject decoded duplicate before schema/normalization (C28, S1 §4/8.3, S2 §3.1). Preserve original bytes under specified failure handling; diagnostic must not dump values |
| O2 numeric boundary | `processedEventCount` token `1.0000000000000001`, compared with an admissible integral value 1 | Reject first as fractional; accept valid 1 under same context, never let conversion collapse the distinction (C205–206, S3/S4). Actual runtime result remains untested |
| O3 canonical strings/order | Same raw event values re-expressed with whitespace/member order and equivalent escapes; keys include U+1F600 and U+FB33 | For admitted values, canonical bytes equal, raw byte inputs differ; JCS orders U+1F600 before U+FB33 by UTF-16 units (S2 §3.2.3). A lone surrogate instead prevents JCS; no new hash string asserted |
| O4 duplicate observations | Two byte-identical event sources named A/B; separately re-import each unchanged | Same payloadHash expected; different observation preimages/IDs with own origins, repeat imports stable. Reject collisions rather than merging; no claim of two business effects (C132–135, 253–258, 413–417; T R2) |
| O5 forward/ref rewriting | Handler source refers to later attempt source through qualified row label; reverse processing traversal without editing bytes, then contrast an actual source-row reorder | Resolve the same target in pass two with unchanged observation IDs for traversal-only change. Actual byte/pointer edit changes preimages; no stable-ID promise across rewrite. Malformed/dangling target is rejected, no recursive ID dependency (C238–251, S5; T R1) |
| O6 ambiguous local identity | Equal execution/request strings under two candidates with unevidenced namespace domains | No explicit match or invented Order; retain candidates/gap/ambiguity as applicable. Known incompatible domains exclude a match; timestamps do not choose winner (C294–329; T R3) |
| O7 missing provider ID | Otherwise admissible supported Acacia event lacks `id` | Current output disposition **decision needed**, not a valid emitted Event. Under proposed M2: raw ref plus gap, no Event/provider ID or event-based link; source-only finding recipe still D5. M1/M3 yield different caller outcomes (F129–135) |
| O8 set order/hash framing | Same evidence with Origin.refs listed in opposite orders; compare identical FixtureRun permutation retained as ordered data | Ref-array canonical order and complete derived artifact hash preimage **decision needed** (D5); JCS alone preserves array order. Permutations must retain order/repeats; sorting them is wrong (C390, 412; S2 §3.2.3) |

Later independent golden process: reviewer freezes each admitted case's exact bytes,
source labels, pointers, expected typed values and normative rationale **before** the
normalizer runs. Use published S2 canonical-byte/number examples as external anchors;
derive observation preimage strings separately from contract tuples. Check canonical
bytes with an independently selected conforming implementation and digest those exact
bytes using a separately verified SHA-256 tool; record versions and reviewer sign-off.
Agreement between implementations alone cannot override the source specification.
Negative cases need located rejection/unknown expectations, not output-generated
goldens. Resolve disagreements and D1–D5 decisions before freezing expectations;
never update a golden just to match the implementation. No digest computed here.

Pure byte/schema/JCS/graph checks cannot qualify safe acquisition, native runtime,
SQLite committed read-back, publication interruption or network/process isolation.
Those retain separate B01/B01a/B01c and T08–T10 gates. Documentation passes none of them.

## Smallest next task and delivery (A5/A6)

**Smallest follow-on:** a documentation-only D1 decision PR choosing M1/M2/M3, with
exact absent-versus-invalid-ID boundaries, unsupported-input precedence, caller/count/
finding consequences and a clause reconciliation checklist. Recommend M2, conditional
on a coherent source-only finding identity plan; if unresolved, keep the gate open.
Acceptance: coordinator can trace O7 to one explicit outcome without invented identity,
schema-invalid output, silent evidence loss or misleading event counts. Founder adopts
only the reviewed exact revision. No executable schema, library trial or fixture work
is implied. D2–D6 remain separate; do not broaden this into a full importer task.

Next two distinct research questions, ranked for coordinator dispatch only:
1. **D2 numeric/encoding profile:** which exact lexical and value boundaries preserve
   truthful accepted data under chosen JCS semantics? Deliver a source-backed decision
   table covering raw versus normalized numbers, Unicode/JSONL and limit units.
2. **D5 deterministic identity registry:** which artifact bytes, array orders and
   source-only finding preimages must be fixed before independent goldens? Deliver
   a hash/ID dependency map and ordering table, preserving no-self-hash/two-pass rules.

This order limits solo-founder rework: settle output shape, admitted data, schema/
graph obligations, then byte identity and independent oracles before implementation.
Maintenance costs are qualitative; no benchmark, customer value or effort estimate
supports a build commitment. Current intake NO-GO and all gates above remain open.

Early draft PR #23/checkpoint `580b34ada620502567ab76509f219191c4940cae` records scope.
Final checks/head/base/attribution/CI and literal Sourcery status belong in its timeline.
Early `pr-record` failed in **44684847520** after summary displaced trailer; preserved
summary/restored trailer; attribution 1/1, repository/25 tests/actionlint/full-base and
40-file/55-heading preservation checks passed. Provider `server_is_overloaded` preceded the
full-record edit; no edit landed, no retry loop/bypass. User explicitly requested
continuation; original deadline retained. No HTTP source failure or quota bypass.
No schemas/goldens/fixtures/harness, library/native trials, existing corpus execution,
customer/API/SDK work, accounts/outreach, installs/environment/model/permission changes
or spend. No approval/merge/self-dispatch; all predecessor work remains preserved.
