import sys
import os
from pathlib import Path
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

# Configure UTF-8 encoding for Windows terminals so circuit characters render cleanly
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Enable ANSI escape codes on Windows 10+ terminals
if sys.platform == "win32":
    os.system("")

# ── ANSI Color Codes ──────────────────────────────────────────────────────────
RESET   = "\033[0m"
BOLD    = "\033[1m"
DIM     = "\033[2m"

# Foreground colors
CYAN    = "\033[96m"
GREEN   = "\033[92m"
YELLOW  = "\033[93m"
RED     = "\033[91m"
MAGENTA = "\033[95m"
BLUE    = "\033[94m"
WHITE   = "\033[97m"
GRAY    = "\033[90m"

# Background accents
BG_BLUE = "\033[44m"


def _header(title: str, number: int, width: int = 55):
    """Prints a styled section header with color."""
    line = "─" * width
    print(f"\n{CYAN}{line}{RESET}")
    print(f"{BOLD}{CYAN}  {number}. {title}{RESET}")
    print(f"{CYAN}{line}{RESET}")


def _circuit_summary(qc: QuantumCircuit) -> str:
    """Returns a one-line summary of the circuit's structure."""
    n_qubits = qc.num_qubits
    n_clbits = qc.num_clbits
    n_gates = sum(1 for inst in qc.data if inst.operation.name not in ("barrier", "measure"))
    n_meas = sum(1 for inst in qc.data if inst.operation.name == "measure")

    parts = []
    parts.append(f"{n_qubits} qubit{'s' if n_qubits != 1 else ''}")
    if n_clbits > 0:
        parts.append(f"{n_clbits} classical bit{'s' if n_clbits != 1 else ''}")
    parts.append(f"{n_gates} gate{'s' if n_gates != 1 else ''}")
    if n_meas > 0:
        parts.append(f"{n_meas} measurement{'s' if n_meas != 1 else ''}")

    return " · ".join(parts)


def _amplitude_color(amp_real: float, amp_imag: float) -> str:
    """Chooses a color based on the amplitude's sign and magnitude."""
    if abs(amp_real) < 1e-10 and abs(amp_imag) < 1e-10:
        return GRAY       # zero amplitude
    elif amp_real < -1e-10:
        return RED         # negative real part
    else:
        return GREEN       # positive real part


def _bar(fraction: float, width: int = 30, filled_char: str = "█", empty_char: str = "░") -> str:
    """Creates a colored progress-bar style string."""
    filled = int(fraction * width)
    empty = width - filled
    return f"{filled_char * filled}{GRAY}{empty_char * empty}{RESET}"


def _format_amplitude(amp) -> str:
    """Formats a complex amplitude as a readable string."""
    real = amp.real
    imag = amp.imag
    if abs(imag) < 1e-10:
        return f"{real:+.4f}"
    elif abs(real) < 1e-10:
        return f"{imag:+.4f}i"
    else:
        return f"{real:+.4f}{imag:+.4f}i"


def show_results(qc: QuantumCircuit, sv: Statevector = None, counts: dict = None,
                 save_plot: str = None):
    """
    Displays the quantum circuit diagram alongside the resulting quantum state
    (statevector) or measurement counts (histogram/dictionary).

    Parameters:
        qc:        The quantum circuit to display.
        sv:        Optional Statevector (pre-measurement theoretical state).
        counts:    Optional measurement counts dict (post-measurement statistics).
        save_plot: Optional filepath to save a matplotlib probability bar chart.
    """

    # ── Circuit Summary ───────────────────────────────────────────────────────
    summary = _circuit_summary(qc)
    print(f"\n{BOLD}{BG_BLUE}{WHITE}  ⟨QuantumCircuit⟩  {summary}  {RESET}")

    # ── Section 1: Circuit Diagram ────────────────────────────────────────────
    _header("CIRCUIT DIAGRAM", 1)
    print(f"{WHITE}{qc.draw('text')}{RESET}")

    section_num = 2

    # ── Section 2: Statevector ────────────────────────────────────────────────
    if sv is not None:
        _header("QUANTUM STATE (STATEVECTOR)", section_num)

        n_states = len(sv.data)
        n_qubits = qc.num_qubits
        probs = sv.probabilities_dict()

        # Column headers
        print(f"  {BOLD}{WHITE}{'State':<8} {'Amplitude':<16} {'Probability':<12} {'Distribution'}{RESET}")
        print(f"  {GRAY}{'─' * 8} {'─' * 16} {'─' * 12} {'─' * 32}{RESET}")

        # One row per basis state
        for i, amp in enumerate(sv.data):
            state_label = format(i, f'0{n_qubits}b')
            prob = abs(amp) ** 2

            if prob < 1e-10:
                # Skip zero-probability states for cleanliness
                continue

            amp_str = _format_amplitude(amp)
            color = _amplitude_color(amp.real, amp.imag)
            bar = _bar(prob)
            pct = f"{prob * 100:5.1f}%"

            print(f"  {BOLD}|{state_label}⟩{RESET}    {color}{amp_str:<16}{RESET} {YELLOW}{pct:<12}{RESET} {bar}")

        # Total probability check
        total_prob = sum(abs(a) ** 2 for a in sv.data)
        check_color = GREEN if abs(total_prob - 1.0) < 1e-6 else RED
        print(f"\n  {DIM}Total probability: {check_color}{total_prob:.4f}{RESET}")

        section_num += 1

    # ── Section 3: Measurement Counts ─────────────────────────────────────────
    if counts is not None:
        _header("MEASUREMENT RESULTS (SHOTS)", section_num)

        total_shots = sum(counts.values())

        # Column headers
        print(f"  {BOLD}{WHITE}{'Outcome':<10} {'Shots':<10} {'Frequency':<12} {'Distribution'}{RESET}")
        print(f"  {GRAY}{'─' * 10} {'─' * 10} {'─' * 12} {'─' * 32}{RESET}")

        for outcome in sorted(counts.keys()):
            cnt = counts[outcome]
            pct = (cnt / total_shots) * 100
            frac = cnt / total_shots
            bar = _bar(frac)

            print(f"  {BOLD}|{outcome}⟩{RESET}      {WHITE}{cnt:<10}{RESET} {YELLOW}{pct:5.1f}%{RESET}       {bar}")

        print(f"\n  {DIM}Total shots: {WHITE}{total_shots:,}{RESET}")

    # ── Footer ────────────────────────────────────────────────────────────────
    print(f"{CYAN}{'─' * 55}{RESET}\n")

    # ── Optional: Save matplotlib plot ────────────────────────────────────────
    if save_plot and (sv is not None or counts is not None):
        _save_probability_plot(sv, counts, save_plot, qc.num_qubits)


