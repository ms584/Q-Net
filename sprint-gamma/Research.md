# 🔬 Q-Net Sprint Gamma — Research Notes
> **Sprint 3 of 4** | Q-NET-2030 | College of Computing, Khon Kaen University  
> ทีมวิจัย: พัทธดนย์ คํานัน · สิทธิโชค มุขนาค · ณัฐภัทร ฉ่ำตะคุ · สรวิศ สุคงเจริญ · อมลวรรณ พิมพิชัย

---

## 1. Sprint Beta Review — สรุปผล Sprint 2 ที่ผ่านมา

### 1.1 What We Built / สิ่งที่ทำใน Sprint 2

Sprint 2 (beta) แก้ปัญหา dynamic feed-forward โดยเปลี่ยนเป็น **static circuit + classical post-processing correction**
สูตร correction: `b_corr = b ⊕ a1 ⊕ a2`

### 1.2 Results Summary / ผลลัพธ์

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

**Mean Sprint 2 Fidelity (v2): ~93.0% — +44 pp improvement from Sprint 1**

### 1.3 Key Wins / สิ่งที่สำเร็จ

- ✅ Eliminated `if_test` operations — static circuit เสถียรกว่ามาก
- ✅ Post-processing correction ทำงานได้ถูกต้องตามทฤษฎี
- ✅ ibm_fez เป็น primary backend ที่ให้ผลดีที่สุด (~93.7% mean)
- ✅ Validated core Q-Net Layer-2 teleportation protocol

### 1.4 Remaining Gap / ช่องว่างที่ยังเหลือ

> **ปัจจุบันอยู่ที่ ~93% — เป้าหมายคือ 97%+ สำหรับ production-grade Q-Net**

สาเหตุที่ยังไม่ถึง 97%:
1. **Readout errors** — qubit measurement บางครั้งอ่านค่าผิด (0→1 หรือ 1→0)
2. **Gate errors** — CNOT gate มี error rate ~0.5–1% บน NISQ
3. **Generic qubit mapping** — ยังไม่ได้เลือก physical qubit ที่ noise ต่ำที่สุด

---

## 2. Sprint Gamma Objectives — เป้าหมาย Sprint 3

### 2.1 Core Problems to Solve

**โจทย์ที่ 1 — Readout Error Mitigation (v2b):**
> ลด systematic readout errors ด้วย confusion matrix inversion
> เป้าหมาย: fidelity ขึ้นจาก 93% → 95%+

**โจทย์ที่ 2 — Hardware-Aware Transpilation (v3):**
> เลือก physical qubits ที่มี error rate ต่ำที่สุดจาก calibration data
> เป้าหมาย: fidelity ขึ้นจาก 93% → 97%+

### 2.2 Sprint Gamma Goals

- [ ] Implement **v2b**: confusion matrix calibration + inversion correction
- [ ] Analyze v2b results — document κ(M) และ calibration drift
- [ ] Implement **v3**: hardware-aware transpilation ด้วย `optimization_level=3`
- [ ] ทดสอบ v3 บน ibm_fez และ ibm_marrakesh
- [ ] เพิ่ม shots เป็น **20,000** เพื่อ statistical significance
- [ ] เพิ่ม 95% confidence intervals ในผลลัพธ์ทุก attempt

---

## 3. Technical Approach — แนวทาง Technical

### 3.1 v2b: Readout Error Mitigation via Confusion Matrix

**แนวคิด:** สร้าง 8×8 confusion matrix M จาก calibration circuits
แล้วใช้ M⁻¹ correct systematic readout errors

