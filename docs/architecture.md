# Architecture snapshot

This diagram is a **non-normative** view of how this repository composes with DTG Labs upstream work and the ToIP Trust Spanning Protocol (TSP).

```mermaid
flowchart TB
  subgraph A[Assurance and Conformance Layer]
    S["Trust Infrastructure Schemas (OTAM)"]
    D[DCAS]
    N[ANAB]
    S --> D --> N
  end

  subgraph T[Transport]
    TSP[ToIP Trust Spanning Protocol]
  end

  subgraph C[Credential Semantics]
    DC[dtg-credentials]
  end

  subgraph I[Ecosystem Architecture]
    VTI[verifiable-trust-infrastructure]
  end

  subgraph R[Reference Implementations]
    O[openVTC]
  end

  %% Typical dependency direction
  DC --> VTI --> O

  %% Transport adjacency (non-normative)
  N -. "trust tasks over transport" .- TSP
  DC -. "artifact exchange over transport" .- TSP

  %% Interop touchpoints (non-normative)
  S -. "trust artifact schemas" .- DC
  D -. "assurance profiles" .- VTI
  N -. "identifier trust tasks" .- O
```

## Notes

- Solid arrows represent a typical dependency direction.
- Dotted edges represent interoperability touchpoints (mapping, evaluation, integration), not hard dependencies.
- The transport layer is shown as an adjacency to highlight where secure message exchange is expected to occur.

## Executable evidence intake (experimental)

The draft Trust Tasks suite owns execution and emits run provenance and vector outcomes. An assessor-controlled DCAS adapter consumes these records into the normalized evaluator, which emits per-requirement findings. This is an informative evidence relationship, not a normative dependency or runtime authority grant. See [integration guide](tt-conformance-evidence-integration.md).
