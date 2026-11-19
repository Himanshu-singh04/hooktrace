# Testing and evaluation proposal

Status: planned product verification, not executed tests. Existing policy checks are
listed in [CONTRIBUTING](../CONTRIBUTING.md). Product cases below accompany future code.
All mandatory CI fixtures are synthetic, offline, and reviewed; no paid inference,
Stripe accounts, secrets, customer exports, or live webhook delivery are required.
The [B01 record](b01-decisions.md) documents executed research assertions and their
limits; those results do not establish the planned product cases below.
[B01a](b01a-acquisition-policy.md) adds source-grounded mount/staging counterexamples
and reruns B01 controls. No device/mount enforcement test was performed; arbitrary
acquisition remains no-go. Future injected mount observations can test pre-leaf
control flow only, not establish native enforcement or a trusted staging boundary.

## Contract and behavior matrix

| Case | Requirements | Planned inputs and assertions |
| --- | --- | --- |
| T01: import | HT-01 | Supported JSON/JSONL plus null optional evidence; reject missing required fields, duplicate keys, unknown schema major/fields, invalid refs, timestamps, depth and unsafe numbers; source location survives diagnostics |
| T02: provenance | HT-02 | Re-import frozen bytes; alter one byte, declared count, or manifest; detect mismatch. Redacted derivative has a new hash and truthful parent. Arbitrary export never becomes Stripe-authenticated |
| T03: evidence separation | HT-03 | 200 with no handler; 500 with completed handler; completed handler with no snapshot; write-claimed with contradictory persisted read; each produces independent observations/gaps, never inferred success/failure or incident cause |
| T04: identity | HT-04 | Same event repeated, explicit retry, two executions, missing execution ID, different event IDs with same object/type, and conflicting payloads for one event ID; retain rows, classify ambiguous links, never choose nearest timestamp |
| T05: boundaries/order | HT-05 | Same IDs in different accounts/test sandboxes, null account, conflicting scope, mixed API versions, thin event, equal `created`, clock skew, missing arrival indices; no cross-boundary explicit link or invented total order |
| T06: local reproduction | HT-06 | Reset buggy/fixed handlers for [U,D], [D,U], and duplicate permutations; close/reopen store before checking access. Buggy inversion fails, fixed cases pass; interruption yields incomplete and fresh reset removes prior state |
| T07: reporting | HT-07 | Golden JSON/Markdown, all source pointers/hashes resolve, escaped HTML/instruction-like payload, repeated runs, independent aggregate count recomputation; modeled outcomes cannot alter observed production findings |
| T08: trust boundary | HT-08 | Path traversal/symlink/device/URL/module/shell-shaped inputs rejected or inert; observe zero product DNS/outbound sockets with network denied; no imported handler/plugin loaded; only packaged fixture IDs accepted |
| T09: resource/recovery | HT-09 | At and above limits, full disk, read-only destination, removable-volume loss, interrupted publication, existing output, dangling citations; bounded diagnostic, original bytes intact, no partial final report |
| T10: operator workflow | HT-10 | Fresh supported Mac environment: documented install, disconnect network, import/analyze/reproduce/read report; no account setup or paid service; record time, versions, RAM, and unknown interpretation |
| T11: later AI | HT-11 | Evidence gaps, malicious retrieved instructions, unsupported claims, wrong citations, conflicting evidence, and exhausted tool budgets; abstain/label hypotheses, reject invalid citations/tool calls, preserve deterministic output |

## Planned contract-review regressions

These cases address contract reviews; product cases are planned tests, not executed
by this documentation change. Milestone/research cases require later evidence review.

