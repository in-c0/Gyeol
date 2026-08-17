# M1-001 — Near-/in-sensor compute data-movement budget

Status: **L1 → L2**  
Moonshot: #6 M1-H1

## Hypothesis under test

Near-/in-sensor computation can remove >90% of off-sensor sensory data movement for a defined always-on Gyeol perception workload while retaining task quality and materially reducing whole-system energy.

The >90% claim applies first to **data movement**. Energy must be measured or supported by a validated hardware energy model separately.

## Reference workload

Use the same event/onset detection workload defined by B-001 so the near-term and moonshot branches share a benchmark.

Conventional conceptual pipeline:

```text
photodiodes
  -> sensor readout / ADC
  -> sensor interface
  -> ISP / memory
  -> accelerator memory
  -> NPU / CPU
  -> semantic event
```

Candidate near-/in-sensor pipeline:

```text
photodiodes
  -> local analog/digital feature extraction
  -> sparse feature / wake signal
  -> main processor only when required
```

## Transfers to account for separately

1. pixel-array → readout
2. ADC output → sensor interface
3. sensor → SoC
4. ISP → DRAM/on-chip memory
5. accelerator activation/weight traffic
6. final semantic output

The experiment must never infer that eliminating transfer (3) eliminates (1), (2), (4), or compute energy.

## First analytic baseline

Default frame-stream reference: 1920×1080 × 30 fps × 12 bpp = **93.31 MB/s**.

The companion `tools/perception_budget.py` shows that an 8-byte event representation remains below this frame-stream bandwidth until ~11.66 million events/s. A semantic stream can be orders of magnitude smaller, but the computation required to create it remains in the budget.

## Candidate architecture classes

Rank candidates against the exact transfers they eliminate:

- conventional event sensor + external processor
- stacked/near-sensor digital accelerator
- in-pixel / in-sensor analog preprocessing
- intelligent skipping during sensor readout
- event + persistent-memory sensor
- compute-in-memory adjacent to sensor

## Advancement criterion to L2

Produce a table for at least five candidate architectures containing:

- eliminated transfers
- retained transfers
- estimated bandwidth reduction
- estimated energy terms and confidence level
- task restrictions
- process/integration assumptions
- technology readiness
- strongest current evidence

At least one architecture must plausibly exceed 90% reduction in **off-sensor** data transfer without depending on a non-existent material/process.

## Advancement criterion to L3

Implement the closest commercially available proxy and measure:

- sensor/interface energy
- processing energy
- total joules/inference or joules/hour
- task accuracy/recall/latency

## Current evidence anchors

Near-/in-sensor computing literature explicitly identifies redundant sensor-memory-compute data traversal as an energy/latency bottleneck. Recent demonstrations include analog in-sensor event/memory processing that removes ADC/digital accumulation stages and projects per-channel power below 1 mW, but this is not yet a Gyeol-system measurement.

## References

- Baek et al. (2025): https://www.nature.com/articles/s44335-025-00040-6
- Kim et al. (2026): https://www.nature.com/articles/s41467-025-68013-8
- Zhou & Chai (2020): https://www.nature.com/articles/s41928-020-00501-9
