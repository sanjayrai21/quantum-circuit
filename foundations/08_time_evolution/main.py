import sys
from pathlib import Path

# Add workspace root so we can import shared helpers from utils/
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler
from utils.display import show_results

# -------------------------------------------------------------
# Concept 08: Continuous Quantum Time Evolution (XY Spin Model)
# -------------------------------------------------------------
# Physical system:
# Two interacting atoms (spins).
# Atom 0 starts excited (|1>), Atom 1 starts in ground state (|0>).
# Hamiltonian interaction allows the excitation to hop continuously
# back and forth between Atom 0 and Atom 1 over time t!

J = 1.0  # Coupling interaction strength
time_steps = np.linspace(0, 2 * np.pi, 30)  # 30 time slices from t = 0 to 2*pi
shots = 1000

circuits = []
for t in time_steps:
    qc = QuantumCircuit(2)
    
    # 1. Initial State: Atom 0 is excited (|1>), Atom 1 is ground (|0>)
    # Qiskit bitstring order is |q1 q0>, so this corresponds to state |01>
    qc.x(0)
    
    # 2. Time evolution for duration t under the XY interaction Hamiltonian:
    # Implemented via parameterized continuous rotation gates Rxx and Ryy
    theta = J * t
    qc.rxx(theta, 0, 1)
    qc.ryy(theta, 0, 1)
    
    # 3. Measurement
    qc.measure_all()
    circuits.append(qc)

# Display sample circuit diagram for one time slice
print("--- Circuit for One Time Step (t = pi/2) ---")
sample_index = len(time_steps) // 4
show_results(circuits[sample_index])

# Simulate all time steps using StatevectorSampler
print("Simulating continuous quantum time evolution across 30 time steps...")
sampler = StatevectorSampler()
results = sampler.run(circuits, shots=shots).result()

prob_atom0 = []
prob_atom1 = []

for res in results:
    counts = res.data.meas.get_counts()
    # In Qiskit 'b1 b0', b0 is Atom 0 and b1 is Atom 1
    p0 = sum(cnt for bits, cnt in counts.items() if bits[1] == '1') / shots
    p1 = sum(cnt for bits, cnt in counts.items() if bits[0] == '1') / shots
    prob_atom0.append(p0)
    prob_atom1.append(p1)

# Generate and save the continuous oscillation plot
plt.figure(figsize=(9, 5))
plt.plot(time_steps, prob_atom0, label="Atom 0 Excitation P(|1>)", color="#3b82f6", linewidth=2.5)
plt.plot(time_steps, prob_atom1, label="Atom 1 Excitation P(|1>)", color="#f97316", linewidth=2.5, linestyle="--")
plt.axhline(0.5, color="gray", linestyle=":", alpha=0.6, label="50/50 Entangled Crossing")
plt.xlabel("Time t (arbitrary units)", fontsize=11)
plt.ylabel("Excitation Probability", fontsize=11)
plt.title("Quantum Time Evolution: Continuous Excitation Hopping", fontsize=13, pad=12)
plt.legend(frameon=True, facecolor="white", fontsize=10)
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()

output_plot = Path(__file__).parent / "atom_time_evolution.png"
plt.savefig(output_plot, dpi=200)
print(f"Plot saved successfully to: {output_plot}")
