import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "conformance/examples/tt_conformance"))
from dcas_evaluate import evaluate
from import_tt_conformance import normalize
from generate_fixture import generate, write


class ImportTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name)
        self.run, self.results, self.manifest = generate(self.path)

    def imported(self, update=True):
        if update:
            self.manifest["source"]["run_sha256"] = write(self.path / "run.json", self.run)
            self.manifest["source"]["results_sha256"] = write(self.path / "results.json", self.results)
            write(self.path / "manifest.json", self.manifest)
        return normalize(self.path / "run.json", self.path / "results.json", self.path / "manifest.json")

    def decision(self):
        return evaluate(self.imported())["decision"]

    def test_deterministic_pass(self):
        self.assertEqual(self.imported(), self.imported())
        self.assertEqual(self.decision(), "PASS")

    def test_outcomes(self):
        for status in ("PASS", "FAIL", "KNOWN-FAIL", "SKIP", "CLARIFY", "QUARANTINED", "SPEC-CHANGED", "SKIPPED-SAFETY"):
            with self.subTest(status=status):
                self.results[0]["results"][1]["status"] = status
                doc = self.imported()
                expected = "PASS" if status == "PASS" else "FAIL" if status in {"FAIL", "KNOWN-FAIL"} else "INDETERMINATE"
                self.assertEqual(evaluate(doc)["decision"], expected)
                self.assertIn(status, [x["source_result"]["status"] for x in doc["claim"]["source_context"]["mapped_results"].values()])

    def test_missing_positive(self):
        self.results[0]["results"].pop(0)
        self.assertEqual(self.decision(), "INDETERMINATE")

    def test_preserve_exclusion(self):
        self.results[0]["results"].pop(0)
        self.results[0]["excludedByTier"] = [{"id": "positive", "reason": "only runs at tier 2", "channel": "registry"}]
        doc = self.imported()
        self.assertEqual(evaluate(doc)["decision"], "INDETERMINATE")
        detail = next(x for x in doc["claim"]["source_context"]["mapped_results"].values() if x["vector"] == "positive")
        self.assertEqual(detail["exclusions"][0]["kind"], "excludedByTier")
        self.assertEqual(detail["exclusions"][0]["reason"], "only runs at tier 2")

    def test_reported_and_excluded(self):
        self.results[0]["retired"] = {"positive": "retired vector"}
        with self.assertRaises(ValueError):
            self.imported()

    def test_nonvacuity(self):
        del self.results[0]["results"][0]["anchor"]
        self.assertEqual(self.decision(), "INDETERMINATE")

    def test_drift(self):
        self.results[0]["drift"] = [{"kind": "spec-drift", "reason": "changed", "vectors": ["positive"]}]
        self.assertEqual(self.decision(), "INDETERMINATE")

    def test_stale(self):
        self.manifest["evaluation_time"] = self.manifest["valid_until"]
        self.assertEqual(self.decision(), "INDETERMINATE")

    def test_invalid_assessor_date(self):
        from jsonschema import ValidationError
        self.manifest["evaluation_time"] = "2026-11-25"
        with self.assertRaises(ValidationError):
            self.imported()

    def test_tamper(self):
        (self.path / "results.json").write_text("[]")
        with self.assertRaises(ValueError):
            self.imported(False)

    def test_duplicate_rows(self):
        self.results[0]["results"].append(copy.deepcopy(self.results[0]["results"][0]))
        with self.assertRaises(ValueError):
            self.imported()

    def test_unreviewed_suite(self):
        self.run["suite"]["dirty"] = True
        with self.assertRaises(ValueError):
            self.imported()

    def test_advisory_and_gate_only(self):
        row = self.results[0]["results"][0]
        row["channel"] = "pr"
        self.results[0]["channels"].append("pr")
        self.assertEqual(self.decision(), "INDETERMINATE")
        row["channel"] = "registry"
        row["acceptedOnlyGate"] = True
        self.assertEqual(self.decision(), "INDETERMINATE")

    def test_candidate_channel(self):
        self.results[0]["channels"].append("candidate")
        self.assertEqual(self.decision(), "PASS")  # registry results from mixed-channel run
        self.results[0]["results"][0]["channel"] = "candidate"
        self.assertEqual(self.decision(), "INDETERMINATE")

    def test_unselected_channel(self):
        self.results[0]["results"][0]["channel"] = "pr"
        with self.assertRaises(ValueError):
            self.imported()

    def test_nonprofile_window(self):
        self.results[0]["windowDifference"] = ["fixture"]
        self.assertEqual(self.decision(), "INDETERMINATE")

    def test_ambiguous_implementation(self):
        self.results.append(copy.deepcopy(self.results[0]))
        with self.assertRaises(ValueError):
            self.imported()

    def test_invalid_anchor_mapping(self):
        self.manifest["requirements"]["synthetic-R1"]["positive_anchors"] = ["absent"]
        with self.assertRaises(ValueError):
            self.imported()

    def test_cli_path(self):
        output = self.path / "input.json"
        subprocess.run([sys.executable, str(ROOT / "tools/import_tt_conformance.py"),
            str(self.path / "run.json"), str(self.path / "results.json"), str(self.path / "manifest.json"),
            "--output", str(output)], check=True)
        subprocess.run([sys.executable, str(ROOT / "tools/dcas_evaluate.py"), str(output), "--expect", "PASS"],
            check=True, capture_output=True)
        self.assertEqual(json.loads(output.read_text()), self.imported(False))


if __name__ == "__main__":
    unittest.main()
