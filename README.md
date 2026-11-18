# HookTrace

**Follow events to business outcomes.**

Local-first investigation of webhook delivery, handler execution, and business-state discrepancies.

## Initial goal

Correlate exported subscription events, logs, and state snapshots, then reproduce a suspected failure in a resettable local fixture. Distinguish successful delivery from verified business effects and preserve uncertainty where evidence is missing.

## Status

Repository initialized. Product design, implementation, and the dedicated OpenCode project session are pending. Stripe subscription workflows are the proposed initial scope. No application or test commands exist yet.

## Development workspace

Local checkout: `/Volumes/AIWorkspace/projects/hooktrace`.

Execution will use existing local or customer-owned resources, with no new initial founder hosting or inference expenditure. This product has an independent repository and release lifecycle.

## Git workflow

- Commit source, documentation, reviewed fixtures, and dependency lockfiles.
- Keep credentials, OpenCode databases, model weights, caches, and raw customer evidence outside Git.
- Complete a bounded task, run its relevant checks, inspect the diff, then commit and push the intended files.
- Report the commit and push result to the coordinator. A local commit is not a remote backup until the push succeeds.
- Use task branches for substantive implementation work and preserve unrelated changes.

Detailed plans and project-specific working instructions will follow during project planning.
