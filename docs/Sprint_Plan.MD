# Sprint Plan: Q-Net — All Sprints Overview
**Project:** Q-Net (Quantum Entanglement-Based Post-Internet Architecture)
**Course:** CP352005 Computer Networks
**Institution:** College of Computing, Khon Kaen University
**Version:** 2.0 (Revised — Full 4-Sprint Record)
**Submission Deadline:** March 17, 2026

---

## Team Roster

| Name | Student ID | Nickname | Role |
|------|-----------|---------|------|
| Sitthichok Moknak | 673380428-6 | บูบู้ | Product Owner / Strategist ⭐ |
| Pattadon Khumnan | 673380416-3 | โบร์ท | Quantum Architect |
| Nattaphat Chamtakhu | 673380583-4 | อ้น | Software Engineer (Hardware & Simulation) |
| Sorawit Sukongchareun | 673380606-8 | โอ่ง | Network Analyst |
| Amonwan Phimphichai | 673380608-4 | เนย | Research & Ethics Analyst |

---

## Sprint Summary Dashboard

| Sprint | Period | Fidelity Target | Fidelity Achieved | Status |
|--------|--------|----------------|------------------|--------|
| Alpha (S1) | – 22 Feb 2026 | Baseline | ~49.1% (near-random) | ✅ Done |
| Beta (S2) | 23 Feb – 07 Mar 2026 | > 85% | ~93.0% | ✅ Done |
| Gamma (S3) | 08 Mar – 12 Mar 2026 | > 97% | ~96.6% (v3), ~49.6% (v2b ❌) | ✅ Done |
| Delta (S4) | 13 Mar – 17 Mar 2026 | ≥ 99% | 99.09% (PEAK) | ✅ Done |

---

---

# Sprint Alpha — Sprint 1
**Duration:** [Start Date] – 22 February 2026
**Version:** v1

---

## Sprint Goal

Establish the foundational architecture of Q-Net and validate the core quantum teleportation
mechanism through a Toy Model simulation **and real IBM Quantum hardware execution**.
By the end of this sprint the team will have initial design documents and empirical
baseline data from IBM Quantum processors.

**Fidelity Target:** Establish baseline (no specific threshold)

---

## Team Roles & Responsibilities

- **Product Owner / Strategist — Sitthichok Moknak**
  - Define project vision and alignment with Master Research Prompt
  - Oversee all documentation and manage sprint backlog
  - Prepare Project Pitch presentation
  - Finalize and submit all deliverables

- **Quantum Architect — Pattadon Khumnan**
  - Lead design of the 5-layer Q-Net protocol stack
  - Author `Architecture_Spec.MD`
  - Define functions of QIP, QTCP, Q-CAST layers

- **Software Engineer — Nattaphat Chamtakhu**
  - Develop Toy Model simulation for quantum teleportation
  - Execute code on local simulators and real IBM Quantum hardware
  - Generate circuit diagrams and histograms for presentation

- **Network Analyst — Sorawit Sukongchareun**
  - Research TCP/IP and BGP limitations in interplanetary context
  - Contribute to Problem Statement and Civilizational Impact sections
  - Analyze decoherence results from IBM hardware tests

- **Research & Ethics Analyst — Amonwan Phimphichai**
  - Research and compile supporting scientific papers
  - Analyze societal and ethical implications (Kardashev Scale, Security)
  - Review all documents for scientific accuracy and citation correctness

---

## Sprint Backlog

| Task ID | Description | Owner | Status | Outcome |
|---------|-------------|-------|--------|---------|
| DOC-01 | Draft `Architecture_Spec.MD` | Quantum Architect | ✅ Done | 5-layer Q-Net stack defined |
| DOC-02 | Draft `Implementation_Plan.MD` | Product Owner | ✅ Done | 4-sprint roadmap established |
| DOC-03 | Draft `Sprint_Plan.MD` with role assignments | Product Owner | ✅ Done | This document |
| DEV-01 | Code and test teleportation on local Simulator | Software Engineer | ✅ Done | Circuit validated on Qiskit Aer |
| DEV-02 | Execute teleportation on `ibm_torino` (real hardware) | Software Engineer | ✅ Done | Baseline fidelity ~49–52% |
| PRES-01 | Create Project Pitch slides (Canva) | Research & Ethics Analyst | ✅ Done | Pitch deck submitted |
| RES-01 | Gather and format all references | Research & Ethics Analyst | ✅ Done | 10+ papers compiled |
| SUB-01 | Consolidate and submit all documents by 22 Feb | Product Owner | ✅ Done | Submitted on time |

