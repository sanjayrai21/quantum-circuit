# 02 - Superposition and the Hadamard Gate

## Core Idea
**Superposition** is the quantum property that allows a qubit to exist in a combination of both
|0> and |1> at the same time. This is not the qubit being "secretly" 0 or 1 and us not knowing—
the qubit is genuinely in both states simultaneously until measured.

## Key Concepts

### The Hadamard Gate (H)
The H gate is the workhorse of quantum computing. It takes a qubit from a boring definite state
and transforms it into a rich superposition:
```
H |0> = (|0> + |1>) / sqrt(2)   ...this is the Plus state |+>
H |1> = (|0> - |1>) / sqrt(2)   ...this is the Minus state |->
```

As a matrix:
```
H = (1/sqrt(2)) [ 1   1 ]
                [ 1  -1 ]
```

Notice the matrix has a `-1` in the bottom-right corner. This asymmetry is what creates the
minus state |-> when applied to |1>. It will become critically important in Concepts 05 and 06.

### Amplitudes vs. Probabilities (The Born Rule)
This is the single most important distinction in quantum mechanics:
- **Amplitude**: the raw number in the statevector. Can be positive, negative, or even complex.
- **Probability**: what you actually observe when measuring. Always positive. Always sums to 1.

The bridge between them is the **Born Rule**:
```
Probability = |amplitude|^2 = (amplitude)^2  (for real amplitudes)
```

For the |+> state:
```
Statevector: [+0.707, +0.707]

P(|0>) = (0.707)^2 = 0.5   (50%)
P(|1>) = (0.707)^2 = 0.5   (50%)
Total   = 0.5 + 0.5 = 1.0  (100%)  ✓
```

Why 0.707 instead of 0.5? Because we need a number whose *square* is 0.5, and sqrt(0.5) = 0.707.

### Self-Inversion of the Hadamard Gate
The H gate is its own inverse, just like the X gate:
```
H( H |0> ) = H |+> = |0>
```

Applying H creates superposition; applying H again collapses it back to a definite state.
This is not obvious at first—I initially predicted that H followed by H would stay in
superposition [0.707, 0.707], but it actually returns to [1, 0].

### The Plus State |+>
The |+> state is quantum computing's most important intermediate state:
```
|+> = (|0> + |1>) / sqrt(2)  =  [0.707, 0.707]
```
It is the starting point for almost every quantum algorithm. Whenever you see H applied at
the beginning of a circuit, it is creating |+> to "spread out" the computation across both
possibilities simultaneously.

## Analogy
Think of a classical coin sitting on a table: it is either heads or tails (definite).
Superposition is like flicking the coin into a spinning state midair—while it spins, it is
genuinely neither heads nor tails, but a blend of both. The moment you catch it (measure it),
it collapses into one definite outcome.

The key difference from a real coin: the spinning quantum coin has precise mathematical
amplitudes governing how likely each outcome is. It is not random ignorance—it is
fundamental indeterminacy.

## Questions Worth Asking
1. If H is its own inverse, and X is its own inverse, is that true for all quantum gates?
   Are there gates where you need a *different* gate to undo them?
2. The Born Rule squares the amplitude to get probability. But amplitudes can be complex
   numbers (like 0.5 + 0.5i). How do you square a complex number to get a real probability?
3. If a qubit in state |+> is measured and collapses to |0>, is there any trace left of the
   |1> component? Can you recover the superposition after measurement?
4. We said the qubit is "genuinely in both states." But Einstein famously objected to this
   interpretation. What was his counterargument, and how was it experimentally resolved?
5. If we apply H to a qubit that is already in |+>, what happens? (Hint: H is its own inverse.)
