# 07 - Simple Quantum Algorithms: Deutsch's Algorithm

## Core Idea
Deutsch's algorithm (1985) is the **first quantum algorithm ever devised** that provably
outperforms any classical algorithm. It is simple enough to understand with the tools we have
built, yet it contains every ingredient used in more powerful algorithms like Grover's and
Shor's: superposition, oracles, phase kickback, and interference.

## The Problem
You are given a black-box function (oracle) that takes a single bit as input and returns a
single bit as output: f(x) where x is 0 or 1, and f(x) is 0 or 1.

There are exactly 4 possible such functions:
```
Constant functions (same output for all inputs):
  f_A: f(0)=0, f(1)=0    (always outputs 0)
  f_B: f(0)=1, f(1)=1    (always outputs 1)

Balanced functions (different outputs):
  f_C: f(0)=0, f(1)=1    (identity: output equals input)
  f_D: f(0)=1, f(1)=0    (NOT: output is flipped input)
```

**The question**: Is the hidden function Constant or Balanced?

**Classical**: You MUST evaluate f twice—once for f(0) and once for f(1)—to compare.
**Quantum**: Deutsch's algorithm answers the question with exactly ONE evaluation.

## Key Concepts

### How Functions Become Quantum Gates (Oracles)
In quantum computing, all operations must be reversible. To compute a function f(x)
reversibly, we use two wires:
```
Input wire:  carries x (unchanged)
Target wire: gets flipped IF AND ONLY IF f(x) = 1
```

The four functions map to these quantum circuits:
```
f_A (f(x)=0, constant):     Empty wire (do nothing)
f_B (f(x)=1, constant):     X gate on target (always flip)
f_C (f(x)=x, balanced):     CNOT gate (flip target when input is 1)
f_D (f(x)=NOT(x), balanced): X on input, CNOT, X on input (flip target when input is 0)
```

The CNOT gate is literally the quantum hardware implementation of f(x) = x, because its
behavior is: "if the input (control) is 1, flip the output (target)."

### Phase Kickback (The Clever Trick)
Phase kickback is the heart of the algorithm. The key insight comes in three steps:

**Step 1**: The X gate acting on the minus state |-> produces a global minus sign:
```
X |-> = X (|0> - |1>) / sqrt(2)
      = (|1> - |0>) / sqrt(2)
      = -(|0> - |1>) / sqrt(2)
      = -|->
```
The minus state is an EIGENSTATE of the X gate with eigenvalue -1. Applying X does not
change |-> into a different state—it just multiplies it by -1.

**Step 2**: In a CNOT, when the control is |1>, the target gets an X gate. If the target
is in |->, that X gate produces a -1 factor. This -1 "kicks back" onto the control qubit:
```
|1> * |->  --CNOT-->  |1> * (X|->) = |1> * (-|->) = -|1> * |->
```
The minus sign has migrated from the target to the control!

**Step 3**: If the control is in superposition |+> = (|0> + |1>)/sqrt(2):
```
Before CNOT: (|0> + |1>) / sqrt(2)  *  |->
After CNOT:  (|0> - |1>) / sqrt(2)  *  |->
```
The control qubit changed from |+> to |->! The target qubit is completely unchanged.

### The Algorithm Flow
```
Step 1: Initialize       |0> |1>         (input qubit, ancilla qubit)
Step 2: Superpositions    H   H    ->     |+> |->
Step 3: Oracle            (1 query)  ->   Phase kickback changes |+> to |+> or |->
Step 4: Final H on input               ->   |0> or |1>
Step 5: Measure input qubit
```

Decoder:
```
Measured 0  ->  Function is CONSTANT
Measured 1  ->  Function is BALANCED
```

### Why It Works
- If f is **Constant**: either both branches get a minus sign (which cancels as a global
  phase) or neither branch gets a minus sign. Either way, the control qubit stays in |+>.
  Applying H maps |+> -> |0>. Measurement: 0.

- If f is **Balanced**: one branch gets a minus sign and the other doesn't. The control
  qubit flips from |+> to |->. Applying H maps |-> -> |1>. Measurement: 1.

## Analogy
Imagine you have a coin that is either fair (constant: both sides are heads, or both are tails)
or rigged (balanced: one side heads, one side tails). Classically, you must look at both sides
to decide. Deutsch's algorithm is like placing the coin in a special quantum spinner that makes
both sides interfere with each other—the spinning pattern tells you whether the coin is fair or
rigged, and you only need to spin it once.

## Questions Worth Asking
1. Deutsch's algorithm gives a speedup from 2 queries to 1. That is a factor of 2. Is that
   really impressive? When does quantum speedup become exponentially better than classical?
   (Hint: look up Deutsch-Jozsa for N-bit functions.)
2. Phase kickback required the ancilla to be in |->. What would happen if the ancilla were
   in |0> instead? Would the algorithm still work?
3. The oracle is treated as a black box. But someone had to BUILD the oracle. Doesn't the
   person who built it already know whether f is constant or balanced?
4. Could you use Deutsch's algorithm to determine WHICH constant function (f_A or f_B)
   or WHICH balanced function (f_C or f_D) you have? Or does it only distinguish
   constant-vs-balanced?
5. Phase kickback is also used in Shor's algorithm (for factoring large numbers) and
   Grover's algorithm (for searching). How does the same trick scale to those more
   complex problems?
6. If the oracle had errors (say, it implemented f(x)=x correctly only 90% of the time),
   would Deutsch's algorithm still give the right answer?
