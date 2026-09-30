import sys
from pathlib import Path

# Add workspace root so we can import shared helpers from utils/
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler
from utils.display import show_results

# Deutsch's Algorithm: Determine if a black-box function is Constant or Balanced in 1 query!
# Qubit 0: Input qubit
# Qubit 1: Ancilla (helper) qubit
# Classical bit: Records the answer (0 = Constant, 1 = Balanced)
qc = QuantumCircuit(2, 1)

# Step 1: Initialize states
# Qubit 0 starts in |0>; Qubit 1 is flipped to |1>
qc.x(1)

# Step 2: Create superpositions
# Qubit 0 becomes |+>; Qubit 1 becomes |->
qc.h(0)
qc.h(1)
qc.barrier()

# Step 3: The Oracle (Black-Box Function)
# Here we test a Balanced function: f(x) = x (implemented by a CNOT gate).
# Phase Kickback effect: because qubit 1 is in |->, a minus phase kicks back to qubit 0!
qc.cx(0, 1)
qc.barrier()

# Step 4: Interference on the input qubit
# If constant: constructive interference to |0>.
# If balanced: constructive interference to |1>.
qc.h(0)

# Step 5: Measure ONLY the input qubit
qc.measure(0, 0)

# Step 6: Sample 1,000 shots
sampler = StatevectorSampler()
job = sampler.run([qc], shots=1000)
result = job.result()
counts = result[0].data.c.get_counts()

# Step 7: Display circuit diagram and algorithm result
show_results(qc, counts=counts)
