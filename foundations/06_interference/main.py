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

# 2. Put qubit into superposition |+>
qc.h(0)

# 3. Apply phase flip Z: transforms |+> into |-> = (|0> - |1>) / sqrt(2)
qc.z(0)

# 4. Apply second Hadamard gate: creates quantum interference!
# The minus sign causes amplitude for |0> to cancel out (destructive interference),
# while amplitude for |1> adds up (constructive interference).
qc.h(0)

# 5. Capture theoretical statevector before measurement
state = Statevector(qc)

# 6. Measure the qubit
qc.measure(0, 0)

# 7. Sample 1,000 shots
sampler = StatevectorSampler()
job = sampler.run([qc], shots=1000)
result = job.result()
counts = result[0].data.c.get_counts()

# 8. Display circuit, statevector, and measurement counts
show_results(qc, sv=state, counts=counts)
