# B-001 — Event-first perception gate

Status: **PRE-REGISTERED / MACHINE-SIDE PROXY**  
Hypothesis: #2 B-H1

## Question

Can sparse/event-derived signals determine when expensive RGB perception is needed while retaining >=95% of task-relevant event onsets?

This first experiment tests **algorithmic gating and data movement**, not physical event-camera energy.

## Why a proxy first

Custom hardware is unnecessary to falsify a weak gating strategy. EPIC-KITCHENS-100 contains 100 hours of unscripted egocentric kitchen footage with timestamped action segments. `v2e` can transform ordinary video into realistic synthetic DVS event streams, including threshold variation, finite photoreceptor bandwidth and noise models.

If the event-first gate cannot work on this proxy, buying hardware does not rescue B-H1.

## Dataset slice

Start deterministic and small before scaling:

- 5 participants
- 2 videos/participant
- up to 10 minutes/video
- preserve untrimmed temporal context
- use official `start_timestamp` / `stop_timestamp` action boundaries as positive task-relevant intervals

Record exact participant/video IDs in the result artifact before model tuning.

## Inputs

1. RGB video
2. EPIC-KITCHENS action intervals
3. synthetic events from `SensorsINI/v2e`

Initial v2e configuration must be frozen in the result file. Sensitivity analyses later vary contrast thresholds and noise.

## Candidate gate v0

No learned model initially.

Per 50 ms window, compute:

- event count
- positive/negative event balance
- spatial entropy / occupied-cell fraction
- event-count derivative

Wake if a normalized weighted score exceeds threshold.

This deliberately tests whether simple sparse dynamics contain enough signal before introducing a neural classifier.

## Baseline

`always-awake RGB`: all time windows are sent to downstream RGB perception.

## Metrics

- **important-event recall:** proportion of annotated action-onset windows causing a wake within tolerance
- **false wake rate:** wakes/hour outside annotated action windows
- **awake duty cycle:** fraction of wall-clock time requiring downstream RGB perception
- **data-movement proxy:** candidate downstream RGB bytes / always-awake RGB bytes
- **wake latency:** delay from annotated action onset to wake

## Pre-registered thresholds

B-H1a passes this proxy stage only if:

- important-event recall >=95%
- median wake latency <=250 ms
- awake duty cycle <=50%
- false wake bound is reported; no post-hoc threshold selection using held-out videos

A later run should target <=20% duty cycle, but that is not required for the first falsification test.

## Split discipline

- tuning: first video per participant
- held-out evaluation: second video per participant
- threshold chosen once on tuning set
- no held-out threshold tuning

## Failure interpretations

- **low recall, low duty cycle:** sparse changes miss semantically important slow/static actions
- **high recall, high duty cycle:** event gate does not meaningfully save downstream work
- **good proxy result:** advance to real event-camera hardware; do not claim energy savings yet

## Next evidence level

L3 requires synchronized real RGB + event-camera recording and measured power for sensor, interface and candidate gate processor.

## References

- EPIC-KITCHENS-100: https://epic-kitchens.github.io/
- Official annotations: https://github.com/epic-kitchens/epic-kitchens-100-annotations
- v2e: https://github.com/SensorsINI/v2e
