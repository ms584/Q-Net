# 🔬 Q-Net Sprint Beta — Research Notes
> **Sprint 2 of 4** | Q-NET-2030 | College of Computing, Khon Kaen University  
> ทีมวิจัย: พัทธดนย์ คํานัน · สิทธิโชค มุขนาค · ณัฐภัทร ฉ่ำตะคุ · สรวิศ สุคงเจริญ · อมลวรรณ พิมพิชัย

---

## 1. Sprint Alpha Review — สรุปผล Sprint 1 ที่ผ่านมา

### 1.1 What We Built / สิ่งที่ทำใน Sprint 1

Sprint 1 (alpha) สร้าง baseline quantum teleportation circuit บน IBM Quantum hardware
โดยใช้ real-time classical feed-forward correction ผ่าน `if_test` operations

**Circuit Design:**
- `q0` — payload qubit (state to teleport)
- `q1` — Alice's entanglement qubit
- `q2` — Bob's receiver qubit
- Bell pair preparation → Bell-state measurement → conditional X/Z corrections

### 1.2 Results Summary / ผลลัพธ์

| Attempt | Backend | Shots | Success Rate |
|---------|---------|-------|-------------|
| 01 | ibm_torino | 1,024 | 51.37% |
| 02 | ibm_marrakesh | 1,024 | 48.24% (queued) |
| 03 | ibm_fez | 1,024 | 47.46% |
| 04 | ibm_fez | 1,024 | 43.75% |
| 05 | ibm_torino | 1,024 | 51.86% |

**Mean Sprint 1 Fidelity: ~49.1% — near-random performance**

### 1.3 Root Cause Analysis / สาเหตุที่ล้มเหลว

> ❌ **Dynamic feed-forward is incompatible with current NISQ hardware timing**

NISQ hardware ไม่รองรับ mid-circuit measurement + feed-forward gate application
อย่างเสถียร เนื่องจาก:

1. **Firmware timing constraint** — gate application เกิดขึ้นก่อน measurement result พร้อม
2. **Mid-circuit measurement latency** — delay ระหว่าง measure → classical bit → gate
3. **Coherence decay** — qubit decohere ระหว่างรอ classical correction

```
Timeline ที่ต้องการ (ideal):
measure q0,q1 → classical bits → apply X/Z to q2

Timeline จริงบน NISQ:
measure q0,q1 ──────────────────────────────→ result ready
apply gate to q2 ──→ (applied BEFORE result!)  ← ปัญหา
```

---

## 2. Sprint Beta Objectives — เป้าหมาย Sprint 2

### 2.1 Core Problem to Solve

**โจทย์หลัก:** ทำให้ teleportation fidelity ขึ้นจาก ~49% → 90%+ โดยไม่ต้องพึ่ง dynamic feed-forward

### 2.2 Hypothesis / สมมติฐาน

> ถ้าย้าย correction logic ออกจาก quantum circuit ไปไว้ใน classical post-processing
> hardware จะไม่ต้องทำ real-time feed-forward อีกต่อไป และ fidelity ควรจะเพิ่มขึ้นอย่างมีนัยสำคัญ

### 2.3 Sprint Beta Goals

- [ ] ออกแบบ **static circuit** ที่ไม่มี `if_test` operations
- [ ] implement **classical post-processing correction**: `b_corr = b ⊕ a1 ⊕ a2`
- [ ] ทดสอบบน ibm_fez และ ibm_torino ด้วย shots ที่มากขึ้น
- [ ] เปรียบเทียบ fidelity กับ Sprint 1 baseline
- [ ] Document failure modes ที่พบ

---

## 3. Technical Approach — แนวทาง Technical

### 3.1 v2 Architecture: Static Circuit + Post-Processing

**Key insight:** แทนที่จะให้ quantum hardware แก้ qubit ตาม measurement result
เราวัด qubit ทั้งหมดพร้อมกัน แล้วค่อย correct ทาง classical computation

```python
# v1 (Sprint 1) — BROKEN on NISQ
with if_test((creg, 1)):      # ← feed-forward ปัญหา
    qc.x(q2)
with if_test((creg, 2)):
    qc.z(q2)

# v2 (Sprint 2) — Static circuit, no if_test
qc.measure([q0, q1, q2], [c0, c1, c2])

# Classical post-processing correction
# b_corr = bob's bit XOR alice_bit1 XOR alice_bit2
b_corr = b ^ a1 ^ a2          # ← correction เกิดใน Python, ไม่ใช่ hardware
```

**ทำไม XOR correction ถูกต้อง:**

ใน standard teleportation protocol:
- ถ้า Alice วัดได้ `|00⟩` → Bob ไม่ต้อง correct (apply I)
- ถ้า Alice วัดได้ `|01⟩` → Bob apply X
- ถ้า Alice วัดได้ `|10⟩` → Bob apply Z  
- ถ้า Alice วัดได้ `|11⟩` → Bob apply XZ

เมื่อเราส่ง `|1⟩` state แล้วใช้ XOR: `b_corr = b ⊕ a1 ⊕ a2`
ผล bit ที่ corrected จะตรงกับ payload state ที่ส่งไป

### 3.2 v3 Architecture: Hardware-Aware Transpilation (เป้าหมายปลาย Sprint)

ถ้า v2 ได้ผลดี จะต่อยอดด้วย:

```python
# ระบุ qubit layout ที่มี error rate ต่ำที่สุดจาก calibration data
from qiskit.transpiler import CouplingMap
from qiskit import transpile

optimized_circuit = transpile(
    qc,
    backend=backend,
    optimization_level=3,          # ← highest optimization
    initial_layout=[0, 1, 2],      # ← เลือก physical qubits ที่ดีที่สุด
)
```

