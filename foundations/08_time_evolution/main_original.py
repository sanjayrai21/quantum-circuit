import sys
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

"""
Simulating the Time Evolution of Two Interacting Atoms (Spins)
============================================================
Physical System:
- Atom 0 and Atom 1 are coupled via an exchange interaction (XY model):
      H = (J/2) * (X_0 X_1 + Y_0 Y_1)
- Initial state at t = 0: 
      Atom 0 is Excited (|1>), Atom 1 is in Ground state (|0>) -> State |01> (in Qiskit ordering)
- Over time t, quantum tunneling causes the excitation energy to oscillate 
  back and forth between Atom 0 and Atom 1!
"""

# Parameters
J = 1.0  # Coupling strength
time_steps = np.linspace(0, 2 * np.pi, 50)  # 50 time slices from t = 0 to 2*pi
shots = 1024

circuits = []
for t in time_steps:
    qc = QuantumCircuit(2)
    
    # 1. Initialize: Atom 0 is excited (|1>), Atom 1 is in ground state (|0>)
    qc.x(0)
    
    # 2. Time-evolution operator U(t) = exp(-i * H * t)
    # Implemented via Rxx and Ryy rotation gates parameterized by t
    theta = J * t
    qc.rxx(theta, 0, 1)
    qc.ryy(theta, 0, 1)
    
    # 3. Measurement: collapse quantum state to classical bits
    qc.measure_all()
    circuits.append(qc)

# Display the quantum circuit for the first time step
print("--- Quantum Circuit for One Time Step ---")
print(circuits[1].draw("text"))

# Run all circuits on the quantum simulator in a single batch
print("\nSimulating quantum time evolution...")
sampler = StatevectorSampler()
results = sampler.run(circuits, shots=shots).result()

prob_atom0_excited = []
prob_atom1_excited = []

for res in results:
    counts = res.data.meas.get_counts()
    # In Qiskit bitstring 'b1 b0', b0 is atom 0 and b1 is atom 1
    p0 = sum(cnt for bits, cnt in counts.items() if bits[1] == '1') / shots
    p1 = sum(cnt for bits, cnt in counts.items() if bits[0] == '1') / shots
    prob_atom0_excited.append(p0)
    prob_atom1_excited.append(p1)

print("Simulation complete! Generating plot...")

# Plotting the excitation exchange over time
plt.figure(figsize=(10, 6))
plt.plot(time_steps, prob_atom0_excited, label="Atom 0 Excited State P(|1>)", color="#3b82f6", linewidth=2.5)
plt.plot(time_steps, prob_atom1_excited, label="Atom 1 Excited State P(|1>)", color="#f97316", linewidth=2.5, linestyle="--")

plt.axhline(0.5, color="gray", linestyle=":", alpha=0.6, label="50/50 Entangled State")
plt.xlabel("Time (arbitrary units)", fontsize=12)
plt.ylabel("Excitation Probability", fontsize=12)
plt.title("Quantum Time Evolution: Excitation Hopping Between Two Coupled Atoms", fontsize=14, pad=15)
plt.legend(frameon=True, facecolor="white", framealpha=0.9, fontsize=11)
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()

# Save the plot image so it can be viewed directly
output_image = "atom_time_evolution.png"
plt.savefig(output_image, dpi=300)
print(f"Plot saved to '{output_image}'.")

# Display the interactive window
plt.show()