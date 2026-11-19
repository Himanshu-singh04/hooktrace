# HookTrace product proposal

Status: planning review under [issue #4](https://github.com/Himanshu-singh04/hooktrace/issues/4) completed in [PR #5](https://github.com/Himanshu-singh04/hooktrace/pull/5).
This is a proposed product, not implemented functionality or validated demand.
[B01](b01-decisions.md) conditional Python/Acacia/SQLite direction was accepted in PR #9;
exact build and acquisition choices remain gated before separate implementation tasks.

## Problem and first customer

An engineer investigating a subscription-access discrepancy may have a Stripe event,
a successful delivery, application logs, and a database snapshot that disagree.
Those artifacts answer different questions. HookTrace should assemble a reviewable
evidence trail and demonstrate a suspected failure mechanism in a local model.

The initial customer hypothesis is a small B2B SaaS team with Stripe subscriptions,
a custom webhook handler, and an engineer who can export logs and state safely.
The first user is that engineer; a technical founder is the proposed buyer.
Support staff can read reports but are not expected to configure mappings.
This excludes a general payment debugger, live incident response, and billing operations.

## Demand and commercial hypotheses

| Hypothesis | Proposed validation | Decision signal, not an achieved result |
| --- | --- | --- |
| H1: joining evidence is a recurring burden | Five interviews about recent incidents and existing tools | At least three concrete incidents with available evidence |
| H2: an offline report is useful without live integration | Three guided, customer-owned pilots after synthetic acceptance | Two users independently explain the evidence gaps and choose a next check |
| H3: a reproducible fixture improves debugging | Compare users' existing workflow with the bundled exercise | Two users run a regression and identify the verified local state change |
| H4: teams will pay for repeat use/support | Ask buyers about a proposed $29–79/team/month range after use | Two explicit willingness-to-pay responses; not revenue or a forecast |

If users cannot export meaningful handler/state evidence, prioritize instrumentation
guidance or narrow the audience before building more analysis. Existing logs, Stripe
Workbench, and manual tests are the baseline alternatives; no superiority is claimed.
Pricing, licensing, distribution, and any paid offering need a later owner decision.

## Agreed constraints versus proposals

Agreed task constraints: local-first, independent repository, zero new initial hosting
or inference spend, no live Stripe calls, no remote replay, no execution of imported
code, honest unknowns, and human-reviewed delivery. Only synthetic artifacts enter Git.
Conditional B01 direction: Python modular CLI, file bundles, normalized v1 schema,
bounded rules, and a bundled SQLite ordering fixture. Runtime/version, dependencies,
and supported Stripe payload versions remain gated in the [design](specs/001-mvp/solution-design.md).

## User workflows

1. **Prepare:** collect a bounded set of exported snapshot events, delivery attempts,
   explicit handler observations, and business-state snapshots; declare scope and gaps.
2. **Import:** freeze exact source bytes with hashes and provenance; validate without
   fetching missing resources. Invalid records receive located diagnostics.
3. **Investigate:** inspect independent delivery, handler, and state evidence; review
   candidate correlations, ambiguity, missing observations, and clock limitations.
4. **Model:** select the bundled synthetic ordering scenario, reset its isolated store,
   run the declared permutation against buggy and fixed handlers, compare assertions.
5. **Share locally:** export deterministic JSON and readable Markdown with citations,
   limitations, and local reproduction results; review redaction before sharing.

The MVP input adapter targets Stripe v1 snapshot `customer.subscription.created`,
`customer.subscription.updated`, and `customer.subscription.deleted` exports.
Invoice events can be retained as unsupported context; deeper invoice linkage,
thin events, entitlement policy, and other providers are later scopes.
Delivery/log/snapshot exports must be supplied in the explicit contract, not guessed
from arbitrary text. Supported API-version fixtures must be selected before implementation.

## Requirements and traceability

Every row is a proposed acceptance obligation, not a shipped capability.
Component names refer to the [solution design](specs/001-mvp/solution-design.md);
case IDs refer to [testing](testing.md), task IDs to [roadmap](roadmap.md).

| ID | Requirement and observable acceptance | Component | Test / task |
| --- | --- | --- | --- |
| HT-01 | Import versioned local bundles; reject invalid required fields with source locations and never silently drop records | Importer, Store | T01 / B02 |
| HT-02 | Preserve exact raw bytes, scope provenance, source hashes, and a verifiable frozen manifest; detect later tampering | Store | T02 / B02 |
| HT-03 | Keep delivery, handler execution, and persisted state as separate evidence dimensions; absence remains unknown | Analyzer | T03 / B03 |
| HT-04 | Preserve duplicate receipts and retries; expose ambiguous and missing correlations without arbitrary selection | Analyzer | T04 / B03 |
| HT-05 | Partition account, environment, and API-version interpretation; never infer arrival or causal order from event creation time | Importer, Analyzer | T05 / B03 |
| HT-06 | Reset and reproduce a declared ordering bug in a bundled synthetic handler; demonstrate fixed-handler assertions against read-back state | FixtureRunner | T06 / B04 |
| HT-07 | Produce offline JSON/Markdown findings with source-level citations, counts, unknowns, and explicit modeled-scenario limitations | Reporter | T07 / B05 |
| HT-08 | Parse imports as inert data; make no live Stripe calls or remote replay; execute only the packaged synthetic fixture | CLI, Importer, FixtureRunner | T08 / B02, B04 |
| HT-09 | Bound input size/work; emit actionable errors and publish only complete bundles; recover without modifying raw evidence | CLI, Store | T09 / B02, B05 |
| HT-10 | Complete a documented local install/demo using existing resources and no paid inference/hosting | CLI | T10 / B06 |
| HT-11 | Later explanations cite evidence and label hypotheses; bounded tools cannot override deterministic findings | Later explanation layer | T11 / B08 |

## MVP exit and exclusions

MVP exit: HT-01 through HT-10 pass the synthetic corpus and clean-machine exercise,
the owner reviews the exact revision, and limitations accompany the release.
HT-11 is deliberately a later gate; AI is not necessary to obtain any MVP finding.
Proposed quality targets and their measurement procedures live in [testing](testing.md).

Excluded: hosted UI/API, webhook receiver, automatic remediation, customer handler
execution, arbitrary plugins, production replay, live Stripe retrieval, RAG/agents in
the MVP, fraud/tax/payment correctness certification, and automatic incident root cause.
A modeled ordering failure proves that the local model can fail that way; it does
not prove that production executed the same code or failed for the same reason.

## Review and next step

The [evidence contract](evidence-contract.md) defines meaning before implementation.
The [roadmap](roadmap.md) starts with contract/runtime decisions and a bounded schema task.
[Operations](operations.md) records actual storage and execution limits. Issue A6's
approval-process changes are coordinated in [development](development.md), outside
this product proposal; this document grants no worker approval authority.
