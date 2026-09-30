# 03 - Measurement and Wavefunction Collapse

## Core Idea
Measurement is the bridge between the quantum world and the classical world. A quantum computer
does all its work with amplitudes, phases, and superpositions—but to get an answer you can read,
you must **measure**, which irreversibly collapses the quantum state into a single classical bit.

## Key Concepts

### Wavefunction Collapse
Before measurement, a qubit in state |+> exists as:
```
|+> = (|0> + |1>) / sqrt(2)
```

The instant you measure it, the superposition is destroyed. The qubit is forced into one
definite outcome: either |0> or |1>. This transition is called **wavefunction collapse**.

There is no way to predict which outcome you will get on any single measurement. The outcome
is genuinely random, governed by the Born Rule probabilities.

After collapse, the qubit is in a definite state. If it collapsed to |0>, measuring it again
immediately (without any gates) will give |0> with 100% certainty. The superposition is gone.

### Shots and Statistical Reconstruction
Because a single measurement gives you only one bit of information (0 or 1), you cannot learn
the probability distribution from a single run. To reconstruct the underlying probabilities,
you must:
1. Prepare the same circuit from scratch.
2. Run it again.
3. Measure again.
4. Repeat thousands of times.

Each repetition is called a **shot**. With 1,000 shots on a 50/50 superposition, you will see
approximately 500 zeros and 500 ones—but rarely exactly 500/500. This statistical noise is
called **shot noise** and decreases as you increase the number of shots (like flipping a coin
more times gives you a ratio closer to 50/50).

### Classical Bits and Classical Registers
In a Qiskit circuit:
- **Quantum wires** (single lines `---`) carry qubits through gates.
- **Classical wires** (double lines `===`) carry measurement results (0 or 1).
- `QuantumCircuit(1, 1)` creates 1 qubit wire and 1 classical bit wire.
- `qc.measure(0, 0)` connects qubit 0's measurement outcome to classical bit 0.

### The Measurement Problem
Wavefunction collapse is one of the deepest unsolved questions in physics. The mathematical
rules of quantum mechanics do not explain *why* or *how* collapse happens—they only tell us
the probabilities. Different interpretations of quantum mechanics (Copenhagen, Many-Worlds,
QBism, etc.) offer different philosophical answers, but they all predict the same experimental
outcomes.

## Analogy
Imagine writing a number on a piece of paper, putting it in a sealed envelope, and shaking
the envelope violently. Before you open the envelope, the paper is in a superposition of
positions. The moment you open it (measure), you see one definite configuration.

But this analogy breaks down in one crucial way: with a real envelope, the paper was always
in one position—you just didn't know which. In quantum mechanics, the qubit genuinely has
no definite value until measured. This is not philosophical hand-waving—Bell's theorem
(1964) proved it experimentally.

## Questions Worth Asking
1. If you measure a qubit and get |0>, then apply an H gate to put it back in superposition,
   then measure again—is the second measurement influenced by the first result in any way?
2. Why can't we just measure a qubit "gently" to learn its state without disturbing it?
   What physical law prevents this?
3. If shot noise decreases with more shots, is there a formula for how many shots you need
   to achieve a desired precision (say, knowing the probability to within 1%)?
4. The Many-Worlds interpretation says collapse doesn't happen—instead, the universe branches.
   If both interpretations give the same math, does it matter which one is "true"?
5. In a real quantum computer, measurements take physical time. During that time, is the qubit
   in superposition, collapsed, or something else entirely?
6. Could you build a useful quantum computer that never measures—one that just feeds quantum
   outputs directly into the next quantum computation forever?
