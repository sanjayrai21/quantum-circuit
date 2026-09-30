# 04 - Two Qubits and Quantum Entanglement

## Core Idea
When you move from 1 qubit to 2 qubits, the state space doesn't just double—it **squares**.
One qubit has 2 basis states. Two qubits have 4. Three qubits have 8. N qubits have 2^N.
This exponential growth of state space is the fundamental reason quantum computers can, in
principle, outperform classical ones for certain problems.

## Key Concepts

### Multi-Qubit Basis States
A 2-qubit system has 4 computational basis states:
```
|00> = [1, 0, 0, 0]   (both qubits are 0)
|01> = [0, 1, 0, 0]   (qubit 0 is 1, qubit 1 is 0)
|10> = [0, 0, 1, 0]   (qubit 0 is 0, qubit 1 is 1)
|11> = [0, 0, 0, 1]   (both qubits are 1)
```

### Qiskit Bit Ordering (Little-Endian)
Qiskit writes bitstrings as |q1 q0>—the **rightmost** digit is qubit 0. This is "little-endian"
ordering (least significant bit on the right), like how we write normal numbers.
```
Bitstring "01" means: qubit 1 = 0, qubit 0 = 1
```
This is a common source of confusion. Always read from right to left for qubit indices.

### The CNOT Gate (Controlled-NOT / CX)
The CNOT is the most important 2-qubit gate. It has two inputs:
- **Control qubit**: the "decision maker"
- **Target qubit**: the one that gets acted upon

The rule is simple:
```
If control qubit's STATE is |0> -> do nothing to target
If control qubit's STATE is |1> -> apply X (flip) to target
```

Important distinction: "control qubit" refers to which physical qubit is chosen as the control
(e.g., qubit 0 or qubit 1). The CNOT's behavior depends on the STATE VALUE of that control
qubit (|0> or |1>), not on its index number.

### Creating Entanglement: H + CNOT
The recipe for entanglement is beautifully simple:
1. Apply H to the control qubit (creating |+>).
2. Apply CNOT from control to target.

Step-by-step trace:
```
Start:     |00>

After H:   (|00> + |01>) / sqrt(2)    [qubit 0 in superposition, qubit 1 still |0>]

After CX:
  |00> branch: control is 0 -> target stays 0 -> |00>
  |01> branch: control is 1 -> target flips to 1 -> |11>

Result:    (|00> + |11>) / sqrt(2)     [The Bell State!]
```

Notice: |01> and |10> are completely absent. The two qubits are now **entangled**.

### What Entanglement Really Means
Entanglement is NOT:
- Faster-than-light communication (you cannot send a message via entanglement alone).
- The qubits "secretly deciding" their values in advance (Bell's theorem rules this out).

Entanglement IS:
- A quantum state of two or more particles that cannot be described by specifying each particle
  separately. The joint system has properties that neither particle has on its own.
- Perfect correlation: if you measure one qubit of a Bell pair and get 0, the other is
  guaranteed to be 0. If you get 1, the other is guaranteed to be 1. Always. Every time.

## Analogy
Imagine a magic pair of dice. You roll one in New York and one in Tokyo, simultaneously.
Somehow, they always show the same number. Not because they were pre-loaded (Bell's theorem
proves they weren't), but because they share a quantum connection that makes their outcomes
perfectly correlated. You can't use this to send a message (each die still looks random
individually), but the correlation is real and instantaneous.

## Questions Worth Asking
1. With 2 qubits we have 4 basis states. With 40 qubits, we would have 2^40 ≈ 1 trillion
   basis states. A classical computer would need to track 1 trillion amplitudes. How does a
   quantum computer handle this without needing 1 trillion physical components?
2. The Bell state (|00> + |11>)/sqrt(2) has zero amplitude for |01> and |10>. Is there a
   different entangled state that has zero amplitude for |00> and |11> instead?
3. Einstein called entanglement "spooky action at a distance." In 1964, John Bell proposed
   a theorem to test whether entanglement is "real" or just classical correlation in disguise.
   What did the experiments show?
4. If entanglement cannot be used to send information faster than light, what IS it useful for
   in practical quantum computing?
5. Can three or more qubits be entangled together? If so, what new properties emerge?
6. If you measure only qubit 0 of an entangled pair (and get, say, 0), what state is qubit 1
   in afterward? Is it still entangled?
