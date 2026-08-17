# M1-003 — L2 advancement scorecard

Status: **L2 candidate evaluation**  
Parent: #6 M1-H1  
Companion: `M1-002-candidate-matrix.md`

This scorecard exists to satisfy the pre-registered M1-001 L2 advancement contract. It separates **modelled off-sensor data reduction** from **energy evidence**.

## Common reference contracts

Raw-frame reference:

- 1920 × 1080 × 30 fps × 12 bpp = **93.312 MB/s**

Sparse-event reference, assuming an 8-byte software event representation:

- 0.1 Mev/s = 0.8 MB/s = **99.14% reduction**
- 0.5 Mev/s = 4.0 MB/s = **95.71% reduction**
- 1.0 Mev/s = 8.0 MB/s = **91.43% reduction**
- 5.0 Mev/s = 40.0 MB/s = **57.13% reduction**
- therefore the >90% M1 data-reduction target is met below approximately **1.17 Mev/s** at 8 B/event

Semantic/wake reference:

- 10 outputs/s × 64 B = 0.00064 MB/s = **99.9993% reduction**

The semantic number is an output-contract target, not evidence that a candidate can produce those semantics at acceptable accuracy or energy.

## L2 scorecard

| ID | Eliminated / retained transfers | Estimated off-sensor bandwidth reduction | Energy terms to measure/model | Energy confidence | Task restriction | Process / integration assumption | Gyeol readiness | Strongest evidence |
|---|---|---|---|---|---|---|---|---|
| **C1 Event sensor + external gate** | eliminates repeated raw frames; retains event sensor readout, sensor→gate event traffic, gate compute and RGB wake path | **57–99%** over the 0.1–5 Mev/s model sweep; **>90% if <~1.17 Mev/s** | event sensor power, event-interface energy, gate compute/SRAM, wake cost, RGB duty cycle | **medium for accounting; low for total Gyeol energy until bench test** | weak for static/slow semantic changes unless fused with other sensing | commercial/available event sensor connected to low-power processor | **near-term control bridge** | mature DVS/event principle; B-001 is Gyeol-specific falsification test |
| **C2 Near-sensor digital gate/accelerator** | retains sensor/readout and local compute; localises T3/T4/T5 and exports sparse feature/wake output | target **>90%**; semantic-output contract would be **99.9993%**, conditional on task quality | sensor + ADC, local accelerator, SRAM, stacked/package interconnect, final wake link, avoided application-SoC/DRAM traffic | **low–medium analytic; no Gyeol hardware measurement** | constrained by accelerator model and local memory; more general than analog fixed functions | conventional sensor plus tightly co-packaged/stacked digital accelerator or companion ASIC | **plausible 1–3 yr engineering branch after C1** | near-sensor literature supports moving compute close to sensors to reduce redundant transfer |
| **C3 Programmable silicon in-sensor convolution** | integrates low-level filtering at photodiodes; retains programming/bias, local readout and feature export | target **>90%** if supported task can export sparse features instead of frames; exact feature dimensionality **TBD** | photodiode/bias energy, analog MAC, programming, readout, feature ADC/link | **low for scaled system** | best for small/fixed front-end convolution/filter bank | electrostatically doped silicon photodiodes integrated into a production-compatible image-sensor flow | **research; not V1 dependency** | Jang et al. fabricated wafer-scale arrays and demonstrated programmable 3×3 in-sensor convolution filters |
| **C4 Dynamic optoelectronic in-sensor processing** | moves adaptive low-level computation into sensor; retains output readout and task-specific downstream stages | target **>90%** for tasks whose processed output is compact; exact Gyeol output rate **TBD** | device bias, adaptation/programming, analog processing, output conversion/link | **low for mobile integration** | specialised machine-vision tasks; function breadth is limited by device/computation mapping | specialised optoelectronic device stack can be fabricated and packaged at mobile sensor scale | **research** | Yang et al. demonstrated in-sensor dynamic computation for robust machine-vision tracking |
| **C5 Analog event + persistent-memory sensor** | demonstrated architecture removes ADC + digital accumulation for its event/memory front end; retains analog sensing/amplification and compressed output/downstream classifier | event-output mode can follow C1 sparse-event range; 4900→16 optical encoder in paper is a **306.25× feature compression stage**, but this is not a raw-Gyeol bandwidth measurement | photodiode/phosphor response, TIA, analog differencing, optical encoder, output readout, downstream classifier | **medium for published prototype/projection; very low for phone integration** | strongest for dynamic vision needing instantaneous change + motion history | phosphor/Si-photodiode/TIA architecture or equivalent integrated analog device can be miniaturised into sensor-scale ASIC/stack | **moonshot; high Gyeol relevance** | Kim et al. reported event+memory sensing, 4900→16 optical encoding, ADC/digital-accumulation elimination, current prototype <5 W and projected realistic-duty ASIC system well below 1 W |
| **C6 Phase-change computational sensor / ISC-IMC** | offloads selected filters and stores weights/state non-volatile near/in sensor; retains sensor readout, selected outputs and any non-offloaded network | target **>90%** only for workloads where enough front-end computation can be offloaded to emit compact features; exact output **TBD** | PCM program/read, sensing circuit, convolution/readout, stacked-CMOS interconnect, residual processor work | **medium for PCM device maturity; low for complete sensor architecture** | strongest for shallow filters, downsampled inputs and preprocessing rather than unrestricted vision | PCM integrated with/stacked on CMOS sensor using dense interconnect/hybrid bonding | **secondary moonshot** | Syed et al. demonstrated device-level computational-sensor concept and analysed PCM/CMOS stacking path |
| **C7 Multifunctional sensing-memory-processing diode** | integrates sensing, local state and supported processing; retains array readout/output and downstream unsupported tasks | semantic/feature-output architecture could target **>99%** off-sensor reduction, but Gyeol task/output dimensionality **TBD** | diode bias, charge trapping/release, array programming/readout, output conversion | **low for scaled/mobile system** | demonstrated denoising/classification functions; unknown generality for continuous embodied vision | GaN/AlGaN/GaN nanowire diode arrays can be scaled, integrated and manufactured with suitable yield | **farther moonshot** | Luo et al. demonstrated one diode integrating photosensing, eight-state memory and processing; device arrays performed denoising/classification without added functional circuits |

