# AIS-1 experimental assurance profile

DCAS includes an **experimental** AIS-1 profile so implementers and verifiers can assess AIS-1 as a bounded identity-and-accountability substrate without overstating what it proves.

## Why this profile exists

The integration objective is practical: make AIS-1 testable within DCAS as a profiled substrate for:

- DID format and resolution checks
- bond integrity validation
- issuer or trust-anchor disclosure
- lifecycle evidence such as active, suspended, or revoked state
- evidence completeness and traceability

This follows the AIS-1 integration plan’s DCAS expectation to define conformance checks, lifecycle checks, evidence requirements, and assurance outputs. The profile is intentionally narrow so DCAS can test AIS-1 without implying production maturity or complete trust semantics.

## Experimental status

This profile is experimental for a reason.

AIS-1 is useful to DCAS as a comparative and evaluative surface, but it is not treated here as a complete production trust execution layer. DCAS therefore preserves four boundaries:

- bond is not delegation
- tier is not full assurance
- verification is not provenance
- identity linkage does not by itself establish runtime authorization

## What DCAS evaluates

The profile is documented at [CP-8 AIS-1 Experimental Bonded Agent](../conformance/profiles/CP-8_AIS1Experimental.md).

A DCAS verifier using this profile evaluates whether:

1. a `did:ais1` identifier is syntactically valid and resolvable
2. the agent-to-sponsor bond is present and verifiable
3. issuer or trust-anchor context is disclosed well enough for policy evaluation
4. lifecycle state is externally checkable
5. evidence is complete, traceable, and repeatable
6. the implementation clearly discloses the profile’s current limitations

## Example claim

See the worked example at [AIS-1 experimental evaluation claim](../conformance/examples/ais1_experimental_evaluation_claim.example.yaml).

## How to rely on it

For exploratory and bounded use, this profile can support a reviewable decision about whether an AIS-1 surface is coherent enough to consume as an accountability input.

For higher-risk use, verifiers should combine this profile with separate evidence for:

- delegated authority
- runtime authorization and policy enforcement
- provenance and transport integrity
- operational controls beyond identity binding
