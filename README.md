# DTG Conformance & Assurance (DCAS)

**Release:** v0.10.0  \
**Last reviewed:** 2026-07-03

This repository publishes **DCAS (Decentralized Conformance and Assurance Standard)** artifacts for DTG ecosystems.

DCAS is an implementation-neutral way to move from implicit trust to **explicit, reviewable, risk-proportionate claims**.

## Status

- **Primary goal (this repo):** make DCAS *operational* — templates, schemas, and a repeatable evaluation method.
- **Spec:** `spec/DCAS_v0.1.md` is a **draft** (contains TODOs). Templates + validation tooling are treated as the stable “adoption surface”.
- **AIS-1 v0.2 integration:** present as an **experimental** assurance profile for bounded evaluation, not as a settled production trust profile.

## Ecosystem & related repositories

DCAS is designed to work with:

- **`trust-systems-meta-model`:** semantic governance model for authority, delegation, evidence, lifecycle state, trust decisions, runtime governance, and operational effects.
- **`trust-infrastructure-schemas` (OTAM implementation):** canonical trust artifact schemas, the normative AL model (`assurance/assurance-levels.md`), and the v0.10 runtime assurance artifact contracts.
- **Domain baselines (example: `agent-name-assurance-baseline`):** domain-specific requirements that emit declarations and evidence bundles.
- **This repo (DCAS):** evaluates those declarations and evidence using a repeatable verifier workflow.

Start with: `docs/ecosystem-overview.md`, `docs/compatibility-matrix.md`, `docs/tsmm-runtime-governance-evaluation-profile.md`, `docs/tis-v0.10-runtime-assurance-evaluation-profile.md`, `docs/ais1-experimental-assurance-profile.md`, `docs/a2a-assurance-profile.md`, and `docs/anab-a2a-evaluation.md`.


## TSMM/TIS v0.10 runtime assurance alignment

DCAS v0.9.0 adds evaluator-facing alignment for TSMM runtime governance and TIS v0.10 runtime assurance artifacts. The key rule is boundary discipline: TSMM owns semantic governance meaning; TIS owns canonical schema contracts; DCAS evaluates whether the artifacts are sufficient evidence for a specific assurance decision.

- TSMM evaluation profile: `docs/tsmm-runtime-governance-evaluation-profile.md`
- TIS v0.10 evaluation profile: `docs/tis-v0.10-runtime-assurance-evaluation-profile.md`
- Legacy TIS v0.9 profile: `docs/tis-v0.9-runtime-artifact-evaluation-profile.md`
- Drift review process: `docs/tis-drift-review.md`
- Portfolio drift review: `docs/portfolio-drift-review-tis-v0.10.md`
- Machine-readable compatibility review: `model/tis-compatibility-review.json`
- Worked example claim: `conformance/examples/tis_v0_10_runtime_assurance_evaluation_claim.example.yaml`
- Known-good stack: `docs/known-good-stack.md`



## Start here

- **Adoption guide (role-based):** `docs/start-here.md`
- **Repository map:** `docs/repo-map.md`
- **FAQ:** `docs/FAQ.md`
- **Verifier workflow:** `docs/verifier-workflow.md`

## Documentation site (GitHub Pages)

This repo is structured so it can be published via **GitHub Pages** from the `/docs` folder.

- Entry point: `docs/index.md`
- Recommended Pages source: **Deploy from a branch → `/docs` folder**


## A2A alignment

This repo includes an explicit **A2A-facing assurance surface** for agent ecosystems.

- **New A2A profile:** `conformance/profiles/CP-7_A2AAgent.md`
- **A2A assurance guidance:** `docs/a2a-assurance-profile.md`
- **A2A example claim:** `conformance/examples/a2a_agent_conformance_claim.example.yaml`

The intent is simple: A2A handles communication. DCAS evaluates whether an A2A agent is trustworthy enough to rely on in production.

### ANAB-over-A2A impact

ANAB now publishes a detailed **ANAB-over-A2A description extension** plus new A2A-oriented controls (`ANAGB-A2A-07` through `ANAGB-A2A-10`). DCAS therefore needs to evaluate not only generic Agent Card integrity, but also:

- operator-to-card coherence
- issuer and trust-anchor disclosure
- freshness and revocation semantics
- downgrade-safe handling when the extension is absent, stale, or unverifiable

This impact is documented in `docs/anab-a2a-evaluation.md` and illustrated in `conformance/examples/anab_over_a2a_evaluation_claim.example.yaml`.

## Experimental AIS-1 v0.2 integration

This repo includes an **experimental AIS-1 v0.2 assurance profile** so DCAS can evaluate AIS-1 as a bonded identity and accountability substrate without overstating it as a complete trust execution layer.

- **Experimental profile:** `conformance/profiles/CP-8_AIS1Experimental.md`
- **Guidance note:** `docs/ais1-experimental-assurance-profile.md`
- **Example claim:** `conformance/examples/ais1_experimental_evaluation_claim.example.yaml`

The evaluation posture is intentionally narrow:
- bond is not delegation
- tier is not full assurance
- verification is not provenance
- SOA status requires parent ALA status validation
- parent ALA revocation should cause SOA downgrade or denial

Use this profile when you need a reviewable decision about whether an AIS-1 v0.2 surface is coherent enough to consume as an accountability input. Do not treat it as a standalone production recommendation.

## OASF publication composition

This repo now includes a small OASF-facing handoff so OASF-described agents can be evaluated under DCAS without flattening discovery metadata into ad hoc local fields.

- Integration note: `docs/oasf-integration.md`
- Envelope schema: `spec/schemas/dcas-oasf-evaluation-envelope.schema.json`
- Example envelope: `conformance/examples/oasf_evaluation_envelope.example.json`
- OASF ↔ ANAB ↔ DCAS mapping table: `controls/oasf_control_mappings.csv`

## Cross-repo composition

This repo includes a concrete composition pack for evaluating a downstream baseline such as ANAB without collapsing its control namespace into DCAS-local labels too early.

- Composition note: `docs/domain-baseline-composition.md`
- Example evaluation claim: `conformance/examples/anab_evaluation_claim.example.yaml`

## Methodology and ecosystem context

- Methodology: `docs/methodology.md`
- Standards & policy references: `docs/standards-and-policies.md`

DCAS is designed to interoperate with other trust-infrastructure repositories (e.g., trust registries, conformance suites, assurance hubs). This repository focuses on the **portable artifact layer**: profiles, assurance levels, control objectives, evidence templates, and evaluation guidance.


## Golden path (issuer-first)

1. Copy the starter bundle: `templates/starter-bundle/`
2. Populate CSVs with your real IDs, risks, evidence, and results
3. Attach real evidence artifacts (or stable URIs)
4. Validate structure:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
make validate
```

Generate a deterministic control coverage report:

```bash
make coverage
```

## Key artifacts

- **Control objectives (CSV):** `controls/control_objectives.csv`
- **Risk register export (CSV):** `risk/exports/risk_assessment.csv`
- **CSV schema descriptors (machine-readable):** `schemas/csv/` (see `schemas/csv/index.json`)
- **Risk → control mapping (CSV):** `risk/mapping/risk_to_control_objectives.csv`
- **Conformance profiles:** `conformance/profiles/`
- **Assurance level definitions:** `conformance/assurance_levels.md`
- **Evaluation method:** `docs/dcas-evaluate/README.md`

## Contributing

See `CONTRIBUTING.md`. CI enforces mechanical correctness (CSV structure + markdown link integrity).


## Standards

**Standards mapping matrix:** see `controls/standards_mapping_matrix.csv` and `docs/standards-mapping-matrix.md`.

## Ecosystem interoperability

See `docs/ecosystem-interoperability.md` and `docs/architecture.md` for how this repo composes with DTG Labs upstream work (`dtg-credentials`, `verifiable-trust-infrastructure`, `openVTC`).


## Experimental agent runtime governance overlay

This release adds an **experimental** runtime-governance overlay informed by the Microsoft Agent Governance Toolkit as an upstream reference. The overlay adds portable control objectives, evidence expectations, and a runtime decision receipt pattern for systems that need to prove what happened **at execution time**, without changing the stable DCAS method core.