| Finding / cases | Planned regression and oracle |
| --- | --- |
| R1 / T01,T04 | Raw attempt rows a1/a2 and handler h1 use only source-qualified row refs, including forward/cross-file refs. Hash frozen files, assign output IDs, rewrite refs in pass two; correct targets resolve without any input knowing a derived ID. Reject duplicate source-local labels, dangling/wrong-collection refs, retry self-links/cycles, and known scope/endpoint/producer mismatches; unknown boundary yields a gap, not explicit confidence |
| R2 / T02,T04 | Declare two byte-identical export files under stable source IDs A/B. Each row gets a different observation ID and its own original source/pointer refs; repeated import yields the same respective IDs. Reject duplicate Source.id; shared physical frozen bytes must not collapse observations |
| R3 / T04,T05 | Two apps emit the same request/execution/transaction/store/stream values under one Stripe account. Known incompatible namespaces cannot join or order; unknown or label-only namespaces cannot produce explicit links. Equal transaction IDs in different store domains remain separate. Positive control uses captured metadata/evidenced mapping for both producers and matching per-family domains, retaining unauthenticated-source limitations. Repeat same-source ambiguous/missing-domain cases; provider event ID equality never selects a local execution |
| R4 / T05,T07 | Import Order accepts observed_arrival only and only imported Attempt nodes in one evidenced stream. Reject a synthetic order basis, fixture snapshot target in Node/Link/Order/Finding, cross-registry Ref, and source/artifact ID collision. FixtureRun.permutation and run-local assertion/artifact refs still resolve independently |
| R5 / T06,T08,T10 | Omitted options and explicit D,U / seed 0 produce identical FixtureRun values; rerun recorded options/hashes to identical output. Exercise U,D; duplicate tokens; lengths 2/8 accepted and 0/1/9 rejected; missing U/D, empty tokens, unknown IDs/fixtures, whitespace, URL/path/payload, unknown/repeated options, negative/fractional/overflow seeds rejected. Seeds 0/4294967295 accepted and recorded with no behavioral effect in this fixture. Direct runFixture calls enforce the same bounds |
| R6 / T02,T08,T09 | At controlled boundaries swap root/ancestor/leaf paths for symlinks to an outside sentinel, including the manifest. Capture only the pinned original descriptor's bytes or fail; no outside-sentinel bytes enter evidence. Check regular-file enforcement, concurrent mutation rejection, descriptor cleanup, and PLATFORM_UNSUPPORTED without unsafe fallback; B01 must prove platform feasibility |
| R7 / T01,T07 | Validate every allowed subscription-state/1 field/type; reject unknown schema/keys, credential or metadata fields, nested structures, null, invalid status, string booleans, and negative/fractional/unsafe counts. Use synthetic secrets to verify rejected values are absent from diagnostics/reports; raw quarantine is still sensitive, not declared secret-free |
| R9 / T01,T03 | Reject a key present in values and absentFields (including false/zero values), duplicate absence names, and unapproved absent fields. Accept disjoint subsets; a key in neither remains unknown, never defaulted |
| R10 / T06,T07 | Valid typed equal values derive pass; unequal values derive fail. Reject forged result, expected/actual mismatch with fixture/snapshot, and cross-type coercion. Missing/absent fields, wrong read-back types, non-persisted reads, invalid artifact hashes, or missing required checks produce incomplete with no fabricated assertion; empty checks never pass |
| R11 / T01 | Reject start>end; accept start=end and start<end; each null-endpoint combination remains unknown and is not inferred from events. Invalid UTC timestamps remain errors |
| R12 / milestone review | B06 can close with developer T10 smoke and Q1/Q2/Q4/Q5 before pilots exist; Q3 is measured and assessed in B07 only. Verify M4→B07/M5 has no pilot prerequisite cycle |
| R13 / B07 evidence review | Require five interviews, three pilots, H2 comprehension/next checks, H3 manual-workflow comparisons and regression outcomes, and H4 post-use buyer/pricing questions. Missing collection blocks completion; negative signals remain negative, not substituted with general pilot feedback |

## Synthetic corpus and oracles

