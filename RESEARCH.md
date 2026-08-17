# Research Operating Model

## Branch model

```text
main
├── research/A-*
├── research/B-*
├── research/C-*
├── research/D-*
├── research/E-*
├── research/F-*
├── research/G-*
├── research/H-*
├── research/I-*
└── moonshot/*
```

Research branches need not map one-to-one to Git branches forever; the metaphor is enforced through hypotheses, evidence, reviews, and merge decisions.

## Every hypothesis requires

- falsifiable claim
- baseline
- primary metric(s)
- acceptance threshold
- minimum experiment
- confounders / failure modes
- evidence location
- disclosure class
- decision: `OPEN`, `ITERATE`, `PARK`, `CLOSE`, or `MERGE-CANDIDATE`

## Merge review

A merge candidate must answer:

1. Was the hypothesis tested against a stated baseline?
2. Is the result reproducible?
3. Is the effect practically meaningful, not just statistically interesting?
4. What whole-system objectives improved?
5. What regressed?
6. Does the result introduce new safety, regulatory, privacy, or manufacturability risk?
7. Is the implementation safe to disclose publicly?
8. Can the mainline architecture adopt it without relying on an unvalidated dependency?

## Research CI

Every proposed merge reports an objective vector:

```text
phone functionality
AI capability
battery/runtime
weight
thickness
comfort
mechanical durability
skin temperature
RF performance
privacy/security
repairability
manufacturing cost
technology readiness
```

A local improvement that causes unacceptable whole-system regression fails research CI.

## Evidence ladder

- L0 — idea / mechanism
- L1 — literature-supported plausibility
- L2 — simulation or analytic model
- L3 — bench experiment
- L4 — integrated prototype
- L5 — repeated internal replication
- L6 — independent replication / external validation
- L7 — production-relevant validation

Merge thresholds vary by risk. Safety-critical claims require higher evidence than UI/ergonomic claims.

## Rebase rule

When one merged result changes the constraints of another branch, the affected hypothesis is explicitly rebased rather than continuing against an obsolete baseline.
