# 05 - Gates, Relative Phase, and the Pauli-Z Gate

## Core Idea
Up to this point, every amplitude we encountered was a positive number. But quantum amplitudes
have a hidden dimension: they can be **negative** (and even complex). This sign or angle is
called **phase**, and it is the secret ingredient that makes quantum computing powerful.

The Pauli-Z gate is the simplest phase gate. It does not change any probabilities—it only
changes the sign of the |1> amplitude. This makes it "invisible" to standard measurement,
yet it is the key that unlocks quantum interference in the next concept.

## Key Concepts

### The Three Pauli Gates (The Complete Family)
Now that we have covered all three, here is the full picture:

```
X gate (bit-flip):    |0> -> |1>,   |1> -> |0>        Swaps amplitudes
Z gate (phase-flip):  |0> -> |0>,   |1> -> -|1>       Flips sign of |1>
Y gate (both):        |0> -> i|1>,  |1> -> -i|0>      Bit-flip + phase-flip
```

Matrix representations:
```
X = [ 0  1 ]     Z = [ 1   0 ]     Y = [ 0  -i ]
    [ 1  0 ]         [ 0  -1 ]         [ i   0 ]
```

Notice: X changes which state you are in. Z changes the phase without changing the state.
Y does both at once. These three gates, together with the identity I, form a complete basis
for describing any single-qubit operation.

### Relative Phase: The Hidden Variable
Consider these two states:
```
|+> = (|0> + |1>) / sqrt(2)    statevector: [+0.707, +0.707]
|-> = (|0> - |1>) / sqrt(2)    statevector: [+0.707, -0.707]
```

Both have identical measurement probabilities:
```
P(|0>) = (0.707)^2 = 50%
P(|1>) = (0.707)^2 = 50%    (regardless of whether it is +0.707 or -0.707!)
```

The difference between |+> and |-> is the **relative phase**—the sign relationship between
the |0> and |1> terms. It is completely invisible to standard measurement because the Born
Rule squares the amplitude, destroying the sign: (-0.707)^2 = (+0.707)^2 = 0.5.

### Why Phase Matters (Preview of Concept 06)
If phase is invisible to measurement, why do we care about it?

Because when we apply *more gates after the phase change*, the phase difference causes
amplitudes to combine differently:
- Same signs (+, +) -> amplitudes ADD (constructive interference)
- Opposite signs (+, -) -> amplitudes CANCEL (destructive interference)

Phase is invisible to *direct* measurement, but it controls what happens in *subsequent*
operations. This is like planting a seed: you can't see the seed underground, but it
determines which plant grows.

### Measuring in a Different Basis
You discovered this insight yourself: applying an H gate before measuring effectively
rotates your measurement from the Z-basis (computational basis) to the X-basis (Hadamard
basis):
```
H then Measure:
  |+> -> H -> |0>   (always 0)
  |-> -> H -> |1>   (always 1)
```

This technique—changing the measurement basis to reveal hidden phase information—is used
throughout quantum computing and quantum cryptography (BB84 protocol).

## Analogy
Think of two identical-looking glasses of clear liquid. One is pure water, the other is
vodka. They look identical (same measurement probabilities). But if you add a chemical
reagent (another gate), one turns red and the other turns blue. The "phase" was there
all along—you just needed the right operation to reveal it.

## Questions Worth Asking
1. The Z gate is "invisible" to standard measurement, yet it is essential for quantum
   algorithms. Can you think of a classical computing analogy where changing something
   invisible has major downstream effects?
2. We learned that |+> and |-> look identical when measured. Are there other pairs of
   quantum states that look identical under standard measurement but differ in phase?
3. The Z gate only affects |1>, not |0>. Is there a gate that does the opposite—affects
   |0> but leaves |1> alone?
4. In quantum cryptography (BB84), Alice sends qubits in either the Z-basis or X-basis,
   and Bob randomly chooses which basis to measure in. Why does this create security?
5. If you applied Z twice in a row (Z followed by Z), what would happen? Is Z its own
   inverse like X and H?
6. Complex phase (like multiplying by "i" instead of "-1") is also possible. What gate
   produces a 90-degree phase rotation instead of 180 degrees?
