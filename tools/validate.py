#!/usr/bin/env python3
"""
Repo validation entrypoint.

Runs:
- CSV structural checks (risk exports + templates)
- Basic referential integrity checks (control IDs referenced)
- Markdown relative link checks

Usage:
    python tools/validate.py
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def fail(msg: str) -> None:
    print(f"[FAIL] {msg}")
    raise SystemExit(1)

def warn(msg: str) -> None:
    print(f"[WARN] {msg}")

def ok(msg: str) -> None:
    print(f"[OK] {msg}")

def read_csv_headers(path: Path) -> set[str]:
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        headers = next(reader, None)
        if not headers:
            return set()
        return {h.strip() for h in headers}

def load_control_ids() -> set[str]:
    path = ROOT / "controls" / "control_objectives.csv"
    if not path.exists():
        fail("Missing controls/control_objectives.csv (required for ID checks).")
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames or "control_objective_id" not in reader.fieldnames:
            fail("controls/control_objectives.csv missing 'control_objective_id' column.")
        ids = {row["control_objective_id"].strip() for row in reader if row.get("control_objective_id")}
    if not ids:
        fail("controls/control_objectives.csv has no control objective IDs.")
    ok(f"Loaded {len(ids)} control objective IDs.")
    return ids

def validate_risk_exports(control_ids: set[str]) -> None:
    risk_csv = ROOT / "risk" / "exports" / "risk_assessment.csv"
    if not risk_csv.exists():
        warn("risk/exports/risk_assessment.csv not found (skipping risk export checks).")
        return

    required = {"Risk ID","Category","Risk Statement","Likelihood","Impact","Inherent Risk","Controls","Residual Risk"}
    headers = read_csv_headers(risk_csv)
    missing = required - headers
    if missing:
        fail(f"{risk_csv} missing required columns: {sorted(missing)}")
    ok("risk_assessment.csv has required columns.")

    # Optional: validate mapped control objective IDs if present
    with risk_csv.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            return
        if "Control Objective IDs" not in reader.fieldnames:
            warn("risk_assessment.csv has no 'Control Objective IDs' column (skipping ID integrity check).")
            return
        bad = []
        for i, row in enumerate(reader, start=2):
            ids_cell = (row.get("Control Objective IDs") or "").strip()
            if not ids_cell:
                continue
            parts = [p.strip() for p in re.split(r"[;,\|]", ids_cell) if p.strip()]
            for cid in parts:
                if cid and cid not in control_ids:
                    bad.append((i, cid))
        if bad:
            sample = ", ".join([f"line {ln}:{cid}" for ln, cid in bad[:10]])
            fail(f"risk_assessment.csv references unknown control objective IDs (sample: {sample}).")
    ok("risk_assessment.csv control objective ID references look valid.")

def validate_templates() -> None:
    base = ROOT / "templates" / "starter-bundle"
    if not base.exists():
        warn("templates/starter-bundle missing (skipping template validation).")
        return

    required_files = {
        "bundle_manifest.csv": {"bundle_id","bundle_version","created_at","issuer_id","issuer_name","target_profile_id","target_assurance_level","file_path","file_purpose"},
        "claims.csv": {"claim_id","claim_type","subject_id","profile_id","assurance_level","statement","issued_at","evidence_bundle_id"},
        "risks.csv": {"Risk ID","Category","Risk Statement","Likelihood","Impact","Inherent Risk","Controls","Residual Risk"},
        "evidence.csv": {"evidence_id","title","description","artifact_path","artifact_type","created_at","owner","control_objective_ids"},
        "mappings_control_evidence.csv": {"control_objective_id","evidence_id","coverage_type"},
        "evaluation_results.csv": {"check_id","profile_id","assurance_level","result","evidence_ids","checked_at","checker"},
    }

    for fn, required in required_files.items():
        p = base / fn
        if not p.exists():
            fail(f"Missing template file: {p}")
        headers = read_csv_headers(p)
        missing = required - headers
        if missing:
            fail(f"{p} missing required columns: {sorted(missing)}")
    ok("Starter bundle templates present with required columns.")

def validate_markdown_links() -> None:
    md_files = [p for p in ROOT.rglob("*.md") if ".git" not in str(p)]
    link_re = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
    checked = 0
    broken = []

    for p in md_files:
        text = p.read_text(encoding="utf-8", errors="ignore")
        for m in link_re.finditer(text):
            target = m.group(1).strip()
            if not target or "://" in target or target.startswith("#") or target.startswith("mailto:"):
                continue
            # strip anchor
            target = target.split("#", 1)[0]
            if not target:
                continue
            # ignore absolute paths
            if target.startswith("/"):
                continue
            dest = (p.parent / target).resolve()
            # constrain within repo
            try:
                dest.relative_to(ROOT.resolve())
            except Exception:
                continue
            checked += 1
            if not dest.exists():
                broken.append((p.relative_to(ROOT), target))
    if broken:
        sample = "\n".join([f"- {src}: {tgt}" for src, tgt in broken[:25]])
        fail(f"Broken relative markdown links found (showing up to 25):\n{sample}")
    ok(f"Markdown link check passed ({checked} links checked).")

def main() -> None:
    print("DTG DCAS repo validation\n")
    control_ids = load_control_ids()
    validate_risk_exports(control_ids)
    validate_templates()
    validate_markdown_links()
    ok("All checks passed.")

if __name__ == "__main__":
    main()
