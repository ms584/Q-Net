"""
Q-Net Project: Layer 2 (Reality Link) Proof of Concept
Quantum Teleportation Simulation using IBM Qiskit (VS Code Version)
"""

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def run_qnet_teleportation():
    print("--- Initializing Q-Net Teleportation Protocol ---")

    # 1. Setup Registers: We need 3 Qubits and 2 Classical Bits
    qr = QuantumRegister(3, name="q")
    cr1 = ClassicalRegister(1, name="c1") # Store Alice's first measurement
    cr2 = ClassicalRegister(1, name="c2") # Store Alice's second measurement
    cr_bob = ClassicalRegister(1, name="result") # Store Bob's final result
    
    qc = QuantumCircuit(qr, cr1, cr2, cr_bob)

    # 2. Prepare the Payload (The Message)
    print("1. Preparing payload state: |1> at Node A")
    qc.x(0) 
    qc.barrier()

    # 3. Create the Entanglement Fabric (Layer 1)
    print("2. Generating Entanglement Fabric between Node A and Node B")
    qc.h(1)
    qc.cx(1, 2)
    qc.barrier()

    # 4. Reality Link / Teleportation Protocol (Layer 2)
    print("3. Executing Reality Link (Collapse Control) at Node A")
    qc.cx(0, 1)
    qc.h(0)
    qc.barrier()

    # Alice measures her qubits, collapsing the state
    qc.measure(0, cr1)
    qc.measure(1, cr2)
    qc.barrier()

    # 5. State Reconstruction at Node B (Qiskit 1.0+ Syntax)
    print("4. Reconstructing State at Node B (Zero-Latency transfer)")
    
    with qc.if_test((cr2, 1)):
        qc.x(2)
    with qc.if_test((cr1, 1)):
        qc.z(2)
        
    qc.barrier()

    # 6. Verify the Result at Node B
    print("5. Measuring final state at Node B...")
    qc.measure(2, cr_bob)

    # --- Execution on Simulator ---
    print("\n--- Running Simulation on AerSimulator ---")
    simulator = AerSimulator()
    compiled_circuit = transpile(qc, simulator)
    job = simulator.run(compiled_circuit, shots=1024)
    result = job.result()
    counts = result.get_counts()

    # Print results
    print(f"\nSimulation Results (1024 shots): {counts}")
    print("Note: The key reading is the furthest left bit (Bob's Result).")
    print("Since we sent '1', all results should start with '1' (e.g., '1 0 0', '1 0 1', '1 1 0', '1 1 1')")
    
    # Check if teleportation was 100% successful
    success_rate = sum([count for key, count in counts.items() if key.startswith('1')]) / 1024 * 100
    print(f"\nTeleportation Success Rate: {success_rate:.2f}%\n")

    # --- Visualization for VS Code / Local Terminal ---
    print("Generating visualizations...")
    
    # 1. Draw Circuit and save to .png
    circuit_fig = qc.draw('mpl')
    circuit_fig.savefig('qnet_circuit.png')
    print(">> Saved circuit diagram to 'qnet_circuit.png'")
    
    # 2. Draw Graph and save to .png
    hist_fig = plot_histogram(counts, title="Q-Net Teleportation Results (Node B)")
    hist_fig.savefig('qnet_histogram.png')
    print(">> Saved results histogram to 'qnet_histogram.png'")
    
    print("\nOpening plot windows... (Close the popup windows to finish the script)")
    
    # Show Picture
    plt.show()

if __name__ == "__main__":
    run_qnet_teleportation()