#!/usr/bin/env python3
"""Repo validation entrypoint (automatable by default).

Runs:
- CSV schema validation using machine-readable descriptors under schemas/csv/
- Referential integrity checks (control objective IDs)
- Markdown relative link checks
- Deterministic coverage report regeneration check

Usage:
    python tools/validate.py
"""
from __future__ import annotations

import csv
import json
import os
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

ROOT = Path(__file__).resolve().parents[1]

def fail(msg: str) -> None:
    print(f"[FAIL] {msg}")
    raise SystemExit(1)

def warn(msg: str) -> None:
    print(f"[WARN] {msg}")

def ok(msg: str) -> None:
    print(f"[OK] {msg}")

def read_csv_headers(path: Path) -> List[str]:
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        headers = next(reader, None)
        if not headers:
            return []
        return [h.strip() for h in headers]

def read_csv_rows(path: Path) -> List[Dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)

def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))

def load_control_ids() -> Set[str]:
    path = ROOT / "controls" / "control_objectives.csv"
    if not path.exists():
        fail("Missing controls/control_objectives.csv (required for ID checks).")

    rows = read_csv_rows(path)
    if not rows:
        fail("controls/control_objectives.csv has no rows.")

    if "control_objective_id" not in rows[0]:
        fail("controls/control_objectives.csv missing 'control_objective_id' column.")

    ids = { (r.get("control_objective_id") or "").strip() for r in rows if (r.get("control_objective_id") or "").strip() }
    if not ids:
        fail("controls/control_objectives.csv has no control objective IDs.")
    ok(f"Loaded {len(ids)} control objective IDs.")
    return ids

def _validate_value(value: str, col: Dict[str, Any], control_ids: Set[str]) -> Optional[str]:
    t = col.get("type", "string")
    value = (value or "").strip()

    # Empty values are allowed unless the column is required (handled elsewhere)
    if not value:
        return None

    if t == "enum":
        allowed = set(col.get("enum") or [])
        if allowed and value not in allowed:
            return f"value '{value}' not in enum {sorted(allowed)}"
    elif t == "datetime":
        # Accept ISO-ish strings; we intentionally avoid strict parsing to keep adoption friction low.
        # Must have at least a date part YYYY-MM-DD
        if not re.match(r"^\d{4}-\d{2}-\d{2}", value):
            return "datetime should start with YYYY-MM-DD"
    elif t == "id_list":
        delim = col.get("delimiter", ";")
        parts = [p.strip() for p in value.split(delim) if p.strip()]
        if not parts:
            return "id_list is empty after splitting"
        # If this list is explicitly control_objective_ids, validate membership
        if col.get("name") in {"control_objective_ids", "Control Objective IDs"}:
            bad = [p for p in parts if p not in control_ids]
            if bad:
                return f"unknown control objective IDs: {bad[:5]}"
    elif t == "string":
        pass

    patt = col.get("pattern")
    if patt:
        if not re.match(patt, value):
            return f"value '{value}' does not match pattern {patt}"

    return None

def validate_csv_against_descriptor(csv_path: Path, descriptor: Dict[str, Any], control_ids: Set[str]) -> None:
    headers = read_csv_headers(csv_path)
    if not headers:
        fail(f"{csv_path} is empty or missing headers.")

    cols = descriptor.get("columns") or []
    required = {c["name"] for c in cols if c.get("required") is True}
    missing = required - set(headers)
    if missing:
        fail(f"{csv_path} missing required columns: {sorted(missing)}")

    # Extensions allowed?
    allow_ext = bool(descriptor.get("allow_extensions", False))
    ext_prefix = descriptor.get("extension_prefix", "x_") or "x_"
    known = {c["name"] for c in cols}

    if not allow_ext:
        unknown = [h for h in headers if h not in known]
        if unknown:
            fail(f"{csv_path} contains unknown columns: {unknown}")
    else:
        unknown = [h for h in headers if h not in known and not h.startswith(ext_prefix)]
        if unknown:
            fail(f"{csv_path} contains unknown non-extension columns: {unknown} (use '{ext_prefix}*' for extensions)")

    # Row-level checks (lightweight)
    rows = read_csv_rows(csv_path)
    if not rows:
        warn(f"{csv_path} has headers but no rows.")
        return

    col_by_name = {c["name"]: c for c in cols}
    problems: List[str] = []
    for idx, row in enumerate(rows, start=2):
        for c in cols:
            name = c["name"]
            v = (row.get(name) or "").strip()
            if c.get("required") and not v:
                problems.append(f"line {idx}: required column '{name}' is empty")
                continue
            err = _validate_value(v, c, control_ids)
            if err:
                problems.append(f"line {idx}: column '{name}': {err}")
        if len(problems) > 50:
            break

    if problems:
        sample = "\n".join(f"- {p}" for p in problems[:25])
        fail(f"{csv_path} failed schema checks (showing up to 25):\n{sample}")
    ok(f"CSV schema checks passed: {csv_path.relative_to(ROOT)}")

