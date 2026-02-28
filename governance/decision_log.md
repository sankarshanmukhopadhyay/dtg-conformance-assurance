# Decision Log

This log records decisions that change meaning, scope, or requirements.

## Format
Each decision is captured as a short entry referencing the PR and (optionally) the issue.

---

## D-0001 — <Decision title>
- **Date:** YYYY-MM-DD
- **Status:** Proposed | Accepted | Superseded
- **Context:** Why was a decision needed?
- **Decision:** What was decided?
- **Rationale:** Why this choice vs alternatives?
- **Consequences:** What changes for implementers/reviewers?
- **Artifacts impacted:** (files/sheets/schemas)
- **Links:** PR #, Issue #


## 2026-02-28 — Adopt “DCAS Evaluate” method packaging

**Decision:** Package DCAS as a repeatable evaluation workflow (“DCAS Evaluate”) including a versioned method, report template, evidence checklist, and scoring + confidence rubric.

**Rationale:** Improves adoption by turning static artifacts into an executable, assessor-friendly workflow while keeping DCAS implementation-neutral.

**Artifacts:**
- `DCAS_METHOD_VERSION`
- `docs/dcas-evaluate/`
