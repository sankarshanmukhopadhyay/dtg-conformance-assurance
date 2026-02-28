# Contributing

DCAS is intended to be **operational**: artifacts should be mechanically verifiable and easy to adopt.

## What to contribute

- Improvements to adopter workflows (`docs/` and `templates/`)
- Control objectives and mappings (`controls/`, `risk/mapping/`)
- Conformance profiles and examples (`conformance/`)
- Tooling and validation improvements (`tools/`)
- Spec edits (`spec/`) — note: draft status, keep changes scoped and testable

## Contribution workflow

1. File an issue using the templates under `.github/ISSUE_TEMPLATE/`
2. Create a branch (e.g., `draft/risk-G12-revocation-latency`)
3. Make changes and run validation:

```bash
pip install -r requirements.txt
make validate
```

4. Open a PR with:
   - a short problem statement
   - acceptance criteria
   - any migration notes if you changed templates or IDs

## Conventions

- **CSV-first** for templates and mappings
- Stable IDs (e.g., `CO1.4`, `EVID-0007`)
- Extensions allowed via `x_*` columns without breaking the core contract
