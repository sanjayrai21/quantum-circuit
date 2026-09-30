# 01 - Single Qubit and the Pauli-X Gate

## Core Idea
A **qubit** is the quantum version of a classical bit. While a classical bit is a switch that is
strictly OFF (0) or ON (1), a qubit is described by a **statevector**—a mathematical column of two
numbers that completely specifies the qubit's quantum state.

## Key Concepts

### The Ground State |0>
Every qubit in Qiskit starts in the **ground state** |0>. Think of it like a freshly minted coin
placed heads-up on a table. Nobody has touched it yet—its state is certain and known.

In statevector form:
```
|0> = [1, 0]
       ^  ^
       |  |
       |  amplitude for state |1> (zero probability)
       amplitude for state |0> (100% probability)
```

### The Excited State |1>
The opposite definite state. The coin is tails-up. In statevector form:
```
|1> = [0, 1]
       ^  ^
       |  |
       |  amplitude for state |1> (100% probability)
       amplitude for state |0> (zero probability)
```

### The Pauli-X Gate (Quantum NOT)
The X gate is the simplest quantum gate. It flips the qubit between its two basis states:
```
X |0> = |1>
X |1> = |0>
```

As a matrix, the X gate looks like:
```
X = [ 0  1 ]
    [ 1  0 ]
```

Multiplying this matrix by the column vector [1, 0] gives [0, 1]—the state has flipped.

### Self-Inversion
The X gate is its own inverse. Applying it twice returns to the original state:
```
X( X |0> ) = X |1> = |0>
```
This is just like pressing a light switch twice: ON -> OFF -> ON. Every quantum gate has an
inverse (quantum operations are always reversible), and some gates happen to be their own inverse.

## Statevector Slot Ordering (Important!)
The statevector is always ordered as `[amplitude_for_|0>, amplitude_for_|1>]`.
- If the vector is `[1, 0]`, the qubit is definitely in state |0>.
- If the vector is `[0, 1]`, the qubit is definitely in state |1>.

This ordering tripped me up initially—I predicted `[1, 0]` after an X gate, but the correct
answer is `[0, 1]` because the X gate moved the amplitude from the |0> slot into the |1> slot.

## Analogy
Think of the statevector slots like two buckets labeled "0" and "1". A gate rearranges or
redistributes the water (amplitude) between the buckets. The X gate pours all the water from
bucket 0 into bucket 1 and vice versa.

## Questions Worth Asking
1. If quantum gates must be reversible, does that mean quantum computers can never erase
   information? How does that differ from classical computing where you can freely overwrite bits?
2. The X gate matrix has only 0s and 1s. Are there quantum gates with fractional or negative
   entries in their matrices? What would those do to the statevector?
3. What happens if you apply the X gate to a state that is not purely |0> or |1> but something
   in between (like [0.6, 0.8])? Does the gate still just "swap the slots"?
4. Classical NOT gates can be chained: NOT(NOT(NOT(x))). Is there any number of X gates in a
   row that produces a state other than |0> or |1>?
5. The X gate is called "Pauli-X." Who was Pauli, and why are there three Pauli gates (X, Y, Z)?