**วิธีเลือก qubit ที่ดี:**
1. เปิด IBM Quantum dashboard → backend calibration
2. ดู 2-qubit gate error rate (CNOT error)
3. เลือก qubit pair ที่มี error ต่ำที่สุด
4. ระบุใน `initial_layout`

### 3.3 v2b Branch: Readout Error Mitigation (Experimental — อาจล้มเหลว)

> ⚠️ **สาขานี้เป็น experimental** — อาจ produce degraded results

แนวคิด: สร้าง confusion matrix เพื่อ correct systematic readout errors

```python
# สร้าง calibration circuits สำหรับทุก basis state
cal_circuits = []
for state in range(2**3):  # 8 states สำหรับ 3 qubits
    qc_cal = QuantumCircuit(3, 3)
    for i, bit in enumerate(format(state, '03b')):
        if bit == '1':
            qc_cal.x(i)
    qc_cal.measure_all()
    cal_circuits.append(qc_cal)

# M[i,j] = P(measure i | prepared j)
# b_corrected = M_inverse @ b_raw
```

**ความเสี่ยง:**
- Condition number κ(M) สูง → matrix inversion unstable
- Hardware drift ระหว่าง calibration และ experiment
- อาจ amplify noise แทนที่จะ suppress

---

## 4. References — เอกสารอ้างอิง

### 4.1 Core Quantum Teleportation

1. **Bennett et al. (1993)** — *Teleporting an unknown quantum state via dual classical and EPR channels*  
   Physical Review Letters, 70(13), 1895  
   → ทฤษฎีพื้นฐานของ quantum teleportation ทั้งหมด

2. **Bouwmeester et al. (1997)** — *Experimental quantum teleportation*  
   Nature, 390(6660), 575–579  
   → การพิสูจน์เชิงทดลองครั้งแรก

### 4.2 NISQ Hardware & Error Mitigation

3. **Preskill, J. (2018)** — *Quantum computing in the NISQ era and beyond*  
   Quantum, 2, 79  
   → ขอบเขตและข้อจำกัดของ NISQ hardware ที่เราใช้งานอยู่

4. **IBM Quantum (2024)** — *IBM Quantum System Two and Heron processor: Technical overview*  
   IBM Research  
   → spec ของ ibm_torino / ibm_fez / ibm_marrakesh

5. **Qiskit Development Team (2024)** — *Qiskit: An open-source framework for quantum computing*  
   Zenodo. doi:10.5281/zenodo.2562111  
   → documentation ของ library ที่ใช้

### 4.3 Quantum Internet Architecture

6. **Wehner, Elkouss & Hanson (2018)** — *Quantum internet: A vision for the road ahead*  
   Science, 362(6412), eaam9288  
   → layer model ที่ Q-Net อ้างอิง

7. **Kozlowski, Wehner & Van Meter (2023)** — *Architectural Principles for a Quantum Internet*  
   RFC 9340, IRTF  
   → มาตรฐาน protocol stack สำหรับ quantum internet

8. **Illiano, Caleffi & Cacciapuoti (2024)** — *Quantum Internet Protocol Stack: A Comprehensive Survey*  
   Computer Networks, 203, 108660  
   → survey ครบที่สุดของ quantum protocol stacks

### 4.4 Routing & Entanglement Distribution

9. **Shi & Zhang (2024)** — *Concurrent Entanglement Routing for Quantum Networks*  
   IEEE/ACM Transactions on Networking, 32(1), 45–59  
   → basis ของ Q-CAST routing algorithm

10. **Rozpędek et al. (2019)** — *Parameter regimes for a single sequential quantum repeater*  
    Quantum Science and Technology, 3(3), 034002  
    → design space ของ quantum repeater nodes

---

## 5. Next Steps — Sprint 3 Plan

### 5.1 ถ้า v2 สำเร็จ (fidelity > 90%)

- [ ] เพิ่ม shots เป็น 20,000 เพื่อ statistical significance
- [ ] ทดสอบ v3 (hardware-aware transpilation) บน ibm_fez
- [ ] เปรียบเทียบ physical qubit layouts จาก calibration data
- [ ] เพิ่ม 95% confidence intervals ในผลลัพธ์

### 5.2 ถ้า v2b (readout mitigation) ล้มเหลว

- [ ] Document condition number κ(M) และ calibration drift
- [ ] Recommend Probabilistic Error Cancellation (PEC) แทน
- [ ] ใช้ผลเป็น negative result ใน paper (Sprint 3 failure analysis)

### 5.3 Sprint Gamma (Sprint 3) Preview

| Target | Goal |
|--------|------|
| Fidelity | > 97% |
| Method | Hardware-aware transpilation + qubit remapping |
| Shots | 20,000 per run |
| Backends | ibm_fez + ibm_marrakesh |
| Statistical | 95% CI + z-test vs Sprint 1 baseline |

---

## 6. Known Issues & Watchlist

> สิ่งที่ต้องระวังใน Sprint Beta

| Issue | Description | Mitigation |
|-------|-------------|------------|
| Queue time | ibm_marrakesh มักมี queue นาน | ใช้ ibm_fez เป็น primary |
| Calibration drift | T1/T2 เปลี่ยนระหว่าง run | บันทึก timestamp ทุก attempt |
| Shot noise | 1024 shots อาจน้อยเกินไป | เพิ่มเป็น 4096–20000 |
| Backend version | Qiskit version mismatch | pin `qiskit==1.0.2` |

---

*Last updated: March 2026 | Q-NET-2030 Sprint Beta*