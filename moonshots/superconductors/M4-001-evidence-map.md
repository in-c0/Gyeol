# M4-001 — Ambient-condition superconductivity evidence map

Status: **L1/L2 LIVING MAP**  
Parent: #7 M4 ambient-pressure high-temperature / room-temperature superconductivity  
Snapshot date: **2026-08-18**

## Claim discipline

The target is not “the highest reported transition.” The target is a reproducible superconducting state that survives useful ambient conditions.

Every candidate is therefore decomposed into evidence channels:

1. **transport onset** — resistance begins to fall;
2. **zero resistance** — stronger transport evidence;
3. **field response** — transition shifts under magnetic field as expected;
4. **magnetic evidence** — Meissner/diamagnetic response;
5. **phase/structure evidence** — the claimed material/phase is characterized;
6. **internal repetition** — more than one sample/cycle within the reporting group;
7. **independent replication** — another group reproduces the relevant state;
8. **ambient-pressure retention** — the state exists after external pressure is removed;
9. **room-temperature stability** — the relevant phase/state survives handling near room temperature.

`Tc_onset`, `Tc_zero`, and `Tc_magnetic` are never silently substituted for one another.

**Current conclusion:** this map contains no validated room-temperature, ambient-pressure superconductor.

## Experimental frontier

### M4-C001 — pressure-quenched Hg1223

**Material:** HgBa2Ca2Cu3O8+δ  
**Route:** pressure-enhance superconductivity, cool, then release pressure to retain a metastable state  
**Ambient-pressure result:** reproducible onset Tc up to **151 K** after pressure quenching  
**Evidence:** transport; DC magnetization indicating a bulk (~78%) superconducting phase; synchrotron XRD; multiple samples from multiple source crystals  
**Specific-state independent replication:** not yet counted in this map  
**Critical limitation:** the retained high-Tc state is metastable; reported Tc degrades after warming above ~200 K and the high-retention protocol used low quench temperatures, including 4.2 K  
**Status:** **ACTIVE — highest-temperature experimental ambient-pressure branch**

Why it matters: it demonstrates that **ambient pressure does not require the superconducting state to be the equilibrium ambient-pressure state**. Metastability engineering is therefore a first-class search strategy.

Next cheapest discriminating work:

- extract pressure, quench temperature, retained Tc, transition width and thermal-cycling outcomes from all reported experiments;
- test whether retention is better explained by pressure, quench temperature, defect proxies, or their interaction;
- identify measurements that distinguish oxygen/vacancy redistribution from generic defect pinning as the retention mechanism.

Primary source: Deng et al., PNAS (2026), DOI `10.1073/pnas.2536178123`.

### M4-C002 — strained (La,Pr)3Ni2O7 bilayer nickelate films

**Route:** compressive epitaxial strain + non-equilibrium/strong-oxidation film growth  
**Ambient-pressure 2026 frontier:** onset Tc ~**63 K**, zero resistance ~**37 K**, diamagnetic transition beginning ~**23 K**  
**Evidence:** transport, field/critical-state characterization, mutual-inductance diamagnetism, synchrotron XRD/STEM  
**Family replication:** ambient-pressure superconductivity in strained bilayer nickelate films has been reported by multiple groups at lower/on-the-order-of-40–50 K scales; the specific ~63 K state is not treated here as independently replicated  
**Critical limitation:** thin-film/epitaxial platform; onset, zero-resistance and magnetic temperatures remain substantially separated  
**Status:** **ACTIVE — best strain/non-equilibrium branch**

Why it matters: strain can replace hydrostatic pressure as a controllable structural variable, and extreme non-equilibrium growth/oxygenation can stabilize states unavailable to bulk equilibrium synthesis.

Next cheapest discriminating work:

- construct a cross-paper dataset of substrate, in-plane strain, composition, oxygenation/growth protocol, onset/zero/magnetic Tc and structural descriptors;
- test whether a small structural/chemical descriptor set predicts Tc across independently grown films;
- prioritize synthesis directions only when predictions survive leave-one-paper/lab-out validation.

