# M1-002 — Candidate architecture matrix

Status: **L2 analytic / literature-grounded**  
Parent: #6 M1-H1  
Baseline: `M1-001-data-movement-budget.md`, `tools/perception_budget.py`

## Question

Which sensing/compute architecture is the best next branch for Gyeol if the objective is to reduce always-on perception data movement by >90% without making Gyeol V1 depend on an immature semiconductor process?

## Reference model

The current architecture reference is 1920×1080 × 30 fps × 12 raw bits/pixel = **93.312 MB/s** before downstream processing.

For comparison only:

- 0.1 Mev/s at 8 B/event = 0.8 MB/s → **99.14%** below the raw-frame reference
- 0.5 Mev/s = 4 MB/s → **95.71%** below reference
- 1.0 Mev/s = 8 MB/s → **91.43%** below reference
- 5.0 Mev/s = 40 MB/s → **57.13%** below reference
- semantic-output reference (10 outputs/s × 64 B) = 0.00064 MB/s → **99.9993%** below reference

These are architecture-model numbers, **not measured energy savings**. Compute, ADC, sensor readout, SRAM/DRAM traffic and interface energy remain separate terms.

## Candidate matrix

| ID | Architecture | What leaves sensing plane | Transfers potentially removed | Evidence anchor | Gyeol readiness | Main limitation |
|---|---|---|---|---|---|---|
| C1 | Event sensor + external ultralow-power gate | sparse events | repeated full-frame transfer; not sensor→processor event transfer | established DVS/event architecture; B-001 tests our gate | **near-term** | event traffic can become dense; temporal context still needs compute/memory |
| C2 | Near-sensor digital accelerator / stacked compute | compact features or wake signal | high-volume sensor→application-SoC traffic; some external memory traversal | near-sensor computing literature | **1–3 yr plausible prototype/partner path** | packaging, accelerator design, task/precision trade-offs |
| C3 | CMOS-compatible programmable in-sensor convolution | filtered/features | raw frame export for supported front-end filters | Jang et al. demonstrated wafer-scale electrostatically doped silicon photodiodes and programmable 3×3 convolution filters | **research** | currently small demonstrated networks; integration with production CIS is non-trivial |
| C4 | Dynamic optoelectronic in-sensor processing | task-specific processed signal | raw transfer plus part of external low-level vision compute | Yang et al. demonstrated in-sensor dynamic computing for machine vision | **research** | specialised device stack and task-specific processing |
| C5 | Analog event + memory sensor | event/memory features | ADC and digital temporal accumulation for the demonstrated front end; can sharply compress temporal context | Kim et al. demonstrated concurrent analog event spikes + persistent memory, optical compression 4900→16, and projected sub-1 W realistic-duty system power for an ASIC implementation | **moonshot / strong Gyeol relevance** | current lab prototype is not a mobile image-sensor product; projection ≠ measured phone power |
| C6 | Phase-change computational sensor / in-sensor-in-memory | filtered/features/class output | sensor→processor data for offloaded filters; weight movement for persistent local operations | Syed et al. demonstrated a phase-change computational-sensor concept using non-volatile PCM and discuss stacked-CMOS integration | **moonshot with mature memory ingredient** | hybrid-bonding/integration, read-disturb constraints, best suited to selected filters/preprocessing |
| C7 | Single multifunctional photosensing-memory-processing diode | locally denoised/processed result | separate sensing/memory/front-end circuits for supported functions | Luo et al. demonstrated a GaN/AlGaN/GaN diode with photosensing, eight-state photomemory and processing; arrays performed denoising/classification without additional circuits | **farther moonshot** | novel device/fabrication integration and limited demonstrated task breadth |

## Transfer accounting

The candidates should not be compared with one undifferentiated “power saving” number.

```text
T1 pixel/photodiode → local readout
T2 readout → ADC / digital event representation
T3 sensor → SoC / near-sensor accelerator
T4 ISP/accelerator → memory
T5 model weights/activations ↔ compute
T6 semantic/wake output → application processor
```

Approximate architectural effect:

