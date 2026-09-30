import sys
from pathlib import Path

# Add workspace root so we can import shared helpers from utils/
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.primitives import StatevectorSampler
from utils.display import show_results

# 1. Create a 1-qubit, 1-classical-bit circuit
qc = QuantumCircuit(1, 1)

# 2. Put qubit 0 into equal superposition |+> = (|0> + |1>) / sqrt(2)
qc.h(0)

# 3. Apply the Pauli-Z gate (Phase-Flip Gate)
# Quantum effect: leaves |0> unchanged, flips the sign of |1> to -|1>.
# The state becomes the minus state |-> = (|0> - |1>) / sqrt(2).
qc.z(0)

# 4. Capture the exact theoretical statevector before measurement
state = Statevector(qc)

# 5. Measure the qubit into the classical bit
qc.measure(0, 0)

# 6. Sample 1,000 shots
sampler = StatevectorSampler()
job = sampler.run([qc], shots=1000)
result = job.result()
counts = result[0].data.c.get_counts()

# 7. Display circuit, statevector, and measurement counts
show_results(qc, sv=state, counts=counts)
