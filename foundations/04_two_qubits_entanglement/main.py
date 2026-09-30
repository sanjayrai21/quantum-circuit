import sys
from pathlib import Path

# Add workspace root so we can import shared helpers from utils/
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.primitives import StatevectorSampler
from utils.display import show_results

# 1. Create a circuit with 2 qubits and 2 classical bits
# Both qubits start in state |00>.
qc = QuantumCircuit(2, 2)

# 2. Put qubit 0 into equal superposition |+>
# State becomes (|00> + |01>) / sqrt(2)  [Note: Qiskit ordering is |q1 q0>]
qc.h(0)

# 3. Apply the CNOT (Controlled-NOT) gate
# Control qubit = 0, Target qubit = 1
# Quantum effect: if qubit 0 is 1, flip qubit 1. This creates entanglement!
qc.cx(0, 1)

# 4. Capture the exact theoretical statevector before measurement
state = Statevector(qc)

# 5. Measure both qubits into their corresponding classical bits
qc.measure([0, 1], [0, 1])

# 6. Sample 1,000 shots
sampler = StatevectorSampler()
job = sampler.run([qc], shots=1000)
result = job.result()
counts = result[0].data.c.get_counts()

# 7. Display circuit, statevector, and measurement counts
show_results(qc, sv=state, counts=counts)
