# B01a acquisition-safety prerequisite

Status: **Research in progress**, [issue #10](https://github.com/Himanshu-singh04/hooktrace/issues/10).
No acquisition policy is approved or implemented by this record.

## Assignment and bounds

Original founder instruction: “ok then proceed with the further tasks”, after the
three first research PRs merged. The coordinator selected B01's unresolved
device-node/mount gate before B02. Issue #10 preserves the full assignment and
fixed A1–A6 acceptance criteria. This persistent worker uses GPT-6 Astra / OpenCode;
no subagents or product implementation are involved.

Base: clean fetched main `97f1669ddd92a510f7d637429b1c21f53713ae40`.
Compare at most two strategies: descriptor-bound local mount policy (including
native nodev), and a genuinely trusted input/staging boundary. Preserve HT-08 and
descriptor-relative/no-follow acquisition. Investigate exact Darwin source/API
and installed SDK evidence before deciding whether a native probe adds evidence.
Never infer prevention from post-open rejection, a mount listing, or injected flags.

Any executable research is limited to generated regular files/directories,
symlinks and FIFO in task-owned cache paths. No devices, mount changes, arbitrary
exports, runtime installation, customer data, privileges or permissions changes.
If primary evidence establishes a counterexample, record no-go rather than build
an unsafe acquisition helper. Tests, explicit met/unmet/unverified verdicts and
remaining gates will accompany the completed decision.

## B01 approval and correction history

[Coordinator merge verification](https://github.com/Himanshu-singh04/hooktrace/pull/9#issuecomment-7002315562)
records founder approval of reviewed head `493027222584493d9722ec2dbfbba39043b53310`,
distinct from the earlier authorization to perform R7. PR #9 merged as the base
above; conditional Python/Acacia/SQLite direction is accepted for a separately
authorized next investigation, not runtime installation or B02 implementation.

R1/R3 validation corrections passed 11 acquisition and 5 store tests. R2's
device/mount limitation remains real. R4/R5 were fixed-literal SQL false positives;
R7 made the statements explicit for static review, preserving behavior. The fresh
Sourcery check passed before the replacement approval; prior failed checks and
superseded unapproved snapshots remain historical. The literal SQL and all B01
research source are preserved. Candidate runtime/build, fixtures, device/mount
and product isolation gates remain open.
