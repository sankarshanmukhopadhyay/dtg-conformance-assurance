# Verifier-first workflow (DCAS)

This workflow assumes an issuer has provided a **CSV evidence bundle** that follows the repo’s bundle contract (see `templates/starter-bundle/`).

The verifier goal is to produce a **repeatable, mostly-automatable** decision trail:

**Bundle intake → structural validation → control coverage → evidence checks → decision record**

---

## Inputs

Minimum expected bundle files:

- `bundle_manifest.csv`
- `claims.csv`
- `evidence.csv`
- `mappings_control_evidence.csv`
- `evaluation_results.csv` (issuer self-eval; optional but strongly recommended)

Supporting registries (from this repo):

- `controls/control_objectives.csv` (canonical CO IDs)
- `conformance/assurance_levels.md` (AL semantics)
- The relevant conformance profile under `conformance/profiles/`

---

## Step 1 — Intake + immutability

1. Copy the submitted bundle into a working directory (do not edit in-place).
2. Record:
   - bundle identifier and version (`bundle_manifest.csv`)
   - submission timestamp
   - submitter identity (issuer)

**Recommended automation:** verify `sha256` values in `bundle_manifest.csv` if present.

---

## Step 2 — Structural validation (automated)

Run the repo validator against the bundle contract and schemas:

```bash
pip install -r requirements.txt
make validate
```

What this should catch automatically:
- missing required columns
- invalid enums (e.g., AL values)
- invalid ID-list formatting (semicolon-delimited)
- unknown control objective IDs

---

## Step 3 — Control coverage report (automated)

Generate a deterministic control coverage report:

```bash
make coverage
```

Outputs:
- `risk/reports/coverage/coverage.csv`
- `risk/reports/coverage/coverage.md`

Use these as the verifier’s first-pass “are we even in the ballpark?” lens:
- uncovered COs are explicit and enumerable
- coverage is measurable and comparable across submissions

---

## Step 4 — Evidence checks (mostly automated)

### 4.1 Evidence presence + path integrity
Automate checks that:
- each `artifact_path` exists in the submitted bundle directory, or resolves to a stable external URI
- each `evidence_id` referenced in mappings exists in `evidence.csv`

### 4.2 Evidence-to-control sufficiency (rule-based)
Automate coarse rules:
- each CO required by the selected profile has ≥1 evidence mapping
- higher assurance levels increase expectations (e.g., more “direct” vs “indirect” mappings)

### 4.3 Spot checks (human-in-the-loop)
Keep human review focused on:
- evidence authenticity (signatures, provenance, tamper resistance)
- evidence relevance (does it actually support the CO claim)
- adversarial plausibility (can this be spoofed cheaply)

---

## Step 5 — Decision record (automatable structure)

Produce a verifier decision artifact (CSV or Markdown) that includes:
- bundle ID + version
- profile + target AL
- coverage summary (numbers + uncovered list)
- failed checks with evidence references
- decision outcome: `accept`, `accept-with-conditions`, `reject`

**Strong recommendation:** treat the decision record as an append-only log entry.

---

## Outputs

At minimum, the verifier produces:
- an updated `evaluation_results.csv` row set **owned by the verifier**, or a separate verifier results CSV
- a coverage report (CSV + Markdown)
- a decision record (Markdown or CSV)



## Experimental runtime overlay step

Where the target deployment performs delegated or side-effecting runtime actions, the verifier SHOULD request runtime decision receipts and negative-path evidence for stale-status or missing-policy scenarios.
