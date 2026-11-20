# B01d offline Linux deployment decision

Status: **Decision ready for review; recommend pausing customer intake**, [issue #16](https://github.com/Himanshu-singh04/hooktrace/issues/16).
The named candidate does not satisfy the unchanged full-chain obligations. No
deployment, actor exclusion, interface, contract delta or implementation is accepted.

## Authorization and bound

Founder asked “whats next, whats the plan, how much is all the three projects completed”
and replied **“ok proceed”** on 2026-11-20 to ReleaseLens-first bounded feasibility work.
Issue #16 preserves authorization, rotating research instructions and fixed A1–A6;
later questions return to the coordinator for dispatch, not automatic execution.

Base: `457a84aec693c5ecb07a2ed32e8b0377c40186f0`, accepted B01c PR #15;
[main CI 44677019272](https://github.com/Himanshu-singh04/hooktrace/actions/runs/44677019272) passed.
Assess exactly one candidate: Apple Virtualization.framework, one offline Linux guest,
guest-owned filesystem, no host shared folders, controlled producer/reader roles,
and no guest network device during capture. Trace origin, ingress, capture and result
extraction; a host copier/stream is not a safe-origin assumption. Host user/admin/
hypervisor and guest admin/mount actors remain explicit obligations.

Deadline 2026-11-20 07:15 UTC; one cycle, eight new primary documents, about 200–250 lines.
No VM, artifact download/install, probe, account, customer input, code, paid spend,
permission/storage/mount/ownership change or portfolio-file read. Same persistent
GPT-6 Astra / OpenCode worker, no subagents; prior branches/checkouts preserved.
Arbitrary-input/current-setup NO-GO, P1–P4 and product gates remain; normative documents,
experiments and all 55 SDD headings are preserved. Sources are not measured enforcement.

## Customer journey and ingress decision (A1)

The prospective user is a SaaS engineer investigating a subscription/access discrepancy.
Events, delivery/handler logs and state normally reside in their app environment; **no customer location,
retention, demand or willingness to provision this appliance has been validated**.

1. Engineer inventories incident scope, account/environment, clocks and retained
   records where the application already holds them. Required identities must validate;
   unavailable optional logs/snapshots remain unknown. No live Stripe retrieval.
2. A separately reviewed source-side producer would need to read application-held
   data through a demonstrated safe acquisition path. “Already open” is not proof of
   that earlier acquisition; an arbitrary export-folder reader is still blocked.
3. **Ingress stops here today.** The application data is not thereby present inside
   the offline guest. No approved producer, transport, framing, size/failure protocol
   or receiving implementation exists. A host stream over D1's console or D4's socket
   can carry bytes but cannot establish the sender's safe origin or source authority.
4. Only after a separately approved origin/ingress chain could a guest producer emit
   fresh generated-name regular files under its controlled job root, with manifest,
   emitted-byte hashes and truthful provenance. A host-populated disk image merely
   moves acquisition to preparation; it does not meet step 2. No host folder is shared.
5. Reader would establish handoff eligibility before leaf reads, freeze/count/hash
   using the same validated descriptors, validate frozen bytes, then publish complete
   output. This is the unimplemented lifecycle below, not a working customer command.
6. Engineer needs a result view and local JSON/Markdown for sharing. Neither guest
   viewer nor safe host extraction exists. Displaying guest text through the console
   is not an exact-byte artifact export; a bounded export channel and host-owned output
   publication require separate review, including untrusted terminal/report content.

Running the customer's application in this guest to originate data would instead
require a new deployment and customer-code execution decision (currently excluded
by product scope); it cannot recover the original production incident or manufacture
missing events. Generating synthetic records in the guest avoids customer ingress
only for a demo, not for customer intake. There is no endorsed pre-capture networking
phase: unplugging a network later would not establish prior origin or remove secrets.

**Costs without invented estimates:** customer engineering must inventory retained
representations, review producer data access, maintain mappings/version compatibility,
and diagnose missing identifiers. Appliance work adds Mac compatibility, runner
build/signing, guest boot/runtime packaging, role provisioning, upgrades and recovery.
Storage includes guest OS, originals, frozen/temporary/derived output and host copies.
CPU/RAM compete locally; D1's sample allocation is not a HookTrace sizing result.
Offline patch delivery and artifact/license maintenance remain costs without paid hosting.
Only historical records still available at a qualifying origin could be re-exported;
loose archives and snapshots of today's state cannot restore lost past evidence.

## Eight-document source ledger (A3)

Read 2026-11-20; **8/8 new primary documents**, no linked sample/archive/image fetched.
Apple pages used their `/tutorials/data/documentation/...json` rendering of the URLs
below; D2 was re-read after truncation, not counted as another document.
Apple pages are live documentation, not pinned framework source. Linux manuals describe
interfaces, not the unselected guest kernel/filesystem. No conformance was measured.

| ID / exact document | Relevant section and supported claim; limit |
| --- | --- |
| D1 [Running Linux in a Virtual Machine](https://developer.apple.com/documentation/virtualization/running-linux-in-a-virtual-machine) | “Configure the Sample Code Project”, boot parameters and serial-port sections: caller supplies architecture-matching kernel/initrd; host configures boot command line and bidirectional stdin/stdout console. Sample starts in initramfs; it is not a provisioned HookTrace appliance or safe importer |
| D2 [VZVirtualMachineConfiguration](https://developer.apple.com/documentation/virtualization/vzvirtualmachineconfiguration) | Overview / “Adding devices to the VM”: host selects boot loader and exposed network, storage, directory-sharing, serial, console, socket and other devices. `validate()` checks configuration viability, not adversarial isolation or data origin |
| D3 [VZDiskImageStorageDeviceAttachment](https://developer.apple.com/documentation/virtualization/vzdiskimagestoragedeviceattachment) | Overview / “Create the disk image” / “Initialize the disk image”: guest writes land in a supplied host disk-image file; RAW offsets map 1:1. `readOnly`/cache/synchronization options exist. Guest filesystem ownership does not make that host file inaccessible to its host controller |
| D4 [VZVirtioSocketDevice](https://developer.apple.com/documentation/virtualization/vzvirtiosocketdevice) | Overview / port-listener and guest-port topics: host–guest service connections are available independently of an IP network device. No reviewed framing/authentication/origin guarantee is supplied by this API |
| D5 [capabilities(7)](https://man7.org/linux/man-pages/man7/capabilities.7.html) | DESCRIPTION, capability list and thread sets: `CAP_DAC_OVERRIDE` bypasses file checks; `CAP_SYS_ADMIN` covers mount operations; `CAP_SYS_PTRACE` permits process-memory access; `CAP_LINUX_IMMUTABLE` controls immutable flags. Credentials/capability sets matter, not UID labels alone; no guest configuration was inspected |
| D6 [open(2)](https://man7.org/linux/man-pages/man2/open.2.html) | DESCRIPTION (`O_CREAT`, `O_EXCL`, `O_NOFOLLOW`, `O_PATH`); NOTES “Open file descriptions” / openat rationale: regular exclusive creation, stable directory references, duplicated/fork-inherited open descriptions. No-follow protects the last component; read-only creation mode can still return a writable FD. O_PATH can avoid triggering an untriggered automount at that target; not a full-chain mount/authority proof |
| D7 [mmap(2)](https://man7.org/linux/man-pages/man2/mmap.2.html) | DESCRIPTION / `MAP_SHARED` / `munmap()` / NOTES: closing an FD does not invalidate a mapping, shared changes reach the underlying file, mappings survive fork. One producer exit does not remove another process's inherited mapping |
| D8 [com.apple.security.virtualization](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.virtualization) | Details / Discussion: Boolean entitlement permits framework use; configuration validation checks required entitlement. Does not supply a signed runner, supported guest or redistribution license |

D6/D7 identify Linux man-pages 6.19 in their colophons. Existing B01a/B01c evidence
supplies the host same-owner/mount threat obligations; Darwin results are not promoted
to Linux results. Source implications below are design reasoning, not native probes.

## Concrete authority and lifecycle (A2)

Candidate storage is a guest-created local filesystem in a host disk-image attached
as virtual block storage (D3), not a shared folder. The host supplies backing bytes,
boot artifacts and devices. “Guest-owned” does not establish a confidential VM or
protection against the controlling host.

| Actor | Authority / proposed constraint / unresolved result |
| --- | --- |
| Host user / runner owner | Chooses kernel/initrd, command line, image URL and device arrays (D1–D3). Same-owner processes can affect owner-controlled artifacts under retained B01c host evidence. Guest UID separation cannot constrain this controller |
| Host administrator / hypervisor | Controls the platform executing the guest and its storage/configuration. A hostile controller can substitute boot/image inputs or an earlier image before boot; guest hashes stored in that same image cannot establish freshness against it. Candidate provides no demonstrated constraint; actor remains in scope |
| Guest OS / bootstrap administrator | Must establish root, mount policy and role credentials before producer creation, from reviewed boot artifacts. Existing trusted-kernel premise is not automatic trust in a guest admin. No bootstrap chain exists |
| Guest mount administrators / services | Relevant `CAP_SYS_ADMIN` authority can mount/unmount; DAC/ptrace/immutable capabilities create further bypasses (D5). Must be constrained or explicitly re-scoped; changing producer UID does neither |
| Producer / helpers | Proposed distinct nonprivileged identity creates fresh regular files only from approved origin. Must not leak descriptors/mappings, regain privileges, alter mount route or write reader output. Review must cover effective/permitted/inheritable/ambient/bounding capabilities, not just UID |
| Reader / Store | Proposed separate nonprivileged identity, no imported code, no writes to originals; owns frozen output. No demonstrated protection from privileged guest actors, host controller, or a second process sharing its identity |
| Other guest writers | DAC can deny new opens when correctly provisioned and no bypass applies (D5/D6); it does not revoke previously acquired writable references (D6/D7). Absence of such references has not been established |

| Transition | Candidate obligation; prevention/exclusion/detection distinction |
| --- | --- |
| Bootstrap → create | Verify host runner/boot/image origin and protected ancestors, then guest-local anchor/mount authority before reading evidence. Guest admin creates controlled job root; producer creates exclusive regular files via retained parents (D6). Prevention at creation is conditional on parent authority, not an arbitrary-tree scanner |
| Write → complete | Producer emits bounded bytes, exact manifest counts/hashes, checks errors, relinquishes all writing references. Completion marker is only a claim. No manifest nominates its own trusted root; captured times/coverage are assertions |
| Complete → handoff | Must exclude unwanted writers and reacquisition, including duplicates, inherited/passed FDs and shared mappings. Ownership/mode changes, renamed directory, UID switch or one process exit are not revocation. A fresh reader copy detects some mismatches but cannot retrospectively make unsafe origin safe |
| Handoff → capture | If any authority/origin condition is unknown, stop before leaf reads. Otherwise retained directory/no-follow walk, same-FD type/metadata checks and bounded freeze/count/hash including manifest; no path reopen fallback. Post-read mismatch detection does not prevent device/mount effects |
| Capture → publish | Parse only frozen data, enforce refs/scope/schema/limits, publish complete output exclusively; no change to originals. Reader ownership/immutable flags do not protect against all D5 actors or the host image owner. “Immutable output” is an unmet requirement here, not a VM property |
| Crash → recovery | Partial jobs/output stay incomplete, never promoted by a marker. Re-establish authority and identity or start a new job; retain original and sensitive incomplete bytes under existing policy. No input-directed recursive cleanup; no automatic deletion/upload, secure-flash-erasure or rollback-detection promise |

The contract already disclaims a filesystem-wide snapshot and protection against an
authorized in-place writer (`evidence-contract.md:111–113`). This decision does not
invent that guarantee. The unsatisfied B01c obligation is establishment of the safe
creation/acquisition boundary against the named namespace/mount/other-writer actors;
privileged access also prevents an absolute post-publication immutability claim.

## Full-chain verdict and absent deployment (A3)

| Link | Verdict under unchanged obligations |
| --- | --- |
| Customer origin → guest producer | **Blocked:** safe source acquisition and ingress interface absent. Fresh receiver-side files cannot attest how host/source bytes were obtained |
| Host → guest storage/boot | **Unmet against controlling actors:** D1–D3 leave the host choosing boot and image; no mechanism prevents substitution by that authority. No shared folders removes one path, not host control |
| Guest roles → eligible handoff | **Unverified and insufficient alone:** D5–D7 support narrower permissions, but privileged actors and retained capabilities/references remain unresolved |
| No network device → offline capture | **Configurable in principle, unverified:** explicitly empty network and directory-sharing arrays; exclude socket/serial/console forwarding and unneeded devices during capture. A sample interactive console cannot silently remain an ingress channel. No-NIC does not prove the host cannot proxy/fetch or export data |
| Frozen output → customer result | **Blocked:** no viewer/extraction protocol; mounting or copying a guest image on the host is not a proven safe exporter. Adding D4 sockets or D1 console transfer needs a separate bounded data-only protocol and safe host publication; extraction after capture still needs retention/authority review |

Required but absent: reviewed macOS runner with D8 entitlement/build/signing recipe;
exact host/CPU/API support; compatible kernel/initrd, root filesystem/distribution and
image hashes; guest mounts/capabilities; offline Python/dependency/SQLite build/linkage;
producer, reader, handoff mechanism and viewer/exporter. Fresh safe host backing-file
creation and boot artifacts need bootstrap authority before guest checks. Disk-attachment
read-only mode cannot revoke host authority or make a writable job disk globally
immutable. No storage target was provisioned.

Exact distribution/kernel/runtime/dependency licenses, applicable source-offer/notices,
artifact provenance and update/rollback policies remain unreviewed; API docs provide
no licensing clearance. B01 runtime pins/results are not a Linux build. No guest boot
or $0 appliance installation was demonstrated. Compatibility, resources, durability
and network confinement remain unverified; no platform substitution is proposed.

## Exact proposed deltas, not adopted (A4)

Only **R0 (pause)** is recommended. R1/R2 expose a reopening trade, not implementation
permission or a completed chain. P1–P4 remain unaccepted; normative documents are unchanged.

**R0 — pause customer workflow; P1/P4, HT-01/02/08/09.** Current
`product.md`, “User workflows”, step 1: “**Prepare:** collect a bounded set of exported
snapshot events, delivery attempts, explicit handler observations, and business-state
snapshots; declare scope and gaps.” Exact proposed replacement for that step:
“**Prepare (customer intake paused):** no customer bundle is eligible on the current
setup or the assessed Linux guest. Preserve the proposed evidence workflow for future
review; only repository-reviewed synthetic evidence may inform separately authorized
development. Reopening requires an explicit scope decision and a demonstrated safe
origin, ingress, handoff and extraction chain.” Loss: no customer incident onboarding
now. Retained: all data meaning, raw preservation, inert-data and complete-publication
obligations. Revised oracle: no customer import path or fallback presented as supported;
synthetic corpus success cannot change intake eligibility. This changes availability,
not the schema or acceptance predicates of future HT-01/02/08/09.

**R1 — operator-trusted appliance boundary, NOT recommended/adopted; P2/P3,
HT-02/08/09.** Current `b01c-producer-intake.md`, actor table, administrator row:
“Existing B01a actors remain in scope. Their mount/namespace actions must be constrained
or handled by a demonstrated mechanism; neither an operator promise nor a new UID
proves that. Excluding them would be an unaccepted threat-model delta.” Exact proposed
replacement, only if explicitly chosen: “For this appliance, the host OS/hypervisor,
host runner and storage administrators, and guest bootstrap/mount administrators are
trusted deployment operators throughout provisioning, capture, extraction and recovery.
HookTrace does not protect evidence against their malicious substitution, mutation,
rollback or disclosure. Other producer/reader processes and payloads remain untrusted;
safe origin, no retained unauthorized writers and fail-closed acquisition still require
demonstration.” Loss: obligation to constrain those privileged actors; a material trust change,
not enforcement. Revised oracle: adversarial non-operator writers must fail; privileged
tampering is an explicit exclusion, never a passed isolation test. Host ordinary
same-UID processes are not automatically trusted: runner/backing-file separation still
needs a demonstrated design. No new stream or customer-data handling is approved.

**R2 — platform/workflow qualification, NOT adopted; P1/P2/P3/P4,
HT-01/02/08/09.** Current `evidence-contract.md:116–117`: “The OS/runtime must provide
verified descriptor-relative/no-follow semantics: B01 must prove feasibility on the
supported Mac/runtime/filesystem, including parent/leaf swaps.” Exact proposed
replacement: “The host runner and its storage/bootstrap path, and the exact Linux
guest kernel/runtime/filesystem, must pass a separately reviewed acquisition policy.
Only jobs from a reviewed producer with demonstrated source-side safe acquisition and
an explicitly approved ingress interface are eligible; unsupported origin, transport,
handoff or extraction fails closed. Descriptor-relative/no-follow parent/leaf-swap
resistance remains mandatory.” Foregone proposed capability: direct Mac job selection; added
appliance/producer burden. Retained: file contract, exact raw bytes/provenance, unknowns,
causal limits, no imported execution and complete bounded publication. Revised oracle:
positive source→guest→result byte/ref preservation plus rejection before unsafe opens
for unknown origins, hostile paths/mounts, leaked FDs/mappings, truncated/oversized
transfers, output collisions and crash/restart. No wire grammar is implicitly adopted.

## Ranked next research questions for coordinator dispatch

1. **Is the evidence customers need actually retainable for this incident?** Needed:
   primary Stripe event/delivery retention/export documentation, instrumentation/export
   specifications and existing public first-party incident accounts. Deliverable: one
   source→field→retention→safe-origin matrix for subscription-access discrepancies,
   separating unavailable historical facts from merely absent instrumentation. Public
   accounts are signals, not interviews or validated demand; no customer artifacts.
2. **What distinct buyer problem remains after existing tools?** Needed: first-party
   Stripe dashboard/CLI and webhook-observability/replay product docs, public pricing
   and attributable user problem reports. Deliverable: cited task-level comparison
   of delivery debugging versus handler/state evidence and offline historical analysis,
   with H1–H4 demand/pricing hypotheses and disconfirming evidence. No invented market
   size, outreach or account creation; rank the niche rather than claim product fit.
3. **Which deterministic contract gates can be resolved without intake?** Needed:
   accepted B01/B01b, RFC8785 and primary schema/runtime/dependency license/release
   documents. Deliverable: ordered readiness ledger with independent canonical-hash/ID
   oracle needs, missing-event-ID disposition choices, exact build/license unknowns
   and smallest later synthetic-only task boundaries. No install/code/new probe;
   fixture coverage must not be reported as importer or deployment readiness.

## Delivery evidence and recommended founder choice (A5–A6)

Passed: `python3 scripts/check_repository.py`; `python3 -m unittest discover -s scripts -p 'test_*.py'` (**25**);
existing actionlint 1.7.12 with `-shellcheck= -pyflakes=`; full-base `git diff --check`;
inline Git/Python comparisons (55 headings, all protected bytes and historical branches).
Exact commands/head/base/CI/complete attribution are recorded in PR #17.
One retrieval attempt using Python urllib failed TLS certificate verification; curl
with normal verification read the same D2 document. No TLS bypass or portfolio reads.
Early PR attribution failed in CI **44679688055** after automatic Sourcery appended a
summary; preserved summary and restored final trailer, live checkpoint attribution 1/1
passed. No manual Sourcery request/label. Final automatic status is reported separately.
Not run: VM/guest/runtime/producer/importer/exporter, acquisition/store/host/corpus
probes, native/device/mount/permission, customer-data or isolation/durability tests.
No artifacts installed/downloaded or sources executed. Research is not intake
acceptance; runtime/build, schema/JCS, canonical hashes/IDs, missing-event-ID disposition,
publication/limits and isolation gates remain. A1–A4 are above; enforcement is unverified
or blocked. No full-chain path is established: **no validation issue is drafted or run**.

**Recommended founder choice: pause customer intake (R0).** Continue separately dispatched
research while ReleaseLens has build priority. The single reopening decision is explicit
acceptance of an **operator-trusted appliance scope** (R1, retaining R2's safe-origin/
transport gate). This exchanges protection from privileged operators for a narrower
boundary; it reopens planning, not ingress, customer use or implementation. If current
actor obligations remain, keep intake paused rather than fund another generic authority
study. Coordinator review precedes any scope decision.
