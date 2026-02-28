# Annex C — Example Conformance Claims  
**Informative**

## C.1 Purpose

Examples of how ecosystems and actors may express DCAS conformance claims.

## C.2 Human-readable example (Issuer)

**Actor:** did:example:issuer:bank-001  
**Actor class:** Issuer  
**Profile:** CP-1 (Credential Issuer Profile)  
**Assurance level:** AL3  
**Controls:** CO3.1, CO3.2, CO3.3  
**Evidence:** Signed issuance logs; assessor attestation  
**Tests:** Sample audit of issued credentials

## C.3 Human-readable example (Verifier)

**Actor:** did:example:verifier:org-001  
**Actor class:** Verifier  
**Profile:** CP-2 (Verifier Profile)  
**Assurance level:** AL2  
**Controls:** CO3.4  
**Evidence:** Verification logs; policy config snapshots  
**Tests:** Log analysis and spot checks

## C.4 Machine-readable examples (YAML)

See:
- `an implementer-supplied artifact appropriate to your context (e.g., risk register entry, test evidence, or approval record).`
- `an implementer-supplied artifact appropriate to your context (e.g., risk register entry, test evidence, or approval record).`

## C.5 Disclosure expectation

Actors SHOULD downgrade AL or profile claim where required evidence/tests cannot be produced at the claimed rigor.
