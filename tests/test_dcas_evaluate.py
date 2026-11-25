import copy
import json
import sys
import unittest
from pathlib import Path
from jsonschema import ValidationError

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from dcas_evaluate import evaluate


def base_input():
    return {"contract_version": "0.2", "evaluation_id": "test",
        "target": {"baseline": "ANAB", "version": "0.10.0", "profile": "Enterprise"},
        "claim": {"requirements": ["R1"], "requirement_evidence": {"R1": ["binding"]}},
        "evidence": [{"id": "binding", "uri": "urn:test:binding", "status": "available"}],
        "policy": {"missing_evidence": "INDETERMINATE"},
        "evaluation_time": "2026-09-03T06:00:00Z"}


class DCASEvaluatorTests(unittest.TestCase):
    def test_pass(self):
        self.assertEqual(evaluate(base_input())["decision"], "PASS")

    def test_states(self):
        for state, expected in (("stale", "FAIL"), ("revoked", "FAIL"), ("contradicted", "FAIL"),
                                ("missing", "INDETERMINATE"), ("unverifiable", "INDETERMINATE")):
            with self.subTest(state=state):
                doc = base_input()
                doc["evidence"][0]["status"] = state
                self.assertEqual(evaluate(doc)["decision"], expected)

    def test_empty_evidence(self):
        doc = base_input()
        doc["evidence"] = []
        self.assertEqual(evaluate(doc)["decision"], "INDETERMINATE")

    def test_unbound(self):
        doc = base_input()
        doc["claim"]["requirement_evidence"] = {}
        self.assertEqual(evaluate(doc)["decision"], "INDETERMINATE")

    def test_distinct_findings(self):
        doc = base_input()
        doc["claim"]["requirements"].append("R2")
        doc["claim"]["requirement_evidence"]["R2"] = ["missing"]
        result = evaluate(doc)
        self.assertEqual(result["decision"], "INDETERMINATE")
        self.assertEqual([f["result"] for f in result["findings"]], ["PASS", "INDETERMINATE"])

    def test_contradiction_dominates(self):
        doc = base_input()
        doc["claim"]["requirement_evidence"]["R1"] += ["bad", "missing"]
        doc["evidence"].append({"id": "bad", "uri": "urn:bad", "status": "contradicted"})
        self.assertEqual(evaluate(doc)["decision"], "FAIL")

    def test_duplicates(self):
        doc = base_input()
        doc["evidence"].append(copy.deepcopy(doc["evidence"][0]))
        with self.assertRaises(ValueError):
            evaluate(doc)

    def test_policy_cannot_force_pass(self):
        doc = base_input()
        doc["policy"]["revoked_evidence"] = "PASS"
        with self.assertRaises(ValidationError):
            evaluate(doc)

    def test_separate_authority(self):
        doc = base_input()
        doc["claim"]["requires_action_authority"] = True
        self.assertEqual(evaluate(doc)["decision"], "INDETERMINATE")
        doc["evidence"].append({"id": "action-authority", "uri": "urn:authority", "status": "available"})
        self.assertEqual(evaluate(doc)["decision"], "INDETERMINATE")  # unbound
        doc["claim"]["requirement_evidence"]["R1"].append("action-authority")
        self.assertEqual(evaluate(doc)["decision"], "PASS")

    def test_legacy_anab_requires_reassessment(self):
        doc = json.loads((ROOT / "conformance/examples/anab_dcas_evaluation_input.example.json").read_text())
        self.assertEqual(evaluate(doc)["decision"], "INDETERMINATE")
        doc["evidence"] = []
        self.assertEqual(evaluate(doc)["decision"], "INDETERMINATE")

    def test_version_and_time_validation(self):
        doc = base_input()
        doc["evaluation_time"] = "invalid"
        with self.assertRaises(ValidationError):
            evaluate(doc)
        doc["contract_version"] = "9"
        with self.assertRaises(ValueError):
            evaluate(doc)


if __name__ == "__main__":
    unittest.main()