```python
from qiskit.primitives import Sampler
import numpy as np

# ── Step 1: สร้าง calibration circuits สำหรับทุก basis state ──
def build_calibration_circuits():
    cal_circuits = []
    for state in range(2**3):  # 8 states: 000, 001, ..., 111
        qc = QuantumCircuit(3, 3)
        bits = format(state, '03b')
        for i, bit in enumerate(bits):
            if bit == '1':
                qc.x(i)
        qc.measure([0, 1, 2], [0, 1, 2])
        cal_circuits.append(qc)
    return cal_circuits

# ── Step 2: รัน calibration และสร้าง confusion matrix ──
def build_confusion_matrix(cal_results, shots=20000):
    M = np.zeros((8, 8))
    for j, result in enumerate(cal_results):
        counts = result.get_counts()
        for bitstring, count in counts.items():
            i = int(bitstring, 2)
            M[i, j] = count / shots
    return M

# ── Step 3: Apply M⁻¹ correction ──
def apply_mitigation(raw_counts, M_inv, shots):
    raw_vector = np.zeros(8)
    for bitstring, count in raw_counts.items():
        idx = int(bitstring, 2)
        raw_vector[idx] = count / shots
    corrected = M_inv @ raw_vector
    corrected = np.clip(corrected, 0, None)  # no negative probabilities
    corrected /= corrected.sum()             # renormalize
    return corrected
```

> ⚠️ **ความเสี่ยงที่ต้องติดตาม:**

| ความเสี่ยง | คำอธิบาย | วิธีตรวจสอบ |
|-----------|---------|------------|
| High condition number | κ(M) สูง → inversion unstable | `np.linalg.cond(M)` ควร < 10 |
| Calibration drift | T1/T2 drift ระหว่าง calibration และ experiment | บันทึก timestamp, รัน calibration ใกล้ experiment |
| Negative probabilities | M⁻¹ อาจให้ค่าติดลบ | `np.clip(corrected, 0, None)` |

### 3.2 v3: Hardware-Aware Transpilation ⭐

**แนวคิด:** แทนที่จะให้ Qiskit เลือก physical qubits เอง
เราเลือกเองโดยดูจาก calibration data ของแต่ละ backend

```python
from qiskit import transpile
from qiskit_ibm_runtime import QiskitRuntimeService

# ── Step 1: ดึง calibration data ──
service = QiskitRuntimeService()
backend = service.backend("ibm_fez")
props = backend.properties()

# ── Step 2: หา qubit pair ที่มี CNOT error ต่ำที่สุด ──
def find_best_qubits(backend, n_qubits=3):
    props = backend.properties()
    best_error = float('inf')
    best_layout = None
    coupling_map = backend.coupling_map

    for edge in coupling_map.get_edges():
        q0, q1 = edge
        cnot_err = props.gate_error('cx', [q0, q1])
        t1_q0 = props.t1(q0)
        t1_q1 = props.t1(q1)
        score = cnot_err / (t1_q0 * t1_q1)  # lower = better
        if score < best_error:
            best_error = score
            best_layout = [q0, q1, q1+1]  # q2 adjacent to q1
    return best_layout

# ── Step 3: Transpile ด้วย explicit layout ──
best_layout = find_best_qubits(backend)

optimized_circuit = transpile(
    teleport_circuit,
    backend=backend,
    optimization_level=3,
    initial_layout=best_layout,  # e.g., [0, 1, 2] สำหรับ ibm_fez
)

# ibm_fez:       best layout → [0, 1, 2]
# ibm_marrakesh: best layout → [0, 3, 4]
```

**ทำไม ibm_marrakesh ถึง layout [0, 3, 4]:**
```
ibm_marrakesh coupling map (simplified):
0 ─── 1 ─── 2
      │
      3 ─── 4 ─── 5

qubit 0→3 และ 3→4 มี CNOT error ต่ำที่สุดในช่วงที่ทดสอบ
```

### 3.3 Statistical Analysis Framework

Sprint Gamma เพิ่ม shots จาก 1,024 → **20,000** พร้อม 95% CI:

