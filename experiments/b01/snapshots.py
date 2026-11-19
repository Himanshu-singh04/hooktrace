"""Assert hand-authored sample differences, not Stripe compatibility or an adapter."""
import json
from pathlib import Path
import unittest


class Samples(unittest.TestCase):
    def test_version_specific_period_location(self):
        for name, version, on_subscription in (
            ("acacia", "2025-02-24.acacia", True),
            ("basil", "2025-03-31.basil", False),
        ):
            with self.subTest(version=version):
                event = json.loads(Path(__file__).with_name(f"{name}.snapshot.json").read_text())
                self.assertEqual(event["api_version"], version)
                self.assertEqual(event["type"], "customer.subscription.updated")
                self.assertIs(event["livemode"], False)
                sub = event["data"]["object"]
                self.assertEqual(sub["object"], "subscription")
                item = sub["items"]["data"][0]
                for field in ("current_period_start", "current_period_end"):
                    self.assertEqual(field in sub, on_subscription)
                    self.assertEqual(field in item, not on_subscription)
                    self.assertIs(type((sub if on_subscription else item)[field]), int)
                period = sub if on_subscription else item
                self.assertLess(period["current_period_start"], period["current_period_end"])
                # Provider snapshots supply no local persisted-access observation.
                self.assertNotIn("access", sub)
                self.assertNotIn("cancellationTombstone", sub)


if __name__ == "__main__":
    unittest.main(verbosity=2)
