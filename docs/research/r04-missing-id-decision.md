# R04 missing-event-ID decision packet

Status: **Research ready for review: recommend absent-only M2**, [issue #24](https://github.com/Himanshu-singh04/hooktrace/issues/24).
Recommendation only; no normative adoption, implementation or intake authorization.

## Authority and bounds

Coordinator dispatched fixed A1–A6 under the founder's ongoing bounded research mandate.
Same persistent GPT-6 Astra / OpenCode worker; no subagents or portfolio-file reads.
Successful start **2026-11-20 06:47:57 UTC**; deadline **08:47:57 UTC**, sooner if ready.
One 180–250-line packet, at most three external primary documents and eight paper cases.
Only one research Markdown addition; all 40 base files and entire SDD/55 headings stay.

Branch `docs/r04-missing-id-decision` starts from approved main
`457a84aec693c5ecb07a2ed32e8b0377c40186f0`. Preserve these unapproved branches/PR heads
and historical review checkouts, including both R03 reviewed revisions:

| PR / branch | Preserved head |
| --- | --- |
| #17 `docs/b01d-deployment-decision` | `65ecb026453e39f2f64692dafbec416ed5914439` |
| #19 `docs/r01-evidence-availability` | `5669bacedd5c226dc631a3b76dd77848b886212f` |
| #21 `docs/r02-scope-fit` | `737d828bed6af498a66ab961023d4559b633d197` |
| #23 `docs/r03-contract-readiness` | `61f0c27a586692dffe9338fe678bb375728d5f6a` |

R03 A1–A6 passed after R03-R1 correction; M2 remains a candidate. B01d full source
audit remains pending. ReleaseLens-only N1–N4 adoption supplies no HookTrace policy;
its synthetic scope/sequence and documentation reconciliation remain the sole founder
decision. Synthetic continuation is not new human assent. Provider/quota error stops
this round without retry/bypass. Intake NO-GO and all existing gates remain open.

## Recommendation and evidence

**Propose retaining an otherwise admissible event row whose `id` member is absent,
emitting one source-only gap and no normalized Event for it. Supplied null, empty,
blank-only or non-string IDs are fatal input errors.** Unsupported provider version/
type does not waive these rules. Required type absence and independent validation
failures remain fatal. This is a proposed policy bundle, not current parser behavior.
It preserves partial evidence without nullable Event callers; demand, frequency and costs are unknown.

Approved local authority: [contract](../evidence-contract.md) (**C**),
[B01 support matrix](../b01-decisions.md) (**B**),
[B01b research](../b01b-fixture-corpus.md) (**F**) and [testing](../testing.md) (**T**).
Line numbers refer to approved base above. Pending
[R03](https://github.com/Himanshu-singh04/hooktrace/blob/61f0c27a586692dffe9338fe678bb375728d5f6a/docs/research/r03-contract-readiness.md)
is provisional motivation only; its M2 preference is independently compared below.

Three primary documents read **2026-11-20**; zero HTTP failures, no linked sources/examples executed.
Text retrieval supplied no verified source-byte digests; none claimed.

| Source | Exact document / evidence | Limit |
| --- | --- | --- |
| S1 | [Stripe v17.7.0 Events.d.ts](https://raw.githubusercontent.com/stripe/stripe-node/v17.7.0/types/Events.d.ts), `EventBase.id: string`, `type: Event.Type`, nullable `api_version` | Tagged generated declaration, not an importer specification or authenticity proof; no ID prefix/character/length rule stated here. B/F supply the already-reviewed Acacia binding; no SDK package fetched |
| S2 | [RFC8785](https://www.rfc-editor.org/rfc/rfc8785.txt), §§3.1–3.2.4 | Informational JCS: immutable decoded strings, ordered arrays, UTF-8 bytes. Supports proposed string-only identity tuple; does not choose its domain or prove source truth |
| S3 | [RFC6901](https://www.rfc-editor.org/rfc/rfc6901.txt), §§3–7 | Escape/evaluate exact tokens, no Unicode normalization, unresolved members fail. Cite an existing row when its `id` is absent; never cite a nonexistent `/id` |

## Authority trace and proposed clause replacements (A1)

Quoted old clauses are verbatim excerpts; exact proposed additions use terms defined below.

| Authority / old clause | Exact proposed replacement or addition |
| --- | --- |
| C156 `eventId: string;` | Retain declaration; add: “An emitted Event requires a usable provider event-ID string. Raw `id` absence alone follows the absent-ID exception; null, empty, blank-only or non-string `id` is INPUT_INVALID. Never coerce, trim or substitute identity.” |
| C253 “All imported rows remain distinct observations, including repeated event exports.” | “All imported rows remain distinct raw observations, including repeated exports. Each admissible mapped event row emits one Event, except an absent-ID row emits no Event and exactly one source-only absent-ID gap. No raw row is discarded or merged.” |
| B216 “Recognized version/type but missing required identity data” → “`insufficient`; no invented values or provider authenticity claim” | “Recognized version/type with usable event ID but missing other required identity data emits an insufficient Event. Absent event ID follows the source-only gap exception; invalid supplied ID is fatal. No invented values or authenticity claim.” |
| B213 “Other, missing or unrecognized API versions” → “`unsupported_version`; never silently treat as latest” | Retain; add: “After fatal validation, version classification precedes type classification. Absent-ID rows retain unsupported context in their source-only gap, without emitting an Event or extracting supported-version fields.” |
| C239–241 “Assign each output ID from the source identity/hash/pointer/kind rule below; build the qualified-row lookup.” | Add: “Enumerate and account for every mapped row before output. Absent-ID event rows are raw locations only, receive no observation ID and never enter the qualified application-row lookup.” |
| C418 “Finding IDs derive from rule/version plus sorted evidence IDs, with collision checks.” | “Node-backed finding IDs retain the existing rule. For absent-ID source-only gaps use the domain-separated source/hash/row-pointer/reason recipe defined here; reject duplicate output IDs or collisions, never use traversal counters.” |
| C408–409 “All findings cite source refs or declare an evidence gap with refs to the bounded input being searched. Aggregate counts count records, not unique incidents or failures.” | Retain; add: “summary.events equals emitted Event count. Every omitted absent-ID row has one resolvable source-only gap; report limitations state raw event-row, emitted Event and absent-ID omission counts. Omissions never prove no event or effect.” |
| C430–431 “Unsupported Stripe interpretation is retained with a finding; unsupported HookTrace schema is a fatal validation error.” | Retain; add: “Fatal validation overrides row-local disposition across the entire bundle. Unsupported context on an absent-ID row is retained by that row's single gap and its limitations, not by a fabricated Event.” |
| T89–92 “10,000 normalized records” / “Reject excess, never truncate silently.” | Retain existing caps; add: “Also cap mapped input data rows at 10,000, counting absent-ID rows before omission. A row-local gap never bypasses raw-byte, input-row, normalized-record or report limits.” |

C39/59–62 bind Ref to a captured source/pointer; C81/109–115 bind Source.sha256 to
exact frozen bytes. C132–137 preserve separate logical sources even with shared bytes.
C227–236 distinguish source-local application `rowId` from provider `eventId`.
C413–417 derives observation `id` from `[Source.id, Source.sha256, rowPointer, collection]`;
neither `rowId` nor provider ID supplies it. The new gap ID is neither an observation
nor provider ID. C336–341 permits empty nodes/linkIds; refs locate the raw row instead.
C363–365 supplies existing counts/limitations, not an omission-count schema field.
C428–434 supplies diagnostic codes and no-report-on-fatal; F129–135 leaves absent-ID
output unresolved. Missing evidence remains unknown under C9–24/294–322.

## Finite boundaries and precedence (A2)

**Proposed lexical policy, not a Stripe guarantee:** let W be this fixed set of code
points: U+0009–000D, U+0020, U+0085, U+00A0, U+1680, U+2000–200A, U+2028–2029,
U+202F, U+205F, U+3000. “Blank-only” means a nonempty decoded string entirely in W.
A usable ID is a nonempty decoded string with at least one code point outside W,
subject to existing encoding/string/resource checks. No prefix, regex, ASCII-only
or provider-length rule is inferred. No trim/case fold/Unicode normalization occurs:
padded strings remain distinct exact values; characters outside W are opaque, not
certified provider identifiers. This explicit acceptance proposal needs founder adoption.

The table uses otherwise valid inputs. **S** = exact `2025-02-24.acacia` snapshot,
`customer.subscription.created/updated/deleted`, embedded subscription. **V** = other
version; **V?** = absent/null version (no declared-version fallback). **T** = other
nonblank type or recognized thin format; **T?** = absent/null/empty/blank-only type.
Wrong-type version/type, nonobject row, malformed mapped container and all independent
shape/safety/hash/scope/ref failures belong to **X**. Missing other identity alone is
not X: keep the existing insufficient category. No full provider schema is invented.
Present version strings outside exact Acacia, including empty strings, classify V;
version metadata with a non-string/non-null value is X. T? is proposed fatal because
required `Event.eventType: string` cannot truthfully represent an absent usable type.

| Raw `id` | S | V | V? | T with Acacia | T? at any version | X at any version/type |
| --- | --- | --- | --- | --- | --- | --- |
| Absent member | G, eligible support context | G, unsupported_version | G, unsupported_version | G, unsupported_type | FATAL | FATAL |
| Explicit null | FATAL | FATAL | FATAL | FATAL | FATAL | FATAL |
| Empty string | FATAL | FATAL | FATAL | FATAL | FATAL | FATAL |
| Blank-only string (W) | FATAL | FATAL | FATAL | FATAL | FATAL | FATAL |
| Number/bool/array/object | FATAL | FATAL | FATAL | FATAL | FATAL | FATAL |
| Usable string | Event supported/insufficient | Event unsupported_version | Event unsupported_version | Event unsupported_type | FATAL | FATAL |

**G** = raw row + exactly one source-only gap, no Event. “Eligible” assigns no Event
interpretation; other missing identity stays raw, with no unsupported extraction.
Unsupported Event cells retain the cited finding requirement; their general finding-ID
recipes remain outside this narrowly specified source-only exception.

Precedence proposal: (1) acquisition/encoding/limits/hashes and all applicable shape,
scope and qualified-ref validation must pass before publication; (2) reject invalid
supplied ID or unusable type; (3) classify version before type/format, so V+T yields
unsupported_version; (4) apply absent-ID G regardless of that support classification;
(5) otherwise emit the valid Event with supported/insufficient/unsupported status.
These are logical gates, not permission to skip later ref checks after seeing a gap.
Known independent failures still fail the whole bundle. Existing rejection obligations
are C28–32/112/129/238–248/433; ID/type and combined unsupported precedence are new choices.
FATAL means located INPUT_INVALID for the new malformed-ID/type cases, or the existing
specific code for other failures; no report/counts are published. Do not echo values.
The packet does not choose an ordering among multiple simultaneous fatal diagnostics.
“Retain” describes future lawful frozen evidence under separately approved acquisition:
original files stay unchanged; owned incomplete copies follow [operations](../operations.md)
59–99. It permits neither customer acquisition now nor sharing rejected raw content.
Row-local G allows an otherwise valid report, not a partial report of a failed bundle.

## M1 / M2 / M3 decision frontier (A3)

Options retain the same malformed-ID/type/fatal gates; absence never proves nonexecution.

| Option / exact proposed absent-ID wording | Callers, raw retention, counts, links and cost |
| --- | --- |
| M1: “An absent provider event ID is INPUT_INVALID; publish no report.” | Existing non-null Event callers stay simple; original/raw failure evidence retained under operations policy, no published normalized count. One incomplete row blocks useful surrounding evidence; no links/report findings for failed bundle. Lowest new output complexity; utility loss unmeasured |
| **M2:** “Retain an otherwise admissible absent-ID raw event row and emit exactly one source-only gap, but no Event or observation ID for that row.” | Keep non-null Event shape; callers must interpret normalized counts alongside omission accounting. Raw refs remain accessible; omitted row is no Node/Link/Order target. New source-only identity/report closure/row cap required. Best bounded partial-evidence trade-off, not measured demand |
| M3: “Emit an insufficient Event with eventId=null for an otherwise admissible absent-ID row; never join null identities by equality.” | Change declaration to nullable; raw and normalized row retained, summary.events includes it and observation ID still uses source/hash/pointer. Every Event consumer/join/conflict renderer must handle null. Unsupported precedence needs additional wording because one interpretation enum cannot express both defects; greatest caller/version surface |

M2 is recommended only with the boundary, precedence, identity, accounting and limits
below adopted together. It does not weaken Event into a sentinel or use a raw digest
as provider identity. Present invalid IDs remain distinguishable from absent IDs.
An Attempt/Handler may retain its own valid eventId even when no Event matches; the
provider-ID association is unresolved, never filled from a nearby ID-less raw row.
Null/absent IDs never join each other. Independently valid qualified attempt refs may
still resolve with existing scope/namespace confidence rules; this is not null equality.

## Exact proposed source-only identity and report closure (A4)

Reserve ruleId `missing-provider-event-id`, ruleVersion `1`, reason token `id_absent`.
For each G row, the ID is `gap:` plus 64 lowercase hex SHA-256 digits of the UTF-8
RFC8785 serialization of this ordered all-string tuple, with no trailing newline:
`["hooktrace.source-gap/1", "missing-provider-event-id", "1", Source.id, Source.sha256, rowPointer, "events", "id_absent"]`.
`events` denotes the intended normalized collection, not an existing Event node.
This reserved domain/prefix is new, not C418. No digest calculated; ID fits C35 syntax/
length. The tuple avoids numbers; full payload/JCS qualification stays a separate gate.

Generate rowPointer from the actual mapped row's location: escape each object token
`~`→`~0`, `/`→`~1`, use zero-based decimal array indexes without leading zeros; JSONL
uses C59's `/line/<1-based>` prefix with empty suffix for a whole row. Plain pointers only:
no URI fragment, mapping-text alias, member `/id`, rowId or guessed ID. Cite the existing
row object; prove absence by inspecting it. Use the decoded Source.id verbatim.

Emit exactly: kind `gap`, severity `review`, nodes `[]`, linkIds `[]`, and one Ref
`{sourceId: Source.id, pointer: rowPointer}`. Fixed summary: “Provider event ID absent;
raw row retained without normalized Event.” Required limitations, in fixed order:
“No provider identity or event-based correlation is inferred.”; “Omission is not
evidence of no event, delivery, execution or effect.”; then “Interpretation context:
eligible Acacia snapshot.” or “Interpretation context: unsupported_version.” or
“Interpretation context: unsupported_type.” according to the table. No raw values echoed.
The eligible-context wording claims only scope eligibility; missing other identity
does not become supported output. The same gap satisfies unsupported retention for G.

The Ref resolves through the frozen manifest to verified bytes/hash and the row; all
Finding/Node/Link/Order refs and IDs must close before publication. No Event payloadHash
or obs ID is emitted for an omitted row. The source digest binds captured bytes only.
Two source labels with identical bytes yield distinct gap preimages; two row pointers
in one source likewise differ. Same inputs/rule version reproduce IDs independent of
traversal order. Rewriting source bytes changes every affected source-bound preimage.
Enumerate once per mapped row; duplicate emitted IDs, whether identical preimages or
hash collisions, fail closed with INTERNAL_ERROR for generated output; duplicate
input Source.id remains INPUT_INVALID. Never merge rows or append encounter counters.
Reserve the domain for this rule; future reason/semantic changes require rule-version
review. Sort final findings by ID; the singleton refs and fixed limitations need no
set-order decision. Other D5 identity domains remain unresolved, not implicitly fixed.

For successful publication, let R be mapped raw event-row count, E emitted Event count,
O count of this rule/version's unique source-row gaps. Require **R = E + O**, exactly
one disposition per raw event row. summary.events=E; findingsByKind.gap counts all gap
records, so it need not equal O. Other collection counts retain their current meaning.
Use existing report limitations for fixed text: “Raw event rows: R; normalized Events:
E; omitted for absent id: O.” Substitute decimal counts; add “Omissions do not prove
no event or effect.” Render the same accounting and source-hash/pointer index in Markdown.
No new count/schema field is silently added. Apply the proposed 10,000 input-row cap
before omission and existing report/byte/time caps; excess is LIMIT_EXCEEDED, no truncation.

## Eight paper oracles, not executed fixtures
Stable control: otherwise admissible Acacia updated snapshot, usable synthetic ID,
fixed source label/pointer and valid scope; no unrelated findings/rows. R/E/O below
refer to successful event-row accounting; G counts only this rule's gaps. Existing
unsupported findings are stated separately. No actual hashes or product results asserted.

| Case | Change from control / contrast | Proposed result, closure and permitted claims |
| --- | --- | --- |
| P1 absence | Remove only `id`; compare usable control | Control R/E/O=1/1/0, G=0; absent 1/0/1, G=1, row Ref resolves, no `/id` Ref/Node. Reader may say captured row lacks ID, never no event/effect; no provider-ID join |
| P2 malformed IDs | Substitute null, empty, W-only or each non-string JSON type; contrast padded usable string | Every invalid substitution fatal INPUT_INVALID, no report/counts; original bytes intact, diagnostics omit values. Padded usable string retains exact value, 1/1/0; it does not match the unpadded string or certify provider validity |
| P3 unsupported precedence | Absent ID with other/missing/null version and other nonblank type; contrast usable ID | Absent 1/0/1, one G with unsupported_version limitation; usable 1/1/0, unsupported_version Event plus existing unsupported finding. Acacia+other type instead uses unsupported_type. No Acacia fallback, authenticity or absent-ID join |
| P4 fatal precedence | Absent ID plus missing type, nonobject row, declared hash mismatch or invalid qualified ref; contrast P1 | Each separate defect fatal with its applicable existing/new code, no published count/gap. G never hides structural/hash/ref errors; retained incomplete bytes are not a complete report or provider proof |
| P5 duplicate captures | Two separately declared source labels A/B containing identical absent-ID bytes | R/E/O=2/0/2, G=2, distinct IDs/Refs despite equal hash; traversal reversal preserves each. Duplicate Source.id is fatal. Reader sees two captures, not proof of two provider events/effects |
| P6 distinct rows | Same source has absent-ID rows at `/0` and `/1`; contrast repeat import | R/E/O=2/0/2, G=2; pointers distinguish identical row contents. Same frozen input reproduces IDs; physical row/source edits change preimages. No merging, null joins or chronology from file order |
| P7 purported ref to omitted row | Handler attemptRef names event source/row with collection attempts (or illegally events) | Fatal REFERENCE_INVALID or input-shape error; qualified refs target attempts only, never raw Event rows (C215–248). No fabricated Node/obs ID, no published counts. A raw citation to that existing event row is valid but is not an attemptRef |
| P8 independent application evidence | P1 plus one valid Attempt and Handler referencing that attempt; their eventId fields null | R/E/O=1/0/1, G=1; attempts=1, handlers=1. Qualified ref resolves in pass two, with existing evidenced boundary/confidence checks; extra boundary gaps counted separately. No event target/null-equality link; direct attempt relationship does not prove handler effect |

## Adoption package and smallest later question (A5/A6)

Adopt together only after independent review and an explicit founder policy decision:
absent-versus-invalid/W predicate; type/version precedence; M2 row exception; reserved
source-only rule/ID/finding text; counting/citation closure; input-row cap and error
semantics. Approval or merge of this research record alone adopts none of them.
Reconcile C Event/two-pass/preservation/Finding/Report/identity/error clauses and B209–216;
append clarification to F120–135 without changing historical outcomes or corpus bytes;
update T01/T02/T04/T07 and R1/R2/R3 plus resource-limit expectations. A later normative
PR must list these exact changes and paper outcomes, not claim historical tests prove M2.
SDD interfaces/import flow/error handling/reporting and its version policy (line 134)
need reconciliation; preserve all 55 headings. Review input/evidence/report schema
compatibility and normalizer/rules/tool version identifiers together. Recommend a new
major for any incompatible published schema/semantics; do not silently rewrite v1.
No version is bumped here; no application implementation exists.

**Smallest later question:** should the founder adopt this complete absent-only M2
package, with an explicit schema/version compatibility decision, in one documentation
reconciliation PR? Prerequisites: coordinator accepts exact packet revision; no open
boundary/identity/count contradictions; founder explicitly authorizes policy decision
work. Stop if any bundled choice is rejected, version impact is unresolved, or scope
needs runtime/customer evidence. No automatic dispatch, schema/golden or build follows.
General numeric admission, other D5 hashes/IDs, independent JCS/goldens, acquisition,
runtime/publication/isolation and customer value remain independent unpassed gates.

Early draft #25/checkpoint and final checks, exact head/base, complete attribution,
preservation, failures and literal Sourcery status are recorded in the PR timeline.
Initial pr-record **44690717897 failed** after automatic summary displaced the trailer;
summary preserved and final trailer restored; checkpoint live attribution 1/1 passed.
No provider/quota interruption in R04 to this point; synthetic continuity is not new
human authorization. No code, fixtures, corpus/runtime/native/library experiments,
customer/API operations, installations, model/provider/permission changes or spend.
No intake/acquisition or implementation gate changes. Stop for review.
