#!/usr/bin/env python3
"""Coverage report generator (CSV + Markdown).

Given a bundle directory (CSV-based) and the control objectives registry, produce:
- coverage.csv: row per control objective with evidence mappings
- coverage.md: human-readable summary + uncovered list

Usage:
    python tools/coverage_report.py --bundle templates/starter-bundle --out risk/reports/coverage
"""
from __future__ import annotations

import argparse
import csv
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Set, Tuple
import hashlib
import datetime

ROOT = Path(__file__).resolve().parents[1]

@dataclass(frozen=True)
class ControlObjective:
    control_objective_id: str
    title: str

def _read_csv(path: Path) -> List[dict]:
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)

def load_controls(registry_path: Path) -> Dict[str, ControlObjective]:
    rows = _read_csv(registry_path)
    controls: Dict[str, ControlObjective] = {}
    for r in rows:
        cid = (r.get("control_objective_id") or "").strip()
        if not cid:
            continue
        title = (r.get("title") or "").strip()
        controls[cid] = ControlObjective(cid, title)
    return controls

def generate(bundle_dir: Path, out_dir: Path, registry_path: Path) -> Tuple[Path, Path]:
    controls = load_controls(registry_path)
    if not controls:
        raise SystemExit("No control objectives loaded; cannot generate coverage.")

    mapping_path = bundle_dir / "mappings_control_evidence.csv"
    evidence_path = bundle_dir / "evidence.csv"

    if not mapping_path.exists():
        raise SystemExit(f"Missing {mapping_path}")
    if not evidence_path.exists():
        raise SystemExit(f"Missing {evidence_path}")

    mappings = _read_csv(mapping_path)
    evid_rows = _read_csv(evidence_path)
    evidence_by_id = {(r.get('evidence_id') or '').strip(): r for r in evid_rows if (r.get('evidence_id') or '').strip()}

    # Build coverage map: control -> list of (evidence_id, coverage_type)
    cov: Dict[str, List[Tuple[str, str]]] = {cid: [] for cid in controls.keys()}
    for r in mappings:
        cid = (r.get("control_objective_id") or "").strip()
        eid = (r.get("evidence_id") or "").strip()
        ctype = (r.get("coverage_type") or "").strip()
        if not cid or not eid:
            continue
        if cid not in cov:
            # allow mapping to controls outside registry; keep but will be reported by validation elsewhere
            cov[cid] = []
        cov[cid].append((eid, ctype))

    out_dir.mkdir(parents=True, exist_ok=True)

    # coverage.csv
    coverage_csv = out_dir / "coverage.csv"
    fieldnames = [
        "control_objective_id",
        "control_title",
        "coverage_status",
        "mapped_evidence_count",
        "evidence_ids",
        "coverage_types",
    ]
    rows_out: List[dict] = []
    uncovered: List[str] = []
    covered = 0

    for cid in sorted(controls.keys()):
        items = cov.get(cid, [])
        eids = [eid for eid, _ in items if eid]
        # stable sort + de-dupe
        eids_unique = sorted({e for e in eids if e})
        ctypes_unique = sorted({ct for _, ct in items if ct})
        status = "covered" if eids_unique else "uncovered"
        if status == "covered":
            covered += 1
        else:
            uncovered.append(cid)

        rows_out.append({
            "control_objective_id": cid,
            "control_title": controls[cid].title,
            "coverage_status": status,
            "mapped_evidence_count": str(len(eids_unique)),
            "evidence_ids": ";".join(eids_unique),
            "coverage_types": ";".join(ctypes_unique),
        })

    with coverage_csv.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows_out)

    total = len(controls)
    pct = (covered / total * 100.0) if total else 0.0

    # coverage.md
    coverage_md = out_dir / "coverage.md"
    epoch_env = os.environ.get('SOURCE_DATE_EPOCH')
    if epoch_env is not None:
        epoch = int(epoch_env)
        now = datetime.datetime.utcfromtimestamp(epoch).strftime("%Y-%m-%d %H:%M UTC")
    else:
        now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    md_lines = []
    md_lines.append("# Coverage report")
    md_lines.append("")
    md_lines.append(f"- Generated: {now}")
    try:
        bundle_display = bundle_dir.relative_to(ROOT).as_posix()
    except ValueError:
        bundle_display = bundle_dir.as_posix()
    md_lines.append(f"- Bundle: `{bundle_display}`")
    md_lines.append(f"- Control objectives (registry): `{registry_path.relative_to(ROOT).as_posix()}`")
    md_lines.append("")
    md_lines.append("## Summary")
    md_lines.append("")
    md_lines.append(f"- Total control objectives: **{total}**")
    md_lines.append(f"- Covered: **{covered}**")
    md_lines.append(f"- Uncovered: **{total - covered}**")
    md_lines.append(f"- Coverage: **{pct:.1f}%**")
    md_lines.append("")
    md_lines.append("## Uncovered control objectives")
    md_lines.append("")
    if not uncovered:
        md_lines.append("_All control objectives are covered by at least one evidence item._")
    else:
        for cid in uncovered:
            title = controls[cid].title
            md_lines.append(f"- `{cid}` — {title}")
    md_lines.append("")
    md_lines.append("## Outputs")
    md_lines.append("")
    md_lines.append(f"- CSV: `{coverage_csv.relative_to(ROOT).as_posix()}`")
    md_lines.append(f"- Markdown: `{coverage_md.relative_to(ROOT).as_posix()}`")
    md_lines.append("")

    coverage_md.write_text("\n".join(md_lines), encoding="utf-8")

    return coverage_csv, coverage_md

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--bundle", required=True, help="Bundle directory containing CSVs (e.g., templates/starter-bundle)")
    ap.add_argument("--out", required=True, help="Output directory for reports")
    ap.add_argument("--registry", default="controls/control_objectives.csv", help="Control objective registry CSV path")
    args = ap.parse_args()

    bundle_dir = (ROOT / args.bundle).resolve()
    out_dir = (ROOT / args.out).resolve()
    registry_path = (ROOT / args.registry).resolve()

    if not bundle_dir.exists():
        raise SystemExit(f"Bundle dir not found: {bundle_dir}")
    if not registry_path.exists():
        raise SystemExit(f"Registry not found: {registry_path}")

    csv_path, md_path = generate(bundle_dir=bundle_dir, out_dir=out_dir, registry_path=registry_path)
    print(f"[OK] Wrote {csv_path}")
    print(f"[OK] Wrote {md_path}")

if __name__ == "__main__":
    main()
