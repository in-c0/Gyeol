# Public Research & IP Policy

Gyeol is research-in-public, not implementation-in-public by default.

## PUBLIC — default for research process

May include:

- research questions and falsifiable hypotheses
- literature reviews
- benchmark definitions
- high-level architecture
- experimental methods where disclosure is safe
- negative results and failures
- non-sensitive datasets
- aggregate measurements
- reviewed decisions
- papers after disclosure review

## EMBARGOED — default for potentially protectable inventions

Do not publicly disclose implementation detail before an explicit IP review when it may contain novel, commercially useful engineering, including:

- variable-stiffness / locking mechanisms
- unusual antenna topology or tuning method
- novel thermal stack
- battery topology / structural integration
- sensor placement optimization with proprietary implementation
- manufacturing processes
- custom silicon / circuit architecture

Public issues may state the hypothesis and benchmark while keeping enabling details in a private evidence package.

## PRIVATE — durable operational know-how

Keep private unless there is a deliberate reason to release:

- supplier pricing and negotiation
- manufacturing tolerances and yield improvements
- factory test procedures
- RF calibration tables
- unreleased CAD
- security-sensitive architecture, keys, credentials, or exploit-relevant detail
- personal/private datasets

## Release gate

Before a research PR is made public, ask:

1. Does this disclose an enabling mechanism rather than merely a problem/result?
2. Could a reasonable competitor reproduce the invention materially faster from this disclosure?
3. Is patentability strategically valuable?
4. Has any required filing occurred before publication?
5. Does publication expose security/privacy/safety-sensitive detail?

If uncertain, embargo the implementation while continuing to publish the hypothesis, benchmark, and non-enabling evidence.
