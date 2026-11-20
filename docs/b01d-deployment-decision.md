# B01d offline Linux deployment decision

Status: documentation-only round one for [issue #16](https://github.com/Himanshu-singh04/hooktrace/issues/16);
decision in progress. No deployment, actor exclusion or contract delta is accepted.

## Authorization and bound

Founder asked “whats next, whats the plan, how much is all the three projects completed”
and replied **“ok proceed”** on 2026-11-20 to ReleaseLens-first prioritization and
bounded independent feasibility decisions. The subsequent rotating business/development
research instruction and fixed A1–A6 are preserved in issue #16. This is one round;
later questions return to the coordinator for dispatch, not automatic execution.

Base: `457a84aec693c5ecb07a2ed32e8b0377c40186f0`, accepted B01c PR #15;
[main CI 44677019272](https://github.com/Himanshu-singh04/hooktrace/actions/runs/44677019272) passed.
Assess exactly one candidate: Apple Virtualization.framework, one offline Linux guest,
guest-owned filesystem, no host shared folders, controlled producer/reader roles,
and no guest network device during capture. Trace origin, ingress, capture and result
extraction; a host copier/stream is not a safe-origin assumption. Host user/admin/
hypervisor and guest admin/mount actors remain explicit obligations.

Deadline: 2026-11-20 07:15 UTC; one cycle, at most eight new primary documents,
roughly 200–250 lines. Sources establish API reasoning, never measured enforcement.
No VM, artifact download, install, new probe, account, customer input, code, paid spend,
permission/storage/mount/ownership change or portfolio-file read. Same persistent
GPT-6 Astra / OpenCode worker, no subagents; prior branches/checkouts preserved.
Arbitrary-input and current-setup NO-GO, unaccepted P1–P4 and remaining product gates
stay in force. Preserve normative documents, experiments and all 55 SDD headings.
