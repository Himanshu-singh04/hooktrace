# R02 subscription-slice scope fit

Status: **Research ready for review; retain the slice for a narrower factual question**, [issue #20](https://github.com/Himanshu-singh04/hooktrace/issues/20).
No normative adoption, implementation or customer intake authorization.

## Authority and bounds

Founder requested ongoing bounded business/development research during ReleaseLens
build priority and explicitly said **“resume everything”**. Coordinator dispatched
R02 with fixed A1–A6 in issue #20. Same persistent GPT-6 Astra / OpenCode worker;
no subagents, portfolio-file reads or changes to model/runtime/permissions.
Successful start **2026-11-20 05:45:04 UTC**; deadline **07:45:04 UTC**, earlier if ready.
One roughly 200–260-line record, at most six external primary documents and five
explicitly synthetic candidate questions. Public documentation only; no customer/API
operations, implementation, accounts/outreach, installations/probes or spend.

Branch `docs/r02-scope-fit` starts from exact approved main
`457a84aec693c5ecb07a2ed32e8b0377c40186f0`. Preserve R01 draft #19 at
`5669bacedd5c226dc631a3b76dd77848b886212f` and B01d draft #17 at
`65ecb026453e39f2f64692dafbec416ed5914439`, plus historical review checkouts.
R01 passed independent review but is founder-unapproved; B01d full source audit is
pending. Neither proposal is adopted. All normative/source/corpus/capture/lock/
workflow bytes and 55 SDD headings stay unchanged; current intake remains **NO-GO**.

Question: can narrow subscription identity interpretation support a useful bounded
access investigation despite invoice/entitlement dependencies? Distinguish recognized
shape, interpreted fields, evidence correlation, observed application state and cause.
Assess cancellation/access, renewal/payment, entitlement changes, incomplete history
and a case existing tools solve; compare narrowing, expansion and pausing. Propose
one direction and later specification oracle without executing another task.

## Finding

**Retain the three-event slice for evidence reconciliation around cancellation (Q1).**
Ask which event, delivery, handler and persisted-access observations the engineer can
link, and which facts remain missing. Do not promise to decide whether access was
correct or what caused it. Subscription identities help locate evidence; they do not
encode the customer's payment, grace-period or feature-access policy.

Confidence: **high** that subscription observations alone underdetermine local access;
**conditional** that the existing contract can express a useful factual comparison;
**low/unvalidated** that customers need or will pay for it over their current workflow.
No implementation exists. This recommendation changes no approved requirement.

## Six-document source ledger

Read **2026-11-20**; primary public documents only. S1–S3 are tagged generated SDK
declarations, inspected as text without installing or invoking the SDK. S4–S6 are
mutable current guides: evidence for present guidance, not historical Acacia behavior.
Exact symbols/sections below delimit each claim; no linked API references were fetched.

| ID / exact primary document | Evidence used and limits |
| --- | --- |
| S1 [v17.7.0 apiVersion.ts](https://raw.githubusercontent.com/stripe/stripe-node/v17.7.0/src/apiVersion.ts) | `ApiVersion = '2025-02-24.acacia'` binds the tagged declarations; not a live delivery test |
| S2 [v17.7.0 EventTypes.d.ts](https://raw.githubusercontent.com/stripe/stripe-node/v17.7.0/types/EventTypes.d.ts) | `CustomerSubscriptionCreatedEvent`, `DeletedEvent`, `UpdatedEvent` bind `data.object` to Subscription; comments describe new plan, subscription end and changes. `EntitlementsActiveEntitlementSummaryUpdatedEvent` binds a separate summary object; invoice event interfaces/types exist. These declarations do not supply application access policy |
| S3 [v17.7.0 Subscriptions.d.ts](https://raw.githubusercontent.com/stripe/stripe-node/v17.7.0/types/Subscriptions.d.ts) | `id/object/customer`, `cancel_at_period_end/canceled_at`, top-level `current_period_start/end`, `collection_method`, `latest_invoice`, `status` and `pause_collection` comments. `send_invoice` marks subscription active before the due-date delinquency transition; a period is invoiced-for time, not proof of payment/access |
| S4 [Using webhooks with subscriptions](https://docs.stripe.com/billing/subscriptions/webhooks) | “Subscription events”, “Track active subscriptions”, “Catch subscription status changes”, “Invoice finalization failure”: current guidance uses `invoice.paid` plus subscription status for extension, entitlement notifications for features; invoices can fail finalization while subscription remains active. No claim those current rules/settings apply to Acacia |
| S5 [Entitlements, API view](https://docs.stripe.com/billing/entitlements.md?dashboard-or-api=api) | “Add your features to products”, “Listen for webhooks to grant or revoke access”, “Retrieve the list of all active entitlements”: product/feature mapping, summary capped at 10 entitlements, full-list pagination and internal persistence recommendation. Current-only guidance; historical Acacia summary fields/pagination semantics not established |
| S6 [How Workbench works](https://docs.stripe.com/workbench/overview) | “Review recent events”, “Manage event destinations”, “View API request logs”, Inspector: event payloads, attempted deliveries and succeeded/failed filters; endpoint selection and recent API-object views. Vendor capability evidence, not a hands-on test or proof of application execution |

Retrieval note: S5's base URL `https://docs.stripe.com/billing/entitlements` returned
only a variant-selection index; the API-view URL supplied that same guide's content.
Six substantive documents, seven URL fetches including the index; no failed HTTP
retrieval. No extra source count hidden behind links; no account/API operations.

Approved local evidence reused: [B01 scope/provenance](../b01-decisions.md),
[B01b field provenance/corpus](../b01b-fixture-corpus.md) and
[evidence contract](../evidence-contract.md). B01/B01b already compare Acacia's
top-level periods with Basil's item-level periods and bind Basil to v18.0.0; those
external files were not re-fetched. This supports rejecting a shared field-path rule.
Pending [R01 at its exact revision](https://github.com/Himanshu-singh04/hooktrace/blob/5669bacedd5c226dc631a3b76dd77848b886212f/docs/research/r01-evidence-availability.md)
is provisional context for retention/export uncertainty, not adopted audience policy.

## Exact approved interpretation boundary (A1)

| Layer | Current approved planning/research boundary | Conclusions excluded |
| --- | --- | --- |
| Shape recognition | Snapshot envelope, exact `2025-02-24.acacia`, `customer.subscription.created`, `customer.subscription.updated`, `customer.subscription.deleted`, embedded `object=subscription`; S1–S3/B01b ground the types | Matching a type name alone does not prove a valid complete payload, authenticity or emitted expansion combination |
| Semantic interpretation | Narrow event/object/subscription/customer identity extraction; event creation metadata and originating request/idempotency key; evidenced scope | No normalized invoice payment, entitlement set, cancellation policy, subscription-period rule or automatic access decision |
| Correlation | Contract links need compatible evidenced scope/namespaces, observed identifiers and a unique target for `explicit`; retain candidate/ambiguous/unresolved cases | Event ID alone cannot select among multiple deliveries/executions/stores. Subscription ID is not a causal link |
| Application observations | `normalized_v1` represents customer-supplied Attempt/Handler/Snapshot rows with source references and declared semantics | Representability does not establish customer retention, safe export, truthful evidence or implemented adapter behavior |
| Captured state | Allowlisted values at a particular store/capture/read kind; persisted and transactional reads stay distinct | A provider `status` field is not a local access observation. A read does not prove the event caused a write or a user could exercise a feature |

**Normalized fields, not an expansion proposal:** Event has `eventId`, `eventType`,
`apiVersion`, `format`, `createdUnixSeconds`, `objectId`, `objectType`, `subscriptionId`,
`customerId`, `triggerRequestId`, `idempotencyKey`, `payloadHash`, `interpretation`,
plus Base observation identity/origin/scope/source references. Created time is never
arrival time. Trigger request is Stripe's originating request, not the receiving HTTP ID.
Customer identity accepts the string or expanded object's ID (S3/B01b). Scope records
`accountId`, `environment`, `environmentId`, `context`; missing boundaries stay unknown.
Attempt adds producer namespace, event/endpoint/provider-attempt/request IDs, sent/
received times, observed stream/index, HTTP status, transport and explicit retry link.
Handler adds producer namespace, execution/event/attempt/request/subscription IDs,
observed time, phase (`started/completed/failed/write_claimed`), transaction/error code.
Snapshot has producer namespace, subscription/store IDs, capture time, read kind,
transaction/execution IDs, values schema, partial values and explicit `absentFields`.
The closed value allowlist is `access`, `status`, `cancellationTombstone`,
`processedEventCount`, `mutationCount`. Status permits `incomplete`, `incomplete_expired`,
`trialing`, `active`, `past_due`, `canceled`, `unpaid`, `paused`; this does not map a
provider event's status into captured local state. Missing, absent, false and zero differ.
Policy versions, feature sets, invoice outcomes and expiry dates are not new Snapshot
keys; none may be hidden in `status`, counters or a fabricated boolean projection.

Exact Basil `2025-03-31.basil`, other/missing versions remain `unsupported_version`;
thin input stays unsupported without fetching resources. Other types, including
invoices/entitlement summaries, remain `unsupported_type`. Recognized type/version
with insufficient identity stays `insufficient`; missing-event-ID output disposition
remains unresolved because Event requires `eventId`. No new status resolves it here.
Raw status/periods remain inert provider context. S3's cancellation and billing comments
allow source-backed discussion, not an unreviewed policy evaluator or adapter extension.

## Five synthetic candidate questions (A2)

All Q1–Q5 are invented investigation prompts, **not customer incidents or demand evidence**.
“Represent” below refers to the proposed contract, not shipped software. Each requires
source/capture provenance and compatible account/environment/identifier domains.

| Question | Required observations and policy | Representable / interpretable now | Unsupported or unknown; minimum defensible output |
| --- | --- | --- | --- |
| **Q1 Cancellation/access:** “Which captured observations accompany this cancellation while local access is true?” | Acacia deleted event; distinct endpoint receipt, explicit handler link/phase, persisted read of actual local `access`, subscription/store identity and capture context. Judging correctness additionally needs deployed cancellation/grace/override policy and relevant non-subscription inputs | Identity interpretation; Attempt status, Handler phase and Snapshot access/tombstone if actually captured; explicit links only with supported unique relations | Policy and correctness unsupported. Minimum: cite deleted-event observation, recorded delivery result/handler claim and captured access value separately; list missing links. No “cancellation failed” or event-caused access verdict (S2/S3) |
| **Q2 Renewal/payment:** “Did this renewal justify extending local access?” | Invoice/payment evidence for the relevant billing obligation and version, subscription identity, collection method, actual deployed extension/grace rule, prior expiry/extension and persisted read | Subscription identities and supplied local access/status observations; raw Acacia periods and latest-invoice reference remain context | Invoice/payment and expiry evaluation unsupported; active/updated is not payment proof (S3/S4). Minimum: observed update plus captured access, with payment/extension justification unknown; no inferred renewal success |
| **Q3 Entitlement change:** “Should this customer have feature F after a plan change?” | Complete relevant entitlement evidence, feature/product mapping and effective policy at the question time; customer-to-user/tenant mapping, local provisioning observations and feature-state read | Customer/subscription identity and generic handler observations; an actual existing subscription-level access boolean only within its declared meaning | Feature sets/mapping/feature-level state not in closed snapshot schema. Minimum: cannot determine F; a subscription update is insufficient. S5's 10-item summary limit means missing F alone is not revocation; current full list cannot recreate missing historical set |
| **Q4 Incomplete history:** “Does the available cancellation/update history explain today's captured access?” | Relevant event/receipt/handler/state coverage, original ordering evidence and historical policy; state before/after if asserting change, with comparable store/read semantics | Available identities/rows and declared coverage gaps; arrival order only from actual receiving-stream index with evidenced namespace | Missing records leave past state, processing and completeness unknown. Minimum: current captured value plus cited observations/gaps; cannot infer no cancellation, zero processing, or historical access from absence |
| **Q5 Existing-tool case:** “Did Stripe record a failed attempt to this endpoint for this event?” | Workbench event/destination/attempt view in the right account/environment; no access policy needed for this provider-observation question | An exported compatible Attempt could represent the observation; no new subscription semantics required | S6 already supplies attempted-delivery and failed/succeeded views. Minimum: provider recorded failed attempt at selected destination. Handler/state/cause remain unknown; prefer Workbench if that answers the whole task |

Policy documents may inform an engineer's explanation only as cited external context;
the contract does not parse them into an executable decision rule. Each source retains
its limitations. HTTP success, handler completion and `write_claimed` are distinct;
none substitutes for a persisted read. Even a persisted `access=true` cannot establish
feature F, cache/session behavior or a successful end-user authorization decision.

## Two decisive paired schedules (A3)

These are paper countermodels within Q1/Q2, not new questions, fixtures or provider
simulation results. “Same observations” means identical selected supported subscription
payloads/identities and indicated receipt/handler observations, not a claim that all
possible Stripe history is identical. Other histories may exist outside the selection.
Step numbers describe stipulated synthetic schedules, not timestamp-derived joins.

### Pair C: identical cancellation evidence, different application policy (Q1)

Common captured evidence: C1 is one Acacia `customer.subscription.deleted` snapshot,
event `evt_C`, object/subscription `sub_C`, customer `cus_C`; identical bytes in both
worlds. C2 is a recorded HTTP 200 receipt. C3 records handler `exec_C` as completed
and explicitly refers to C2; all scopes/namespaces and unique identifier links agree.
No handler log claims an access write. The policy inputs below are invented assumptions.

| Step | World C-deny | World C-grace |
| --- | --- | --- |
| C0 deployed rule | Revoke local access at subscription end, no local grace | Keep local access through an authorized grace interval after subscription end |
| C1–C3 | Common deleted event, receipt and completed-handler observation | Exactly the same selected event/receipt/handler observations |
| C4 independent state read | `persisted_read`, store `store_C`, `access=false` | Same store/capture context, `persisted_read`, `access=true`; grace still applies |
| Defensible answer | Captured local access is false; conditional on stated rule, consistent with deny | Captured local access is true; conditional on stated rule, consistent with grace |

Neither handler completion nor the deleted-event type determines C4. S2 says the
subscription ended; it does not prescribe either customer's rule. If C4 is missing,
actual local access stays unknown in both worlds. If policy evidence is missing,
correctness stays unknown even with C4. No source here proves C1 caused C4.

### Pair P: identical subscription evidence, different payment evidence (Q2)

Common P1: Acacia `customer.subscription.updated`, `evt_P/sub_P/cus_P`, with raw
`collection_method=send_invoice`, `status=active`, and the same unexpanded
`latest_invoice` ID and period values. Hold the entire selected P1 payload fixed.
Both worlds use a synthetic app rule requiring observed payment of this invoice
before extending access; prior local access has expired. This is a chosen app policy,
not Stripe's rule. S3 allows active send-invoice subscriptions before delinquency.

| Step | World P-paid | World P-open |
| --- | --- | --- |
| P1 | Common captured subscription snapshot before the invoice due date | Same captured snapshot and supported normalized fields |
| P2 outside interpreted slice | Separately evidenced payment of the named invoice | Separately evidenced invoice still open/unpaid; not inferred from missing event |
| P3 local observations | Provisioner records completion; independent persisted read captures `access=true` | No extension under the stipulated rule; independent persisted read captures `access=false` |
| Defensible answer | Payment/extension justification requires those extra observations and policy | Subscription's active status alone cannot justify extension or establish payment |

Any further provider updates are outside this selected evidence window, not asserted
absent. S4 supplies current payment-driven guidance; S3 supplies only the historical
shape/status compatibility. Historical invoice transition details remain outside this
round's proof. These worlds differ in application evidence, so the complete evidence
can distinguish them; the three-event projection cannot. No timestamp matching needed.

**Useful narrower conclusion:** with Q1's explicit, compatible unique references, an
engineer can say “this captured delivery and completed-handler observation refer to
the captured subscription event; this separately captured persisted value is true.”
Snapshot-to-handler linkage additionally requires its own supported execution or
transaction evidence; sharing a subscription ID does not establish that link. This
can expose the next missing check without declaring a failed cancellation or cause.

## Three options and costs (A4)

| Option | Value and lost value | Input/export burden | Version/schema/test/maintenance cost; evidence needed |
| --- | --- | --- | --- |
| **Retain slice, narrow promise** | Useful cited observation reconciliation and gap identification for Q1; loses automatic “should have access,” payment/feature diagnosis and causal explanation | Still needs explicit receipt/handler identity, meaningful persisted state and compatible namespaces; policy questions need separate human evidence. Narrowing does not make exports safe or cheap | No schema change proposed here; still needs deterministic schema/JCS/hash/ID oracles, version-negative and ambiguous-link tests, report wording and source-map upkeep. Need evidence-ready cases where manual/Workbench workflow leaves a useful unresolved task |
| **Expand supported signals** | Could address more Q2/Q3 policy dependencies; still cannot guarantee actual enforcement or cause. Loses a small review/test surface and may delay useful factual output | Requires historical invoice/payment links, entitlement completeness/feature mappings, app policy version and corresponding local state, often across owners; missing history remains missing | Separate reviewed adapter/schema decisions, version-grounded invoice/entitlement semantics, pagination/truncation and temporal-policy oracles, cross-object cardinality and conflicts, feature-state schema, negative fixtures and ongoing migrations. Need a concrete recurring question and retained data before choosing this cost |
| **Pause the customer question** | Avoids a misleading access promise and premature expansion; loses opportunity to learn whether cross-layer reports help | No new customer preparation now; engineers can use existing Workbench plus logs/DB/manual review | Existing research/gates remain; later restart must revalidate sources, scope and deterministic contract readiness. Need evidence of unresolved demand and acceptable preparation burden; pause is plausible if Q1 adds little |

Negative evidence: S3 already defeats “active means paid/access”; S4/S5 require signals
the slice does not interpret. A captured boolean cannot encode a feature matrix.
S6 already answers Q5, and engineers with correlated logs/DB tools may answer Q1
manually. No measured export cost, frequency, buyer fit or willingness-to-pay result
supports expansion. Hypothetical buyer remains the technical owner of a SaaS team;
retention, preparation burden and demand remain unverified. No interviews conducted.

## Recommendation, stop conditions and later specification (A5)

Recommend **retaining the current slice for Q1's factual reconciliation** as the next
planning target, conditional on demonstrable value beyond existing tools. Keep policy
correctness, invoice/feature diagnosis and causation outside that promise. The paired
schedules justify this limit without requiring an expanded adapter. They do not prove
commercial usefulness or close the acquisition/runtime/product gates.

Continue this direction only if the engineer can define the captured access value,
identify compatible retained application evidence and name a missing cross-layer fact
that the report could clarify. Narrow to Q5/use Workbench if delivery is the whole
question. Pause Q1 if retained state/links are absent, local access means an unsupported
feature/policy expression, or manual inspection already suffices. Reconsider expansion
only after a separately authorized case demonstrates needed signals and tolerable burden.

**Smallest later specification question (Q1 refinement):** what exact report sentences
and unknowns follow from a deleted event, one receipt, one linked handler claim and
one independent persisted-access read under the existing contract?
Proposed acceptance oracle: reviewer-authored paper input→claim table, independent of
any normalizer, with exact field/source references and forbidden inferences. Include
C-deny/C-grace; removing policy must leave factual claims unchanged and correctness
unknown. Removing the persisted read must make access unknown; replacing it with a
transactional read must not assert committed state. Missing scope, multiple candidate
deliveries without a disambiguating reference, unknown namespace or absent execution/
transaction evidence must weaken the applicable link; timestamps cannot repair it.
Missing/absent/false/zero must stay distinct.
Each asserted fact must trace to an allowed field; no invoice/feature/status shortcut,
new Snapshot key or provider authenticity claim. This proposes a specification oracle;
no fixtures, executable tests, adapters or report templates were implemented here.

Ranked follow-ons for coordinator dispatch, **not started**:
1. **Q1 report-claim specification** using approved contract/B01b and the two schedules;
   deliver the small independent claim/unknown table and review against the oracle above.
2. **Deterministic contract readiness** using approved B01/B01b plus separately budgeted
   schema/RFC8785/runtime sources: resolve missing-event-ID disposition and independent
   schema/JCS/hash/observation-ID goldens before any synthetic implementation proposal.

Current intake **NO-GO** and acquisition/runtime/schema/identity/publication/isolation
gates persist. P1–P4 remain unaccepted. No new adapter, schema, interpretation status,
policy, authority or normative requirement follows from this recommendation.

## Delivery evidence (A6)

Early draft PR #21 records scope checkpoint `eee1e9ec316c65a679510b9ba5a02887cbe53358`.
Final checks/head/base/attribution/CI and literal automatic Sourcery state belong in
the PR timeline. Local repository checker, **25 policy tests**, existing actionlint
1.7.12 and full-base whitespace check passed. Byte comparison confirmed every approved-
base tracked file unchanged, entire SDD/55 headings intact and R01/B01d refs preserved.
Early `pr-record` failed in **44683364352** after automatic summary
displaced the trailer; preserved summary, restored final trailer, live attribution
1/1 passed. Repository checker passed at checkpoint. No manual review request/label.
No source HTTP failure; S5 index-only response and selected view are disclosed above.
No customer/API/SDK operations, accounts/outreach, installed artifacts, native probes,
code/fixtures, environment/runtime/model/permission changes or spend. Existing corpus/
host/store probes and product/enforcement tests were not rerun. Previous branches and
historical review checkouts remain intact; no approval, merge or next-task dispatch.