```python
import numpy as np
from scipy import stats

def compute_stats(success_rate_pct, shots=20000):
    p = success_rate_pct / 100
    se = np.sqrt(p * (1 - p) / shots)
    ci_95 = (p - 1.96*se, p + 1.96*se)
    return {
        "success_rate": p,
        "std_error": se,
        "ci_95_low":  ci_95[0] * 100,
        "ci_95_high": ci_95[1] * 100,
    }

# ตัวอย่าง: attempt 29 — 99.09% ที่ 20,000 shots
stats_29 = compute_stats(99.09, shots=20000)
# → CI = [98.96%, 99.22%]

# z-test: Sprint 1 vs Sprint 4
def z_test_two_proportions(p1, p2, n1, n2):
    p_pool = (p1*n1 + p2*n2) / (n1 + n2)
    se = np.sqrt(p_pool*(1-p_pool)*(1/n1 + 1/n2))
    z = (p2 - p1) / se
    p_value = 2 * (1 - stats.norm.cdf(abs(z)))
    return z, p_value
```

---

## 4. Expected Results — ผลที่คาดหวัง

### 4.1 v2b Prediction (Readout Mitigation)

> 🔴 **ทีมคาดว่า v2b อาจล้มเหลว** — แต่ต้องทดสอบเพื่อ document เป็น scientific finding

| Scenario | ผลที่คาดหวัง | สาเหตุ |
|----------|------------|--------|
| κ(M) < 10, drift < 2% | fidelity ขึ้น → 95%+ | matrix inversion stable |
| κ(M) > 20, drift > 5% | fidelity ลด → ~50% | inversion amplifies noise |
| Calibration ทำไม่ถูก | fidelity ลด → random | M ไม่ represent noise จริง |

### 4.2 v3 Prediction (Hardware-Aware Transpilation)

> 🟢 **ทีมมั่นใจว่า v3 จะให้ผลดีกว่า v2**

- ibm_fez (v3): คาดว่า ~96–98%
- ibm_marrakesh (v3): คาดว่า ~98–99%
- Peak: อาจแตะ 99%+ ถ้า qubit selection โชคดี

---

## 5. References — เอกสารอ้างอิง

### 5.1 Error Mitigation

1. **Temme, Bravyi & Gambetta (2017)** — *Error Mitigation for Short-Depth Quantum Circuits*  
   Physical Review Letters, 119, 180509  
   → ทฤษฎีพื้นฐานของ probabilistic error cancellation (PEC) ที่ดีกว่า matrix inversion

2. **Kandala et al. (2019)** — *Error mitigation extends the computational reach of a noisy quantum processor*  
   Nature, 567, 491–495  
   → การประยุกต์ใช้ error mitigation บน real NISQ hardware

3. **van den Berg et al. (2023)** — *Probabilistic error cancellation with sparse Pauli–Lindblad models on noisy quantum processors*  
   Nature Physics, 19, 1116–1121  
   → PEC approach ที่ robust กว่า confusion matrix inversion

### 5.2 Transpilation & Qubit Mapping

4. **Cowtan et al. (2019)** — *On the qubit routing problem*  
   TQC 2019, LIPIcs, 135, 5:1–5:32  
   → algorithms สำหรับ optimal qubit routing บน coupling maps

5. **Tannu & Qureshi (2019)** — *Not All Qubits Are Created Equal: A Case for Variability-Aware Policies for NISQ-Era Quantum Computers*  
   ASPLOS 2019  
   → พิสูจน์ว่าการเลือก qubit ที่ถูกต้องเพิ่ม fidelity ได้ 2–3×

6. **IBM Quantum (2024)** — *Qiskit Transpiler Documentation*  
   → `optimization_level=3` และ `initial_layout` API

### 5.3 Statistical Methods for Quantum Experiments

7. **Helsen et al. (2022)** — *A general framework for randomized benchmarking*  
   PRX Quantum, 3, 020357  
   → statistical framework สำหรับ benchmarking quantum hardware

