"""
Q-Net Project: Layer 2 (Reality Link) Proof of Concept
Quantum Teleportation Test on IBM Quantum

Run These code on Colab following by these step

"""

# STEP 1 — Install Qiskit Runtime
# pip install qiskit qiskit-ibm-runtime

# STEP 2 — Authentication 
# You can get your API KEY and CRN from https://quantum.cloud.ibm.com/
from qiskit_ibm_runtime import QiskitRuntimeService

QiskitRuntimeService.save_account(
    channel="ibm_cloud",
    token="YOUR_API_KEY",
    instance="YOUR_CRN",
    overwrite=True
)

# STEP 3 — Copy And Paste these code _____________________________________________
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler
import matplotlib.pyplot as plt

def run_qnet_teleportation_ibm():

    print("Connecting to IBM Quantum...")

    service = QiskitRuntimeService(channel="ibm_cloud")
    backend = service.backend("ibm_torino")
    print("Using backend:", backend.name)

    # Registers
    qr = QuantumRegister(3, name="q")
    cr1 = ClassicalRegister(1, name="c1")
    cr2 = ClassicalRegister(1, name="c2")
    cr_bob = ClassicalRegister(1, name="result")

    qc = QuantumCircuit(qr, cr1, cr2, cr_bob)

    # Prepare |1>
    qc.x(0)
    qc.barrier()

    # Entanglement
    qc.h(1)
    qc.cx(1, 2)
    qc.barrier()

    # Teleportation
    qc.cx(0, 1)
    qc.h(0)
    qc.barrier()

    qc.measure(0, cr1)
    qc.measure(1, cr2)
    qc.barrier()

    with qc.if_test((cr2, 1)):
        qc.x(2)

    with qc.if_test((cr1, 1)):
        qc.z(2)

    qc.barrier()
    qc.measure(2, cr_bob)

    # Transpile
    pm = generate_preset_pass_manager(backend=backend, optimization_level=1)
    isa_circuit = pm.run(qc)

    # Run
    sampler = Sampler(mode=backend)

    print("Submitting job to QPU...")
    job = sampler.run([isa_circuit], shots=1024)
    print("Job ID:", job.job_id())

    result = job.result()

    # Extract counts safely
    databin = result[0].data

    if hasattr(databin, "meas"):
        counts = databin.meas.get_counts()
    else:
        field = list(databin.__dict__.values())[0]
        counts = field.get_counts()

    print("Counts:", counts)

    shots = sum(counts.values())
    success = sum(v for k, v in counts.items() if k.startswith('1'))

    print("Teleportation Success Rate:", success / shots * 100, "%")

    # --- ASCII Circuit (ไม่ใช้ mpl) ---
    print("\nCircuit:")
    print(qc.draw(output="text"))

    # --- Custom Histogram (ไม่ใช้ plot_histogram) ---
    labels = list(counts.keys())
    values = list(counts.values())

    plt.figure()
    plt.bar(labels, values)
    plt.xlabel("Measurement Result")
    plt.ylabel("Counts")
    plt.title("Teleportation on IBM Hardware")
    plt.show()


run_qnet_teleportation_ibm()


"""
_____________________________________________
# Job Check using this command
"""

job.status()