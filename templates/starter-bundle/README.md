# Starter evidence bundle (CSV)

This folder is a **copy/paste starting point** for issuers to build a DCAS evidence bundle.

## Files

- `bundle_manifest.csv` — index of the bundle contents (what’s included)
- `claims.csv` — conformance + assurance claims being asserted
- `risks.csv` — risk snapshot used for evaluation
- `evidence.csv` — evidence catalog (each entry references a real artifact)
- `mappings_control_evidence.csv` — trace links from control objectives to evidence
- `evaluation_results.csv` — self-evaluation outputs

## Conventions

- IDs are stable and human-readable (e.g., `CLM-0001`, `EVID-0001`).
- Use `;` to separate multiple IDs in a single cell (e.g., `CO1.4; CO1.1`).
- Extensions are allowed via `x_*` columns (e.g., `x_ticket_url`).

## Next steps

1. Copy this folder into your implementation repo.
2. Replace example IDs/rows with your real data.
3. Add real artifacts under `artifacts/` (or use stable URIs).
4. Run `make validate` from the repo root to ensure the bundle is structurally valid.
