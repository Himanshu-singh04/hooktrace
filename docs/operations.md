# Local execution and operations proposal

Status: repository foundation plus proposed product documentation. No application,
package release, dedicated project worker, server, model endpoint, or customer pilot
has been provisioned. This task authorizes documentation, not deployment.

## What lives where

| Resource | Current reality | Proposed next step / limitation |
| --- | --- | --- |
| Source and these docs | `/Volumes/AIWorkspace/projects/hooktrace` on pendrive | Keep project artifacts here; disconnecting it interrupts file access |
| Execution | Mac CPU/RAM; observed 16 GiB RAM, 8 logical CPUs | Storage placement does not move computation; no GPU/model speed claim |
| Current OpenCode history | `/Users/himanshusingh/.local/share/opencode/opencode.db` on Mac | Changing checkout directory does not relocate history |
| Credentials | Mac, outside Git; portfolio App helper described in development | Never copy secrets into project/evidence/model directories |
| Models and caches | Directories exist; runtime redirection has not been configured or verified | Creating pendrive directories alone does not move caches/weights |
| Dedicated workers/server | Not provisioned; temporary specialists assist coordinator | Session/database routing, startup, and recovery need a separate task |
| GitHub | Remote source/history/PR/CI copies after authorized push | Local unpushed edits are not remotely backed up; evidence stays outside Git |

Pendrive capacity/free space, filesystem durability, and model performance are not
established by the RAM/CPU observations. No new initial founder spend is permitted.
Development can use existing local/customer-owned resources; CI may download pinned
tools, but product checks must require no paid hosting or inference API.

## Startup today and proposed product startup

Today: open the pendrive checkout and use only [CONTRIBUTING](../CONTRIBUTING.md)
commands for repository verification. There is no product install/start/replay command.
The proposed CLI grammar in the [design](specs/001-mvp/solution-design.md) is a future
interface, not an instruction that works now. No Stripe CLI/login/listener is needed.

After B01/B06: install the pinned runtime and reviewed package using documented exact
versions, verify artifact checksum, then run the bundled synthetic demo offline.
Choose an operator-owned evidence directory outside the checkout (proposed pendrive
root `/Volumes/AIWorkspace/hooktrace-evidence/`, not created by this task).
Check mounted volume, free space for raw + derived + temporary copies, and write
permissions before import. Use a fresh output directory for each run; review source
scope/coverage and hash validation before reading findings. Run fixture variants only
against the bundled resettable store, then inspect persisted read-back assertions.

Proposed future subcommand examples (not runnable today):
`reproduce --fixture subscription-ordering-v1 --variant buggy --permutation D,U --seed 0 --out DIR1`
and `reproduce --fixture subscription-ordering-v1 --variant fixed --permutation D,U --seed 0 --out DIR2`.
Omitting permutation/seed resolves to `D,U` and `0`; record those resolved values and
package/fixture hashes for repeat runs. The proposed input limit is 2–8 U/D tokens,
both present, repeats allowed; seed is decimal 0–4294967295. This fixture does not use
randomness. Unsupported fixtures, tokens, seeds, options, and arbitrary input paths/
payloads are rejected. Only `--out` chooses a write location; it cannot select a handler.

## Data lifecycle and safety boundaries

Collect → freeze exact bytes/hash provenance → validate → normalize → analyze →
render → operator-reviewed sharing → explicit operator deletion. The
[contract](evidence-contract.md) defines each record and immutable relationship.
Imported event data never becomes code or a remote replay request. No live Stripe
lookup fills a gap. Do not put credentials or raw customer evidence into Git, issues,
PRs, chat prompts, or model corpora. Reports can contain sensitive identifiers too.
Use a separately redacted derivative for sharing; recompute hashes and retain truthful
provenance. Redaction and hashing do not certify anonymity or authenticity.

Raw originals and reports use local OS access controls; no built-in encryption or
secure-erasure guarantee is proposed. Operator chooses retention/backups; default is
no automatic upload or deletion. Future packaging should create owner-only files where
supported and document volume-permission limitations. Do not claim encryption at rest
unless an actual configured storage mechanism has been verified.

## Failure and recovery

- Invalid import: fix a new input manifest/export, preserve original bytes, rerun into
  a new directory. Unsupported schemas fail; unsupported provider fields stay limited.
- Hash mismatch: stop analysis; compare source provenance with the operator. Never
  “repair” hashes in place to make an altered bundle look original.
- Disk full, unplug, permission failure, or crash: preserve original input, inspect
  incomplete temporary output, remount/check storage, rerun to a fresh directory.
  Only explicitly owned incomplete output may be removed after inspection.
- Corrupt derived report: verify frozen hashes and regenerate with the same versions.
  Corrupt raw evidence requires a trustworthy backup/new export; inference cannot repair it.
- Fixture failure: retain run hashes/assertions, reset a fresh synthetic store, repeat
  exact permutation. A failed buggy assertion can be expected demonstration output.
- Package regression: select a prior reviewed artifact; do not downgrade schema in place.
- Lost pendrive: GitHub restores pushed source only. Local evidence and unpushed files
  need operator backups; Mac session history is separate, not a project backup.

## Packaging, AI, and future isolation gates

Proposed first release: versioned local CLI package and synthetic fixtures, checksum,
source SHA, runtime/OS support matrix, dependency/license list, and offline runbook.
Build/package tooling and registry publishing remain owner-approved later work.
No daemon, hosted API, public endpoint, deployment secret, or autoscaling plan is needed.

RAG is later optional local retrieval over reviewed source docs/evidence with cited
explanations and hypotheses. Deterministic findings remain authority; a model cannot
change source records or turn unknown into observed. No model is selected, downloaded,
benchmarked, or promised to fit the observed hardware. Evaluate license, memory,
quality, and budget first; default workflow remains usable with AI disabled.

Future trusted local handler adapters require a separate threat model and tested
OS/container-level network denial, filesystem allowlists, stripped environment,
timeouts/resource quotas, and explicit code trust. A child process alone supplies
none of those boundaries. Do not advertise “networkless sandbox” before enforcement
tests pass, and never let an imported bundle choose executable code or remote targets.
Product model tooling and project development worker provisioning are separate tasks.

## Release ownership

Use [development and delivery](development.md) for exact-revision review/approval,
authentication, attribution, and recovery. Temporary documentation specialists are not
persistent project owners and cannot approve their own work. B06/B07 must record
actual startup/recovery/packaging checks before any alpha is described as runnable.
