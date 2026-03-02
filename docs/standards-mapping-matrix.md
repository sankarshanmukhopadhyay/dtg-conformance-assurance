---
title: Standards mapping matrix
---

# Standards mapping matrix (control objectives ↔ ISO/NIST/OWASP/etc)

This repo includes a **control objectives catalog** in `controls/control_objectives.csv`. To make adoption and procurement easier, the project also provides a **suggested standards mapping matrix**:

- **Machine-readable:** `controls/standards_mapping_matrix.csv`
- **Human-readable guidance (this page):** `docs/standards-mapping-matrix.md`

## What this matrix is (and is not)

- It **is** a practical crosswalk: “If you already use ISO/NIST/OWASP, where do these control objectives *roughly* land?”
- It is **not** a certification claim, and it is **not** a substitute for your organization’s formal compliance mapping.

All mappings are **non-normative** and should be treated as *starting hypotheses* for implementation teams and auditors.

## How to use it

1. Pick the control objectives you are implementing (by `control_objective_id`).
2. Use the matrix to identify which external standards/policies your organization cares about.
3. Capture your local decisions as “evidence”: why you consider the objective satisfied and what proof you retain.
4. If you need strict compliance, replace “theme-level” mappings with **your organization’s official control IDs**.

## Column notes

- **ISO/IEC 27001/27002 alignment (themes):** Uses **control themes** (not numeric IDs) to avoid false precision.
- **NIST CSF alignment:** Mapped at the **function level** (Govern/Identify/Protect/Detect/Respond/Recover).
- **NIST AI RMF alignment:** Mapped at the **function level** (Govern/Map/Measure/Manage).
- **OWASP ASVS / SAMM:** Mapped at a **section/practice level** to support engineering teams.
- **SLSA/OpenSSF:** Included where objectives touch software supply chain integrity.

## Extending the matrix

If your ecosystem has additional upstream requirements (e.g., sector regulations, procurement rules, national AI policy), extend the CSV with additional columns and keep the mapping notes explicit.
