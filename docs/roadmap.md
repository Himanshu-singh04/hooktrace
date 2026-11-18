# Roadmap and bounded backlog

Status: proposal under [issue #4](https://github.com/Himanshu-singh04/hooktrace/issues/4).
No product milestone below has shipped; ordering denotes dependencies, not dates.
Each implementation task requires its own issue, reviewed acceptance, checks, and PR.
Requirements: [product](product.md); ADRs: [design](specs/001-mvp/solution-design.md).

## Ordered milestones

| Milestone | Depends on | Observable exit / verification |
| --- | --- | --- |
| M0: reviewable plan | Foundation | Owner reviews exact documentation revision; ADR proposals and unresolved choices recorded; foundation checks pass |
| M1: trustworthy import | M0, B01 | Frozen synthetic bundles with located validation, version/scope handling, and tamper detection; T01–02,08–09 |
| M2: evidence investigation | M1 | Independent evidence dimensions, ambiguous links, partial orders, unknowns; T03–05 |
| M3: reproducible local bug | M1, approved fixture design | Resettable buggy/fixed model and persisted read-back; T06,08 |
| M4: usable offline alpha | M2, M3 | Deterministic cited reports and documented clean install/demo; T07,09–10 |
| M5: reviewed pilot/release | M4 | Operator-owned pilot feedback, privacy review, supported-version matrix, release evidence |
| M6: optional explanations | M5, demonstrated demand | Cited RAG/agent evaluation and enforced tool boundaries; T11; no impact on deterministic core |

## Tasks

| Task | Scope and dependency | Acceptance and tests |
| --- | --- | --- |
| B01 | Runtime/contract spike after M0; ADR-1–4 | Compare supported Node/TypeScript versions and minimal packaging/test/schema/canonicalization choices; pin exact versions only after approval. Review at least two differing Stripe snapshot API-version samples and select explicit supported/unsupported matrix. Choose transactional synthetic store with close/reopen verification. Record install/license/offline findings; no production integration |
| B02 | Implement contract/import/freeze after B01; HT-01,02,08,09 | Valid synthetic bundle imports; invalid fields/paths/refs/hashes fail with locations; immutable source hashes survive interruption; T01–02,08–09 |
| B03 | Deterministic correlation/rules after B02; HT-03–05 | Retry/duplicate rows retained, uncertain links visible, no timestamp-derived causal claims; exact expected findings for T03–05 |
| B04 | Packaged ordering fixture after B02 and fixture ADR; HT-06,08 | Buggy [D,U] fails access assertion; fixed both orders and duplicates pass after reset/read-back; no exported inputs executed; T06,08 |
| B05 | JSON/Markdown reporting after B03/B04; HT-07,09 | Every finding resolves evidence citations, aggregates count observations, model limits visible, byte-identical repeated output; T07,09 |
| B06 | Package/demo after B05; HT-10 | Clean supported-Mac install and offline runbook; record actual dependency/runtime versions, elapsed time/RSS, supported payload versions; T10 and Q1–Q5 |
| B07 | Three proposed pilots after B06 | Users run in their own environment; record task completion/unknown interpretation with consent, retain no raw customer evidence in Git; review H1–H4 and release/no-release decision |
| B08 | Explanation feasibility after B07 and ADR-5 approval; HT-11 | Pin local retrieval/model corpus and licensing, measure on available hardware, pass T11; agent cannot modify facts or execute arbitrary tools |

## Initial bounded implementation task

After documentation approval, **B01** is the first task: resolve runtime/adapter/store
choices with small synthetic experiments and a decision record. It must not quietly
bootstrap a full application. Exit requires exact recommended versions, alternatives,
licensing/install constraints, supported payload fixtures, and owner decision on ADRs.

The first code-bearing product slice, **B02**, is one bounded import: a manifest,
two subscription event exports, an attempt, a handler observation, and a state snapshot.
Include invalid scope/hash/path cases; publish normalized evidence with source refs.
Acceptance excludes report generation, AI, networking, or fixture execution so importer
trust boundaries can be verified independently. Preserve those later tasks explicitly.

## Pilot and release plan

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