def validate_csv_schemas(control_ids: Set[str]) -> None:
    index_path = ROOT / "schemas" / "csv" / "index.json"
    if not index_path.exists():
        fail("Missing schemas/csv/index.json (machine-readable CSV schema descriptors).")

    index = load_json(index_path)
    descriptor_paths = index.get("descriptors") or []
    if not descriptor_paths:
        fail("schemas/csv/index.json contains no descriptors.")

    checked = 0
    for rel in descriptor_paths:
        dpath = (ROOT / rel).resolve()
        if not dpath.exists():
            fail(f"Descriptor missing: {rel}")
        desc = load_json(dpath)
        applies_to = desc.get("applies_to")
        if not applies_to:
            fail(f"Descriptor {rel} missing applies_to.")
        csv_path = (ROOT / applies_to).resolve()
        if not csv_path.exists():
            warn(f"CSV not present for descriptor {desc.get('id')}: {applies_to} (skipping)")
            continue
        validate_csv_against_descriptor(csv_path, desc, control_ids)
        checked += 1

    ok(f"Validated {checked} CSV files against schema descriptors.")

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
            target = target.split("#", 1)[0]
            if not target:
                continue
            if target.startswith("/"):
                continue
            dest = (p.parent / target).resolve()
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

def _compute_coverage_csv(bundle_dir: Path, registry_path: Path) -> str:
    # Minimal deterministic computation (must match tools/coverage_report.py output)
    controls = read_csv_rows(registry_path)
    control_map = { (r.get('control_objective_id') or '').strip(): (r.get('title') or '').strip() for r in controls if (r.get('control_objective_id') or '').strip() }
    if not control_map:
        fail("Cannot compute coverage: control registry empty.")

    mappings = read_csv_rows(bundle_dir / "mappings_control_evidence.csv")
    cov: Dict[str, Set[str]] = {cid: set() for cid in control_map.keys()}
    ctypes: Dict[str, Set[str]] = {cid: set() for cid in control_map.keys()}

    for r in mappings:
        cid = (r.get("control_objective_id") or "").strip()
        eid = (r.get("evidence_id") or "").strip()
        ct = (r.get("coverage_type") or "").strip()
        if cid in cov and eid:
            cov[cid].add(eid)
            if ct:
                ctypes[cid].add(ct)

    out = []
    out.append("control_objective_id,control_title,coverage_status,mapped_evidence_count,evidence_ids,coverage_types")
    for cid in sorted(control_map.keys()):
        eids = sorted(cov.get(cid) or set())
        cts = sorted(ctypes.get(cid) or set())
        status = "covered" if eids else "uncovered"
        out.append(",".join([
            cid,
            _csv_escape(control_map[cid]),
            status,
            str(len(eids)),
            _csv_escape(";".join(eids)),
            _csv_escape(";".join(cts)),
        ]))
    return "\n".join(out) + "\n"

def _csv_escape(s: str) -> str:
    # Escape a single CSV field, returning a safe representation without relying on csv module formatting differences.
    if s is None:
        s = ""
    if any(ch in s for ch in [',','\n','\r','"']):
        s = '"' + s.replace('"','""') + '"'
    return s

def validate_coverage_reports() -> None:
    bundle_dir = ROOT / "templates" / "starter-bundle"
    registry = ROOT / "controls" / "control_objectives.csv"
    out_dir = ROOT / "risk" / "reports" / "coverage"
    csv_path = out_dir / "coverage.csv"
    md_path = out_dir / "coverage.md"

    if not csv_path.exists() or not md_path.exists():
        fail("Coverage report outputs missing. Run `make coverage` and commit outputs under risk/reports/coverage/.")

    expected_csv = _compute_coverage_csv(bundle_dir=bundle_dir, registry_path=registry)
    actual_csv = csv_path.read_text(encoding="utf-8")
    if actual_csv != expected_csv:
        fail("Coverage CSV is out of date. Run `make coverage` to regenerate and commit the updated outputs.")

    # Markdown: we only require it to be deterministic + to reference the output paths.
    md = md_path.read_text(encoding="utf-8")
    if "- CSV: `risk/reports/coverage/coverage.csv`" not in md or "- Markdown: `risk/reports/coverage/coverage.md`" not in md:
        fail("Coverage markdown missing expected output references.")

    # Require deterministic timestamp convention
    if "- Generated: 1970-01-01 00:00 UTC" not in md:
        warn("Coverage markdown does not appear deterministic (expected SOURCE_DATE_EPOCH=0 output). Consider regenerating with `make coverage`.")
    ok("Coverage report outputs are up-to-date and deterministic.")

def main() -> None:
    print("DTG DCAS repo validation\n")
    control_ids = load_control_ids()
    validate_csv_schemas(control_ids)
    validate_coverage_reports()
    validate_markdown_links()
    ok("All checks passed.")

if __name__ == "__main__":
    main()
