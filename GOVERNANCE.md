# Governance

This repository is the working home for DTG WG risk, conformance, and assurance artefacts. The goal is to keep changes reviewable, auditable, and reproducible.

## Roles

### Maintainers
Maintainers are responsible for repository health and decision hygiene.

**Responsibilities**
- Triage issues, apply labels, and manage milestones
- Review and merge PRs into `main`
- Enforce branch protection rules and required checks
- Cut releases/tags for WG milestones
- Maintain the decision log and ensure decisions are captured

**Powers**
- Push protection: Maintainers are the only users allowed to merge to `main`
- May revert PRs when necessary to restore integrity

**Selection**
- Maintainers are nominated by the WG leads and confirmed by consensus in a WG meeting.
- Changes to the Maintainers list must occur via PR.

### Reviewers
Reviewers are domain owners for specific areas (risk, controls, conformance, spec).

**Responsibilities**
- Provide timely review feedback on PRs
- Confirm changes preserve traceability (risk → control → evidence/test)
- Request updates when changes introduce ambiguity or break alignment

### Contributors
Contributors propose changes via issues and PRs.

**Responsibilities**
- Use issue templates to propose additions/changes
- Ensure exports are updated (XLSX → CSV) or rely on CI
- Keep PRs small and focused

## Decision policy

- Technical/editorial decisions are captured via PR + Decision Log entry.
- Breaking changes to schemas, scoring scales, or profile requirements require explicit WG approval and MUST be recorded as a Decision.

## Approval rules (default)

- Minimum: 1 approval from a Maintainer
- If CODEOWNERS applies: 1 approval from a relevant Code Owner
- CI checks must pass prior to merge

## Maintainers

- @dtg-wg-maintainers (team)
- (Add named maintainers here)

## Code Owners

Defined in `CODEOWNERS`.
