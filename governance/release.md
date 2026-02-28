# Release checklist

Use this checklist before cutting a tagged release.

## Required artifacts (content)

- [ ] Risk register XLSX updated (if applicable): `risk/source/Risk an implementer-supplied artifact appropriate to your context (e.g., risk register entry, test evidence, or approval record).`
- [ ] Risk export regenerated: `python tools/export_xlsx_to_csv.py`
- [ ] Risk export validated: `python tools/validate_csv.py`
- [ ] Risk → CO mapping reviewed: `an implementer-supplied artifact appropriate to your context (e.g., risk register entry, test evidence, or approval record).`
- [ ] Control objectives reviewed: `an implementer-supplied artifact appropriate to your context (e.g., risk register entry, test evidence, or approval record).`
- [ ] Catalogs updated and internally consistent:
  - [ ] `an implementer-supplied artifact appropriate to your context (e.g., risk register entry, test evidence, or approval record).`
  - [ ] `an implementer-supplied artifact appropriate to your context (e.g., risk register entry, test evidence, or approval record).`
  - [ ] `an implementer-supplied artifact appropriate to your context (e.g., risk register entry, test evidence, or approval record).`
- [ ] Coverage report refreshed: `an implementer-supplied artifact appropriate to your context (e.g., risk register entry, test evidence, or approval record).`
- [ ] Conformance profiles reviewed: `conformance/profiles/`
- [ ] DCAS spec updated (if applicable): `an implementer-supplied artifact appropriate to your context (e.g., risk register entry, test evidence, or approval record).`
- [ ] Evaluation method reviewed + versioned:
  - [ ] `docs/dcas-evaluate/`
  - [ ] `DCAS_METHOD_VERSION`

## Required artifacts (repo hygiene)

- [ ] README updated (routing for new adopters)
- [ ] Roadmap updated: `an implementer-supplied artifact appropriate to your context (e.g., risk register entry, test evidence, or approval record).`
- [ ] Release notes drafted (see `docs/releases/`)
- [ ] Decision log updated (if applicable): `an implementer-supplied artifact appropriate to your context (e.g., risk register entry, test evidence, or approval record).`

## Tagging

- [ ] Version tag created (SemVer)
- [ ] Release notes published with the tag
