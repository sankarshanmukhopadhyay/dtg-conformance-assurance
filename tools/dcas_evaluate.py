#!/usr/bin/env python3
"""Evaluate assessed evidence; does not authenticate external artifacts."""
import argparse
import hashlib
import json
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
VALID_DECISIONS = {"PASS", "FAIL", "INDETERMINATE"}
DEFAULTS = {"stale_evidence": "FAIL", "revoked_evidence": "FAIL",
            "authority_absent": "INDETERMINATE", "assurance_overclaim": "FAIL",
            "missing_evidence": "INDETERMINATE"}


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def parse_json(raw):
    def invalid(value):
        raise ValueError(f"invalid JSON constant: {value}")
    return json.loads(raw, object_pairs_hook=unique_object, parse_constant=invalid)


def read_json(path):
    return parse_json(Path(path).read_bytes())


def validate_schema(value, filename):
    schema = read_json(ROOT / "spec" / "schemas" / filename)
    Draft202012Validator(schema, format_checker=FormatChecker()).validate(value)


def digest(value):
    return "sha256:" + hashlib.sha256(json.dumps(value, sort_keys=True,
        separators=(",", ":"), allow_nan=False).encode()).hexdigest()


def evaluate(document):
    version = document.get("contract_version")
    if version not in {"0.1", "0.2"}:
        raise ValueError("unsupported evaluator contract")
    suffix = "" if version == "0.1" else "-v0.2"
    validate_schema(document, f"dcas-evaluation-input{suffix}.schema.json")
    claim, policy = document["claim"], document["policy"]
    for key in DEFAULTS:
        if key in policy and policy[key] not in {"FAIL", "INDETERMINATE"}:
            raise ValueError(f"unsafe policy: {key}")
    if policy.get("authority_inference_from_identity", False) is not False:
        raise ValueError("identity cannot establish action authority")
    statuses = {e["id"]: e["status"] for e in document["evidence"]}
    if len(statuses) != len(document["evidence"]):
        raise ValueError("duplicate evidence ID")
    requirements = claim.get("requirements") or [claim.get("fixture_id", "source-requirement")]
    if not isinstance(requirements, list) or not all(isinstance(r, str) and r for r in requirements):
        raise ValueError("invalid requirements")
    if len(set(requirements)) != len(requirements):
        raise ValueError("duplicate requirement")
    bindings = claim.get("requirement_evidence", {}) if version == "0.2" else {}
    if set(bindings) - set(requirements):
        raise ValueError("binding for undeclared requirement")
    findings, consumed, missing, rejected = [], set(), set(), set()
    for requirement in requirements:
        refs = sorted(bindings.get(requirement, [])) if version == "0.2" else sorted(statuses)
        states = {ref: statuses.get(ref, "missing") for ref in refs}
        consumed.update(k for k, v in states.items() if v == "available")
        missing.update(k for k, v in states.items() if v == "missing")
        rejected.update(k for k, v in states.items() if v in {"stale", "revoked", "unverifiable", "contradicted"})
        problems = []
        if "contradicted" in states.values():
            problems.append(("FAIL", "mapped proposition contradicted"))
        for state in ("stale", "revoked"):
            if state in states.values():
                key = state + "_evidence"
                problems.append((policy.get(key, DEFAULTS[key]), state + " evidence"))
        if claim.get("assurance_overclaim"):
            problems.append((policy.get("assurance_overclaim", "FAIL"), "assurance overclaim"))
        if claim.get("requires_action_authority") and states.get("action-authority") != "available":
            problems.append((policy.get("authority_absent", "INDETERMINATE"), "action authority not established"))
        if version == "0.1":
            problems.append(("INDETERMINATE", "legacy contract lacks explicit bindings; migrate to 0.2"))
        elif not refs:
            problems.append(("INDETERMINATE", "no evidence bound to requirement"))
        if any(v in {"missing", "unverifiable"} for v in states.values()):
            problems.append(("INDETERMINATE", "required evidence missing or unverifiable"))
        decision = "FAIL" if any(p[0] == "FAIL" for p in problems) else "INDETERMINATE" if problems else "PASS"
        findings.append({"requirement": requirement, "result": decision,
            "reason": "; ".join(p[1] for p in problems) if problems else "all bound assessed evidence supports requirement",
            "evidence_ids": refs})
    decisions = {f["result"] for f in findings}
    result = {"contract_version": version, "evaluation_id": document["evaluation_id"],
        "decision": "FAIL" if "FAIL" in decisions else "INDETERMINATE" if "INDETERMINATE" in decisions else "PASS",
        "evaluator": {"name": "dcas-reference-evaluator", "version": "0.2.0"},
        "findings": findings, "evidence_summary": {"consumed": sorted(consumed), "missing": sorted(missing), "rejected": sorted(rejected)},
        "receipt_material": {"input_digest": digest(document), "result_digest_algorithm": "sha256"}}
    validate_schema(result, f"dcas-evaluation-result{suffix}.schema.json")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--expect", choices=sorted(VALID_DECISIONS))
    args = parser.parse_args()
    result = evaluate(read_json(args.input))
    rendered = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return int(bool(args.expect and result["decision"] != args.expect))


if __name__ == "__main__":
    raise SystemExit(main())
