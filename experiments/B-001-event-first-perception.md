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

Use a deterministic slice before any model tuning:

- participants `P01` through `P05`
- for each participant, select the first two available videos by lexicographic `video_id`
- use the first 10 minutes of each selected video, or the full video if shorter
- preserve untrimmed temporal context
- use official `start_timestamp` / `stop_timestamp` action boundaries as positive task-relevant intervals
- if a selected video is unavailable/corrupt, record the exclusion before substitution and take the next lexicographic video for that participant

The final exact video IDs and any exclusions must be committed to the result artifact before gate parameters are tuned.

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

## Wake-state definition

A gate trigger wakes the downstream RGB path for **1.0 second**. Any trigger during that interval extends the awake interval to 1.0 second after the most recent trigger.

This fixed hold time defines awake duty cycle and the downstream RGB data-movement proxy.

## Baseline

`always-awake RGB`: all time windows are sent to downstream RGB perception.

## Metrics

- **important-event recall:** proportion of annotated action-onset windows causing a wake within tolerance
- **false wake rate:** triggers/hour outside annotated action intervals and outside the 250 ms onset-tolerance window
- **awake duty cycle:** fraction of wall-clock time in the fixed wake state
- **data-movement proxy:** awake duty cycle × always-awake downstream RGB bytes
- **wake latency:** delay from annotated action onset to first gate trigger

## Pre-registered thresholds

B-H1a passes this proxy stage only if the held-out set satisfies all of:

- important-event recall >=95%
- median wake latency <=250 ms
- awake duty cycle <=50%
- false wake rate <=60 triggers/hour

A later run should target <=20% duty cycle, but that is not required for the first falsification test.

## Split discipline

For each participant:

- tuning: first selected video
- held-out evaluation: second selected video
- threshold chosen once on tuning set
- no held-out threshold tuning

## Failure interpretations

- **low recall, low duty cycle:** sparse changes miss semantically important slow/static actions
- **high recall, high duty cycle:** event gate does not meaningfully save downstream work
- **false wakes >60/hour:** gate is too noisy for the current 1-second hold policy even if recall is high
- **good proxy result:** advance to real event-camera hardware; do not claim energy savings yet

## Next evidence level

L3 requires synchronized real RGB + event-camera recording and measured power for sensor, interface and candidate gate processor.

## References

- EPIC-KITCHENS-100: https://epic-kitchens.github.io/
- Official annotations: https://github.com/epic-kitchens/epic-kitchens-100-annotations
- v2e: https://github.com/SensorsINI/v2e
