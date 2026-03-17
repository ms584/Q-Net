# 🌌 Q-Net (Quantum Entanglement Network)

![Status](https://img.shields.io/badge/Status-All%20Sprints%20Complete-brightgreen)
![Documentation](https://img.shields.io/badge/Documentation-Comprehensive-blue)
![Simulation](https://img.shields.io/badge/Simulation-Passing-brightgreen)
![Hardware](https://img.shields.io/badge/Hardware-IBM%20Quantum%20Tested-blueviolet)
![Peak Fidelity](https://img.shields.io/badge/Peak%20Fidelity-99.09%25-gold)
![Sprints](https://img.shields.io/badge/Sprints-4%20%2F%204%20Complete-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Qiskit](https://img.shields.io/badge/Qiskit-1.0.2-6929C4?logo=ibm)
![IBM Quantum](https://img.shields.io/badge/IBM%20Quantum-Heron%20r1-6929C4?logo=ibm)
![Colab](https://img.shields.io/badge/Notebook-Open%20in%20Colab-F9AB00?logo=googlecolab&logoColor=white)
![Course](https://img.shields.io/badge/Course-CP352005%20Networks-informational)
![University](https://img.shields.io/badge/KKU-College%20of%20Computing-darkred)

> **"Bridging the cosmic silence through quantum state teleportation."**

---

> [!IMPORTANT]
> **Q-Net does not achieve faster-than-light communication.**
> Both entanglement pre-distribution and classical correction channels remain bounded by *c*.
> Q-Net's advantage is the **elimination of connection-establishment overhead** (SYN/SYN-ACK/ACK),
> saving 6–44 minutes of setup time per session in Earth–Mars scenarios — not superluminal signaling.

---

## 1. Project Description

**Q-Net** is a conceptual framework for a post-Internet communication architecture designed to overcome the fundamental light-speed latency limitations of classical networks. It proposes a radical shift from electromagnetic packet switching (TCP/IP) to **Quantum State Teleportation**, enabling pre-distributed entanglement-based communication for an interplanetary civilization.

This repository contains the full architectural specification, agile implementation plans, and Python-based quantum teleportation circuits validated across **34 test attempts** on **3 real IBM Quantum backends** over **4 development sprints**, achieving a peak fidelity of **99.09%**.

---

## 2. The Problem: The Cosmic Bottleneck

Classical networking protocols fail at the interplanetary scale due to fundamental physics and design limitations:

- **The Latency Wall:** A standard TCP 3-way handshake between Earth and Mars takes 6–44 minutes, making session-oriented real-time control impossible.
- **BGP Instability:** Routing tables cannot converge over astronomical distances, leading to persistent routing challenges and data expiration.
- **Security Vulnerabilities:** Wide-beam RF signals in deep space are easily intercepted without immediate detection.

**Existing solution:** NASA's Delay-Tolerant Networking (DTN) and Bundle Protocol (RFC 9171) address store-and-forward messaging but do not eliminate per-session connection overhead. Q-Net complements DTN with two specific advantages: (1) information-theoretic security via the no-cloning theorem, and (2) reduced connection-setup latency for high-frequency session-oriented communication.

---

## 3. Core Concepts & Features

- **🔗 Pre-Distributed Entanglement:** Entangled pairs are distributed in advance, eliminating connection-setup latency when communication is needed.
- **🔒 Security by Physics:** Governed by the **No-Cloning Theorem** — any interception attempt inherently destroys the quantum state and alerts the network.
- **🧠 Cognitive Routing (Q-CAST):** A fidelity-aware pathfinding algorithm that routes connections based on quantum link quality and entanglement freshness rather than physical distance.
- **🛰️ Decentralized Infrastructure:** A resilient "Entanglement Fabric" formed by autonomous Phononic Memory satellite nodes.
- **📊 Empirically Validated:** 97–99% teleportation fidelity demonstrated on real NISQ hardware through 4 iterative development sprints.

---

## 4. Known Limitations

> [!WARNING]
> **Scale:** All experiments were conducted at **3-qubit scale**. Production quantum networks require thousands to millions of logical qubits with full quantum error correction. Our results demonstrate protocol feasibility, not network scalability.

> [!WARNING]
> **Single-Hop Only:** Fidelity degrades multiplicatively with entanglement swapping hops (F_net ≈ F₁ × F₂). Our 97–99% single-hop fidelity would be significantly lower at multi-hop scale without quantum error correction.

> [!WARNING]
> **No Planetary-Scale Distribution:** No experiment has demonstrated sustained entanglement distribution beyond LEO satellite experiments (Micius satellite, ~1,200 km). Earth-Mars entanglement distribution (56–401 million km) requires breakthroughs not yet demonstrated.

> [!NOTE]
> **Sprint 3 Failure (v2b):** Readout error mitigation via confusion matrix inversion **failed catastrophically** (~49.6%) due to matrix ill-conditioning (κ(M) ≈ 47.3) and hardware drift. This is documented as a scientific finding supporting Probabilistic Error Cancellation (PEC) over matrix inversion for NISQ hardware.

---

## 5. Architecture Overview

Q-Net replaces the traditional OSI model with a 5-layer stack dedicated to quantum state manipulation.

| Layer | Name | Core Function | Technology |
|:---:|:---|:---|:---|
| **L5** | **Application Layer** | **Reality API:** Interface for AI synchronization | Neural-Qubit Interface |
| **L4** | **Transport Layer** | **State Consistency:** End-to-end fidelity management | QTCP |
| **L3** | **Network Layer** | **Cognitive Routing:** Fidelity-aware entanglement pathfinding | Q-CAST |
| **L2** | **Link Layer** | **Reality Link:** Collapse Modulation / teleportation protocol | Bell State Measurement |
| **L1** | **Physical Layer** | **Entanglement Fabric:** Qubit generation, distribution, storage | Phononic Memory / Satellite Links |

*For in-depth technical details, refer to `docs/Architecture_Spec.MD`.*

---

## 6. Implementation & Proof of Concept

### 🔗 Full Test Run Notebook (Colab)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1zXrPBkwNGIn2XLGjwUW_jj5L3ldmKCGr?usp=sharing)

All 34 test attempts across 4 sprints — including circuit code, raw results, and the summary analysis cell.

---

### 6.1 Local Simulation (`simulation/`)

- **Environment:** `AerSimulator` (ideal, noise-free)
- **Result:** **100% Success Rate**
- **Conclusion:** Proves the mathematical and logical soundness of the teleportation circuit.

<img width="1889" height="721" alt="Simulation Result" src="https://github.com/user-attachments/assets/c158a0a2-acb5-4151-813b-c0fbe3d1a371" />

---

### 6.2 IBM Quantum Hardware — 4-Sprint Development

#### Sprint Summary

| Sprint | Version | Key Innovation | Mean Fidelity | Δ |
|--------|---------|---------------|-------------|---|
| Alpha (S1) | `v1` | Real-time feed-forward correction | ~49.1% ❌ | Baseline |
| Beta (S2) | `v2` | Post-processing correction | ~93.0% ✅ | +44 pp |
| Gamma (S3) | `v2b` | Readout error mitigation | ~49.6% ❌ | −43 pp (FAILED) |
| Gamma (S3) | `v3` | Hardware-aware transpilation | ~96.6% ✅ | +3.6 pp |
| **Delta (S4)** | **`v3`** | **ibm_marrakesh + v3** | **~98.0% ✅** | **+1.4 pp** |

#### All 34 Attempts

| Attempt | Backend | Version | Success Rate | 95% CI |
|---------|---------|---------|-------------|--------|
| 01 | ibm_torino | v1 | 51.37% | [50.68%, 52.06%] |
| 02 | ibm_marrakesh | v1 | 48.24% | — (queued) |
| 03 | ibm_fez | v1 | 47.46% | [46.77%, 48.15%] |
| 04 | ibm_fez | v1 | 43.75% | [43.06%, 44.44%] |
| 05 | ibm_torino | v1 | 51.86% | [51.17%, 52.55%] |
| 06 | ibm_fez | v2 | 92.38% | [92.01%, 92.75%] |
| 07 | ibm_torino | v2 | 87.11% | [86.57%, 87.65%] |
| 08 | ibm_fez | v2 | 93.85% | [93.52%, 94.18%] |
| 09 | ibm_torino | v2 | 84.13% | [83.54%, 84.72%] |
| 10 | ibm_fez | v2 | 93.89% | [93.56%, 94.22%] |
| 11 | ibm_fez | v2 | 93.94% | [93.61%, 94.27%] |
| 12 | ibm_fez | v2 | 93.79% | [93.46%, 94.12%] |
| 13 | ibm_fez | v2 | 93.68% | [93.35%, 94.01%] |
| 14 | ibm_fez | v2b | 49.73% ❌ | [49.04%, 50.42%] |
| 15 | ibm_fez | v2b | 49.56% ❌ | [48.87%, 50.25%] |
| 16 | ibm_fez | v2 | 93.58% | [93.24%, 93.92%] |
| 17 | ibm_fez | v3 | 96.65% | [96.40%, 96.90%] |
| 18 | ibm_fez | v3 | 96.32% | [96.06%, 96.58%] |
| 19 | ibm_torino | v3 | 92.83% | [92.46%, 93.20%] |
| 20 | ibm_fez | v3 | 97.90% | [97.70%, 98.10%] |
| 21–27 | ibm_fez | v3 | 96.12–96.43% | ~[95.85%, 96.70%] |
| 28 | ibm_fez | v3 | 97.86% | [97.66%, 98.06%] |
| **29** | **ibm_marrakesh** | **v3** | **99.09% 🏆** | **[98.96%, 99.22%]** |
| 30 | ibm_marrakesh | v3 | 98.75% | [98.59%, 98.91%] |
| 31 | ibm_marrakesh | v3 | 97.89% | [97.68%, 98.10%] |
| 32 | ibm_marrakesh | v3 | 97.63% | [97.41%, 97.85%] |
| 33 | ibm_marrakesh | v3 | 97.37% | [97.14%, 97.60%] |
| 34 | ibm_marrakesh | v3 | 97.45% | [97.22%, 97.68%] |

#### Statistical Validation

| Comparison | z-score | p-value |
|-----------|---------|---------|
| Sprint 1 vs Sprint 4 | > 100 | < 0.0001 ✅ |
| Sprint 2 vs Sprint 4 | ~29.8 | < 0.0001 ✅ |

#### Backend Comparison (v3 — version controlled)

| Backend | Qubits | Processor | Mean Fidelity (v3) | Peak |
|---------|--------|-----------|-------------------|------|
| ibm_marrakesh | 156 | Heron r1 | ~98.00% | **99.09%** 🏆 |
| ibm_fez | 156 | Heron r1 | ~96.60% | 97.90% |
| ibm_torino | 133 | Heron r1 | 92.83% | 92.83% |

---

### 6.3 How to Run

1. **Install Prerequisites:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Run Local Simulation:**
   ```bash
   python simulation/teleport_simulation.py
   ```
3. **Run on IBM Hardware** *(Requires IBM Quantum API token):*
   ```bash
   python IBM_Quantum/teleport_test_on_ibm_quantum.py
   ```
4. **View Full Test Run & Summary:**
   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1zXrPBkwNGIn2XLGjwUW_jj5L3ldmKCGr?usp=sharing)

---

## 7. Repository Structure

```text
Q-NET/
│
├── README.md                        # This file
├── LICENSE                          # MIT License
├── CITATION.cff                     # Citation metadata (GitHub "Cite this repo" button)
├── CONTRIBUTING.md                  # How to contribute
├── requirements.txt                 # Python dependencies
│
├── docs/
│   ├── Architecture_Spec.MD
│   ├── Implementation_Plan.MD
│   └── Sprint_Plan.MD
│
├── sprint-alpha/
│   ├── ibm_quantum/                 # Sprint 1 — v1 hardware execution
│   ├── simulation/                  # AerSimulator test
│   └── Research.md
│
├── sprint-beta/
│   ├── ibm_quantum/                 # Sprint 2 — v2 hardware execution
│   └── Research.md
│
├── sprint-gamma/
│   ├── ibm_quantum/                 # Sprint 3 — v2b (failed) + v3
│   └── Research.md
│
├── sprint-delta/
│   ├── ibm_quantum/                 # Sprint 4 — v3 on ibm_marrakesh
│   └── Research.md
│
└── .gitignore
```

---

## 8. Experimental Environment

| Parameter | Value |
|-----------|-------|
| Qiskit | 1.0.2 |
| qiskit-ibm-runtime | 0.20.0 |
| Shots per run | up to 20,000 |
| Transpiler optimization_level | 3 (Sprint 4) |
| ibm_fez qubit mapping | [q0→0, q1→1, q2→2] |
| ibm_marrakesh qubit mapping | [q0→0, q1→3, q2→4] |

---

## 9. Team & Contributors

| Role | Name | Student ID |
|------|------|-----------|
| Product Owner / Strategist ⭐ | Sitthichok Moknak | 673380428-6 |
| Quantum Architect | Pattadon Khumnan | 673380416-3 |
| Software Engineer | Nattaphat Chamtakhu | 673380583-4 |
| Network Analyst | Sorawit Sukongchareun | 673380606-8 |
| Research & Ethics Analyst | Amonwan Phimphichai | 673380608-4 |

---

## 10. Academic Paper

This repository supports the paper:

> **"Q-Net: Quantum Entanglement-Based Post-Internet Architecture — Hardware Implementation and Teleportation Fidelity Analysis on IBM Quantum Systems"**
> Pattadon Khumnan, Sitthichok Moknak, Nattaphat Chamtakhu, Sorawit Sukongchareun, Amonwan Phimphichai
> CP352005 Computer Networks | College of Computing, Khon Kaen University | March 2026

---

## 11. Citation

If you use this work in your research or coursework, please cite:

```bibtex
@software{qnet2026,
  author    = {Moknak, Sitthichok and
               Khumnan, Pattadon and
               Chamtakhu, Nattaphat and
               Sukongchareun, Sorawit and
               Phimphichai, Amonwan},
  title     = {{Q-Net: Quantum Entanglement-Based Post-Internet Architecture}},
  year      = {2026},
  publisher = {GitHub},
  url       = {https://github.com/YOUR_USERNAME/Q-NET},
  note      = {CP352005 Computer Networks,
               College of Computing, Khon Kaen University.
               Peak teleportation fidelity: 99.09\% on ibm\_marrakesh}
}
```

> You can also use the **"Cite this repository"** button on the GitHub sidebar,
> powered by [`CITATION.cff`](./CITATION.cff).

---

## 12. Acknowledgements

We gratefully acknowledge:

- **[IBM Quantum](https://quantum.ibm.com)** — for free cloud access to ibm_torino, ibm_fez, and ibm_marrakesh (Heron r1 processors) through the IBM Quantum Network.
- **[Qiskit Community](https://github.com/Qiskit)** — for the open-source framework that made this empirical work possible.
- **College of Computing, Khon Kaen University** — for academic resources and support.
- **CP352005 Computer Networks Instructor** — for the course structure that motivated the Q-Net concept and iterative sprint methodology.
- **Bennett et al. (1993)** and **Bouwmeester et al. (1997)** — whose foundational quantum teleportation work this project builds upon.

---

## 13. Contributing

Contributions, new backend experiments, and bug reports are welcome!
See [`CONTRIBUTING.md`](./CONTRIBUTING.md) for full guidelines.

---

## 14. License

This project is licensed under the **MIT License** — see [`LICENSE`](./LICENSE) for details.

---

*Developed as part of CP352005 Computer Networks | College of Computing, Khon Kaen University*
*Corresponding: sitthichok.m@kkumail.com*