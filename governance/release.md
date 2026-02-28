# Release checklist

Use this checklist before cutting a tagged release.

## Required artifacts (content)

- [ ] Risk register XLSX updated (if applicable): `risk/source/Risk the referenced artifact (not included in this repo)`
- [ ] Risk export regenerated: `python tools/export_xlsx_to_csv.py`
- [ ] Risk export validated: `python tools/validate_csv.py`
- [ ] Risk → CO mapping reviewed: `the referenced artifact (not included in this repo)`
- [ ] Control objectives reviewed: `the referenced artifact (not included in this repo)`
- [ ] Catalogs updated and internally consistent:
  - [ ] `the referenced artifact (not included in this repo)`
  - [ ] `the referenced artifact (not included in this repo)`
  - [ ] `the referenced artifact (not included in this repo)`
- [ ] Coverage report refreshed: `the referenced artifact (not included in this repo)`
- [ ] Conformance profiles reviewed: `conformance/profiles/`
- [ ] DCAS spec updated (if applicable): `the referenced artifact (not included in this repo)`
- [ ] Evaluation method reviewed + versioned:
  - [ ] `docs/dcas-evaluate/`
  - [ ] `DCAS_METHOD_VERSION`

## Required artifacts (repo hygiene)

- [ ] README updated (routing for new adopters)
- [ ] Roadmap updated: `the referenced artifact (not included in this repo)`
- [ ] Release notes drafted (see `docs/releases/`)
- [ ] Decision log updated (if applicable): `the referenced artifact (not included in this repo)`

## Tagging

- [ ] Version tag created (SemVer)
- [ ] Release notes published with the tag
