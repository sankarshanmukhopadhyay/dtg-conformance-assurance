# ANAB-over-A2A evaluation guidance

## Why this document exists

ANAB now defines a detailed **ANAB-over-A2A description extension** and extends its normative catalog with controls `ANAGB-A2A-07` through `ANAGB-A2A-10`. That changes what DCAS has to look at when it evaluates an A2A-deployed named agent.

The old posture was mostly transport and endpoint assurance:

- Is the Agent Card authentic?
- Are task flows scoped correctly?
- Are callbacks, webhooks, and artifacts safe to consume?

The new posture adds a second layer:

- Is the published ANAB trust description actually bound to the accountable operator?
- Is the verifier told who issued or anchored a verified identity state?
- Are freshness, expiry, and revocation semantics explicit?
- Does the client fail safely when ANAB trust metadata is absent, stale, or unsupported?

## Evaluation model

DCAS SHOULD treat the ANAB-over-A2A extension as a **trust input** attached to the A2A interaction surface. It is not itself an authorization grant. It is evidence-bearing metadata that a verifier can evaluate before accepting the agent for consequential use.

### Inputs DCAS SHOULD collect

1. The A2A Agent Card as published to relying parties
2. The ANAB declaration referenced from the extension
3. The evidence bundle referenced from the extension, where present
4. The card-binding material, such as a JWKS, DID document, or registry entry
5. The identity-verification or trust-anchor endpoint, where a verified status is claimed
6. Local verifier policy describing whether ANAB processing is optional or required for the transaction class

## Mapping ANAB controls into DCAS evaluation posture

| ANAB control | DCAS evaluation concern | Typical verifier question |
| --- | --- | --- |
| `ANAGB-A2A-07` | Card and operator coherence | Does the card-binding method actually link the published card to the accountable operator named in ANAB? |
| `ANAGB-A2A-08` | Issuer and trust-anchor disclosure | Can the verifier identify who issued the identity state and under what policy it should be interpreted? |
| `ANAGB-A2A-09` | Freshness and revocation | Are issued-at, expiry, cache rules, and revocation checks explicit and operationally testable? |
| `ANAGB-A2A-10` | Downgrade-safe handling | Does the relying system fail safely when the extension cannot be processed or validated? |

## Recommended DCAS evidence additions

In addition to the normal A2A evidence starter pack, evaluators SHOULD request:

- sample Agent Cards carrying the ANAB extension
- proof that `agentName.displayName`, Agent Page content, and ANAB declaration naming are materially consistent
- card-signing or card-binding verification material
- issuer or registry evidence for externally verified identity status
- revocation and expiry test results
- downgrade tests showing that clients do not silently upgrade trust from partial metadata

## Practical decision rule

A verifier SHOULD distinguish three separate questions:

1. **Can the agent talk to me?** A2A interoperability
2. **Can I identify and name the agent reliably?** ANAB naming and operator binding
3. **Should I rely on the agent for this transaction?** DCAS evaluation under local policy

Keeping those layers separate is the point of the stack.
