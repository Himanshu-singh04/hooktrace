# B01b narrow synthetic fixture corpus

Status: **Accepted fixture research**, [issue #12](https://github.com/Himanshu-singh04/hooktrace/issues/12).
PR #13 merged at `313801ae7292931a6ce7e40b9f9faf73e67e33e1`;
[main CI 44524101287](https://github.com/Himanshu-singh04/hooktrace/actions/runs/44524101287) passed.
Original corpus and integration evidence below remain historical; acceptance does not
close acquisition, canonicalization or product-implementation gates.
Original founder instruction: “ok proceed with the further tasks”, following
authorization for independent rolling work with sequential exact-revision approvals.
The issue preserves the full refined scope and A1–A6 acceptance criteria.

Original branch base was approved main `97f1669ddd92a510f7d637429b1c21f53713ae40`,
independent of then-pending B01a.
PR #9 accepted conditional Acacia/SQLite research after the R7 correction and later
founder approval; see [merge verification](https://github.com/Himanshu-singh04/hooktrace/pull/9#issuecomment-7002315562).
This does not approve a runtime build, arbitrary-export acquisition or product B02.
The original delivery changed only new B01b files. Following B01a approval/merge,
the coordinator assigned integration of accepted main
`529f8d5e06601def268828eaad993111987c9a76` into this same branch/PR without rebase
or force-push. Issue #12 A1–A6 and all corpus semantics remain unchanged.

## Scope and oracle boundary

One [positive bundle](../experiments/b01b/) contains two event exports (updated and
deleted), one attempt, one handler observation and one state snapshot, plus scope
and namespace metadata. A manifest, independent expected facts and finite targeted
variants accompany the raw files. The created event and customer-shape alternatives
are variants, not extra positive bundles. Inputs are original, synthetic and partial;
they are not complete Stripe responses or provider-certified fixtures.

All semantics follow the existing [contract](evidence-contract.md), B01 support
matrix, and T01/T02/T08/T09 in [testing](testing.md). No importer, normalized output,
correlation, canonical serializer, freeze/publication layer or handler is delivered.
The small stdlib harness reads only explicitly listed repository fixtures;
mutations and forbidden-path strings stay in memory. Golden normalized IDs/JCS
payload hashes remain pending an independent canonicalization oracle.

## Primary field provenance

Read 2026-11-19; documentation/declarations are evidence, not instructions to execute.
No Stripe SDK, API, CLI, account, keys, copied exports or installed dependency used.

- **P1:** [v17.7.0 apiVersion](https://github.com/stripe/stripe-node/blob/v17.7.0/src/apiVersion.ts)
  binds the tagged declarations to exact `2025-02-24.acacia`.
- **P2:** [v17.7.0 EventBase/Request](https://github.com/stripe/stripe-node/blob/v17.7.0/types/Events.d.ts)
  defines event ID/type, optional connected account, nullable API version, Unix-seconds
  created, livemode, nullable originating request and nullable request ID/idempotency key.
- **P3:** [v17.7.0 EventTypes](https://github.com/stripe/stripe-node/blob/v17.7.0/types/EventTypes.d.ts)
  `CustomerSubscriptionCreatedEvent` (1131), `DeletedEvent` (1147), `UpdatedEvent`
  (1243) each binds `data.object` to Subscription. Deletion is a subscription end,
  not an instruction to infer a local tombstone or access change.
- **P4:** [v17.7.0 Subscription](https://github.com/stripe/stripe-node/blob/v17.7.0/types/Subscriptions.d.ts)
  has subscription-level period fields and `customer: string | Customer | DeletedCustomer`.
  [Customer/DeletedCustomer](https://github.com/stripe/stripe-node/blob/v17.7.0/types/Customers.d.ts)
  gives IDs/object tags and `deleted: true`. These are admissible type shapes, not a
  claim every event expansion or deleted-customer combination is emitted in practice.
- **P5:** [v18.0.0 apiVersion](https://github.com/stripe/stripe-node/blob/v18.0.0/src/apiVersion.ts)
  binds `2025-03-31.basil`; [SubscriptionItem](https://github.com/stripe/stripe-node/blob/v18.0.0/types/SubscriptionItems.d.ts)
  places billing periods on items. Retain this version as unsupported, with no Acacia fallback.
- **P6:** [v18.0.0 ThinEvent](https://github.com/stripe/stripe-node/blob/v18.0.0/types/ThinEvent.d.ts)
  and [V2.EventBase](https://github.com/stripe/stripe-node/blob/v18.0.0/types/V2/Events.d.ts)
  define `object=v2.core.event`, string created and related-object reference. The
  [event-format documentation](https://docs.stripe.com/event-destinations) describes
  unversioned notifications, not Acacia subscription snapshots. Thin input remains
  unsupported; related URLs are inert and never fetched. Unknown versions are
  deliberately invented negative labels, not invented provider releases.

Provider declarations are Stripe/Ask Bjørn Hansen MIT-licensed source; only links,
field names and original synthetic values are used. Website docs are cited, not
relicensed as MIT. The coordinator independently audited these expectations at
`ce33c6429a0bcf9d80784280be127ff246b1457a`; see
[verification](https://github.com/Himanshu-singh04/hooktrace/pull/13#issuecomment-7004044531).
No normalizer generates its own goldens; integration re-verification was required
before the accepted merge recorded above.

## Corpus inventory and independent expectations (A2)

All paths below are within `experiments/b01b/`. The manifest contains unique IDs and
five mappings: one per data source; citation-only `meta` has none. All use the cited
`scope-test`: account `acct_synthetic`, test environment `sandbox_synthetic`, unknown
context. Source order deliberately places handlers before attempts.

| Logical source | File | Bytes | SHA-256 |
| --- | --- | ---: | --- |
| updated | events-updated.json | 688 | `79df2dedab36d64116f39aef3be93e44333eb9a4c72f840194ff564e03211b1a` |
| deleted | events-deleted.json | 605 | `83d07e60341a22e97d80b435d176a9a29542bc45b64ffd3856e4ad68bffb0e58` |
| handlers | handlers.jsonl | 904 | `a27f2450d3b9262f2c401d5491231a0c05742e808dd92c249516360c0167875b` |
| attempts | attempts.jsonl | 894 | `72e98f67afa6a55438794da04cdf14caa1e32ca07b53a14dc3534b101072363a` |
| snapshots | snapshots.jsonl | 734 | `c9a9b7e97ce21b86a52fb93b5e97c1821a76ff44dadf94b2abb81bac88c6e0fb` |
| meta | metadata.json | 957 | `e0aca1046b1cb7518795521e220757827f5db795afce08e7e94e7bbffd50fbe7` |

Manifest identity: **3221 bytes**, SHA-256
`3bc8599e56d5a28d2a1b0d11fb86bfa815690acd71a24785329868dda4a07683`.
This hashes exact UTF-8 file bytes, including final newlines. It is not JCS, a
payload hash, or the frozen-manifest identity of an implemented importer.

[`expected.json`](../experiments/b01b/expected.json) contains **40 manually authored
field assertions**, expected counts, observation-origin keys, qualified row resolution
and snapshot presence. The checker does not write this file. Positive interpretations:

| Contract field/fact | Independently expected binding |
| --- | --- |
| Event.eventId | updated `/0/id` = `evt_synthetic_update`; deleted = `evt_synthetic_delete` |
| Event.eventType / apiVersion / format / interpretation | respectively updated/deleted subscription types; exact Acacia; snapshot; supported within this narrow field subset (P1–P4) |
| Event.objectId / subscriptionId / objectType | `/0/data/object/id` = `sub_synthetic`, object = `subscription`, on both exports |
| Event.customerId | updated string `/0/data/object/customer`; deleted expanded `/0/data/object/customer/id`; both `cus_synthetic` (P4) |
| Event.createdUnixSeconds | both `1740787200`; equal provider times neither determine delivery order nor make the events identical |
| Event.triggerRequestId / idempotencyKey | updated `req_synthetic_origin` / `synthetic-key`; deleted request null means both unknown (P2) |
| Attempt/Handler.requestId | receiving HTTP `http_synthetic_receipt` plus cited request namespace; never joined to originating API request |
| Handler.attemptRef | `handlers/h1` resolves to `attempts/a1`, although the target source comes later; this is a source assertion, not proven causality |
| Snapshot | observed persisted read, access **false**, status canceled, processed count **0**, tombstone **absent**, mutation count **unknown** |

There are **five observations**, not five unique business effects: two events and one
each attempt/handler/snapshot. Origins are source/pointer/collection tuples; the
contract's derived observation ID additionally includes raw source hash and RFC8785.
`rowId`, `eventId`, origin tuple and final derived ID are different identities. No
derived ID or canonical payload hash is emitted. Duplicate exports add a distinct
logical source and origin even when raw bytes, hash and provider ID are identical.

### Oracle boundary and unresolved missing identity

The field values and variant outcomes were written from the cited contract and
tagged declarations, then checked against source bytes. They are not output captured
from an implementation under test. The harness's predicates are reviewable research
logic, **not an independent certification of their own correctness**. The linked
coordinator verification audits both expected table and predicates against those
authorities at the original head, without claiming production schema conformance.

B01 classifies absent required event/entity/customer identity as `insufficient`.
The normalized Event type nevertheless requires a non-null `eventId`. Therefore the
missing-event-ID variant asserts only the interpretation/evidence category; it does
not invent a placeholder ID or emit an invalid Event. Retention/diagnostic/output
disposition requires an explicit B02 contract clarification. Known identity conflicts
are fatal; an unknown boundary is not a known contradiction. A raw account missing
from one payload may use the explicit cited scope, still without authenticity.

## Finite variants and corruption controls (A3–A5)

[`variants.json`](../experiments/b01b/variants.json) is the complete **76-case table**.
Every case has a stable ID, expected outcome, exact issue set and source/contract
rationale. These are bounded research labels, not a new public diagnostic schema:

- `fatal:*`: invalid input prevents publication (mapping/ref/scope/hash/shape errors).
- `unsupported:*`: version/type/thin interpretation not supported; preserve evidence
  without applying Acacia fields. This is distinct from fatal HookTrace schema errors.
- `insufficient:*`: required identity or scope evidence unavailable.
- `valid_unknown`: valid nullable/partial evidence; absence of an issue does not
  establish a relationship, ordering, completeness or business result.
- `valid`: targeted predicates accept the case, not a certification of a complete
  provider payload, application policy or full input schema.

Coverage includes created/string and deleted-customer union variants; missing identity
and scope; conflicting account/mode/context; Basil with item-level periods, invented,
null and missing versions, wrong event type and thin notification; missing/malformed/
overlapping mappings; duplicate logical sources/rows; duplicate exports; forward
same-file and cross-file references; dangling/wrong-type refs, known event/producer
conflicts, null refs and self-retry cycle; raw byte/count/hash/manifest mismatches;
inert absolute/parent paths; closed snapshot schema/fields/types, booleans versus
0/strings, status case, negative/fractional/unsafe/boolean counts and inclusive maximum,
nested/null values, unique/disjoint/allowlisted absence, empty partial values, explicit
false tombstone; unknown namespaces, insufficient/dangling/contradictory citations;
coverage equality, inversion, each/both null endpoints, invalid calendar/UTC format,
contradictory captured coverage and nullable capture time.

The positive bundle and table are loaded **only from nine literal filenames** in
`FILES`. `Source.path`, citation URLs and variant path strings never drive a read.
No root/path argument is accepted. The checker reads the repository files before
running variants; all mutations are deep copies in memory. It is not descriptor-safe
acquisition, an arbitrary-root importer, or authority to point at customer exports.

Semantic edits apply **after raw identity verification** to parsed structures; their
unchanged source hashes are not presented as a valid modified on-disk bundle. Raw
integrity variants separately mutate bytes or declarations. The duplicate-export
case uses the already-read updated bytes and a new logical ID/path, never a new file
open. Only source/row/ref facts are evaluated: no normalized records, correlations,
business assertions or golden report snapshots are produced. No finite mutation
recipe is evaluated as Python, shell, a URL, or a filesystem traversal.

In addition to the negative variants, five controls require rejection of:

1. A raw event's appended whitespace (valid JSON, different byte identity).
2. The manifest's appended whitespace (separate manifest identity).
3. A wrong independently expected provider event ID (checker must not bless it).
4. Duplicate JSON object keys.
5. A nonfinite JSON number.

The checker verifies the table's exact issue sets/categories, selected explicit
values, observation counts/origins and qualified refs. It checks every positive
namespace citation against captured triples and scope/coverage against captured
metadata. Its namespace rule is deliberately bounded to this corpus's direct
captured triples, not a general operator-mapping language. It does not implement
complete JSON Schema validation, all numeric/depth/size limits, all producer policies,
all malformed container shapes or arbitrary pointer structures. Passing this corpus
does not pass all T01/T02/T08/T09 product cases. B02 must implement those separately.

## Rerun evidence and limits (A6)

Original reviewed-head commands, from the repository root with installed Python
3.13.4 and existing actionlint 1.7.12 (retained as historical evidence):

```sh
python3 experiments/b01b/check_corpus.py
python3 scripts/check_repository.py
python3 -m unittest discover -s scripts -p 'test_*.py'
/Volumes/AIWorkspace/caches/actionlint/1.7.12/actionlint -shellcheck= -pyflakes=
git diff --check 97f1669ddd92a510f7d637429b1c21f53713ae40
```

Local outcomes (all exit 0): corpus **6 raw sources + manifest identity, 40 facts,
5 observations, 76 variants, 5 additional corruption controls**; repository formatting/
relative-link check passed; **25 policy tests passed**; actionlint passed; full-diff
whitespace check passed. Inline Git boundary assertions confirmed only new B01b paths,
approved base, preserved B01a branch at `65be90c910d5448afe067239efa301f3c8d89b4f`, and
unchanged B01 experiments. Initial 72- and 75-case corpus runs also passed; later
coverage-citation/invalid-container cases and unsupported-with-scope-conflict control
were added during self-review, not to mask a failed check. No local check failure.
The early checkpoint's live CI history and final SHA/CI/attribution are recorded in
[PR #13](https://github.com/Himanshu-singh04/hooktrace/pull/13); any bot-displaced final
trailer is restored while preserving its summary. Repository checks do not certify
these semantic expectations. No schema/JCS dependency installed; no candidate
Python/SQLite build validated.
Not run: B02 importer, freeze/publication, acquisition/mount/device probes, product
isolation/network-denied tests, complete Stripe schemas/SDK validation, handler/store
execution, correlation, canonicalization conformance or customer exports. Unchanged
B01 probes retain their prior evidence and were not rerun for this fixture-only task.

B01a's accepted research retains NO-GO for arbitrary exports; an enforceable acquisition
boundary, runtime/build, schema/JCS, isolation and separate B02 authorization remain
open gates. Producer-created intake remains an unaccepted workflow proposal. Corpus
readiness addresses one fixture prerequisite only. The original A1–A6 audit passed;
integration re-verification and founder approval preceded the accepted merge above.

## Accepted-main integration

Standing founder instruction: keep independent work progressing while approvals are
sequential. The integration assignment preserves issue #12 A1–A6 and directs a merge
of accepted B01a main into existing PR #13, with status/docs reconciliation only.
Verified clean branch head `ce33c6429a0bcf9d80784280be127ff246b1457a` and unchanged
remote B01b, then fetched and confirmed exact main
`529f8d5e06601def268828eaad993111987c9a76` (accepted B01a, main CI 44510104992 passed).

`git merge --no-ff --no-commit 529f8d5e06601def268828eaad993111987c9a76` completed
automatically with **zero conflicts**. No conflict resolutions or corpus edits were
needed. The merge preserves both original B01b commits and accepted B01a history.
Status reconciliation updates README, B01 prerequisites, B01a acceptance status,
B01b review/integration history, roadmap, testing and SDD bodies. Primary-source
observations, requirements and all SDD headings are preserved. All files under
`experiments/`, including raw corpus, manifest, expected facts, variants and checker,
remain byte-identical to the prior reviewed head. The historical coordinator review
checkout is untouched.

Integration rerun commands:

```sh
python3 -B experiments/b01b/check_corpus.py
python3 scripts/check_repository.py
python3 -m unittest discover -s scripts -p 'test_*.py'
/Volumes/AIWorkspace/caches/actionlint/1.7.12/actionlint -shellcheck= -pyflakes=
git diff --check 529f8d5e06601def268828eaad993111987c9a76
```

Integration local results: all five commands exited 0; corpus checks passed with
6 raw sources plus manifest identity, 40 facts, 5 observations, 76 variants and
5 additional corruption controls; repository checks passed, 25 policy tests passed,
actionlint and full-diff checks passed. Inline Git comparisons found all experiments
byte-identical to the prior reviewed head, contract/product/operations identical to
accepted main, and all **55 SDD headings** identical to both revisions. Zero unmerged
paths; only documentation changes relative to the prior reviewed head. Replacement
SHA/CI and final attribution are recorded in the PR implementation response.
No dependency acquisition, runtime/drive change, new product test, native
acquisition probe or provider retrieval is needed for this documentation integration.
Canonical identity/hash oracles and missing-event-ID disposition remain explicit gates.
