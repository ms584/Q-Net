# 🌌 Q-Net (Quantum Entanglement Network)

![Status](https://img.shields.io/badge/Status-Sprint%20Alpha%20Complete-brightgreen)
![Documentation](https://img.shields.io/badge/Documentation-Comprehensive-blue)
![Simulation](https://img.shields.io/badge/Simulation-Passing-brightgreen)
![Hardware](https://img.shields.io/badge/Hardware-IBM%20Quantum%20Tested-blueviolet)

> **"Bridging the cosmic silence through instantaneous state teleportation."**

---

## 1. Project Description

**Q-Net** is a conceptual framework for a post-Internet communication architecture designed to overcome the fundamental light-speed latency limitations of classical networks. It proposes a radical shift from electromagnetic packet switching (TCP/IP) to **Quantum State Teleportation**, enabling effective zero-latency communication for an interplanetary civilization.

This repository contains the full architectural specification, agile implementation plans, and Python-based "Toy Models" validated on both **local simulators** and **real IBM Quantum Hardware**.

---

## 2. The Problem: The Cosmic Bottleneck

Classical networking protocols fail at the interplanetary scale due to fundamental physics and design limitations:
- **The Latency Wall:** The speed of light is too slow. A standard TCP 3-way handshake between Earth and Mars can take up to 45 minutes, rendering real-time system control impossible.
- **BGP Instability:** Routing tables cannot converge over astronomical distances, leading to infinite routing loops and data packet expiration.
- **Security Vulnerabilities:** Wide-beam radio frequency (RF) signals in deep space are easily intercepted by adversaries without immediate detection.

Q-Net addresses these critical bottlenecks at a foundational, physical level.

---

## 3. Core Concepts & Features

- **🚀 Zero-Latency Communication:** Information is transmitted instantaneously via the collapse of an entangled quantum state, bypassing the speed of light.
- **🔒 Security by Physics:** Governed by the **No-Cloning Theorem**, passive eavesdropping is physically impossible. Any interception attempt inherently destroys the data and alerts the network.
- **🧠 Cognitive Routing (Q-CAST):** An AI-driven pathfinding algorithm that routes connections based on quantum link fidelity rather than physical distance.
- **🛰️ Decentralized Infrastructure:** A resilient "Entanglement Fabric" formed by autonomous quantum repeater satellites.

---

## 4. Architecture Overview

The Q-Net architecture replaces the traditional OSI model with a 5-layer stack dedicated to quantum state manipulation.

| Layer | Name                  | Core Function                                    |
| :---: | :-------------------- | :----------------------------------------------- |
| **L5**| **Application Layer** | **Reality API:** Interface for AI/Human consciousness sync. |
| **L4**| **Transport Layer**   | **State Consistency:** Manages end-to-end fidelity and purification. |
| **L3**| **Network Layer**     | **Cognitive Routing:** Finds the optimal path of entangled pairs. |
| **L2**| **Link Layer**        | **Reality Link:** Executes the core teleportation protocol. |
| **L1**| **Physical Layer**    | **Entanglement Fabric:** Generates, distributes, and stores entangled pairs. |

*For in-depth technical details, please refer to `docs/Architecture_Spec.MD`.*

---

## 5. Implementation & Proof of Concept

To provide a proof-of-concept for the "Reality Link" (Layer 2), we developed a 3-qubit quantum teleportation circuit to send a payload state (`|1⟩`) from Node A to Node B. We tested this on two different environments:

### 5.1 Local Simulation (`simulation/`)
- **Environment:** `AerSimulator` (Ideal conditions).
- **Result:** **100% Success Rate.**
- **Conclusion:** Proves the mathematical and logical soundness of the Q-Net routing and teleportation architecture.

<img width="1889" height="721" alt="Image" src="https://github.com/user-attachments/assets/c158a0a2-acb5-4151-813b-c0fbe3d1a371" />

### 5.2 IBM Quantum Hardware Execution (`IBM_Quantum/`)
- **Environment:** `ibm_torino` (Real 133-qubit quantum processor).
- **Result:** **~51.36% Success Rate.**
- **Academic Insight:** The drop in success rate on real hardware is expected due to **Quantum Noise and Decoherence** (Thermal Relaxation) during the mid-circuit measurement delay. This real-world limitation experimentally proves exactly *why* Q-Net's **Layer 1 (Phononic Memory)** and **Layer 4 (State Consistency/Error Correction)** are absolutely required for the network to function in reality.

*For detailed circuit architecture and implementation specifications, refer to docs/Architecture_Spec.md.*

### 5.3 How to Run
1. **Install Prerequisites:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Run Local Simulation:**
   ```bash
   python simulation/teleport_simulation.py
   ```
3. **Run on IBM Hardware (Requires IBM Cloud Token):**
   ```bash
   python IBM_Quantum/teleport_test_on_ibm_quantum.py
   ```

---

## 6. Repository Structure

This project is organized as follows:

```text
Q-Net_Project/
|
├── README.md                   # Main documentation and project overview.
├── requirements.txt            # Python dependencies (Qiskit, Runtime, etc.).
|
├── docs/                       # Project documentation and specifications.
|   ├── Architecture_Spec.MD    
|   ├── Implementation_Plan.MD  
|   └── Sprint_Plan.MD          
|
├── IBM_Quantum/                # Real Hardware Execution.
|   ├── Result-01_Measurement-Result.png
|   ├── Result-01_Teleportation-Success-Rate.png
|   └── teleport_test_on_ibm_quantum.py
|
└── simulation/                 # Local Ideal Simulation.
    ├── Result_Simulation-01.png
    ├── qnet_circuit.png        
    ├── qnet_histogram.png      
    └── teleport_simulation.py  
```

---

## 7. Team & Contributors (Sprint Alpha)

- **Quantum Architect:** [Pattadon Khumnan 673380416-3]
- **Product Owner / Strategist:** [Sitthichok Moknak 673380428-6]
- **Software Engineer:** [Nattapat Chamtakhu 673380583-4]
- **Network Analyst:** [Sorawit Sukongchareun 673380606-8]
- **Research & Ethics Analyst:** [Amonwan Phimphichai 673380608-4]

---
*This conceptual project was developed as part of the CP352005 Networks course.*
