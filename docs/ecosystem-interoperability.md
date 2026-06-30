# Ecosystem interoperability

This repository is designed to compose with upstream DTG Labs projects. The objective is **interoperability by construction**: clear role boundaries, explicit assumptions, and traceable artifacts.

## Upstream projects in scope

- **dtg-credentials**: credential schemas and issuance/verifier semantics used by ecosystem implementations.
- **verifiable-trust-infrastructure**: reference architecture and operational building blocks for verifiable trust ecosystems.
- **openVTC**: reference implementation patterns and tooling for deploying and operating verifiable trust components.

## Compatibility model

This repository provides the **assurance and conformance layer**. The upstream repos provide **ecosystem architecture, credential semantics, and implementation surfaces**.

### What composes cleanly

- Use *dtg-credentials* as a credential schema substrate and map credential families to this repo’s data structures and assurance expectations.
- Use *verifiable-trust-infrastructure* to describe system architecture; use this repo to define how that architecture is assessed (controls, evidence, evaluation workflows).
- Use *openVTC* as a reference deployment surface for validating conformance and evidence collection patterns.

### What is explicitly out of scope

- This repo does not define new VC data model semantics beyond what is required for assurance artifacts.
- This repo does not attempt to be a certification program or an authority.
- This repo does not ship production-grade infrastructure components (that’s where openVTC and VTI fit).

## Transport alignment

Interoperability depends on a transport substrate for secure, privacy-preserving exchange of messages and artifacts between endpoints. This repo aligns with the **Trust Spanning Protocol (TSP)** from ToIP as a candidate transport layer for these exchanges.

See: https://trustoverip.github.io/tswg-tsp-specification/


## Experimental AIS-1 composition

DCAS can also compose with AIS-1 as an **experimental** identity-and-accountability substrate.

In this repo, that means DCAS evaluates whether an AIS-1 surface is sufficiently coherent to consume as a bounded trust input:
- `did:ais1` identifiers are testable
- agent-to-sponsor bond integrity is reviewable
- issuer or trust-anchor disclosure is available for policy decisions
- lifecycle state is externally checkable

This composition is intentionally limited. AIS-1 is not treated here as a full delegation, provenance, or execution-layer trust protocol.

## TSMM/TIS v0.10 runtime assurance alignment

DCAS v0.9.0 aligns with TSMM v0.21.0 and TIS v0.10.0 by consuming runtime governance and runtime assurance artifacts as evaluation evidence.

The intended control-plane flow is:

1. TSMM defines the semantic governance model for actor, authority, delegation, evidence, decision, lifecycle state, and effect.
2. TIS defines the canonical machine-validatable artifact shape.
3. DTG/OpenVTC/VTI systems produce runtime artifacts.
4. DCAS evaluates whether the artifacts are sufficient for a declared assurance level and relying-party context.
5. Domain baselines such as ANAB preserve their own control namespace while referencing the same evidence surface.

This makes governance executable without turning DCAS into a schema registry or implementation repository.

See also:

- `tsmm-runtime-governance-evaluation-profile.md`
- `tis-v0.10-runtime-assurance-evaluation-profile.md`
- `tis-v0.9-runtime-artifact-evaluation-profile.md`
- `tis-drift-review.md`
- `tis-dcas-anab-alignment-matrix.md`
