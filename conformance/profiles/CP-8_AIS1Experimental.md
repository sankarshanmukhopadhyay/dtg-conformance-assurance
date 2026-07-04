# CP-8 AIS-1 v0.2 Experimental Bonded Agent

**Status:** Experimental

**Purpose:** evaluate an AIS-1 v0.2-described agent as an experimental bonded identity and accountability substrate without overstating it as a complete delegation, runtime authorization, or provenance layer.

## What this profile is for

Use this profile when an implementation exposes an AIS-1-style agent identity surface that includes:

- a `did:ais1` identifier
- `agentClass` set to `ala` or `soa`
- `parentDid` for subordinate operating agents
- a sponsor-backed bond or equivalent accountability linkage
- issuer or trust-anchor metadata
- lifecycle state such as active, suspended, or revoked
- DID resolution and registry status evidence
- optional `timestampServiceRef`
- optional Assurance Container reference
- evidence references for bond issuance, verification, and status changes

This profile is designed to help verifiers assess whether the AIS-1 surface is coherent enough to consume as an **identity and accountability input**.

It is **not** a claim that AIS-1 is a complete trust execution stack.

## Experimental boundary conditions

This profile is intentionally constrained.

- **Bond is not delegation.**
- **Tier is not full assurance.**
- **Verification is not provenance.**
- **Identity linkage does not by itself prove runtime authorization.**
- **SOA status is not sufficient unless the parent ALA is active.**
- **Parent ALA revocation should cause SOA downgrade or denial.**

Verifiers should therefore treat AIS-1 evidence as a bounded trust signal and require additional delegation, policy, and provenance artifacts for higher-risk use.

## Mandatory control objectives

- **CO3.1** Identity binding
- **CO3.2** Delegation constraints
- **CO3.3** Lifecycle governance
- **CO4.1** Evidence completeness
- **CO4.2** Traceability
- **CO4.3** Testability
- **CO4.4** Repeatability
- **CO5.1** Disclosure baseline
- **CO5.2** Change disclosure
- **CO6.2** Key management
- **CO6.3** Monitoring & response
- **CO3.9** AIS-1 SOA parent-chain validation
- **CO4.8** AIS-1 v0.2 evidence sufficiency
- **CO6.6** AIS-1 cascade revocation handling

## Minimum assurance level

- **AL1** for exploratory or lab use
- **AL2** when an AIS-1 surface is consumed across organizational boundaries as an accountability input
- **AL3** only when AIS-1 evidence is combined with separate delegation, policy, and operational controls

## Minimum verifier checks

A verifier using this profile should confirm at minimum:

1. **DID format and resolution**
   - `did:ais1` syntax is valid
   - resolution path is documented or reproducible
2. **Bond integrity**
   - bond exists and links agent to sponsor
   - bond status is current and verifiable
   - bond hash or equivalent integrity check is reproducible
3. **Agent class and parent state**
   - ALA records have no parent DID
   - SOA records include parent DID
   - parent ALA status is current and active before relying on the SOA
4. **Issuer / trust-anchor disclosure**
   - issuer or trust-anchor basis is disclosed
   - verifier can determine whether the issuer is recognized in policy
5. **Lifecycle state**
   - active, suspended, or revoked status can be determined
   - status transitions are logged
   - SOA cascade revocation behavior is tested where `agentClass` is `soa`
6. **Timestamp and assurance evidence**
   - `timestampServiceRef` is interpreted as supporting evidence only
   - Assurance Container references are versioned and traceable where claimed
7. **Evidence traceability**
   - bond issuance, status checks, and verification results are trace-linked to evidence
8. **Limitations disclosure**
   - the implementation discloses that AIS-1 does not by itself provide delegated authority or message provenance

## Typical evidence

- Bond issuance artifact or contract event reference
- DID method documentation or resolver output
- Sponsor metadata and accountability disclosure
- Issuer or trust-anchor registry entry
- ALA/SOA class evidence and parent DID evidence where applicable
- Parent ALA status check for SOA evaluations
- Revocation or suspension evidence
- Cascade revocation negative-path test evidence
- Timestamp service evidence where claimed
- Assurance Container reference where claimed
- Verification logs showing repeated verifier outcomes
- Key rotation or key custody evidence where applicable
- Plain-language relying-party disclosure text

## Typical outcomes

### Pass
The AIS-1 surface is coherent as an experimental identity and accountability input. Evidence is complete enough for bounded use.

### Conditional pass
The AIS-1 surface is structurally usable, but issuer recognition, lifecycle evidence, or disclosure remains incomplete.

### Fail
The verifier cannot establish bond integrity, current lifecycle state, or reproducible evidence traceability.

## Notes

This profile exists to make AIS-1 testable inside DCAS while preserving the correct maturity signal. It should be read as an **experimental assurance profile**, not a settled production recommendation.
