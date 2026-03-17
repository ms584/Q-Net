# Contributing to Q-Net

Thank you for your interest in Q-Net! 🌌  
This project originated as a course assignment for **CP352005 Computer Networks**
at the College of Computing, Khon Kaen University, and is shared openly for
educational and research purposes under the MIT License.

---

## 📋 Ways to Contribute

### 🐛 Bug Reports
Found an issue with the teleportation circuit or simulation code?

1. Check [existing issues](../../issues) first to avoid duplicates
2. Open a new issue with the label `bug`
3. Include: Python version, Qiskit version, backend used, and the full error message

### 💡 Suggestions & Ideas
Have an idea to improve the circuit, add a new backend test, or extend the architecture?

1. Open an issue with the label `enhancement`
2. Describe your idea and why it improves the project
3. Reference any relevant papers if applicable

### 🔬 Extending the Experiments
Want to run the teleportation circuit on a new IBM Quantum backend or with different parameters?

1. Fork the repository
2. Create a branch: `git checkout -b experiment/your-backend-name`
3. Add your results to a new folder: `sprint-delta/ibm_quantum/your_attempt/`
4. Include: backend name, shots, success rate, Qiskit version, calibration date
5. Submit a Pull Request with your results table

### 📝 Documentation Improvements
Spotted a typo, unclear explanation, or outdated information?

- For small fixes (typos, formatting): submit a Pull Request directly
- For larger changes: open an issue first to discuss

---

## ⚙️ Development Setup

```bash
# 1. Fork and clone the repo
git clone https://github.com/YOUR_USERNAME/Q-NET.git
cd Q-NET

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run local simulation to verify setup
python simulation/teleport_simulation.py
# Expected: 100% success rate on AerSimulator
```

---

## 🖥️ Running on IBM Quantum Hardware

You will need a free IBM Quantum account:

1. Sign up at [quantum.ibm.com](https://quantum.ibm.com)
2. Copy your API token from the dashboard
3. Set your token:
   ```python
   from qiskit_ibm_runtime import QiskitRuntimeService
   QiskitRuntimeService.save_account(channel="ibm_quantum", token="YOUR_TOKEN")
   ```
4. Run: `python IBM_Quantum/teleport_test_on_ibm_quantum.py`

> **Note:** Free IBM Quantum accounts have limited access to backends.
> `ibm_sherbrooke` or `ibm_brisbane` are commonly available alternatives
> if `ibm_fez` / `ibm_marrakesh` are unavailable.

---

## 📐 Code Style

- Follow **PEP 8** for Python code
- Add comments in English for all circuit logic
- Include result output (success rate %) as a comment or print statement
- Use `optimization_level=3` for hardware transpilation (Sprint 4 standard)

---

## 🔬 Reporting New Hardware Results

If you run the circuit on a new backend, please include the following in your PR:

```markdown
## New Result: [Backend Name]

| Parameter | Value |
|-----------|-------|
| Backend | ibm_xxx |
| Qubits | XXX |
| Processor | Heron r1 / Eagle r3 / etc. |
| Qiskit version | X.X.X |
| qiskit-ibm-runtime version | X.X.X |
| Shots | X,XXX |
| optimization_level | X |
| Qubit layout | [q0→X, q1→X, q2→X] |
| Success Rate | XX.XX% |
| 95% CI | [XX.XX%, XX.XX%] |
| Date | YYYY-MM-DD |
```

---

## 📜 Academic Use & Citation

If you use Q-Net in your research or coursework, please cite:

```bibtex
@software{qnet2026,
  author    = {Moknak, Sitthichok and Khumnan, Pattadon and Chamtakhu, Nattaphat
               and Sukongchareun, Sorawit and Phimphichai, Amonwan},
  title     = {Q-Net: Quantum Entanglement-Based Post-Internet Architecture},
  year      = {2026},
  publisher = {GitHub},
  url       = {https://github.com/YOUR_USERNAME/Q-NET},
  note      = {CP352005 Computer Networks, College of Computing, Khon Kaen University}
}
```

---

## 🤝 Code of Conduct

This is an academic project. All contributors are expected to:

- Be respectful and constructive in all discussions
- Give credit to original authors when building on this work
- Follow academic integrity standards — do not misrepresent results

---

## 📬 Contact

For questions beyond GitHub issues, contact the corresponding author:

**Sitthichok Moknak** — sitthichok.m@kkumail.com  
College of Computing, Khon Kaen University

---

*Thank you for helping advance open quantum networking research!* 🚀