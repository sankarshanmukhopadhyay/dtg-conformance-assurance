#!/usr/bin/env python3
"""Import a pinned draft Trust Tasks run using a separately trusted assessor manifest."""
import argparse
import hashlib
import json
import re
from datetime import datetime
from pathlib import Path
from dcas_evaluate import parse_json, read_json, validate_schema

SUITE_COMMIT = "864687a5bc072b12c952e16539b42e738c4a7dd5"
STATUSES = {"PASS", "FAIL", "SKIP", "KNOWN-FAIL", "CLARIFY", "QUARANTINED", "SPEC-CHANGED", "SKIPPED-SAFETY"}
CHANNELS = {"registry", "pr", "proposed", "candidate"}
HEX = re.compile(r"^[0-9a-f]{64}$")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def timestamp(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def normalize(run_path, results_path, manifest_path):
    manifest = read_json(manifest_path)
    validate_schema(manifest, "dcas-tt-assessor-manifest.schema.json")
    source = manifest["source"]
    run_raw, results_raw = Path(run_path).read_bytes(), Path(results_path).read_bytes()
    require(sha(run_raw) == source["run_sha256"], "run digest mismatch")
    require(sha(results_raw) == source["results_sha256"], "results digest mismatch")
    run, runs = parse_json(run_raw), parse_json(results_raw)
    require(isinstance(run, dict) and run.get("format") == "tt-conformance-run/0.2" and "tool" not in run, "unsupported run")
    require(run["suite"] == {"commit": SUITE_COMMIT, "dirty": False, "version": "0.1.0-draft"}
            and run["suite"]["dirty"] is False, "unreviewed suite revision")
    files = run["vectors"]["files"]
    require(isinstance(files, dict) and files and all(p and isinstance(h, str) and HEX.fullmatch(h)
            for p, h in files.items()), "invalid vector inventory")
    inventory = "".join(f"{files[p]}  {p}\n" for p in sorted(files, key=lambda p: p.encode("utf-16-be")))
    require("sha256:" + sha(inventory.encode()) == run["vectors"]["digest"] == source["vector_digest"], "vector digest mismatch")
    for key in ("exceptions", "quarantine"):
        entry = run.get(key)
        require(entry is None or (isinstance(entry, dict) and isinstance(entry.get("sha256"), str)
                and HEX.fullmatch(entry["sha256"])), "invalid exception/quarantine record")
    require("exceptions" in run and run.get("todaySource") in {"pinned", "clock"}, "missing exception date provenance")
    datetime.strptime(run["today"], "%Y-%m-%d")
    caps = [i["capabilities"] for i in run["implementations"] if i["capabilities"].get("name") == source["implementation"]]
    require(len(caps) == 1 and caps[0].get("version") == source["implementation_version"], "implementation mismatch")
    require(isinstance(runs, list) and all(isinstance(r, dict) for r in runs), "expected results array")
    selected = [r for r in runs if r.get("impl") == source["implementation"] and type(r.get("tier")) is int and r["tier"] == source["tier"]]
    require(len(selected) == 1, "missing or ambiguous run selection")
    selected = selected[0]
    require(isinstance(selected.get("channels"), list) and "registry" in selected["channels"]
            and len(set(selected["channels"])) == len(selected["channels"])
            and all(c in CHANNELS for c in selected["channels"]), "registry channel not established")
    rows = {}
    require(isinstance(selected["results"], list), "invalid result rows")
    for row in selected["results"]:
        vid = row["id"]
        require(isinstance(vid, str) and vid and vid not in rows, "duplicate or invalid vector")
        require(row["status"] in STATUSES and row.get("channel", "registry") in CHANNELS, "unknown outcome")
        require(row.get("channel", "registry") in selected["channels"], "vector channel not selected")
        require(type(row["tier"]) is int and 1 <= row["tier"] <= source["tier"], "invalid vector tier")
        require(all(isinstance(row.get(k), str) and row[k] for k in ("group", "family")), "missing group/family")
        for flag in ("anchor", "synthetic", "acceptedOnlyGate"):
            require(flag not in row or row[flag] is True, "invalid vector flag")
        rows[vid] = row
    require(isinstance(selected["drift"], list) and isinstance(selected["windowDifference"], list)
            and all(isinstance(v, str) for v in selected["windowDifference"]), "missing applicability observations")
    drifted = set()
    for finding in selected["drift"]:
        require(finding["kind"] == "spec-drift" and finding["reason"] in {"changed", "missing-source", "unpinned"}
                and isinstance(finding["vectors"], list) and all(isinstance(v, str) for v in finding["vectors"]), "invalid drift")
        drifted.update(finding["vectors"])
    probe = selected["essentialProbe"]["result"]
    require(probe in {"consistent", "mismatch", "not-probed", "not-run"}, "unknown governance probe")
    excluded = set()
    for field in ("excludedFromRun", "retired"):
        require(isinstance(selected.get(field, {}), dict), "invalid exclusions")
        excluded.update(selected.get(field, {}))
    for values in selected.get("excludedByChannel", {}).values():
        require(isinstance(values, list), "invalid channel exclusions")
        excluded.update(values)
    excluded.update(item["id"] for item in selected.get("excludedByTier", []))
    require(not excluded.intersection(rows), "reported vector also excluded")
    observed, evaluated, expires = (timestamp(manifest[k]) for k in ("observed_at", "evaluation_time", "valid_until"))
    require(observed <= evaluated and observed < expires, "invalid assessor interval")
    require(timestamp(run["today"] + "T00:00:00Z") <= observed, "run date after observation")
    bindings, evidence, detail = {}, [], {}
    for requirement, mapping in sorted(manifest["requirements"].items()):
        anchors = set(mapping["positive_anchors"])
        require(anchors <= set(mapping["vectors"]), "anchor not mapped")
        bindings[requirement] = []
        for vid in sorted(mapping["vectors"]):
            row = rows.get(vid)
            eid = "tt:" + json.dumps([requirement, vid], separators=(",", ":"))
            bindings[requirement].append(eid)
            if row is None:
                state, reason = "missing", "required vector absent"
            elif evaluated >= expires:
                state, reason = "stale", "assessor interval expired"
            elif vid in drifted or row["status"] == "SPEC-CHANGED":
                state, reason = "unverifiable", "specification drift"
            elif row.get("channel", "registry") != "registry" or row.get("synthetic") or row.get("acceptedOnlyGate") or selected["windowDifference"]:
                state, reason = "unverifiable", "advisory/synthetic/gate-only or non-profile window"
            elif row["status"] in {"FAIL", "KNOWN-FAIL"}:
                state, reason = "contradicted", "mapped vector failed"
            elif probe == "mismatch" or row["status"] != "PASS":
                state, reason = "unverifiable", "governance mismatch or non-pass"
            elif vid in anchors and row.get("anchor") is not True:
                state, reason = "unverifiable", "positive anchor not established"
            else:
                state, reason = "available", "reviewed mapped registry vector passed"
            evidence.append({"id": eid, "uri": "urn:sha256:" + source["results_sha256"],
                "digest": "sha256:" + source["results_sha256"], "status": state})
            detail[eid] = {"vector": vid, "source_result": row, "excluded": vid in excluded,
                "required_positive": vid in anchors, "reason": reason}
    document = {"contract_version": "0.2", "evaluation_id": manifest["evaluation_id"], "target": manifest["target"],
        "claim": {"requirements": sorted(bindings), "requirement_evidence": bindings,
            "source_context": {"repository": "https://github.com/bmiller59/dtgwg-conformance",
                "manifest": manifest, "run": run, "selected_run": {k: selected[k] for k in
                ("impl", "tier", "channels", "drift", "windowDifference", "essentialProbe")}, "mapped_results": detail}},
        "evidence": evidence, "policy": {"missing_evidence": "INDETERMINATE", "stale_evidence": "INDETERMINATE"},
        "evaluation_time": manifest["evaluation_time"]}
    validate_schema(document, "dcas-evaluation-input-v0.2.schema.json")
    return document


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for field in ("run", "results", "manifest"):
        parser.add_argument(field, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    document = normalize(args.run, args.results, args.manifest)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(document, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