def _save_probability_plot(sv: Statevector, counts: dict, filepath: str, n_qubits: int):
    """Saves a matplotlib bar chart of the probability distribution."""
    try:
        import matplotlib.pyplot as plt
        import numpy as np
    except ImportError:
        print(f"  {YELLOW}[Warning] matplotlib not installed; skipping plot save.{RESET}")
        return

    fig, axes = plt.subplots(1, 1 + (1 if counts else 0), figsize=(8, 4), squeeze=False)
    fig.patch.set_facecolor("#1a1a2e")

    colors_map = {
        0: "#3b82f6",   # blue
        1: "#f97316",   # orange
        2: "#10b981",   # emerald
        3: "#a855f7",   # purple
    }

    # --- Statevector probabilities ---
    if sv is not None:
        ax = axes[0, 0]
        ax.set_facecolor("#16213e")

        probs = sv.probabilities_dict()
        states = sorted(probs.keys())
        values = [probs[s] for s in states]
        labels = [f"|{s}⟩" for s in states]
        bar_colors = [colors_map.get(i % 4, "#3b82f6") for i in range(len(states))]

        bars = ax.bar(labels, values, color=bar_colors, edgecolor="white", linewidth=0.5, alpha=0.9)
        ax.set_ylabel("Probability", color="white", fontsize=11)
        ax.set_title("Theoretical Probabilities", color="white", fontsize=12, pad=10)
        ax.set_ylim(0, 1.05)
        ax.tick_params(colors="white")
        ax.spines["bottom"].set_color("white")
        ax.spines["left"].set_color("white")
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

        for bar_obj, val in zip(bars, values):
            if val > 0.02:
                ax.text(bar_obj.get_x() + bar_obj.get_width() / 2, bar_obj.get_height() + 0.02,
                        f"{val * 100:.1f}%", ha="center", va="bottom", color="white", fontsize=9)

    # --- Measurement counts ---
    if counts is not None:
        ax_idx = 1 if sv is not None else 0
        ax = axes[0, ax_idx]
        ax.set_facecolor("#16213e")

        total = sum(counts.values())
        outcomes = sorted(counts.keys())
        values = [counts[o] / total for o in outcomes]
        labels = [f"|{o}⟩" for o in outcomes]
        bar_colors = [colors_map.get(i % 4, "#f97316") for i in range(len(outcomes))]

        bars = ax.bar(labels, values, color=bar_colors, edgecolor="white", linewidth=0.5, alpha=0.9)
        ax.set_ylabel("Frequency", color="white", fontsize=11)
        ax.set_title(f"Measured ({total:,} shots)", color="white", fontsize=12, pad=10)
        ax.set_ylim(0, 1.05)
        ax.tick_params(colors="white")
        ax.spines["bottom"].set_color("white")
        ax.spines["left"].set_color("white")
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

        for bar_obj, val in zip(bars, values):
            if val > 0.02:
                ax.text(bar_obj.get_x() + bar_obj.get_width() / 2, bar_obj.get_height() + 0.02,
                        f"{val * 100:.1f}%", ha="center", va="bottom", color="white", fontsize=9)

    plt.tight_layout()
    plt.savefig(filepath, dpi=200, facecolor=fig.get_facecolor())
    plt.close()
    print(f"  {GREEN}Plot saved to: {filepath}{RESET}")