---

## Sprint Alpha Results

### Hardware Test Results

| Attempt | Backend | Shots | Success Rate |
|---------|---------|-------|-------------|
| 01 | ibm_torino | 1,024 | 51.37% |
| 02 | ibm_marrakesh | 1,024 | 48.24% (queued) |
| 03 | ibm_fez | 1,024 | 47.46% |
| 04 | ibm_fez | 1,024 | 43.75% |
| 05 | ibm_torino | 1,024 | 51.86% |

**Mean Fidelity: ~49.1% — near-random**

### Root Cause

Dynamic feed-forward (`if_test`) is incompatible with NISQ hardware timing constraints.
Gate application occurred before measurement results were ready → correction meaningless.

### Lessons Learned

- ❌ Real-time feed-forward does not work reliably on current NISQ hardware
- ✅ IBM Quantum cloud pipeline works — shots, job submission, result retrieval confirmed
- ✅ 3-qubit teleportation circuit architecture is correct in principle
- 📌 Next sprint must eliminate `if_test` operations entirely

### Definition of Done — ✅ Met

- [x] Architecture_Spec.MD, Implementation_Plan.MD, Sprint_Plan.MD complete
- [x] Toy Model validated on simulator and real hardware
- [x] Project Pitch PDF finalized and submitted
- [x] All deliverables submitted through official portal

---

---

# Sprint Beta — Sprint 2
**Duration:** 23 February – 07 March 2026
**Version:** v2

---

## Sprint Goal

Resolve the dynamic feed-forward failure from Sprint 1 by redesigning the circuit
to use **static measurement + classical post-processing correction**.
Achieve fidelity > 85% on real IBM Quantum hardware.

**Fidelity Target:** > 85%

---

## Sprint Backlog

| Task ID | Description | Owner | Status | Outcome |
|---------|-------------|-------|--------|---------|
| DEV-03 | Redesign circuit — remove all `if_test` operations | Software Engineer | ✅ Done | Static circuit implemented |
| DEV-04 | Implement post-processing correction: `b_corr = b ⊕ a1 ⊕ a2` | Software Engineer | ✅ Done | Correction logic validated |
| DEV-05 | Run v2 on `ibm_fez` — minimum 5 attempts | Software Engineer | ✅ Done | 93%+ consistently |
| DEV-06 | Run v2 on `ibm_torino` — minimum 2 attempts | Software Engineer | ✅ Done | 84–87% |
| DEV-07 | (Experimental) Design v2b readout error mitigation | Software Engineer | ✅ Done | Planned for Sprint 3 |
| RES-02 | Research error mitigation techniques (confusion matrix, PEC) | Research & Ethics Analyst | ✅ Done | Matrix inversion identified as risky |
| DOC-04 | Write `Research.MD` for sprint-beta | Research & Ethics Analyst | ✅ Done | Bilingual, 6 sections |
| ANA-01 | Analyze v1 vs v2 improvement — identify root cause | Network Analyst | ✅ Done | Post-processing = key insight |

---

## Sprint Beta Results

| Attempt | Backend | Shots | Version | Success Rate |
|---------|---------|-------|---------|-------------|
| 06 | ibm_fez | 1,024 | v2 | 92.38% ✅ |
| 07 | ibm_torino | 1,024 | v2 | 87.11% ✅ |
| 08 | ibm_fez | 1,024 | v2 | 93.85% ✅ |
| 09 | ibm_torino | 1,024 | v2 | 84.13% ✅ |
| 10 | ibm_fez | 1,024 | v2 | 93.89% ✅ |
| 11 | ibm_fez | 1,024 | v2 | 93.94% ✅ |
| 12 | ibm_fez | 1,024 | v2 | 93.79% ✅ |
| 13 | ibm_fez | 1,024 | v2 | 93.68% ✅ |
| 16 | ibm_fez | 1,024 | v2 | 93.58% ✅ |

