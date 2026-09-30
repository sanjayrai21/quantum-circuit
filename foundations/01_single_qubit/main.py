import sys
from pathlib import Path

# Add workspace root so we can import shared helpers from utils/
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from utils.display import show_results

# 1. Create a quantum circuit with 1 qubit
# By convention, newly created qubits always start in the ground state |0>.
qc = QuantumCircuit(1)

# 2. Apply the Pauli-X gate to qubit 0
# Quantum effect: flips the basis state from |0> into |1> (quantum NOT gate).
qc.x(0)

# 3. Compute the resulting statevector
# Mathematical state of the qubit after the gate operation.
state = Statevector(qc)

# 4. Display the circuit diagram and quantum state
show_results(qc, sv=state)
