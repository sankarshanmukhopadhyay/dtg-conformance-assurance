#!/usr/bin/env python3
"""Thin DCAS reference evaluator for the portable v0.1 contract.

This evaluator intentionally implements only the evidence-state and bounded
claim rules needed by the first ANAB interoperability experiment. Source
baseline requirements remain authoritative outside this tool.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

VALID_DECISIONS = {"PASS", "FAIL", "INDETERMINATE"}


def digest(value: dict) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def evaluate(document: dict) -> dict:
    claim = document.get("claim", {})
    policy = document.get("policy", {})
    evidence = document.get("evidence", [])
    statuses = {item["id"]: item["status"] for item in evidence}
    requirements = claim.get("requirements") or [claim.get("fixture_id", "source-requirement")]

    consumed = sorted(key for key, status in statuses.items() if status == "available")
    missing = sorted(key for key, status in statuses.items() if status == "missing")
    rejected = sorted(key for key, status in statuses.items() if status in {"stale", "revoked", "unverifiable"})

    if "revoked" in statuses.values():
        decision = policy.get("revoked_evidence", "FAIL")
        reason = "revoked evidence contradicts current reliance"
    elif "stale" in statuses.values():
        decision = policy.get("stale_evidence", "FAIL")
        reason = "stale evidence cannot establish current reliance"
    elif claim.get("assurance_overclaim"):
        decision = policy.get("assurance_overclaim", "FAIL")
        reason = "claimed assurance exceeds demonstrated evidence"
    elif claim.get("requires_action_authority") and statuses.get("action-authority") != "available":
        decision = policy.get("authority_absent", "INDETERMINATE")
        reason = "identity assurance does not establish required action-specific authority"
    elif any(status in {"missing", "unverifiable"} for status in statuses.values()):
        decision = policy.get("missing_evidence", "INDETERMINATE")
        reason = "required evidence is missing or unverifiable"
    else:
        decision = "PASS"
        reason = "available evidence satisfies this bounded evaluation input"

    if decision not in VALID_DECISIONS:
        raise ValueError(f"unsupported decision {decision!r}")

    return {
        "contract_version": document["contract_version"],
        "evaluation_id": document["evaluation_id"],
        "decision": decision,
        "evaluator": {"name": "dcas-reference-evaluator", "version": "0.1.0"},
        "findings": [
            {
                "requirement": requirement,
                "result": decision,
                "reason": reason,
                "evidence_ids": sorted(statuses),
            }
            for requirement in requirements
        ],
        "evidence_summary": {"consumed": consumed, "missing": missing, "rejected": rejected},
        "receipt_material": {"input_digest": digest(document), "result_digest_algorithm": "sha256"},
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--expect", choices=sorted(VALID_DECISIONS))
    args = parser.parse_args()

    document = json.loads(args.input.read_text(encoding="utf-8"))
    result = evaluate(document)
    rendered = json.dumps(result, indent=2) + "\n"

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")

    if args.expect and result["decision"] != args.expect:
        print(f"expected {args.expect}, observed {result['decision']}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
