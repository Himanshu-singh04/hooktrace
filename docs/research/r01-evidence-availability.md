# R01 customer evidence availability

Status: **Research ready for review; narrow the audience to evidence-ready teams**, [issue #18](https://github.com/Himanshu-singh04/hooktrace/issues/18).
Availability is not safe acquisition, authenticity, handler execution or causality.

## Authorization and bounds

Founder requested rotating research during ReleaseLens build priority and explicitly
said **“resume everything”** on 2026-11-20. Issue #18 preserves authority and fixed A1–A6.
Same original GPT-6 Astra / OpenCode worker, no subagents.
Successful start: **2026-11-20 05:29:51 UTC**; deadline **07:29:51 UTC**, earlier if ready.
One roughly 200–250-line record; at most eight distinct primary documents, two public
first-party incident examples and one official dashboard/debugging-tool comparison.

Base: approved main `457a84aec693c5ecb07a2ed32e8b0377c40186f0` (accepted B01c NO-GO).
Saved [B01d PR #17](https://github.com/Himanshu-singh04/hooktrace/pull/17) remains at
`65ecb026453e39f2f64692dafbec416ed5914439`; full source/acceptance review is pending.
Its pause/operator-trust/workflow proposals are **not adopted** or part of this base.
Preserve previous branches/review checkouts, all normative/source/corpus/capture/
workflow bytes and all 55 SDD headings. Current/arbitrary-input NO-GO and P1–P4 persist.

Question: what event/delivery/handler/state facts can a small SaaS team retain/export,
and where does preparation fail? Distinguish capability, retention and instrumentation.
No customer/API calls, installs/probes/code, accounts/outreach/marketing, permission/
storage/runtime changes, portfolio reads or spend. Later rounds/pilots need authorization.

## Finding and evidence limits

**Documented availability is conditional; actual customer retention is unverified.**
Stripe exposes recent events and delivery outcomes. Application execution and local
access state require separately retained, semantically useful customer records.
No source establishes that small SaaS teams commonly retain that combination, can
export it safely, or prefer another report over their existing tools. Recommend
narrowing discovery to teams with retained cross-layer evidence; do not promise
arbitrary historical incident reconstruction. Current intake remains NO-GO.

The useful window is the **overlap** of records needed for the question, not a universal
30-day allowance. Missing optional sources may permit narrower questions, never inferred
handlers/history or default zeros. Docs are not interviews, tests or telemetry coverage.
No public incident account was retrieved (0/2).

## Primary-source ledger (A1/A4)

All eight documents read **2026-11-20**. Stripe/OTel pages are live; PostgreSQL URLs
target major 18. These are possible customer systems, not a mandatory stack or HookTrace
runtime. Only Workbench is compared; no extra documents retrieved through embedded links.

| ID / exact primary document | Sections used; evidence boundary |
| --- | --- |
| S1 [Stripe webhook guide](https://docs.stripe.com/webhooks) | “Create a handler”, “View event deliveries”, “Automatic retries”, “Manual retries”, “Event ordering”, “API versioning”, “Handle duplicate events”, signature/replay sections: acknowledgments, retry windows, ordering and raw-body/signature conditions; not customer retention evidence |
| S2 [Event object](https://docs.stripe.com/api/events/object) | Attributes `id`, `account`, `context`, `api_version`, `created`, `data`, `livemode`, `pending_webhooks`, `request`, `type`: provider fields and nullable scope/version; not a delivery-attempt or execution record |
| S3 [List all events](https://docs.stripe.com/api/events/list) | Opening retention/version/account statement, Parameters and Returns: up to 30 days; per-request account, connected-account separation, filters and cursor pagination; not a complete delivery-history export |
| S4 [How Workbench works](https://docs.stripe.com/workbench/overview) | Access roles, Inspector, API request Logs, Events, Manage event destinations: browser visibility into payloads and attempts, account filters and resend capability; no bulk export or fixed event/attempt retention SLA established by this page |
| S5 [OpenTelemetry Logs Data Model](https://opentelemetry.io/docs/specs/otel/logs/data-model/) | Log and Event Record Definition; Timestamp/ObservedTimestamp, optional TraceId/SpanId, Body, Resource, InstrumentationScope, Attributes: representational fields, not automatically emitted business facts or a retention policy |
| S6 [PostgreSQL 18 transaction isolation](https://www.postgresql.org/docs/18/transaction-iso.html) | §13.2.1 Read Committed and §13.2.2 Repeatable Read: command/transaction read snapshots and own-write visibility; no historical audit retention or event attribution guarantee |
| S7 [Stripe subscription webhooks](https://docs.stripe.com/billing/subscriptions/webhooks) | Subscription events, Track active subscriptions, Catch subscription status changes: subscription notifications versus application access logic, invoice/entitlement dependencies; vendor integration guidance, not an observed incident |
| S8 [PostgreSQL 18 continuous archiving/PITR](https://www.postgresql.org/docs/18/continuous-archiving.html) | §25.3 introduction, WAL archiving, recovery and timelines: base backup plus continuous WAL can recover prior state; WAL normally recycles without archiving, recovery target must follow backup end, whole-cluster/storage burden. No assurance a customer has suitable backups |

Failed discovery: `https://docs.stripe.com/workbench/events` returned **404**, no document.
S4 is the official overview linked from S2. Total: eight documents, one failed URL,
one tool, zero incidents; no authenticated views, API results or customer rows inspected.

## Source → field → retention → availability matrix (A1)

“Potential” means documented or customer-instrumentable, **not known to exist**.
S1–S8 dates are above. Account/environment/version qualifiers apply before joining;
the source producer and export representation must remain visible in every case.

| Evidence / producer / fields | Retrieval or export and retention | Applicability / unavailable later |
| --- | --- | --- |
| Snapshot event / Stripe: `id`, `type`, `created`, `api_version`, `data.object`, available scope (S2/S3) | API list potentially supplies event objects for up to **30 days**; cursor pagination/filtering required. Workbench shows recent payloads (S4), with no retention duration established here. Neither is the original HTTP request byte stream | v1 event representation; `api_version` fixes event data, not caller's current version. Listing is for the requesting account, not all connected accounts. Beyond documented API window, retrieval is not established; customer-retained copies may survive separately |
| Original webhook receipt / customer's receiver: exact body, received signature header, local receipt time and endpoint context (S1) | Only retained original bytes/header preserve that delivery representation; storage period/export mechanism is customer-specific and unknown. A parsed/re-encoded event is a new representation | Endpoint/test/live signing context differs. Retried deliveries have new signature/timestamp. Lost raw bytes or header cannot be recreated from object JSON; HookTrace does not accept secrets or upgrade an export to authenticated evidence |
| Provider delivery observation / Stripe: event, destination/endpoint, attempted delivery outcome and HTTP status (S1/S4) | Workbench Events/Webhooks expose attempts, delivered/pending/failed and attempt metadata. **Bulk machine-readable attempt export, stable provider-attempt ID and retention window not established** by reviewed sources | Endpoint/account-specific; sandbox/live retry behavior differs. Dashboard visibility is not an exported contract row. When unavailable, individual attempts/times/responses remain unknown; event-list `delivery_success` is not a per-attempt history |
| Aggregate delivery indication / Stripe: `pending_webhooks`, list filter `delivery_success` (S2/S3) | Potentially in event/API results within supported retrieval; retain the observation's scope/time. `pending_webhooks` can include platform/app endpoints absent from the account's own endpoint list | Not proof that the customer's selected endpoint, queue consumer or DB completed. Zero pending is not a substitute for handler/state evidence; cannot infer historical attempt count or retry edges |
| Receiver/queue linkage / customer: event ID, receiving request ID, queue job/attempt, stream epoch/index, observed time (S1 asynchronous guidance; S5 generic fields) | Requires explicit instrumentation and backend retention/export; **no default duration or automatic Stripe-event binding** in S5. Must retain relation across HTTP acknowledgment and worker processing | Application/deployment/account/test-live/queue namespace required. Collector observation time is not necessarily HTTP arrival. Without recorded stream sequence, provider time or log sort cannot recover actual arrival order |
| Handler observation / customer: execution ID, event ID, `started/completed/failed/write_claimed`, transaction correlation (S5; contract) | Potentially structured Body/Attributes plus Resource/InstrumentationScope; TraceId/SpanId are optional. Customer must have emitted, retained and exported the relevant phase; logging standard does not guarantee any phase is present | A trace ID is not automatically an execution, event or transaction ID. Namespace and field semantics need evidence. Missing instrumentation or expired logs cannot be retroactively generated; a “saved” line is only a claim |
| Current persisted-state observation / customer DB: subscription/store IDs, capture scope/time, actual allowlisted values (S6; contract) | A future reviewed exporter might query retained rows. PostgreSQL Read Committed sees a statement snapshot, including its own earlier writes; Repeatable Read gives a transaction snapshot, not a past-incident lookup. No retention duration specified | DB/version/isolation and primary/replica/store context must be declared. Read after repair is evidence of that read, not state during incident. Own uncommitted writes must not be labelled committed read-back |
| Historical DB state / customer backup/audit owner (S8) | Conditional recovery from a suitable base backup and continuous WAL covering target on correct timeline; retention set by customer's archive policy. Ordinary recycled WAL is not a durable history. Restore is whole-cluster, not a one-record export | PostgreSQL 18 example, no customer stack assumed. Target must be after backup end; missing required chain prevents promised recovery. Historical state alone does not identify the event/handler that caused it or restore app logs/external caches |
| Access policy and mapping / customer app; subscription signals / Stripe (S7) | Need retained app policy/deployment meaning and mapping from subscription/customer to local access. S7 describes access-expiration handling, invoice.paid and entitlement notifications, not the customer's implementation or retention | `active` subscription status is not an observed local `access=true`. Unsupported invoice/entitlement evidence must remain context, not silently interpreted by the three-event Acacia adapter |
| Scope/coverage metadata / customer exporter + Stripe fields (S1–S3; contract) | Preserve account, environment, sandbox/context, selected filters/pages, capture time, source/version and declared gaps. `livemode=false` alone does not identify which sandbox. No completeness claim from one page or absence of hits | `account`/`context`/`api_version` can be absent/null under S2. Documented API shape is not evidence that a given retained export has fields. Unknown boundaries block confirmed cross-source links |

**Retention is not one clock.** S1's live automatic retries run up to three days;
sandbox retries run three times over a few hours. Dashboard manual resend is up to
15 days, CLI manual resend up to 30 days. These are **redelivery capabilities**, not
event/attempt archive retention promises; no resend is authorized or needed here.
S3's 30-day event-list window is a distinct retrieval bound. S4's 30-day Health alert
history is also distinct and must not be reassigned to Events, Logs or deliveries.

`cancellationTombstone`, `processedEventCount` and `mutationCount` are not guaranteed
Stripe/database fields; customers must actually maintain them. Never invent zeros or
count incomplete logs. `access` needs app semantics; `status` needs an allowlisted value.
Omitted values stay unknown unless absence was observed (`absentFields`); partial
snapshots are allowed.

## Observations versus inference (A2)

- **Delivery ≠ execution ≠ persisted effect:** S1 recommends acknowledgment before complex
  logic. A `2xx` could precede queue failure; a timeout could coexist with completed work.
  These are possibilities, not incidents. Handler/write claims and DB reads stay separate.
- **Three distinct times:** Stripe `created` is event creation in seconds (S2); S1
  disclaims ordered delivery and warns equal timestamps occur. S5 distinguishes source
  Timestamp from collection ObservedTimestamp. None establishes a global arrival,
  execution or commit order. An observed stream ordinal needs its actual stream epoch.
- **Identity:** repeated same event ID may represent multiple receipts; different IDs
  with same object/type suggest possible semantic duplication, not row equivalence.
  Keep logical observations separate and require explicit evidence for retry edges.
  Stripe's triggering API request is not the receiver's HTTP request ID (contract).
- **Missing ID:** S2's event ID may be lost in a truncated/redacted export. Never create
  one from a hash/time/subscription ID; missing-event-ID disposition remains unresolved.
  Missing application correlations stay unknown, never a timestamp-nearest match.
- **Bytes/signatures:** S1 verification needs unmodified body, signature and endpoint
  secret at verification time; each retry is signed anew, with recency checks. A
  customer-retained verification claim is external evidence, not HookTrace verification.
  API JSON, pretty-printing and redaction cannot stand in for the original signed body.
  Hashes identify captured bytes only; new redactions get new hashes and truthful lineage.
- **Version/scope:** S2/S3 freeze event data's rendering version; requesting a newer
  version does not upgrade old evidence. Current docs include newer formats/versions
  than accepted B01b's narrow Acacia research. No support expansion follows: thin,
  Basil/newer or unknown versions stay unsupported/limited under the current contract.
- **State:** S6/S8 distinguish a current transaction snapshot from recoverable history.
  Read-back can establish captured values at its scope, not event causation, historic
  entitlement, cache state or whether every side effect committed. Do not restore a
  database or replay a webhook merely to manufacture missing investigation evidence.

## Candidate customer journey and burden (A3)

Illustrative question, **not an observed customer incident**: “This subscription was
canceled, but the user still appears to have access; what evidence distinguishes
delivery failure, handler failure and a mismatch in persisted local state?”

1. Engineer defines access semantics, incident interval/account/environment/subscription
   and historical/current symptom. A future authorized Workbench check might already
   answer a destination-failure question; this study did not log in.
2. Inventory retained event objects/original requests and separate attempt observations,
   handler logs and state reads. Record known retention coverage, filters, dropped or
   absent fields and capture times. Do not call every event within 30 days available.
3. Engineer would need reviewed data access and mappings to preserve received bytes,
   map explicit execution phases and join keys, and project only permitted snapshot
   fields. Workbench views need an established export path; hand-transcription/screenshots
   are not automatically contract-compliant evidence. No exporter is supplied here.
4. **HookTrace intake remains blocked.** Exportable data, customer ownership and a
   local folder do not establish safe acquisition. Producer origin, interface/handoff
   and capture still require separately authorized work under accepted B01a/B01c.
   Pending B01d is neither approved nor needed to justify this availability finding.
5. If those gates eventually pass, investigation could cite each retained observation,
   expose ambiguous/missing links and choose a next check. Example: delivery present,
   handler unknown, current access true does **not** prove cancellation handler failure.
   A synthetic ordering model would demonstrate only its own behavior, not production.
6. Later sharing needs reviewed redaction/provenance; secrets/evidence stay outside Git.
   These steps authorize no collection, upload, retention change or pilot.

**Engineering burden:** coordinate receiver/queue/worker/DB owners; establish identifier
domains, policy/read semantics, schema/version mappings and citations. Instrumentation
added later helps future events only and requires separate work.
**Privacy/export burden:** event/log bodies can contain sensitive/free-text fields;
minimization may remove correlation keys or invalidate original-byte/signature claims.
Retain originals only under the customer's applicable policy, never silently rewrite.
**Historical recovery burden:** S8 needs backup/WAL coverage, correct timeline, space
and DB expertise; restoring a cluster for one fact may be disproportionate. No measured
cost, acceptance or restore permission exists. Current reads answer less than history.

## One existing alternative and counterevidence (A4)

**Stripe Workbench only; documented vendor capabilities, not hands-on results.**

| Question | What S1/S4 already offer | Limit / inference for HookTrace |
| --- | --- | --- |
| Was this event generated, and did delivery fail? | Events payload/details; endpoint attempts, status codes, pending deliveries and filters | Simple endpoint/TLS/status failures may be adequately diagnosed here; another delivery viewer is not a demonstrated unmet need |
| What did a Stripe API request return? | API request logs with status, account, endpoint and version filters; JSON object Inspector | API request logs are not the application's worker logs or a receipt-to-commit trace |
| What is the Stripe object now? | Inspector JSON and related API objects/events | Does not establish local access state or the historical DB values; this is a boundary of the documented evidence, not a claim about every possible integration |
| Can an engineer share or retry a view? | Shareable view links and resend/retry controls; full tool access for Administrator/Developer roles | Link access is not an offline raw export. Retry is a new operation, not passive evidence; no retry or role/account change performed |

**Scope counterevidence:** S7's common access flow uses `invoice.paid` and can use
entitlement notifications; HookTrace interprets only three proposed subscription event
types. Fresh JSON is insufficient when policy depends on unmodeled signals; never infer
invoice/entitlement effects from subscription status.
Conversely, a team with useful correlated logs and state tooling might already answer
the cross-layer question manually. That is a disconfirming hypothesis, not a user report.

**Public signal limit:** vendor guidance establishes integration duties/tools, not pain
frequency, retention or demand. No first-party incident was reviewed within this budget;
no interviews, willingness-to-pay, market-size or pricing results exist. H1–H4 stay
unverified; absence of reviewed incidents does not mean incidents never occur.

## Pilot prerequisites and recommendation (A5)

Checklist for **screening a future separately authorized pilot**, not new schema fields
or a requirement that every optional source be present:

- [ ] One bounded question with defined local access semantics, incident interval,
  account/environment/subscription identity and an identified engineer/data owner.
- [ ] Inventory distinguishes original receipt bytes, retrieved event objects, delivery
  views/exports, handler phases and state reads; retention covers the needed overlap.
- [ ] Available sources have usable provenance/version/identifier domains and export
  paths. Missing fields, expiry, pagination/filter coverage and unsupported types are
  explicit; no false complete-history or authentication assertion.
- [ ] For a handler/state question, at least meaningful retained application observation
  or state evidence exists and joins are defensible; otherwise narrow to the facts
  actually available. Do not fabricate optional evidence to qualify a pilot.
- [ ] Customer-controlled minimization/export effort is acceptable to that engineer,
  recorded rather than estimated; existing Workbench/manual answer is documented.
- [ ] Separate safe-intake/runtime/schema/publication/isolation, synthetic acceptance
  and owner pilot authorization gates pass before any customer use. This study closes none.

**Candidate user/buyer hypothesis:** engineer at a small Stripe-backed B2B SaaS team
with retained explicit handler and state evidence; technical founder or engineering
owner may buy. Neither that audience's size nor willingness to pay is known.

**Recommend narrow, conditional discovery—not broader intake or a build commitment.**
Continue planning if a concrete cross-layer question has retained compatible evidence
and an unresolved task beyond Workbench/manual inspection. Narrow to current-state or
delivery-only conclusions when history is missing, and prefer existing tools where
they suffice. Pause the proposed customer use case if critical history is expired,
needed instrumentation never existed, semantics fall outside the supported slice, or
preparation exceeds the engineer's accepted burden. All customer intake remains NO-GO
until independent safety/product gates pass; pending B01d proposals stay pending.

Draft questions, **not asked and not outreach authorization**:
1. For your last concrete access discrepancy, what question stayed unanswered after
   Workbench and your logs/database checks, and what evidence was already gone?
2. Which exact representations/fields survive for the incident interval, with what
   retention and filtering? Are receipt bytes distinct from reserialized objects?
3. Can event IDs survive receiver→queue→worker→state linkage? What is logged after
   commit versus before acknowledgment, and which identifiers can be reused?
4. Who can export/minimize those records, what work would be unacceptable, and what
   redaction would destroy the identifiers or semantics needed for this question?
5. Would a report that preserves unknowns change your next check compared with your
   existing workflow? What negative result would make you stop using it?

## Next two questions and delivery evidence (A6)

1. **Scope fit:** can the three subscription-event slice answer the targeted access
   questions when invoice/entitlement signals drive policy? Sources: official versioned
   Stripe event/object/entitlement docs and current contract. Deliverable: question→
   required-observation→supported/unsupported matrix and one bounded scope recommendation.
2. **Deterministic development readiness:** what independent schema/JCS/hash/ID and
   missing-event-ID oracles remain before a synthetic-only slice? Sources: B01/B01b,
   RFC8785 and selected schema/runtime primary specifications. Deliverable: ordered
   readiness ledger and smallest proposed task; no install or implementation by default.

Coordinator dispatches these later; neither has started. Exact head/base/attribution/CI
are in PR #19. Local checks passed: repository checker, **25 policy tests**, actionlint
1.7.12, full-base diff and protected-byte/55-heading/branch comparisons. Eight sources,
one tool, zero incidents; one 404. Early `pr-record` failed in **44681559806** after bot
summary displaced the final trailer; preserved summary, restored trailer, attribution 1/1 passed. No manual Sourcery
request/label; final literal status is reported separately from required CI.
No customer/API retrieval, accounts/outreach, installs/code/probes, capture/export/restore,
runtime/permission/storage changes or product/enforcement tests. Existing probes were
not rerun. Normative/source/corpus/capture/workflow bytes and 55 headings are unchanged.
Availability research is not demand validation or evidence-intake acceptance.
