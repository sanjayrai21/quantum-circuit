import sys
from pathlib import Path

# Add workspace root so we can import shared helpers from utils/
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler
from utils.display import show_results

# 1. Create a circuit with 1 qubit and 1 classical bit
# The qubit holds the quantum state; the classical bit records the measurement result.
qc = QuantumCircuit(1, 1)

# 2. Put qubit 0 into equal superposition |+>
qc.h(0)

# 3. Measure qubit 0 into classical bit 0
# Quantum effect: forces the superposition to collapse into either 0 or 1.
qc.measure(0, 0)

# 4. Run the experiment for 1,000 shots on the quantum sampler
sampler = StatevectorSampler()
job = sampler.run([qc], shots=1000)
result = job.result()
counts = result[0].data.c.get_counts()

# 5. Display circuit diagram and shot distribution
show_results(qc, counts=counts)
