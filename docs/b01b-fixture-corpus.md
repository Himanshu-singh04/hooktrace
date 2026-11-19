# B01b narrow synthetic fixture corpus

Status: in progress for [issue #12](https://github.com/Himanshu-singh04/hooktrace/issues/12).
Original founder instruction: “ok proceed with the further tasks”, following
authorization for independent rolling work with sequential exact-revision approvals.
The issue preserves the full refined scope and A1–A6 acceptance criteria.

Base is approved main `97f1669ddd92a510f7d637429b1c21f53713ae40`, not pending B01a.
PR #9 accepted conditional Acacia/SQLite research after the R7 correction and later
founder approval; see [merge verification](https://github.com/Himanshu-singh04/hooktrace/pull/9#issuecomment-7002315562).
This does not approve a runtime build, arbitrary-export acquisition or product B02.
B01a branch/PR #11 is preserved and independent; this task changes only new B01b files.

## Scope and oracle boundary

One [positive bundle](../experiments/b01b/) contains two event exports (updated and
deleted), one attempt, one handler observation and one state snapshot, plus scope
and namespace metadata. A manifest, independent expected facts and finite targeted
variants accompany the raw files. The created event and customer-shape alternatives
are variants, not extra positive bundles. Inputs are original, synthetic and partial;
they are not complete Stripe responses or provider-certified fixtures.

All semantics follow the existing [contract](evidence-contract.md), B01 support
matrix, and T01/T02/T08/T09 in [testing](testing.md). No importer, normalized output,
correlation, canonical serializer, freeze/publication layer or handler is delivered.
The small stdlib harness will read only explicitly listed repository fixtures;
mutations and forbidden-path strings stay in memory. Golden normalized IDs/JCS
payload hashes remain pending an independent canonicalization oracle.

## Primary field provenance

Read 2026-11-19; documentation/declarations are evidence, not instructions to execute.
No Stripe SDK, API, CLI, account, keys, copied exports or installed dependency used.

- **P1:** [v17.7.0 apiVersion](https://github.com/stripe/stripe-node/blob/v17.7.0/src/apiVersion.ts)
  binds the tagged declarations to exact `2025-02-24.acacia`.
- **P2:** [v17.7.0 EventBase/Request](https://github.com/stripe/stripe-node/blob/v17.7.0/types/Events.d.ts)
  defines event ID/type, optional connected account, nullable API version, Unix-seconds
  created, livemode, nullable originating request and nullable request ID/idempotency key.
- **P3:** [v17.7.0 EventTypes](https://github.com/stripe/stripe-node/blob/v17.7.0/types/EventTypes.d.ts)
  `CustomerSubscriptionCreatedEvent` (1131), `DeletedEvent` (1147), `UpdatedEvent`
  (1243) each binds `data.object` to Subscription. Deletion is a subscription end,
  not an instruction to infer a local tombstone or access change.
- **P4:** [v17.7.0 Subscription](https://github.com/stripe/stripe-node/blob/v17.7.0/types/Subscriptions.d.ts)
  has subscription-level period fields and `customer: string | Customer | DeletedCustomer`.
  [Customer/DeletedCustomer](https://github.com/stripe/stripe-node/blob/v17.7.0/types/Customers.d.ts)
  gives IDs/object tags and `deleted: true`. These are admissible type shapes, not a
  claim every event expansion or deleted-customer combination is emitted in practice.
- **P5:** [v18.0.0 apiVersion](https://github.com/stripe/stripe-node/blob/v18.0.0/src/apiVersion.ts)
  binds `2025-03-31.basil`; [SubscriptionItem](https://github.com/stripe/stripe-node/blob/v18.0.0/types/SubscriptionItems.d.ts)
  places billing periods on items. Retain this version as unsupported, with no Acacia fallback.
- **P6:** [v18.0.0 ThinEvent](https://github.com/stripe/stripe-node/blob/v18.0.0/types/ThinEvent.d.ts)
  and [V2.EventBase](https://github.com/stripe/stripe-node/blob/v18.0.0/types/V2/Events.d.ts)
  define `object=v2.core.event`, string created and related-object reference. The
  [event-format documentation](https://docs.stripe.com/event-destinations) describes
  unversioned notifications, not Acacia subscription snapshots. Thin input remains
  unsupported; related URLs are inert and never fetched. Unknown versions are
  deliberately invented negative labels, not invented provider releases.

Provider declarations are Stripe/Ask Bjørn Hansen MIT-licensed source; only links,
field names and original synthetic values are used. Website docs are cited, not
relicensed as MIT. Hand-reviewed expectations are worker research proposals until
the coordinator independently audits them; no normalizer generates its own goldens.