8. **Flammia & Liu (2011)** — *Direct Fidelity Estimation from Few Pauli Measurements*  
   Physical Review Letters, 106, 230501  
   → วิธีประมาณ fidelity จาก measurement data

### 5.4 IBM Hardware

9. **Maronese et al. (2022)** — *Quantum activation functions for quantum neural networks*  
   Quantum Information Processing, 21, 128  
   → การใช้ Heron processor ใน real experiments

10. **Qiskit IBM Runtime (2024)** — *qiskit-ibm-runtime 0.20.0 Release Notes*  
    GitHub: Qiskit/qiskit-ibm-runtime  
    → API changes ที่ affect `Sampler` และ `optimization_level`

---

## 6. Failure Mode Documentation — บันทึก v2b Failure (ถ้าเกิดขึ้น)

> ส่วนนี้จะ fill in หลังจากรัน v2b จริง

### 6.1 Template: Confusion Matrix Analysis

```
Confusion Matrix M (8×8):
[[ ?, ?, ?, ?, ?, ?, ?, ? ],
 ...fill after experiment...]

Condition Number κ(M): ___________
Calibration timestamp: ___________
Experiment timestamp:  ___________
Drift interval:        ___________ hours
Estimated T1 drift:    ___________  %
Estimated T2 drift:    ___________  %

Result: v2b mean fidelity = ___________  %
Conclusion: [ ] Stable  [ ] Degraded  [ ] Failed (random)
```

### 6.2 Why Document Failure?

> ผลลัพธ์ที่ล้มเหลวมีคุณค่าทางวิทยาศาสตร์เท่ากับผลที่สำเร็จ

- พิสูจน์ว่า confusion matrix inversion ไม่เหมาะกับ NISQ hardware ที่มี drift
- เป็น evidence สนับสนุนการใช้ PEC แทนใน future work
- Reviewers จะถามเรื่องนี้ — ต้องมีคำตอบที่ชัดเจน

---

## 7. Next Steps — Sprint Delta (Sprint 4) Plan

### 7.1 ถ้า v3 ทำงานได้ตามเป้า (≥ 97%)

- [ ] รัน v3 บน ibm_marrakesh อย่างน้อย 5 attempts
- [ ] เปรียบเทียบ ibm_fez vs ibm_marrakesh ด้วย code version เดียวกัน
- [ ] คำนวณ 95% CI และ z-test สำหรับ improvement claims
- [ ] เขียน paper draft Section 4 (Methodology) และ Section 5 (Results)

### 7.2 Sprint Delta Goals

| Target | Value |
|--------|-------|
| Peak Fidelity | ≥ 99% |
| Mean Fidelity (v3) | ≥ 97% |
| Primary Backend | ibm_marrakesh |
| Shots | 20,000 |
| Statistical | 95% CI + z-test (Sprint 1 vs Sprint 4, p < 0.0001) |
| Deliverable | Complete paper draft + peer review submission |

### 7.3 Paper Writing Timeline

```
Sprint Gamma end     → Section 4.3 (Sprint 3 analysis) complete
Sprint Delta week 1  → Section 5 (Results + Stats) complete  
Sprint Delta week 2  → Full paper draft + internal review
Submission date      → March 17, 2026
```

---

## 8. Lessons Learned — บทเรียนจาก Sprint 1–2

| Sprint | บทเรียน | นำไปใช้ใน Sprint 3 |
|--------|---------|-------------------|
| Sprint 1 | Dynamic feed-forward ไม่เสถียรบน NISQ | ✅ ใช้ static circuit ทั้งหมด |
| Sprint 2 | Post-processing correction ทำงานได้ | ✅ ต่อยอดใน v3 |
| Sprint 2 | 1,024 shots noise สูง | ✅ เพิ่มเป็น 20,000 shots |
| Sprint 2 | Generic qubit mapping ให้ผลต่างกันมาก | ✅ ใช้ hardware-aware layout |

---

*Last updated: March 2026 | Q-NET-2030 Sprint Gamma*