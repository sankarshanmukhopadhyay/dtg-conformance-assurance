# Standards and policy references

This repo is intentionally implementation-neutral, but DCAS artifacts often need anchoring in recognized standards and policy requirements.

This document provides a practical reference map so adopters can cite upstream sources consistently.

## How to use this document

- Treat **Normative** references as “may be required if your ecosystem claims alignment”.
- Treat **Informative** references as “recommended reading / design guidance”.
- If your profile or assurance level depends on a standard, cite it explicitly in the profile and identify what is required vs optional.

## Normative references (commonly applicable)

### Identity, credentials, and cryptography

- **W3C Verifiable Credentials Data Model** — for credential structure and proof mechanisms (when DCAS claims reference VC artifacts).
- **W3C Decentralized Identifiers (DIDs)** — for identifier formats and DID resolution expectations.
- **IETF JOSE / JWT** — when claims or evidence include JWT-based artifacts.
- **IETF COSE** — when constrained environments use COSE structures.

### Software and supply chain integrity (for tooling and pipelines)

- **SLSA** (Supply-chain Levels for Software Artifacts) — when evidence includes build provenance for evaluators/verifiers.
- **OpenSSF best practices** — when toolchain assurance is part of the claim boundary.

### Conformity assessment vocabulary (for consistent language)

- **ISO/IEC 17000** — terminology for conformity assessment concepts (useful when formalizing evaluator roles).
- **ISO/IEC 17020 / 17021 / 17025** — if an ecosystem uses inspection bodies, management system certification, or testing labs.

> Note: ISO standards are copyrighted; cite the standard identifiers and relevant clauses, but don’t reproduce the text.

## Policy-aligned references (often used by adopters)

- **NIST AI RMF 1.0** — when DCAS is used to structure AI governance evidence or assurance claims.
- **OECD AI Principles** — when public-sector programs require broad policy alignment.

## Informative references (strongly recommended)

- **NIST CSF** — for organizational security posture framing.
- **ISO/IEC 27001 / 27002** — for information security controls; frequently used as a control library input.
- **OWASP ASVS / SAMM** — for application security verification and software assurance maturity.
- **OpenTelemetry** — for observability evidence patterns (logs, traces, metrics) when runtime verification is relevant.

## Where these references show up in this repo

- **Profiles** should list the standards that constrain the claim’s scope and evidence expectations.
- **Assurance levels** may reference evaluation rigor expectations that are aligned to conformity assessment practices.
- **Templates** should include fields for recording the upstream standard/policy identifier and the clause/control mapping.

## Planned enhancements

- Add an explicit mapping matrix: DCAS control objectives → common upstream standards clauses, with “starter defaults” vs ecosystem-specific overlays.
