# TIS drift review process

**Status:** Active synchronization process for DCAS v0.9.0
**Aligned TIS release:** v0.10.0
**Last reviewed:** 2026-06-29

## Purpose

This process tells DCAS maintainers when a change in `trust-infrastructure-schemas` requires a local DCAS review. The goal is to keep DCAS aligned with TIS without copying TIS schemas or silently changing DCAS evaluation semantics.

## Source of truth

DCAS tracks TIS through:

- TIS release notes;
- TIS `model/cross-repo-compatibility-matrix.json`;
- TIS schemas under `credentials/`, `profiles/`, `decision/`, `evidence/`, and `common/`;
- TIS documentation for DTG/OpenVTC/VTI interoperability;
- the local manifest at `../model/tis-compatibility-review.json`;
- portfolio drift review records such as `portfolio-drift-review-tis-v0.10.md`;
- release impact records such as `release-impact-v0.9.0.md`.

## Drift triggers

Open a DCAS drift review when any of the following changes upstream:

- new or renamed TIS schema `$id`;
- new DTG, OpenVTC, or VTI artifact family;
- changed artifact authority surface;
- changed revocation, expiry, delegation, or scope semantics;
- changed decision receipt or evidence bundle manifest structure;
- changed assurance-level guidance;
- changed TSMM runtime governance projection semantics;
- changed Trust Task lifecycle or execution receipt semantics;
- changed status-list, revocation, suspension, expiry, or activation semantics;
- changed evidence bundle integrity, digest, detached proof, or signature metadata;
- changed registry publication profile semantics;
- upstream DTG/OpenVTC/VTI implementation change that alters artifact shape or evidence meaning.

## Portfolio drift classification

Use the portfolio change-management classifications when recording a review:

| Classification | DCAS interpretation |
|---|---|
| Documentation drift | README, onboarding, compatibility, or evaluator guidance needs refresh. |
| Artifact drift | Schema, example, evidence output, decision receipt, registry publication, or fixture expectations changed. |
| Assurance drift | Assurance-level interpretation, control mapping, receipt expectation, status freshness, or evidence integrity expectation changed. |
| Standards drift | External standard or binding reference changed and requires crosswalk or policy update. |

## Review record

Each review SHOULD produce a machine-readable or issue-trackable record with these fields:

```json
{
  "drift_review_id": "dcas-tis-drift-YYYYMMDD-001",
  "source_repo": "trust-infrastructure-schemas",
  "source_version": "v0.10.0",
  "affected_dcas_controls": [],
  "affected_examples": [],
  "assurance_impact": "none | additive | breaking",
  "required_action": "none | docs | examples | validation | release",
  "review_status": "open | aligned | blocked"
}
```

## Decision rules

- If TIS adds a new artifact family, DCAS SHOULD add evaluation guidance only when that artifact can affect control objectives, evidence sufficiency, or assurance level interpretation.
- If TIS changes schema shape without changing evidence meaning, DCAS MAY update examples and validation notes without changing controls.
- If TIS changes authority, delegation, revocation, or enforcement semantics, DCAS MUST review the evaluation profile and compatibility matrix.
- If TIS changes the assurance-level model, DCAS MUST not redefine AL semantics locally. The repo should update references and examples to consume the canonical model.

## Cadence

DCAS SHOULD review TIS drift:

- before every DCAS minor release;
- when TIS publishes a minor release;
- when DTG/OpenVTC/VTI upstreams introduce runtime evidence changes;
- at least monthly while the DTG/OpenVTC/VTI profiles remain experimental.

## Output expectations

A completed drift review updates one or more of:

- `../model/tis-compatibility-review.json`;
- `compatibility-matrix.md`;
- `tis-v0.10-runtime-assurance-evaluation-profile.md`;
- `tsmm-runtime-governance-evaluation-profile.md`;
- examples under `../conformance/examples/`;
- release notes under `releases/`.
