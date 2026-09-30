import sys
from pathlib import Path

# Add workspace root so we can import shared helpers from utils/
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from utils.display import show_results

# 1. Create a 1-qubit circuit (qubit starts in state |0>)
qc = QuantumCircuit(1)

# 2. Apply the Hadamard gate (H) to qubit 0
# Quantum effect: creates an equal superposition of |0> and |1>
qc.h(0)

# 3. Calculate the resulting statevector
# Mathematical representation of the superposition state |+>
state = Statevector(qc)

# 4. Display circuit diagram and quantum state
show_results(qc, sv=state)
