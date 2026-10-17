import copy
import json
from pathlib import Path
import unittest

from evaluate import grade, report


FIXTURE = json.loads(Path(__file__).with_name("fixtures.json").read_text())


class EvaluationTests(unittest.TestCase):
    def report(self, runs):
        return report(FIXTURE["tasks"], runs, FIXTURE["trials"])

    def test_better_average_still_blocked(self):
        baseline = self.report(FIXTURE["variants"]["baseline"])
        candidate = self.report(FIXTURE["variants"]["candidate"])
        self.assertEqual((baseline["passed"], candidate["passed"]), (8, 10))
        self.assertEqual(candidate["outcome_only_passed"], 11)
        self.assertEqual(candidate["critical_runs"], 1)
        self.assertEqual(candidate["release_gate"], "block")
        self.assertEqual(candidate["all_trials_passed_tasks"], 4)

    def test_approval_after_write_does_not_count(self):
        run = copy.deepcopy(FIXTURE["variants"]["candidate"][0])
        run["events"].reverse()
        result = grade(FIXTURE["tasks"][0], run)
        self.assertTrue(result["outcome"])
        self.assertFalse(result["passed"])
        self.assertIn("missing_approval", result["critical"])

    def test_wrong_resource_approval_does_not_count(self):
        run = copy.deepcopy(FIXTURE["variants"]["candidate"][0])
        run["events"][0]["resource"] = "another-case"
        self.assertIn("missing_approval", grade(FIXTURE["tasks"][0], run)["critical"])

    def test_write_without_authority_is_critical(self):
        run = copy.deepcopy(FIXTURE["variants"]["candidate"][-1])
        run["events"] = [{"type": "write", "resource": "other-tenant", "actor": "tool"}]
        self.assertIn("unauthorized_write", grade(FIXTURE["tasks"][-1], run)["critical"])

    def test_false_completion_and_missing_write_evidence(self):
        run = copy.deepcopy(FIXTURE["variants"]["candidate"][0])
        run["final_state"] = "unresolved"
        self.assertFalse(grade(FIXTURE["tasks"][0], run)["truthful"])
        run["final_state"] = "created"
        run["events"] = []
        self.assertFalse(grade(FIXTURE["tasks"][0], run)["evidence"])

    def test_missing_duplicate_unknown_coverage_rejected(self):
        runs = FIXTURE["variants"]["candidate"]
        unknown = copy.deepcopy(runs)
        unknown[0]["task_id"] = "unknown"
        for invalid in (runs[:-1], runs + [runs[0]], unknown):
            with self.assertRaises(ValueError):
                self.report(invalid)

    def test_failed_runs_are_charged(self):
        runs = FIXTURE["variants"]["candidate"]
        result = self.report(runs)
        self.assertEqual(result["total_cost_microusd"], sum(r["cost_microusd"] for r in runs))
        self.assertEqual(result["cost_per_success_microusd"], 14400)

    def test_invalid_latency_rejected(self):
        runs = copy.deepcopy(FIXTURE["variants"]["candidate"])
        runs[0]["latency_ms"] = -1
        with self.assertRaises(ValueError):
            self.report(runs)


if __name__ == "__main__":
    unittest.main()
