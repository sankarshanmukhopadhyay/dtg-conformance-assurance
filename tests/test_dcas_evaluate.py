import importlib.util
import unittest
from pathlib import Path

MODULE = Path(__file__).resolve().parents[1] / "tools" / "dcas_evaluate.py"
spec = importlib.util.spec_from_file_location("dcas_evaluate", MODULE)
dcas = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(dcas)


def base_input():
    return {
        "contract_version": "0.1",
        "evaluation_id": "test",
        "target": {"baseline": "ANAB", "version": "0.10.0", "profile": "Enterprise"},
        "claim": {"fixture_id": "ANAB-FX-001", "requirements": ["ANAGB-RES-01"]},
        "evidence": [{"id": "binding", "uri": "urn:test:binding", "status": "available"}],
        "policy": {"missing_evidence": "INDETERMINATE"},
        "evaluation_time": "2026-09-03T06:00:00Z",
    }


class DCASEvaluatorTests(unittest.TestCase):
    def test_available_evidence_passes(self):
        self.assertEqual(dcas.evaluate(base_input())["decision"], "PASS")

    def test_stale_evidence_fails(self):
        document = base_input()
        document["evidence"][0]["status"] = "stale"
        self.assertEqual(dcas.evaluate(document)["decision"], "FAIL")

    def test_missing_evidence_is_indeterminate(self):
        document = base_input()
        document["evidence"][0]["status"] = "missing"
        self.assertEqual(dcas.evaluate(document)["decision"], "INDETERMINATE")

    def test_identity_does_not_create_action_authority(self):
        document = base_input()
        document["claim"]["requires_action_authority"] = True
        document["claim"]["requirements"] = ["ANAGB-AI-06"]
        document["evidence"] = [
            {"id": "identity-binding", "uri": "urn:test:identity", "status": "available"},
            {"id": "action-authority", "uri": "urn:test:authority", "status": "missing"},
        ]
        self.assertEqual(dcas.evaluate(document)["decision"], "INDETERMINATE")


if __name__ == "__main__":
    unittest.main()
