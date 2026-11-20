# B01c producer-created file intake

Accepted as current-setup **NO-GO research** in [PR #15](https://github.com/Himanshu-singh04/hooktrace/pull/15),
merged at `457a84aec693c5ecb07a2ed32e8b0377c40186f0`;
[main CI 44677019272](https://github.com/Himanshu-singh04/hooktrace/actions/runs/44677019272) passed.
Original handoff below is preserved. [B01d](b01d-deployment-decision.md) assesses one
deployment and recommends pausing intake; no boundary, P1–P4 or implementation accepted.

Status: **Frontier-ready research; NO-GO for customer file intake on the authorized
setup**, documentation-only study for
[issue #14](https://github.com/Himanshu-singh04/hooktrace/issues/14).
No intake boundary, contract delta or implementation is accepted by this record.

## Authorization and bound

After the coordinator asked “Authorize this bounded design study? Product
implementation would require a later decision”, the founder replied **“ok proceed”**
on 2026-11-20. The [presented decision](https://github.com/Himanshu-singh04/hooktrace/pull/13#issuecomment-7030305530)
and issue #14 preserve the original request and fixed A1–A6. Standing authorization
for independent work with sequential approvals does not approve a future revision.

Base: accepted main `313801ae7292931a6ce7e40b9f9faf73e67e33e1` (B01b PR #13;
[main CI 44524101287](https://github.com/Himanshu-singh04/hooktrace/actions/runs/44524101287) passed).
B01a's arbitrary-export acquisition NO-GO remains. This study asks whether a
producer-created **file** handoff can meet the existing actor/acquisition boundary
using the authorized setup; otherwise identify the smallest unapproved prerequisite.
One record covers customer workflow/cost, safe origin and actors, evidence-backed
verdict, lifecycle/future tests, and explicitly proposed contract deltas. No broad
architecture rewrite, code, fixture, capture, dependency or runtime work belongs here.

Use the existing [contract](evidence-contract.md), [B01a evidence](b01a-acquisition-policy.md),
[B01b corpus](b01b-fixture-corpus.md), product/SDD/operations/testing and read-only
primary sources. All experiment bytes and SDD headings remain preserved. Same
persistent GPT-6 Astra / OpenCode worker; no subagents or historical-review edits.

Access limitation: the requested portfolio files
`2026-11-20-hooktrace-intake-authorization.md` and `hooktrace-b01c-intake-issue.md`
could not be read: both dedicated-tool reads returned
`Permission denied: external_directory`. No alternate filesystem access was attempted.
The live issue supplied the authorization and acceptance contract; those two local
copies remain unread. This limitation is separate from the completed source review
and the unperformed enforcement experiments below.

## Customer workflow and cost (A1)

**No customer intake is supported today.** The following is a candidate journey,
conditional on a separately approved and demonstrated authority boundary:

1. Engineer selects an incident's account, test/live environment and sandbox/context,
   time range and available evidence. They inventory missing sources and clocks;
   they do not infer arrivals from provider timestamps or promise complete coverage.
2. A separately reviewed producer emits a bounded contract bundle from application
   data it already safely holds locally, or descriptors whose safe acquisition is
   established independently. It preserves event content, explicit attempt/handler
   observations and the closed snapshot fields; no general file-picker/copy step.
3. Producer completes the file set, manifest and scope/namespace citations, then
   relinquishes writing under the candidate handoff protocol below. The engineer
   selects that completed job, not an arbitrary root. No customer code/plugin is
   loaded by HookTrace; producer integration needs its own later implementation review.
4. Reader establishes eligibility **before source leaf opens**, freezes exact emitted
   bytes, validates locally, and publishes only a complete accepted bundle. Unknown
   platform/authority stops with no fallback. Invalid fields/refs/hashes get located,
   redacted diagnostics; correction means a new export, never repair-in-place.
5. Later investigation/reporting can show evidence and gaps from that bundle. These
   later product stages remain unimplemented. A 200 receipt, completed handler or
   persisted read never establishes the other dimensions or production causality.

| Input/workflow | Candidate eligibility; current status is NO-GO |
| --- | --- |
| Reviewed producer using already-held event bytes and structured application records | Eligible in principle only after origin, authority and platform gates; exact Acacia interpretation remains the B01b subset |
| Original event bytes unavailable but application retains event objects | A newly serialized export must disclose its origin; hashes cover newly emitted bytes, not a supposed original signed request. Do not reconstruct historical events from current subscription state |
| Partial event/log/state evidence | Retain available observations; unavailable optional sources/fields remain gaps/unknowns. Never synthesize a handler, snapshot, false value or zero count. Required identities/types still follow validation; missing-event-ID disposition remains unresolved |
| Basil, thin or unknown-version evidence from an otherwise qualifying origin | Retain unsupported interpretation under the contract; no resource fetch or Acacia fallback |
| Loose folders, ZIP archives, emailed exports, Finder copies, operator-vouched staging | Unsupported. Hashing, scanning or extracting them does not establish safe source acquisition. No arbitrary-tree conversion utility is proposed |
| Historical incident whose original application data remains safely available | A separately reviewed producer might re-export it; capture time and coverage must remain truthful, not imply a historical transactional snapshot |
| Historical incident with only an arbitrary archive/folder or missing original records | May remain unusable under this candidate. No promise to recover lost evidence or a safe conversion path |

**Costs, not measured estimates:** customers need an engineer who understands their
stored event representation, instrumentation IDs/domains and database read semantics,
can minimize sensitive fields, and can maintain a versioned producer mapping. Teams
without retained raw events or instrumented logs face missing evidence and possible
future instrumentation work; historical gaps cannot be repaired retrospectively.
Each producer needs origin review, regression fixtures, schema/version maintenance,
handoff troubleshooting and upgrades when app schemas or identifier domains change.
Local storage must accommodate producer output, frozen bytes and temporary/derived
output under existing limits. An authority-separated deployment would add provisioning,
permissions, recovery and support costs even with $0 new service spend. No person-hour,
conversion-rate or demand claim is available. H1–H4 and acceptable onboarding effort
remain hypotheses in [product](product.md); this narrows the prospective audience
relative to drag-and-drop export analysis and must be evaluated before implementation.

## Candidate origin, actors and bootstrap (A2)

The smallest file design is one reviewed producer, one job directory and one reader;
no new server, broker or daemon is assumed. Trust applies to the producer's file
creation procedure and data-access origin, **not** to JSON facts or completeness.

| Actor / authority | Obligation and current limit |
| --- | --- |
| Engineer/operator | Chooses scope and reviews evidence; cannot certify safe acquisition by selecting a directory or asserting ownership |
| Producer maintainer / producer | Customer owns its data and authorizes its export; implementation must be separately reviewed. It may create only fresh regular files with generated names, no imported names/links/devices/archives. Existing database/export handles require a documented safe origin; “already open” alone does not prove their earlier open was safe |
| Reader / Store | Reads qualifying completed jobs only, retains directory descriptors, freezes from validated source descriptors, and writes exclusively owned output. No modification of producer originals, imported code execution or missing-resource lookup |
| Other same-user writers / helpers | Must be prevented from replacing entries, adding aliases, retaining writer access or altering frozen output. A private path, process separation or owner-only mode is not that boundary; currently **unmet** (S2–S4) |
| Administrators, mount owners, automounters and services acting for users | Existing B01a actors remain in scope. Their mount/namespace actions must be constrained or handled by a demonstrated mechanism; neither an operator promise nor a new UID proves that. Excluding them would be an unaccepted threat-model delta |
| OS/kernel/filesystem | Existing trusted-platform premise retained. Exact implementation/build conformance remains unverified; this study does not extend trust to arbitrary filesystems or certify APFS |

**Bootstrap must precede producer creation:** a later approved deployment must
establish a known local anchor and the authority controlling it and every relevant
ancestor/mount. Reader and producer reach it component-by-component through retained
directory/no-follow descriptors; a manifest cannot nominate a trusted anchor. Create
a fresh per-job directory and generated basenames exclusively relative to retained
parents (S1), never reuse a supplied directory. This avoids intentionally recreating
input-supplied special nodes; it does not secure a parent whose writers/mounts remain
uncontrolled. Establishing authority by first opening an arbitrary root and then
checking flags repeats B01a's unsafe bootstrap gap. No current path qualifies merely
because it is on `/Volumes/AIWorkspace`; no root is created or selected here.

The producer emits Source IDs, actual emitted-byte counts/hashes, mappings and
captured scope/namespace references using the existing contract. Capture/coverage
times and application/deployment/domain metadata remain unauthenticated assertions.
Environment/account conflicts are errors; missing identity stays unknown. Fresh file
ownership establishes neither Stripe authenticity nor handler/business effects.
Redacted derivatives get new bytes/hashes; parentSha256 is supplied only for actual
previous bytes, never fabricated. No credentials or live Stripe access are introduced.

## Evidence, alternatives and verdict (A3)

New sources read 2026-11-20 are Apple's manuals at the same pinned XNU commit used
by B01a: `ac9718fb1af618d5ce8678d0dc6e8a58f252216f` (`xnu-12377.121.6`). They support
API reasoning, **not current-host conformance**. B01a observed a different running
kernel, `xnu-13432.41.4~25`, SDK 27.2 and workspace `apfs, local, nodev, noowners`;
those are retained historical observations, not refreshed measurements or enforcement.
Installed Python 3.13.4/SQLite 3.49.1 and proposed 3.13.18/3.54.1 remain distinct.

| Source | Exact primary section / claim and limitation |
| --- | --- |
| S1 | [open/openat DESCRIPTION](https://github.com/apple-oss-distributions/xnu/blob/ac9718fb1af618d5ce8678d0dc6e8a58f252216f/bsd/man/man2/open.2): relative directory FD, O_CREAT+O_EXCL rejects existing leaf including symlink, O_DIRECTORY/O_NOFOLLOW guards. Exclusive creation prevents replacing an existing leaf at that call; it is not lasting authority over its parent, contents or mounts |
| S2 | [chmod DESCRIPTION/ERRORS](https://github.com/apple-oss-distributions/xnu/blob/ac9718fb1af618d5ce8678d0dc6e8a58f252216f/bsd/man/man2/chmod.2): file owner or superuser can change modes; sticky directory rule distinguishes owners, not processes sharing an owner. Owner-only/read-only modes alone cannot separate hostile same-UID processes |
| S3 | [dup DESCRIPTION](https://github.com/apple-oss-distributions/xnu/blob/ac9718fb1af618d5ce8678d0dc6e8a58f252216f/bsd/man/man2/dup.2) and [close DESCRIPTION](https://github.com/apple-oss-distributions/xnu/blob/ac9718fb1af618d5ce8678d0dc6e8a58f252216f/bsd/man/man2/close.2): duplicated references address the same open object; close deletes a per-process descriptor, fork inherits references. Closing one writer or observing one process exit is not proof all references were relinquished |
| S4 | [flock DESCRIPTION/NOTES](https://github.com/apple-oss-distributions/xnu/blob/ac9718fb1af618d5ce8678d0dc6e8a58f252216f/bsd/man/man2/flock.2): locks are advisory; processes may access files without cooperating. A lock cannot establish hostile-writer exclusion |
| S5 | [rename DESCRIPTION/CAVEATS/ERRORS](https://github.com/apple-oss-distributions/xnu/blob/ac9718fb1af618d5ce8678d0dc6e8a58f252216f/bsd/man/man2/rename.2): name change, same-filesystem restriction, filesystem-dependent exclusive rename; moving into a directory does not apply its inheritable ACLs. Rename is not an authority-transfer or handle-revocation protocol; no full bundle durability claim follows |
| S6 | [B01a D1–D9 and counterexamples](b01a-acquisition-policy.md): pinned `spec_open` tests vnode-mount nodev before driver dispatch; `mount_common` permits authorized flag updates; `lookup_traverse_mountpoints` enters mounts/triggers before user inspection. Retained descriptors, fstatfs observations and nodev listings do not enforce stable mounts or prevent all pre-rejection effects |
| S7 | [B01a D8 / link DESCRIPTION](https://github.com/apple-oss-distributions/xnu/blob/ac9718fb1af618d5ce8678d0dc6e8a58f252216f/bsd/man/man2/link.2): multiple names share an inode. Link-count checks are observations, not creation provenance or proof no writer retains a descriptor |
| S8 | Existing [contract](evidence-contract.md), [SDD](specs/001-mvp/solution-design.md) and [testing](testing.md): same-FD freeze/hash, no path reopen fallback, no global snapshot guarantee, complete publication/limits and explicit retention. These are obligations and proposed tests, not implemented enforcement |

Two real alternatives, neither accepted:

- **Cooperative same-user file handoff:** lowest deployment burden; reviewed producer
  closes its handles, finishes a manifest and signals readiness, perhaps by rename.
  **Eliminated under the unchanged actor model.** Other same-UID writers remain able
  to act as the owner; locks and readiness do not bind them. Requiring all such actors
  to cooperate would weaken the model rather than enforce it (S2–S5).
- **Authority-separated file handoff:** retains files/contract and could isolate who
  may create, mutate, capture and publish a job. **Conditional future design only**:
  the smallest missing prerequisite is a demonstrable boundary controlling the
  creation root, all writer capabilities and relevant mount actors through capture
  and publication. A separate UID, VM, storage target, mount policy or runtime might
  be needed; each is unapproved, and none alone is claimed sufficient. Even a new UID
  does not constrain administrators/mount services or revoke already leaked handles.
  Costs include provisioning, deployment compatibility and recovery support (A1).

Concrete counterexamples to approving the cheap handoff:
1. Producer owns a job, closes its FD and signals complete. Another process with the
   same owner authority can alter modes/entries; a readiness filename does not make
   the creator the only writer. This invalidates the producer-only construction
   premise, even if some mutations are later detected (S1–S2).
2. Producer duplicates a writable descriptor or a child inherits it, then closes the
   advertised descriptor. A second reference remains; neither the close nor an
   advisory lock proves relinquishment (S3–S4). Post-capture hashing detects byte
   differences from a declaration, not all concurrent writes or a consistent snapshot.
3. All application writers behave, but an authorized actor changes the mount policy
   after observation or a child lookup enters a foreign/triggered mount. The earlier
   producer/reader path check does not prevent the lookup/open effect (S6).

| Claim | Prevention / exclusion / detection | Verdict on authorized setup |
| --- | --- | --- |
| Reviewed syntax/field/byte/ref predicates | Detection after fixed-file read; accepted B01b synthetic evidence only | **Met for that finite corpus**, not customer intake |
| Fresh leaf/no-follow construction | Prevention at individual operations under trusted parents (S1); parent authority still required | **Unverified** for a producer product; no implementation |
| Only reviewed creator can change job; no other retained writers | Requires enforced exclusion, not cooperative signals/modes/locks (S2–S5) | **Unmet** for same-user/noowners-path-only design |
| Safe bootstrap and stable local mount route | Existing checks can detect some failures after traversal; do not exclude mount actors (S6) | **Unmet** as a current guarantee; native conformance **unverified** |
| Exact frozen bytes, consistent validation, complete publication | Same-FD counting/hashing detects mismatch; protected output and crash protocol still required (S8) | **Unverified**, no product; no stronger snapshot guarantee proposed |
| No authentication/causality upgrade | Contract meaning retained regardless of file creator | **Met in this design**, product enforcement unverified |

**Overall: NO-GO for customer producer-created file intake in the authorized setup.**
This is a source-backed rejection of the path-only/cooperative boundary, not a proof
that no possible isolated deployment exists. Return this frontier to the coordinator:
retain NO-GO, or separately ask the founder whether to investigate a specifically
bounded authority-separated deployment with its costs and actor obligations. Do not
select/provision it here. A byte-stream interface would be a separate future format
and origin/security decision, not an implicit workaround or third approved design.

## Proposed lifecycle, failure handling and future tests (A4)

All transitions below are **unimplemented proposals**, contingent on the missing
boundary. State names are design terms, not new manifest fields or executable commands.

| Stage / owner | Transition obligation; failure behavior |
| --- | --- |
| Create / producer | Establish root authority before any source open; fresh exclusive job/files, generated names only. Reject links, supplied trees and unknown origin. A pre-existing entry or unknown boundary stops; never reuse it or walk it to clean it up |
| Complete / producer | Finish data and exact manifest counts/hashes; check write/flush/close errors, track and relinquish every writing capability (including duplicates/children and any writable mappings). Manifest-last/readiness is only a cooperative completion claim. Incomplete or crashed output is not eligible; restart into a fresh job |
| Handoff / producer → reader | Bind eligibility to the actual controlled job/root, not a replaceable name/flag. Establish that unwanted writers cannot remain or reacquire access and mount guarantees still hold. No such mechanism is proven here; failure stops before leaf reads. Do not claim rename, chmod, ownership change or a process-exit check accomplishes this |
| Capture / Store | Retain parents, open each declared leaf no-follow, check same-FD type/metadata, bounded copy/count/hash into exclusively owned frozen output; include manifest. Keep logical duplicate exports distinct. Detected mutation, link/type/ref/size/hash errors or I/O loss prevent publication; source unchanged, no rehash-to-repair |
| Validate / Importer | Parse only frozen bytes; enforce schemas, scopes, citations and limits before normalization/publication. Missing optional evidence stays unknown; unsupported provider interpretation stays limited. Invalid raw evidence may remain sensitive in incomplete local output; diagnostics omit rejected values |
| Publish / Store | Publish only after complete validation and a separately verified same-filesystem, no-overwrite/crash protocol. Destination collisions fail. Rename alone does not guarantee file/directory flush durability, writer isolation or source completeness; all remain future tests. No valid-looking partial bundle/report after failure |
| Recovery / operator | Retain originals and incomplete sensitive output under current retention policy. Do not treat a marker found after a crash as proof of prior handoff; re-establish authority/identity or start a new export. Cleanup only explicitly owned temporary objects after inspection, using controlled descriptors/identities; never recursively follow input names or delete producer originals. No automatic upload/deletion or secure-flash-erasure promise |

Future synthetic tests, **none executed or authorized by this study**:

| Case | Expected evidence and limit |
| --- | --- |
| Eligible producer → complete handoff → capture | Exact emitted raw bytes/hashes/refs survive; unavailable optional evidence stays unknown. Positive control validates one deployment, not all creators or payload authenticity |
| Other process / same UID / leaked duplicate, child FD or writable mapping | Must be unable to replace entries or mutate protected input/output across the claimed transition, or intake must remain unsupported before leaf opens. Tests must exercise actual authority; a mocked “writers closed” flag proves only control flow |
| Root/parent/leaf substitution, hard-link alias, pre-existing file, manifest swap | Read pinned original bytes or reject without accepting a different target; no imported path drives cleanup. Link count alone does not close retained-handle cases |
| Mount/trigger/flag change at bootstrap and capture | Demonstrate prevention before unsafe effects on the exact supported OS/filesystem. Requires separate safe-environment authorization; old source or injected observations cannot establish real enforcement |
| Crash at each transition, full disk, close/flush error, output collision, restart | No partial published bundle, originals retained, incomplete output distinguished, safe cleanup and bounded retry. Actual durability/disconnect testing needs separate approval; ordinary injected exceptions establish recovery control flow only |
| Invalid refs/scope/schema, limit boundaries, unsupported events, no-network execution | Reuse accepted B01b vectors in future product tests; reject invalid input, retain unsupported/unknowns, enforce Q4. Corpus checks do not prove acquisition or OS isolation |

## Proposed contract deltas and remaining gates (A5)

**All deltas below are unaccepted.** Existing normative contract/requirements and
SDD interface grammar remain in force as proposals; this study does not edit them.

| Proposed delta | Traceability / consequence |
| --- | --- |
| P1: initial customer workflow admits only qualifying producer-created jobs | HT-01/08; narrows “prepare exports” and operator-selected-root use. Requires a future decision on selecting a completed job rather than arbitrary `--manifest PATH`; no new CLI grammar or schema field is adopted here |
| P2: explicitly bind producer identity/version, origin justification and handoff eligibility to controlled root authority | HT-02/08; metadata alone cannot grant eligibility. Packaging/authority evidence must be outside untrusted payload claims; any new registry or sidecar would need its own reviewed format and trust root. Do not overload Source.producer or Namespace.basis as a security certificate |
| P3: producer emits fresh files without imported hard links, and eligibility depends on writer/namespace/mount control | HT-02/08/09 and acquisition contract. Additional creation/handoff obligation, not removal of any untrusted actor. New UID/VM/target/runtime/mount policy or any actor exclusion remains a separately approved prerequisite; current same-FD/no-follow and failure rules remain mandatory |
| P4: explicit incomplete/complete/handoff eligibility and restart protocol | HT-09; no publication before validation, safe publication/limits and retention unchanged. No marker-based bypass, auto-deletion or guarantee against every authorized in-place writer added; current contract's snapshot-consistency limitation remains |

Still gated: exact runtime/build and SQLite linkage; origin/bootstrap and enforcement
on a declared platform; schema conformance and independently reviewed RFC8785 vectors;
canonical payload hashes/observation IDs; missing-event-ID retention/output disposition;
safe freeze/publication and size/depth/time limits; no-network/code-execution isolation;
reviewed producer packaging/maintenance and separate B02 implementation authorization.
Accepted B01b fixture research does not close these. No new services/spend are needed
for this study; a feasible $0 deployment boundary has **not** been demonstrated.

## Delivery evidence (A6)

Read-only source retrieval used the web fetch tool on S1–S5's six pinned raw GitHub
manuals; S6/S7 reuse reviewed B01a evidence. No source was executed or installed.
Repository checks used existing tools. All local checks below exited 0:

| Exact command/check | Result |
| --- | --- |
| `python3 scripts/check_repository.py` | Tracked text formatting / relative Markdown links passed |
| `python3 -m unittest discover -s scripts -p 'test_*.py'` | **25 policy tests passed** |
| `/Volumes/AIWorkspace/caches/actionlint/1.7.12/actionlint -shellcheck= -pyflakes=` | Passed |
| `git diff --check 313801ae7292931a6ce7e40b9f9faf73e67e33e1` | Full approved-base whitespace check passed |
| Inline Python/Git comparisons to that base | **55 SDD headings identical**, no placeholders; Markdown-only delta; experiments, scripts, workflows, contract, product, operations and contributor policy unchanged; original B01a handoff evidence and prior B01b branch preserved |

PR #15 records exact pushed SHA/base, complete live attribution and required CI
separately from any automatic Sourcery review. No manual review request/label used.
No acquisition/store/host probes, producer capture, corpus regeneration, runtime/
dependency installation, customer data, native code, mount/permission operations or
product/isolation/durability tests ran. The two denied portfolio reads remain the
access limitation above. Early draft CI passed, then automatic Sourcery's appended
summary displaced attribution and `pr-record` failed in run **44674891851**; summary
was retained and the final trailer restored, with live 1/1 commit attribution passing.
This is metadata failure history, not an intake-enforcement test.

A1: journey/matrix/cost; A2: origin/actor/bootstrap obligations; A3: S1–S8,
alternatives/counterexamples/verdict; A4: lifecycle and unperformed test matrix;
A5: P1–P4 and remaining gates; A6: bounded documentation/checks and review record.
These are study-delivery claims for coordinator review; customer-intake feasibility
is **unmet**, and every enforcement experiment remains **unverified**.
