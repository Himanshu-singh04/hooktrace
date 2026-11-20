# Roadmap and bounded backlog

Status: M0 planning review completed in [PR #5](https://github.com/Himanshu-singh04/hooktrace/pull/5);
[B01 research](b01-decisions.md) accepted conditionally in PR #9. [B01a](b01a-acquisition-policy.md)
research NO-GO was accepted in PR #11; arbitrary exports remain blocked and the
producer-created intake workflow is still an unaccepted proposal. [B01b](b01b-fixture-corpus.md)
fixture research is accepted in PR #13. [B01c](b01c-producer-intake.md) is accepted
current-setup NO-GO research in PR #15. [B01d](b01d-deployment-decision.md) assesses
one offline Linux deployment and recommends pausing intake; no final boundary or
contract/threat change is accepted.
No M1–M6 product milestone has shipped; ordering denotes dependencies, not dates.
Each implementation task requires its own issue, reviewed acceptance, checks, and PR.
Requirements: [product](product.md); ADRs: [design](specs/001-mvp/solution-design.md).

## Ordered milestones

| Milestone | Depends on | Observable exit / verification |
| --- | --- | --- |
| M0: reviewable plan | Foundation | Owner reviews exact documentation revision; ADR proposals and unresolved choices recorded; foundation checks pass |
| M1: trustworthy import | M0, B01 | Frozen synthetic bundles with located validation, version/scope handling, and tamper detection; T01–02,08–09 |
| M2: evidence investigation | M1 | Independent evidence dimensions, ambiguous links, partial orders, unknowns; T03–05 |
| M3: reproducible local bug | M1, approved fixture design | Resettable buggy/fixed model and persisted read-back; T06,08 |
| M4: usable offline alpha | M2, M3 | Deterministic cited reports and developer-run clean install/demo; T07,09–10 and Q1/Q2/Q4/Q5; Q3 remains for M5 |
| M5: reviewed pilot/release | M4 | B07 interview/pilot/pricing evidence for H1–H4, Q3 measurement, privacy review, supported-version matrix, release decision |
| M6: optional explanations | M5, demonstrated demand | Cited RAG/agent evaluation and enforced tool boundaries; T11; no impact on deterministic core |

## Tasks

| Task | Scope and dependency | Acceptance and tests |
| --- | --- | --- |
| B01 | Runtime/contract spike after M0; ADR-1–4 | Compare supported Node/TypeScript versions and minimal packaging/test/schema/canonicalization choices; pin exact versions only after approval. Prove pinned-root descriptor-relative/no-follow acquisition feasible on the proposed Mac/runtime/filesystem, including ancestor/leaf swaps; review any required helper or runtime change before B02. Review at least two differing Stripe snapshot API-version samples and select explicit supported/unsupported matrix. Choose transactional synthetic store with close/reopen verification. Record install/license/offline findings; no production integration |
| B01a | Acquisition threat-policy decision after accepted B01 research; before B02 | Compare descriptor-bound nodev policy and genuinely trusted intake; exact Darwin/SDK evidence, explicit actor/device/mount/hard-link assumptions and no-go where guarantees remain unsupported. Issue #10 A1–A6; no product importer or arbitrary-tree authority |
| B01b | Narrow synthetic fixture corpus after B01; independent of acquisition implementation | Issue #12 A1–A6 accepted in PR #13: one positive bundle, tagged field provenance, independent expectations, finite variants and fixed-file stdlib corruption checks. No canonicalizer or importer |
| B01c | Producer-created intake design after explicit founder study authorization | Issue #14 A1–A6: customer workflow/cost, origin/actor/bootstrap authority, source-backed feasibility or NO-GO, lifecycle/future tests and unaccepted contract deltas. Documentation only; no implementation or actor-model weakening |
| B01d | One offline Linux guest deployment decision | Issue #16 A1–A6: origin/ingress and host/guest authority, customer cost, exact unaccepted deltas and pause recommendation; three later questions for coordinator dispatch. Documentation only |
| B02 | Implement contract/import/freeze after B01; HT-01,02,08,09 | Valid synthetic bundle imports; invalid fields/paths/refs/hashes fail with locations; descriptor-based capture resists symlink substitution; closed snapshot fields/types, disjoint presence/absence, and coverage bounds validated; immutable source hashes survive interruption; T01–02,08–09 |
| B03 | Deterministic correlation/rules after B02; HT-03–05 | Retry/duplicate rows retained, uncertain links visible, no timestamp-derived causal claims; exact expected findings for T03–05 |
| B04 | Packaged ordering fixture after B02 and fixture ADR; HT-06,08 | Buggy [D,U] fails access assertion; fixed both orders and duplicates pass after reset/read-back; derive typed comparisons from available persisted evidence, missing checks yield incomplete; reject inconsistent serialized assertions; no exported inputs executed; T06,08 |
| B05 | JSON/Markdown reporting after B03/B04; HT-07,09 | Every finding resolves evidence citations, aggregates count observations, model limits visible, byte-identical repeated output; T07,09 |
| B06 | Package/demo after B05; HT-10 | Developer-run clean supported-Mac install and offline runbook; record actual dependency/runtime versions, elapsed time/RSS, supported payload versions; T10 smoke and Q1/Q2/Q4/Q5. Q3 pilot usability is deferred to B07 |
| B07 | Five interviews and three proposed pilots after B06 | Collect and assess each H1–H4 signal using the acceptance matrix below; measure Q3 with pilot engineers. Consent-based local runs, no raw customer evidence in Git; record met/unmet/unverified evidence and owner release/no-release decision |
| B08 | Explanation feasibility after B07 and ADR-5 approval; HT-11 | Pin local retrieval/model corpus and licensing, measure on available hardware, pass T11; agent cannot modify facts or execute arbitrary tools |

## Initial bounded implementation task

**B01** is complete as conditional research, not an application or validated runtime.
**B01a** is accepted as a research NO-GO; it does not resolve the acquisition gate or
approve producer-created intake. **B01b** supplies the narrow synthetic corpus and
finite expectations as accepted research. B01c's current-setup NO-GO is accepted;
its proposed deltas remain unaccepted. Runtime/build,
complete provider/schema validation, independent canonical identity/hash oracles,
missing-event-ID output disposition and isolation remain open before separately
authorizing B02. Unsupported acquisition primitives block that platform/runtime
proposal; path validation alone is not an accepted fallback.

The first code-bearing product slice, **B02**, is one bounded import: a manifest,
two subscription event exports, an attempt, a handler observation, and a state snapshot.
Include invalid scope/hash/path cases; publish normalized evidence with source refs.
Acceptance excludes report generation, AI, networking, or fixture execution so importer
trust boundaries can be verified independently. Preserve those later tasks explicitly.

## Pilot and release plan

B07 acceptance explicitly covers the [product hypotheses](product.md):

| Hypothesis | Required collection and assessment before the B07 decision |
| --- | --- |
| H1 | Conduct five interviews about recent subscription incidents, evidence availability, and current tools; assess whether at least three concrete incidents have available evidence. Record counts and counterexamples without collecting the incident payloads |
| H2 | Complete three guided customer-owned pilots; assess whether at least two users independently explain report evidence gaps and select a next check. Separately measure Q3 timing and unknown-versus-failed comprehension |
| H3 | Record each pilot's existing debugging workflow/manual baseline and compare with the bundled exercise; assess whether at least two users run a regression and identify the verified local state change, without claiming production causality |
| H4 | After use, ask each pilot team's buyer about repeat use/support and the proposed $29–79/team/month range; record positive, negative, and declined responses and assess the target of two explicit willingness-to-pay responses. Interest is not revenue |

Interviewees may also be pilot participants; record unique participant counts and
engineer/buyer roles. Task completion requires collecting and assessing all four signals,
not obtaining positive answers. Missing interviews/workflow comparisons/buyer questions
remain unverified and block claiming B07 complete. Unmet signals and Q3 failures lead
to an explicit revise/pause/release decision, not an invented validation success.

Recruit interviewees using synthetic demos first. No customer data is needed to prove
M1–M4. For pilots, operators keep evidence locally and share only reviewed redacted
feedback/report excerpts voluntarily; neither remote access nor upload is a requirement.
Record observed completion time and manual baseline, not self-reported “AI accuracy.”
Stop expansion if users mistake reproduction for production proof or cannot supply
enough evidence to make reports useful. Revise wording/workflow and repeat the exercise.

Alpha packaging is proposed local distribution with a versioned artifact, checksum,
runtime/OS matrix, synthetic demo, source commit, dependency license inventory, and
known limitations. No public package publishing is authorized by this planning task.
Release requires acceptance review of HT-01–10, exact SHA/check evidence, honest unmet
quality targets, and the owner decision through [development](development.md).
Rollback uses a previous package and fresh output directory; raw inputs are untouched.
Pilot feedback determines whether broader adapters, a UI, or paid support merit work.