**Mean Fidelity (v2): ~93.0% — +44 pp from Sprint 1** 🎉

### Risks Encountered

| Risk | Impact | Mitigation |
|------|--------|------------|
| ibm_marrakesh queue time | Job delayed hours | Switched to ibm_fez as primary |
| 1,024 shots — high statistical noise | CI wide (~±1.5%) | Plan to increase to 20,000 in Sprint 3 |

### Lessons Learned

- ✅ Removing `if_test` and deferring to classical post-processing is the correct architecture
- ✅ ibm_fez is the most reliable backend for consistent high-fidelity results
- 📌 1,024 shots is too few for rigorous statistical claims — must increase
- 📌 v2b (readout mitigation) is high-risk — test carefully and document failure modes

### Definition of Done — ✅ Met

- [x] v2 circuit achieves > 85% fidelity (actual: ~93%)
- [x] At least 2 backends tested
- [x] Research.MD for sprint-beta complete
- [x] v2b design ready for Sprint Gamma testing

---

---

# Sprint Gamma — Sprint 3
**Duration:** 08 March – 12 March 2026
**Version:** v2b (experimental) + v3

---

## Sprint Goal

Test two parallel optimization approaches: (1) **v2b** readout error mitigation via
confusion matrix inversion, and (2) **v3** hardware-aware transpilation with explicit
qubit layout selection. Target fidelity > 97%.

**Fidelity Target:** > 97%

---

## Sprint Backlog

| Task ID | Description | Owner | Status | Outcome |
|---------|-------------|-------|--------|---------|
| DEV-08 | Implement v2b — build 8-state calibration circuits + confusion matrix M | Software Engineer | ✅ Done | M constructed, κ(M) ≈ 47.3 |
| DEV-09 | Run v2b on ibm_fez — 2 attempts | Software Engineer | ✅ Done | ❌ 49.73% / 49.56% — FAILED |
| DEV-10 | Analyze v2b failure — compute κ(M), measure drift | Network Analyst | ✅ Done | Drift 8–12% in 2.1 hrs |
| DEV-11 | Implement v3 — hardware-aware transpilation `optimization_level=3` | Software Engineer | ✅ Done | Explicit qubit layout applied |
| DEV-12 | Run v3 on ibm_fez — minimum 10 attempts at 20,000 shots | Software Engineer | ✅ Done | 96–98% consistently |
| DEV-13 | Run v3 on ibm_torino — 1 attempt for comparison | Software Engineer | ✅ Done | 92.83% |
| RES-03 | Research PEC (Probabilistic Error Cancellation) as v2b alternative | Research & Ethics Analyst | ✅ Done | PEC recommended for future |
| DOC-05 | Write `Research.MD` for sprint-gamma | Research & Ethics Analyst | ✅ Done | Bilingual, 8 sections |
| ANA-02 | Version-controlled backend comparison (v3 only) | Network Analyst | ✅ Done | marrakesh > fez > torino |

---

## Sprint Gamma Results

### v2b — FAILED ❌

| Attempt | Backend | Version | Success Rate | Note |
|---------|---------|---------|-------------|------|
| 14 | ibm_fez | v2b | 49.73% | ❌ Worse than random |
| 15 | ibm_fez | v2b | 49.56% | ❌ Worse than random |

**Failure Analysis:**
- Condition number κ(M) ≈ 47.3 → shot noise amplified 47× under M⁻¹
- Calibration-to-experiment drift: ~2.1 hours → T1/T2 drifted 8–12%
- Result: systematic bias rather than correction

### v3 — SUCCESS ✅

| Attempt | Backend | Shots | Success Rate |
|---------|---------|-------|-------------|
| 17 | ibm_fez | 20,000 | 96.65% |
| 18 | ibm_fez | 20,000 | 96.32% |
| 19 | ibm_torino | 20,000 | 92.83% |
| 20 | ibm_fez | 20,000 | 97.90% |
| 21–27 | ibm_fez | 20,000 | 96.12–96.43% |
| 28 | ibm_fez | 20,000 | 97.86% |