| Candidate | T1 | T2 | T3 | T4 | T5 | T6 |
|---|---|---|---|---|---|---|
| C1 event + external gate | retained | retained/changed | sparse | reduced if gate is local | retained | sparse wake |
| C2 near-sensor accelerator | retained | retained | localised | reduced | localised/reduced | sparse feature/wake |
| C3 in-sensor convolution | integrated | may be reduced | feature-only | reduced | front-end weights local | feature |
| C4 dynamic in-sensor | integrated | reduced by architecture | processed signal | reduced | task-specific local | processed signal |
| C5 analog event+memory | integrated analog | **ADC/accumulation eliminated in demonstrated front end** | compressed event/memory | strongly reduced for temporal front end | partly optical/analog | feature/event |
| C6 PCM computational sensor | integrated + PCM | architecture-dependent | filtered/features | reduced | **non-volatile local weights/state** | feature/class |
| C7 multifunctional diode | integrated | architecture-dependent | processed result | reduced | device-local state | feature/class |

`retained`, `reduced`, and `eliminated` are architectural labels, not measured Gyeol energy results.

## Decision: what to prototype first

### Merge into the *research plan*: C1 → C2

The first hardware-facing prototype should **not** attempt a novel semiconductor.

1. **C1 — real event sensor + low-power external/near-sensor gate** is the control bridge from B-001. It is the fastest way to measure whether sparse sensing actually reduces Gyeol joules/hour at useful recall.
2. **C2 — move the validated gate physically closer to the sensor** is the first plausible 1–3 year engineering breakthrough. It tests how much of the benefit comes specifically from avoiding sensor/application-SoC and memory traffic.

This gives a direct comparison:

```text
RGB + application SoC
        ↓
C1 event sensor + external gate
        ↓
C2 event sensor + near-sensor gate
```

If C1 does not produce a meaningful system-energy advantage, C2 should be parked rather than custom-designed.

### Keep as parallel moonshot: C5

C5 is the most Gyeol-specific moonshot because Gyeol needs **both instantaneous change and persistent temporal context**. Kim et al.'s analog event-memory architecture directly targets the otherwise expensive step of reconstructing temporal memory from event streams. It therefore deserves a standing research branch even though its current technology readiness is too low for V1.

### Secondary moonshot: C6

C6 is attractive because phase-change memory is a much more mature ingredient than many exotic photosensor materials. Its strongest Gyeol role may be **persistent, task-specific front-end filters/wake models** rather than general-purpose vision.

## Falsification / advancement gates

### Gate M1-A — C1 hardware bridge

Advance only if real sensor + gate measurements preserve B-001 task quality while reducing **whole perception subsystem** energy materially versus the matched RGB baseline. The original moonshot target remains >90% off-sensor data reduction; energy gets its own measured threshold.

### Gate M1-B — C2 near-sensor value

After C1 is measured, simulate or prototype relocation of the same gate near the sensor. Advance only if the energy saved by avoided transfer/memory traffic is large enough to justify new packaging/ASIC complexity.

### Gate M1-C — custom-device moonshot

C3–C7 do not advance toward custom fabrication from literature alone. Require:

1. a Gyeol workload where C1/C2 leave a measured bottleneck;
2. a device architecture that specifically removes that bottleneck;
3. simulation or proxy hardware showing a credible ≥10× advantage in the constrained subsystem;
4. an integration/fabrication partner or process path.

## Evidence anchors

- Zhou & Chai, *Near-sensor and in-sensor computing*, Nature Electronics (2020): https://doi.org/10.1038/s41928-020-00501-9
- Jang et al., *In-sensor optoelectronic computing using electrostatically doped silicon*, Nature Electronics (2022): https://doi.org/10.1038/s41928-022-00819-6
- Yang et al., *In-sensor dynamic computing for intelligent machine vision*, Nature Electronics (2024): https://doi.org/10.1038/s41928-024-01124-0
- Syed et al., *Phase change computational sensor*, npj Unconventional Computing (2025): https://doi.org/10.1038/s44335-024-00018-w
- Baek et al., *Edge intelligence through in-sensor and near-sensor computing for the artificial intelligence of things*, npj Unconventional Computing (2025): https://doi.org/10.1038/s44335-025-00040-6
- Kim et al., *In-sensor analog optoelectronic processing of concurrent event and memory signals for dynamic vision sensing*, Nature Communications (2026): https://doi.org/10.1038/s41467-025-68013-8
- Luo et al., *A single diode with integrated photosensing, memory and processing for neuromorphic image sensors*, Nature Electronics (2026): https://doi.org/10.1038/s41928-026-01588-2