## L2 decision

### Does any non-fictional architecture plausibly exceed 90% off-sensor data reduction?

**Yes: C1**, under a measurable condition rather than a blanket claim.

At the common 8 B/event representation, C1 exceeds the >90% off-sensor reduction threshold whenever the average event stream stays below ~1.17 Mev/s relative to the 1080p30/12-bit raw-frame reference. Event sensors are existing technology, so this does not depend on a new material or fabrication process.

This is enough to advance M1 from literature-only framing to a hardware falsification path, **not enough to validate the energy hypothesis**.

## Research branch decisions

- **C1 — MERGE into experiment plan.** Measure first.
- **C2 — CONDITIONAL / REBASE on C1.** Prototype only if C1 shows transfer/memory energy is a material residual bottleneck.
- **C3 — PARK as silicon-compatible research branch.** Revisit if a fixed front-end filter emerges from B-001/C1.
- **C4 — PARK.** Interesting, but less direct integration path than C3/C5.
- **C5 — KEEP ACTIVE MOONSHOT.** Best match to Gyeol's event + temporal-memory requirement.
- **C6 — KEEP ACTIVE SECONDARY MOONSHOT.** Mature memory ingredient and plausible task-specific front-end role.
- **C7 — WATCH.** Strong device-level integration result but too far from a manufacturable Gyeol sensor to drive V1.

## Next falsification target

The next machine/hardware bridge is **C1**:

1. complete B-001 synthetic-event proxy;
2. reproduce it with a real event sensor;
3. measure the full perception subsystem in joules/hour at the same recall/latency target;
4. only then estimate the incremental value of moving the gate from external processor to C2 near-sensor silicon.

This preserves the core M1 rule: **data movement is not energy until measured or validated by an energy model.**

## Evidence anchors

- Zhou & Chai (2020): https://doi.org/10.1038/s41928-020-00501-9
- Jang et al. (2022): https://doi.org/10.1038/s41928-022-00819-6
- Yang et al. (2024): https://doi.org/10.1038/s41928-024-01124-0
- Syed et al. (2025): https://doi.org/10.1038/s44335-024-00018-w
- Baek et al. (2025): https://doi.org/10.1038/s44335-025-00040-6
- Kim et al. (2026): https://doi.org/10.1038/s41467-025-68013-8
- Luo et al. (2026): https://doi.org/10.1038/s41928-026-01588-2