Keep fixture source, provenance, expected findings, supported API-version labels, and
human-reviewed rationale together. Do not obtain fixtures by triggering Stripe events.
Fixture U is a synthetic active subscription update; D is cancellation of the same ID.
The model defines cancellation as terminal. The buggy implementation overwrites with
each snapshot; the fixed implementation transactionally tombstones and deduplicates.
Expected final access is false after D under either order, independent of timestamps.
Use fixture-defined ordering, not invented provider sequence numbers.

The test oracle checks read-back persisted values and mutation/idempotency counts,
not just successful function returns or emitted logs. Reuse the same inputs/initial
state to compare variants; record fixture, handler, initial-state hashes and seed.
Have a reviewer inspect expected findings so tests do not merely mirror implementation.
Include “same result, unknown cause” cases to prevent a plausible narrative becoming fact.

## Proposed measurable targets

These are engineering budgets to validate, **not benchmarks already achieved**.
Observed host: 16 GiB RAM and 8 logical CPUs; no inference throughput is known.

| Target | Proposed measurement / pass condition |
| --- | --- |
| Q1 determinism | T07: ten runs of identical frozen inputs/tool/rules/fixture produce identical JSON and Markdown bytes; separate timing logs excluded |
| Q2 bounded performance | T09: synthetic 10,000-record, 50 MiB bundle; five runs, report median and max wall time/RSS; every analysis ≤10 s and ≤512 MiB peak RSS on recorded host/runtime |
| Q3 first use (B07) | T10 pilot evaluation after B06: three proposed pilot engineers, at least two complete synthetic workflow and correctly distinguish unknown from failed in ≤15 min after dependencies installed |
| Q4 isolation | T08: network-denied integration run plus socket/DNS observation shows zero outbound attempts; adversarial import cases cause no code execution or writes outside owned output |
| Q5 publication integrity | T09: interrupt at each write/publication boundary; zero valid-looking partial final bundles; re-run to new directory verifies source hashes |

B06 uses developer-run T10 installation/demo smoke plus Q1/Q2/Q4/Q5; it does not
require pilot participants or a Q3 result. B07 owns Q3 and H1–H4 evidence collection/
assessment, following the explicit [roadmap acceptance matrix](roadmap.md).

Initial proposed hard caps: 50 MiB total raw input, 10 MiB/file, 10,000 normalized
records, depth 32, 16 KiB normalized strings, 100 candidate targets/link, 100,000 total
links, 20 MiB report, 30 s analysis timeout, 5 s per fixture run. Reject excess,
never truncate silently. Performance target is below timeout; the target dataset must
fit candidate/report caps. Measure startup separately. Revisit limits with recorded evidence.

## Later RAG and bounded-agent evaluation

MVP has no model. For B08, use an owner-reviewed frozen local corpus of provider docs
and synthetic reports, with document hashes, section citations, fetch dates, and scope.
Retrieval should explain known rules and suggest next evidence checks, not supply
missing incident facts. Proposed initial evaluation: 30 reviewed cases, including
10 missing-evidence and 10 prompt-injection/unsafe-tool cases (categories may overlap).
Require 100% resolvable citations, zero unsupported assertions presented as observed
facts, zero unauthorized tool actions, and ≥90% reviewer-rated useful explanations.
Record sample size, grader rubric/disagreements, model/version/quantization, corpus,
latency, peak RSS, and failures; these thresholds are proposed gates, not accuracy claims.
Bounded agent proposal: at most five read-only evidence tools and one approved synthetic
run per request, 60 s timeout, allowlisted arguments, no network/shell/imported code.
Enforcement and a model hardware/license spike must pass before enabling any agent.

## Reporting checks honestly

Record exact command, revision, corpus hash, environment, exit/result, and limitations
in each task/PR. Repository checks do not verify product semantics or demand.
The tracked-file checker misses untracked new docs until staging; independently check
their formatting/relative links and SDD template headings before handoff.
The documentation PR can pass planning acceptance while ADR approval and all product
tests remain pending. It cannot claim MVP acceptance or runtime readiness.