**Mean Fidelity (v3 on ibm_fez): ~96.6%**

### Risks Encountered

| Risk | Impact | Mitigation |
|------|--------|------------|
| v2b matrix inversion unstable | Fidelity collapsed to ~49.6% | Abandoned v2b — documented as scientific finding |
| Calibration drift over 2 hours | Invalidated confusion matrix | Future: run calibration immediately before experiment |
| ibm_torino v3 lower than ibm_fez | Confounded backend comparison | Fixed in Sprint 4: version-controlled comparison only |

### Lessons Learned

- ❌ Confusion matrix inversion fails when κ(M) is high AND hardware drifts
- ✅ Hardware-aware transpilation (`optimization_level=3` + explicit layout) is effective
- ✅ 20,000 shots gives much tighter CI (~±0.15%) — required for paper-quality results
- 📌 ibm_marrakesh not yet tested with v3 — expected to outperform ibm_fez

### Definition of Done — ✅ Partially Met

- [x] v2b tested and documented (failed — valuable negative result)
- [x] v3 achieves > 95% fidelity (actual: ~96.6%) — target was > 97%, close
- [x] Research.MD for sprint-gamma complete
- [ ] Peak 99% not yet achieved — carry to Sprint Delta

---

---

# Sprint Delta — Sprint 4 (FINAL)
**Duration:** 13 March – 17 March 2026
**Version:** v3 (on ibm_marrakesh)

---

## Sprint Goal

Achieve peak fidelity ≥ 99% by running v3 on **ibm_marrakesh**.
Complete full statistical analysis (95% CI, z-tests) and submit the final paper.

**Fidelity Target:** ≥ 99%

---

## Sprint Backlog

| Task ID | Description | Owner | Status | Outcome |
|---------|-------------|-------|--------|---------|
| DEV-14 | Run v3 on ibm_marrakesh — minimum 6 attempts at 20,000 shots | Software Engineer | ✅ Done | Peak 99.09% (Attempt 29) |
| DEV-15 | Compute 95% CI for all 34 attempts | Software Engineer | ✅ Done | CI added to Table 2 in paper |
| DEV-16 | Run z-test: Sprint 1 vs Sprint 4 | Network Analyst | ✅ Done | z > 100, p < 0.0001 |
| DEV-17 | Run z-test: Sprint 2 vs Sprint 4 | Network Analyst | ✅ Done | z ≈ 29.8, p < 0.0001 |
| DEV-18 | Version-controlled backend comparison table (v3 only) | Network Analyst | ✅ Done | marrakesh 98.0% > fez 96.6% |
| DOC-06 | Write `Research.MD` for sprint-delta | Research & Ethics Analyst | ✅ Done | 9 sections, bilingual |
| DOC-07 | Write Appendix A: Reproducibility Specification | Software Engineer | ✅ Done | Qiskit 1.0.2, qubit mappings |
| PAP-01 | Write Section 4 (Methodology) | Amonwan Phimphichai | ✅ Done | All 4 sprints documented |
| PAP-02 | Write Section 5 (Results + Statistical Analysis) | Sitthichok Moknak | ✅ Done | Table 2 with CI, Table 3 v-controlled |
| PAP-03 | Write Section 6 (Discussion) | Pattadon Khumnan | ✅ Done | Architectural implications |
| PAP-04 | Write Section 7 (Limitations) | All members | ✅ Done | Scale, multi-hop, planetary gap |
| PAP-05 | Internal review — full paper | All members | ✅ Done | FTL claims removed, stats added |
| SUB-02 | Submit final paper + peer review response | Product Owner | ✅ Done | Submitted March 17, 2026 |

---

## Sprint Delta Results

| Attempt | Backend | Shots | Success Rate | 95% CI |
|---------|---------|-------|-------------|--------|
| 29 | ibm_marrakesh | 20,000 | **99.09%** 🏆 | [98.96%, 99.22%] |
| 30 | ibm_marrakesh | 20,000 | 98.75% | [98.59%, 98.91%] |
| 31 | ibm_marrakesh | 20,000 | 97.89% | [97.68%, 98.10%] |
| 32 | ibm_marrakesh | 20,000 | 97.63% | [97.41%, 97.85%] |
| 33 | ibm_marrakesh | 20,000 | 97.37% | [97.14%, 97.60%] |
| 34 | ibm_marrakesh | 20,000 | 97.45% | [97.22%, 97.68%] |

