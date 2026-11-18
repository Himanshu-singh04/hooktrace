# HookTrace

**Follow events to business outcomes.**

Local-first investigation of webhook delivery, handler execution, and business-state discrepancies.

## Initial goal

Correlate exported subscription events, logs, and state snapshots, then reproduce a suspected failure in a resettable local fixture. Distinguish successful delivery from verified business effects and preserve uncertainty where evidence is missing.

## Status

Repository foundation exists; the product plan below is a draft for owner review under [issue #4](https://github.com/Himanshu-singh04/hooktrace/issues/4). The proposed MVP investigates exported Stripe subscription evidence offline and reproduces an ordering bug in a bundled synthetic handler. Architecture decisions remain pending; no product runtime, release, or dedicated project worker/server exists. Current commands are only the checks in [CONTRIBUTING](CONTRIBUTING.md).

## Product documentation

- [Product and requirements](docs/product.md): users, hypotheses, workflows, scope, requirement IDs.
- [Solution design](docs/specs/001-mvp/solution-design.md): proposed modular CLI, interfaces, pending ADRs.
- [Evidence contract](docs/evidence-contract.md): versioned records, provenance, uncertainty, ordering, reports.
- [Roadmap](docs/roadmap.md): dependencies, bounded tasks, pilot and release gates.
- [Testing](docs/testing.md): synthetic scenarios, missing-evidence cases, proposed targets and later AI evaluation.
- [Operations](docs/operations.md): storage reality, offline execution, recovery, packaging and provisioning gates.

Delivery success is not proof of handler execution or persisted business effect. A local modeled reproduction is not proof of production incident cause. Imports never execute code, contact live Stripe, or replay exported customer events to remote endpoints.

## Development workspace

Local checkout: `/Volumes/AIWorkspace/projects/hooktrace`.

Execution will use existing local or customer-owned resources, with no new initial founder hosting or inference expenditure. This product has an independent repository and release lifecycle.

Source/docs are on the pendrive; computation uses Mac CPU/RAM. Current session history and credentials remain on the Mac. Model/cache redirection and dedicated worker storage are not configured; see [operations](docs/operations.md).

## Git workflow

See [contributing](CONTRIBUTING.md), [development and delivery](docs/development.md),
and the [foundation record](docs/foundation.md) for checks, authenticated review,
agent attribution, and evidence requirements.

- Commit source, documentation, reviewed fixtures, and dependency lockfiles.
- Keep credentials, OpenCode databases, model weights, caches, and raw customer evidence outside Git.
- Complete a bounded task, run its relevant checks, inspect the diff, then commit and push the intended files.
- Report the commit and push result to the coordinator. A local commit is not a remote backup until the push succeeds.
- Use task branches for substantive implementation work and preserve unrelated changes.

These plans are review proposals. Product implementation and measured acceptance evidence follow approved, bounded tasks.
