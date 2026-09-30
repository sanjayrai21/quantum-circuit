# Learning Quantum Computing with Qiskit

A structured, hands-on curriculum for learning quantum computing from absolute zero.
Built with Python, [Qiskit 2.5](https://qiskit.org/), and a step-by-step pedagogy that
prioritizes real understanding over working code.

## Prerequisites

- Python 3.14+ (via [uv](https://docs.astral.sh/uv/))
- No prior quantum computing knowledge required

## Setup

```powershell
# Clone and enter the project
cd "d:\python\quantum circuit"

# Install dependencies (uv handles the virtual environment automatically)
uv sync
```

## How to Run Any Experiment

### Option 1: Quick Runner (Recommended)

You can run any experiment by number or keyword without typing long paths:

```powershell
# Run by experiment number
.\run 1              # In PowerShell: runs 01_single_qubit
run 1                # In CMD: runs 01_single_qubit
uv run python run.py 1

# Run by keyword
.\run interference   # runs 06_interference
.\run bloch          # generates 3D Bloch sphere diagrams

# List all available experiments and shortcuts
.\run
```

### Option 2: Direct Path Execution

You can also run any specific `main.py` directly using `uv run`:

```powershell
uv run python foundations/01_single_qubit/main.py
uv run python foundations/02_superposition/main.py
```

## Curriculum Roadmap

### Stage 1: Foundations ✅ Complete

| # | Folder | Concept | Key Gates / Ideas |
|---|--------|---------|-------------------|
| 01 | `foundations/01_single_qubit/` | The Qubit and Pauli-X | Ground state `\|0>`, excited state `\|1>`, quantum NOT gate |
| 02 | `foundations/02_superposition/` | Superposition and Hadamard | H gate, amplitudes, Born rule, the `\|+>` state |
| 03 | `foundations/03_measurement/` | Measurement and Collapse | Wavefunction collapse, shots, classical bits, shot noise |
| 04 | `foundations/04_two_qubits_entanglement/` | Entanglement | CNOT gate, Bell state, correlation |
| 05 | `foundations/05_gates_and_phase/` | Relative Phase and Pauli-Z | Z gate, the `\|->` state, invisible phase, basis rotation |
| 06 | `foundations/06_interference/` | Quantum Interference | Constructive/destructive interference, H-Z-H circuit |
| 07 | `foundations/07_simple_algorithms/` | Deutsch's Algorithm | Oracles, phase kickback, first quantum speedup |
| 08 | `foundations/08_time_evolution/` | Hamiltonian Time Evolution | Rxx/Ryy gates, XY spin model, Rabi oscillations |

### Stage 2: Algorithms 🔜 Next

| Folder | Concept | Prerequisites |
|--------|---------|---------------|
| `algorithms/teleportation/` | Quantum Teleportation | Entanglement, Measurement |
| `algorithms/grover_search/` | Grover's Search Algorithm | Interference, Phase Kickback |
| `algorithms/deutsch_jozsa/` | Deutsch-Jozsa (N-bit) | Deutsch's Algorithm |
| `algorithms/superdense_coding/` | Superdense Coding | Entanglement |
| `algorithms/quantum_fourier_transform/` | QFT | Phase, Multi-qubit states |
| `algorithms/phase_estimation/` | Phase Estimation | QFT, Phase Kickback |
| `algorithms/shor_factoring/` | Shor's Factoring | QPE, QFT, Simon's |

### Stage 3: Applications — Planned

| Folder | Concept |
|--------|---------|
| `applications/vqe_chemistry/` | Variational Quantum Eigensolver |
| `applications/qaoa_optimization/` | Quantum Approximate Optimization |
| `applications/quantum_machine_learning/` | Quantum ML |
| `applications/quantum_cryptography_bb84/` | BB84 Protocol |
| `applications/quantum_simulation/` | Quantum Simulation |

### Stage 4: Hardware — Planned

| Folder | Concept |
|--------|---------|
| `hardware/ibm_basics/` | Running on Real IBM Chips |
| `hardware/noise_and_errors/` | Decoherence, T1/T2 |
| `hardware/error_mitigation/` | Zero-noise Extrapolation, M3 |
| `hardware/error_correction/` | Surface Codes, Logical Qubits |

## Project Structure

```
quantum-circuit/
├── foundations/                    # Stage 1: Core quantum concepts (COMPLETED)
│   ├── 01_single_qubit/
│   │   ├── main.py
│   │   └── NOTES.md
│   ├── 02_superposition/
│   ├── 03_measurement/
│   ├── 04_two_qubits_entanglement/
│   ├── 05_gates_and_phase/
│   ├── 06_interference/
│   ├── 07_simple_algorithms/
│   ├── 08_time_evolution/
│   └── bloch_examples/            # Pre-generated Bloch sphere images
│
├── algorithms/                    # Stage 2: Quantum algorithms (NEXT)
│   ├── teleportation/
│   ├── grover_search/
│   ├── deutsch_jozsa/
│   ├── superdense_coding/
│   ├── quantum_fourier_transform/
│   ├── phase_estimation/
│   └── shor_factoring/
│
├── applications/                  # Stage 3: Real-world applications (PLANNED)
│   ├── vqe_chemistry/
│   ├── qaoa_optimization/
│   ├── quantum_machine_learning/
│   ├── quantum_cryptography_bb84/
│   └── quantum_simulation/
│
├── hardware/                      # Stage 4: Real quantum chips (PLANNED)
│   ├── ibm_basics/
│   ├── noise_and_errors/
│   ├── error_mitigation/
│   └── error_correction/
│
├── utils/                         # Shared helper utilities
│   ├── display.py                 #   Colored terminal output for circuits and states
│   └── bloch.py                   #   Bloch sphere visualization (saves PNG images)
│
├── LEARNING_LOG.md                # Session-by-session progress tracker
├── PREREQUISITE_MAP.md            # Dependency graph: which topics unlock which
├── AGENTS.md                      # Teaching rules and project conventions
├── pyproject.toml                 # Python project config and dependencies
└── README.md                      # This file
```

## Utilities

### `utils/display.py` — Terminal Display
The `show_results()` function provides colored, structured terminal output:
- Circuit summary header (qubit count, gate count)
- ASCII circuit diagram
- Statevector table (state, amplitude, probability, visual bar)
- Measurement counts table (outcome, shots, frequency, visual bar)

```python
from utils.display import show_results
show_results(qc, sv=statevector, counts=measurement_counts)
```

### `utils/bloch.py` — Bloch Sphere Visualization
Saves a Bloch sphere PNG showing where a qubit sits on the 3D sphere:

```python
from utils.bloch import save_bloch_sphere
save_bloch_sphere(statevector, filepath="my_state.png", title="After H gate")
```

Run standalone to generate all example spheres:
```powershell
uv run python utils/bloch.py
```

## Learning Methodology

This project follows strict pedagogical rules (defined in `AGENTS.md`):

1. **One concept per step** — never two new ideas at once
2. **Predict before running** — forces active engagement with the physics
3. **Plain words first** — the idea in English before any math
4. **Math only as needed** — just enough to verify predictions
5. **Check questions** — 3 questions after every concept to solidify understanding
6. **Progress tracking** — `LEARNING_LOG.md` records what was learned and what was corrected

## Status: Living Project

This repository is **not finished** — it is a living learning journal that grows as new
topics are studied. See [`PREREQUISITE_MAP.md`](PREREQUISITE_MAP.md) for the full dependency
graph showing which topics unlock which, and which are ready to start now.

## Dependencies

- `qiskit >= 2.5.1` — Quantum circuit SDK
- `matplotlib >= 3.11.1` — Plotting (time evolution, Bloch spheres)
- `qiskit-ibm-runtime >= 0.48.0` — IBM Quantum hardware access (future use)