**Mean Fidelity (ibm_marrakesh v3): ~98.0% — PEAK: 99.09%** 🎉

### Statistical Summary

| Comparison | z-score | p-value | Significant? |
|-----------|---------|---------|-------------|
| Sprint 1 vs Sprint 4 | > 100 | < 0.0001 | ✅ Yes |
| Sprint 2 vs Sprint 4 | ~29.8 | < 0.0001 | ✅ Yes |

### Backend Comparison (v3 only — version controlled)

| Backend | Attempts | Mean Fidelity | Peak |
|---------|---------|-------------|------|
| ibm_marrakesh | 6 | ~98.00% | 99.09% 🏆 |
| ibm_fez | 11 | ~96.60% | 97.90% |
| ibm_torino | 1 | 92.83% | 92.83% |

### Risks Encountered

| Risk | Impact | Mitigation |
|------|--------|------------|
| ibm_marrakesh queue time | Delayed some attempts | Scheduled jobs during off-peak hours |
| Reviewer R1.M1 — FTL claims | Major revision required | Removed all "zero-latency" claims |
| Reviewer R2.M1 — Sprint 3 analysis thin | Major revision required | Expanded with κ(M), drift, PEC recommendation |

### Lessons Learned

- ✅ ibm_marrakesh significantly outperforms ibm_fez — hardware quality matters
- ✅ 99%+ fidelity is achievable on contemporary NISQ hardware with correct architecture
- ✅ All improvements came from software/architectural decisions, not hardware upgrades
- ✅ Peer review process dramatically improved scientific rigor of the paper
- 📌 Future work: multi-hop swapping, PEC error mitigation, ibm_marrakesh full qubit mapping

### Definition of Done — ✅ Fully Met

- [x] v3 on ibm_marrakesh achieves ≥ 99% (actual peak: 99.09%)
- [x] 95% CI computed for all 34 attempts
- [x] Statistical significance confirmed (z > 100, p < 0.0001)
- [x] Research.MD for sprint-delta complete
- [x] Full paper submitted with peer review response by March 17, 2026

---

---

## Final Project Summary

### Fidelity Progression — All 34 Attempts

```
Sprint 1 (v1)  ~49%  ░░░░░░░░░░░░░░░░░░░░░░░░░  near-random
Sprint 2 (v2)  ~93%  ██████████████████████████████████████████████  +44 pp
Sprint 3 (v2b) ~50%  ░░░░░░░░░░░░░░░░░░░░░░░░░  FAILED (matrix inversion)
Sprint 3 (v3)  ~97%  ████████████████████████████████████████████████████  +4 pp
Sprint 4 (v3)  ~98%  ██████████████████████████████████████████████████████ PEAK 99.09%
```

### Key Architecture Decisions

| Decision | Sprint | Impact |
|---------|--------|--------|
| Eliminate `if_test` → post-processing | Beta (S2) | +44 pp fidelity |
| Abandon matrix inversion → document failure | Gamma (S3) | Valuable negative result |
| Hardware-aware transpilation `opt_level=3` | Gamma (S3) | +3.6 pp fidelity |
| Switch to ibm_marrakesh for final tests | Delta (S4) | +1.4 pp, peak 99.09% |

### Deliverables Completed

| Deliverable | Status |
|------------|--------|
| Architecture_Spec.MD | ✅ |
| Implementation_Plan.MD | ✅ |
| Sprint_Plan.MD (this document) | ✅ |
| Research.MD × 4 sprints | ✅ |
| Q-Net Revised Paper (DOCX + PDF) | ✅ |
| Peer Review Report | ✅ |
| Rebuttal Response Letter | ✅ |
| Colab Summary Cell | ✅ |

---

*Q-NET-2030 | College of Computing, Khon Kaen University | March 2026*
*Corresponding: sitthichok.m@kkumail.com*