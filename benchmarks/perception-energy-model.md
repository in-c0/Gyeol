# Perception data-movement baseline

Status: **L2 analytic model**  
Related: #2 B-H1, #6 M1-H1

## Purpose

Establish a reproducible bandwidth/data-movement baseline before claiming whole-device energy savings.

This benchmark separates:

1. sensor output bandwidth
2. downstream memory/interconnect traffic
3. whole-device energy

A reduction in (1) does not automatically prove the same reduction in (3). Hardware power measurements are required before B-H1 can advance beyond L2/L3.

## Baseline model

For a frame stream:

`B_rgb = width × height × fps × bits_per_pixel / 8`

Default reference point:

- 1920 × 1080
- 30 fps
- 12 raw bits/pixel
- `B_rgb = 93.31 MB/s`

This is an architecture reference, not a claim about a particular phone's external memory traffic. ISP compression, tiling, on-chip SRAM, frame reuse, HDR and camera-pipeline details can materially change physical traffic.

## Event-stream model

`B_event = events_per_second × bytes_per_event`

The supplied script sweeps 4/8/16-byte event representations. The 8-byte default is a conservative software-record representation and **not** a sensor wire-format claim.

At 8 bytes/event:

| Event rate | Stream | RGB/event bandwidth ratio |
|---:|---:|---:|
| 0.1 Mev/s | 0.8 MB/s | 116.6× |
| 0.5 Mev/s | 4.0 MB/s | 23.3× |
| 1.0 Mev/s | 8.0 MB/s | 11.7× |
| 5.0 Mev/s | 40.0 MB/s | 2.3× |

Break-even with the default RGB baseline occurs at ~11.66 Mev/s for an 8-byte event representation.

## Semantic-state model

A hypothetical post-sensor stream of 10 semantic events/s at 64 bytes/event is 0.00064 MB/s, roughly 145,800× below the raw RGB reference stream.

This demonstrates the *upper-bound architectural opportunity* from aggressive semantic compression. It does **not** include the computation needed to produce semantic events.

## Research consequence

B-H1 is decomposed into:

- **B-H1a — gating quality:** >=95% important-event recall at a pre-registered false-wake bound.
- **B-H1b — data movement:** >=5× reduction in defined sensor/downstream data transfer for the same task window.
- **B-H1c — whole-system energy:** >=5× lower measured perception energy on representative hardware.

Only B-H1c satisfies the original energy claim.

M1-H1 uses this model to identify exactly which transfers a near-/in-sensor architecture eliminates rather than counting all raw bandwidth as saved energy.

## References

- Gehrig & Scaramuzza, *Nature* (2024), hybrid event+frame perception: https://www.nature.com/articles/s41586-024-07409-w
- Baek et al., *npj Unconventional Computing* (2025), in-/near-sensor computing: https://www.nature.com/articles/s44335-025-00040-6
- Kim et al., *Nature Communications* (2026), in-sensor event + memory processing: https://www.nature.com/articles/s41467-025-68013-8
