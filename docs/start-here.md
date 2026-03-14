# Start here: adopting DCAS for DTG ecosystems

DCAS gives you a practical “traceability spine”:

**Risks → Control Objectives → Evidence → Evaluation outcome**

This repo is **issuer-first**: the fastest path to adoption is producing a consistent evidence bundle that others can verify.

## 30-minute onboarding (issuer)

1. **Pick a profile**
   - Start with `conformance/profiles/CP-1_Issuer.md`

2. **Pick an assurance level**
   - Read `conformance/assurance_levels.md` (AL1–AL4)

3. **Start from templates**
   - Copy `templates/starter-bundle/` into your implementation and replace example rows with real ones.

4. **Map risks to control objectives**
   - Use `risk/mapping/risk_to_control_objectives.csv` and `controls/control_objectives.csv` as your baseline.

5. **Run a self-evaluation**
   - Document results in `evaluation_results.csv` (pass/partial/fail + evidence links)

6. **Validate (automated)**
```bash
pip install -r requirements.txt
make validate
```

7. **Generate a coverage report (automated)**
```bash
make coverage
```
This produces `risk/reports/coverage/coverage.csv` and `risk/reports/coverage/coverage.md` using the canonical control objective registry and the upstream OTAM-aligned assurance model.

## Next paths (other roles)

- **Verifier:** follow `docs/verifier-workflow.md` for an intake → validation → coverage → decision pipeline.
- **Auditor/assessor:** see `docs/roles/auditor-assessor.md` for a repeatable sampling approach.
- **Tool builder:** see `docs/roles/tool-builder.md` for automation patterns.