Primary frontier source: Zhou et al., National Science Review (2026), DOI `10.1093/nsr/nwag151`.  
Earlier ambient-pressure bilayer film evidence: Nature (2025), DOI `10.1038/s41586-025-08755-z`; Nature Materials (2025), DOI `10.1038/s41563-025-02258-y`.

### M4-C003 — hole-doped infinite-layer Sm-family nickelate films

**Route:** composition/doping and high-quality infinite-layer thin-film synthesis rather than large external pressure  
**Ambient-pressure result:** Tc approaching **40 K**, zero resistance reported at **31 K**, with Meissner evidence  
**Critical limitation:** thin-film synthesis; far below the temperature target; independent reproduction of the exact high-Tc composition must be tracked separately  
**Status:** **WATCH / MECHANISM DIVERSITY**

Why it matters: this is an ambient-pressure nickelate route with negligible lattice compression in the reported material, providing a useful contrast to strain-stabilized bilayer nickelates.

Primary source: Chow, Luo & Ariando, Nature (2025), DOI `10.1038/s41586-025-08893-4`.

## Computational / synthesis-target frontier

### M4-C004 — RbPH3 metastable hydride

**Route:** synthesize a high-pressure perovskite phase at moderate pressure, then exploit predicted quantum-anharmonic dynamical stability after decompression  
**Predicted ambient-pressure Tc:** around **100 K**  
**Evidence:** ab initio / anharmonic theory only; no superconducting experiment counted  
**Stability claim:** predicted thermodynamic stability near 30 GPa and dynamically stable lower-pressure phase down to ambient due to ionic quantum fluctuations  
**Status:** **ACTIVE THEORY CANDIDATE — synthesis is the decisive test**

Why it matters: unlike megabar superhydrides, the predicted synthesis pressure is moderate enough that a pressure-synthesis/decompression route is at least experimentally imaginable.

Next cheapest discriminating work:

- independent re-computation with a materially different first-principles workflow;
+- calculate decomposition/metastability barriers and finite-temperature survival, not only phonons/Tc;
+- only after independent theory agreement should synthesis planning become active.
+
+Primary source: Dangić et al., Computational Materials Today (2025), DOI `10.1016/j.commt.2025.100043`.
+
+### M4-C005 — Mg2XH6 (X = Rh, Ir, Pd, Pt) hydride family
+
+**Predicted ambient-pressure Tc:** roughly **45–80 K**, with higher values proposed under suitable doping  
+**Evidence:** high-throughput + first-principles prediction; no experimental superconductivity counted  
+**Critical limitation:** synthesis/thermodynamic accessibility of high-Tc phases  
+**Status:** **WATCH THEORY FAMILY**
+
+Primary source: npj Computational Materials (2024), DOI `10.1038/s41524-024-01214-9`.
+
+### M4-C006 — thermodynamically stable GNoME hydrides
+
+**Purpose:** stability control, not temperature leader  
+**2026 result:** systematic search of stable cubic hydrides found modest Tc values; the strongest candidate, LiZrH6Ru, falls dramatically below the ~100 K metastable predictions when treated with more demanding Coulomb calculations  
+**Status:** **ACTIVE NEGATIVE/TRADE-OFF CONTROL**
+
+Why it matters: the dataset strengthens the working hypothesis that **high conventional Tc at ambient pressure is entangled with metastability**, so searching only the equilibrium convex hull may systematically miss the interesting region.
+
+Primary source: Sanna et al., Communications Physics (2026), DOI `10.1038/s42005-026-02552-4`.
+
+## High-pressure source states — not ambient-pressure successes
+
+### M4-R001 — LaH10
+
+**Observed Tc:** ~**250 K** near **170 GPa**  
+**Status:** **SOURCE-STATE RESERVOIR, NOT AN AMBIENT CANDIDATE RESULT**
+
+Why it matters: it proves that conventional electron-phonon systems can reach near-room-temperature Tc, but pressure removal/stability is the unsolved problem.
+
+Primary source: Drozdov et al., Nature (2019), DOI `10.1038/s41586-019-1201-8`.
+
+### M4-R002 — H3S
+
+**Observed Tc:** **203 K** near **155 GPa**  
+**Evidence:** zero resistance, field-dependent transition, isotope effect, and magnetic-susceptibility measurements at the superconducting transition; later diffraction work characterized the superconducting H3S phase.  
+**Status:** **SOURCE-STATE RESERVOIR, NOT AN AMBIENT CANDIDATE RESULT**
+
+Primary superconductivity source: Drozdov et al., Nature (2015), DOI `10.1038/nature14964`.  
+Structure/mechanism source: Nature (2016), DOI `10.1038/nature17175`.
+
+## Negative controls / failed-claim registry
+
+These stay in the map permanently. Deletion would create survivorship bias.
+
+### M4-N001 — N-doped lutetium hydride near-room-temperature claim
+
+**Original claim:** near-room-temperature superconductivity at near-ambient pressure  
+**Status:** **DISCONFIRMED / RETRACTED**  
+**Why:** Nature retracted the report after author and journal concerns over sample provenance, measurements, processing and resistance-data reliability; an independent Nature study reported no superconductivity above 2 K over 0.4–40.1 GPa in a closely matched nitrogen-doped lutetium hydride.  
+**Use:** evidence-process negative control.
+
+Sources: Nature retraction DOI `10.1038/s41586-023-06774-2`; independent negative result DOI `10.1038/s41586-023-06162-w`.
+
+### M4-N002 — carbonaceous sulfur hydride room-temperature claim
+
+**Original claim:** ~287.7 K at extreme pressure  
+**Status:** **RETRACTED**  
+**Why:** Nature retracted the paper after concluding that non-standard, insufficiently documented background subtraction undermined confidence in the magnetic-susceptibility evidence.  
+**Use:** raw-data/provenance and analysis-pipeline negative control.
+
+Source: Nature retraction DOI `10.1038/s41586-022-05294-9`.
+
+### M4-N003 — LK-99
+
+**Original claim:** room-temperature, ambient-pressure superconductivity  
+**Status:** **DISCONFIRMED**  
+**Why:** independent replication/material-characterization work did not support superconductivity; impurity/ferromagnetic explanations accounted for the headline signatures.  
+**Use:** reminder that levitation-like behaviour and resistance anomalies are not sufficient evidence.
+
+Claim preprints: arXiv `2307.12008`, `2307.12037`. Replication record should be linked to primary negative studies as the map expands.
+
+## Working hypotheses created by the map
+
+### M4-H1 — controlled metastability is a better search axis than equilibrium stability alone
+
+> Among ambient-pressure conventional candidates, high predicted/retained Tc will correlate with a controlled metastability metric more strongly than with equilibrium thermodynamic stability alone.
+
+Falsification path:
+
+- build a cross-family dataset containing Tc, distance-to-hull/free-energy proxy, synthesis pressure, decompression route, kinetic/dynamic stability, strain and retention temperature;
+- compare predictive models with and without metastability descriptors using leave-family-out validation;
+- reject H1 if metastability descriptors do not improve out-of-family prediction.
+
+### M4-H2 — stabilization route is transferable
+
+> Structural states that host elevated Tc under pressure can sometimes be retained or recreated at ambient pressure through pressure quenching, epitaxial strain, defect engineering or non-equilibrium growth when the required electronic/structural configuration is metastably accessible.
+
+Falsification path:
+
+- define structural/electronic descriptors before selecting target materials;
+- predict which high-pressure states are retainable/recreatable;
+- evaluate prospectively rather than retrospectively explaining successes.
+
+### M4-H3 — evidence quality must be a separate optimization objective from Tc
+
+> A candidate-selection system that optimizes `expected useful Tc × probability of replication × ambient stability` will outperform one that ranks by claimed/predicted Tc alone.
+
+This is partly methodological and can be evaluated retrospectively against historical failed claims and prospectively against new candidates.
+
+## Next branch
+
+**M4-002 should operationalize H1 first.** It is the cheapest machine-side experiment and directly tests whether the most interesting current evidence — pressure-quenching, strained nickelates and metastable hydride predictions — shares a measurable stabilization principle.
+
+No synthesis is recommended from this map alone.
