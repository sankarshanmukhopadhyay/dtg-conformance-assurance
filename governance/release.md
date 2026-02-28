# Release checklist

Use this checklist before cutting a tagged release.

## Required artifacts (content)

- [ ] Risk register XLSX updated (if applicable): `risk/source/Risk Register.xlsx`
- [ ] Risk export regenerated: `python tools/export_xlsx_to_csv.py`
- [ ] Risk export validated: `python tools/validate_csv.py`
- [ ] Risk → CO mapping reviewed: `risk/mapping/risk_to_control_objectives.csv`
- [ ] Control objectives reviewed: `controls/control_objectives.md`
- [ ] Catalogs updated and internally consistent:
  - [ ] `controls/control_catalog.csv`
  - [ ] `controls/evidence_catalog.csv`
  - [ ] `controls/test_suites.csv`
- [ ] Coverage report refreshed: `risk/reports/coverage_summary.md`
- [ ] Conformance profiles reviewed: `conformance/profiles/`
- [ ] DCAS spec updated (if applicable): `spec/DCAS_v0.1.md`
- [ ] Evaluation method reviewed + versioned:
  - [ ] `docs/dcas-evaluate/`
  - [ ] `DCAS_METHOD_VERSION`

## Required artifacts (repo hygiene)

- [ ] README updated (routing for new adopters)
- [ ] Roadmap updated: `docs/roadmap.md`
- [ ] Release notes drafted (see `docs/releases/`)
- [ ] Decision log updated (if applicable): `governance/decision_log.md`

## Tagging

- [ ] Version tag created (SemVer)
- [ ] Release notes published with the tag
