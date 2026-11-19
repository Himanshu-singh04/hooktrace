# B01 runtime, contract and store decision frontier

Status: research in progress for [issue #8](https://github.com/Himanshu-singh04/hooktrace/issues/8).
Owner confirmation of ADR-1–4 remains pending; this is not an accepted ADR or product.

## Assignment and bounds

Original founder instruction: “ok proceed”, responding to the first bounded decision
tasks including runtime and payload/storage choices for HookTrace. The full refined
assignment and A1–A6 acceptance criteria are preserved in issue #8.

Bound: compare Node/TypeScript with a simpler runtime; exercise descriptor-relative
no-follow acquisition and transactional synthetic storage on this Mac/pendrive;
review two version-grounded Stripe snapshot samples; return exact proposed pins,
tradeoffs, limitations and B02 prerequisites. No importer, product CLI, packaged
handler, live Stripe integration or optional AI implementation belongs in this spike.

Planning/rename PR #5 and provisioning issue #7 are complete. Handoff main was
`87f64dd1fd0840c4567e5476d89c8ca31ff7bc93`; fetched main matched it at research start.
Worker history/OAuth is on pendrive; coordinator history/App key remains on Mac,
per [coordinator verification](https://github.com/Himanshu-singh04/hooktrace/issues/7#issuecomment-6999734294).
Worker inference is development assistance, not product-local AI.

## Evidence to complete

- A1: exact runtime/toolchain/schema/canonicalization comparison and primary sources.
- A2: positive, ancestor/leaf substitution, identity and cleanup acquisition assertions.
- A3: versioned schema evidence, synthetic samples, explicit support boundary.
- A4: atomic state/tombstone/dedup, injected rollback, duplicate/reset/reopen assertions.
- A5: proposed/blocked ADR mapping, reruns and remaining B02 gates.
- A6: local checks, issue-linked PR, checkpoint and CI evidence.
