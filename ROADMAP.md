# Gyeol Research Roadmap

## Mainline objective

Build the best complete personal computer currently supported by merged evidence.

Whole-system objectives:

1. full daily-driver smartphone functionality
2. body-conformal comfort
3. useful local-AI capability
4. battery life
5. RF/cellular performance
6. thermal safety
7. durability
8. privacy/security
9. repairability
10. manufacturability and cost

## Priority research branches — plausible 1–3 year breakthroughs

### A — Morphing mechanical architecture

**A-H1:** A passive or low-energy variable-stiffness spine can achieve >=80% of a rigid smartphone's flat-state bending stiffness while conforming comfortably to a forearm.

**A-H2:** The device can mechanically lock in both flat and wrapped states without continuous power.

**A-H3:** The structure can survive 100,000 accelerated phone↔arm cycles with <10% stiffness drift and no critical failure.

**A-H4:** A finite set of articulated zones can fit a useful range of forearm geometries without requiring a fully stretchable computer.

### B — Event-driven local AI

**B-H1:** Event camera + IMU + low-power audio can decide when expensive perception is required using >=5x less energy than continuous RGB+NPU processing while retaining >=95% important-event recall.

**B-H2:** A hierarchical wake-up stack can keep the high-power application SoC asleep for most of an ordinary day without materially reducing useful contextual awareness.

**B-H3:** Semantic event compression can reduce retained sensory state by >=10x while causing <5% degradation on defined downstream LifeOS tasks.

### C — Morphology-aware RF

**C-H1:** Bend geometry, body proximity, grip, orientation, and recent RF state can predict a near-optimal antenna configuration without continuous exhaustive search.

**C-H2:** A morphology-aware distributed antenna system improves poor wrapped-state link performance by >=3 dB versus a static antenna configuration.

**C-H3:** At least one wrapped geometry can provide better useful antenna diversity than the flat configuration rather than merely reducing the penalty of deformation.

### D — Wrist-centric machine perception

**D-H1:** A properly oriented forearm camera observes a greater fraction of task-relevant hand–object interactions than phone-pocket, watch-face, or chest-mounted baselines.

**D-H2:** RGB + event + selective depth sensing can match or exceed continuous-RGB activity/context recognition at <=50% of perception energy.

**D-H3:** Camera location/FOV can be optimized from activity data rather than chosen manually, yielding a measurable improvement in useful-context capture per unit of privacy exposure and energy.

**D-H4:** A trusted near-sensor processor can discard irrelevant/private imagery before raw frames reach the primary OS while preserving defined context-recognition tasks.

### E — Electronic skin / biometric interface

**E-H1:** Distributed forearm sensing reduces unusable biometric signal intervals during exercise by >=30% versus a watch-sized sensing window.

**E-H2:** Multiple imperfect sensing sites plus contact-pressure/IMU context outperform one optimized sensing site under motion.

**E-H3:** The sensing surface can estimate its own measurement confidence well enough to reject unreliable biometric readings before they are exposed as trusted measurements.

**E-H4:** The Armpad inner surface can eventually supply enough validated sensing to remove the need for a separate biometric wearable for selected tasks.

## Supporting research branches

### F — Directional thermal architecture

**F-H1:** An anisotropic thermal stack can reduce skin-side temperature rise by >=5 °C at an equal sustained compute workload versus a symmetric spreader baseline.

**F-H2:** Shape/contact awareness can steer workload between device segments, home compute, or throttled modes to increase sustained useful compute under skin-temperature constraints.

### G — Distributed energy

**G-H1:** Multiple protected rigid cells can provide comparable usable energy density to the selected single-cell baseline while materially improving conformity.

**G-H2:** Failure of one energy segment can be electrically isolated while the device remains operational in a safe degraded mode.

**G-H3:** Shape- and temperature-aware power routing measurably improves usable runtime or thermal headroom versus static routing.

### H — Strain-managed display

**H-H1:** Concentrating deformation into designed joint zones increases display-stack fatigue life by >=5x versus uniform arbitrary bending at equivalent overall curvature.

**H-H2:** A replaceable sacrificial outer layer can reduce lifecycle display replacement cost without materially harming optical/touch performance.

### I — Fault-tolerant interconnect

**I-H1:** A redundant inter-segment topology can preserve core phone operation after any single non-critical interconnect path failure.

**I-H2:** Modules can self-identify faults and reroute supported buses automatically without requiring a reboot or service intervention for defined failure classes.

## Moonshots — parallel, never on the V1 critical path

See [moonshots/README.md](moonshots/README.md).

Candidate branches:

- near-/in-sensor computing
- flexible or deformable computation
- nonvolatile compute
- new ultra-low-energy semiconductor devices
- programmable-stiffness materials
- flexible solid-state energy storage
- self-healing display/material stacks
- ambient-pressure high-temperature / room-temperature superconductivity
- neuromorphic personal-computing architectures
