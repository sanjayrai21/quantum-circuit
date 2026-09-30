import sys
from pathlib import Path
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector


def save_bloch_sphere(sv: Statevector, filepath: str = None, title: str = None):
    """
    Saves a Bloch sphere visualization of the given quantum state as a PNG image.

    The Bloch sphere is a 3D unit sphere that represents a single qubit's state:
      - |0> sits at the North Pole (top)
      - |1> sits at the South Pole (bottom)
      - |+> sits on the equator facing you (positive X axis)
      - |-> sits on the equator behind the sphere (negative X axis)
      - Any other state sits somewhere on or inside the sphere

    For multi-qubit states, one sphere per qubit is drawn side by side.

    Parameters:
        sv:       A Qiskit Statevector object.
        filepath: Where to save the PNG. Defaults to 'bloch_sphere.png' in the cwd.
        title:    Optional title to display above the plot.
    """
    if filepath is None:
        filepath = "bloch_sphere.png"

    fig = plot_bloch_multivector(sv)

    if title:
        fig.suptitle(title, fontsize=14, y=1.02)

    fig.savefig(filepath, dpi=200, bbox_inches="tight", facecolor="white")
    print(f"  Bloch sphere saved to: {filepath}")


# ── Standalone demo: run this file directly to see example Bloch spheres ──────
if __name__ == "__main__":
    # Add workspace root for imports
    sys.path.append(str(Path(__file__).resolve().parent.parent))

    output_dir = Path(__file__).resolve().parent.parent / "bloch_examples"
    output_dir.mkdir(exist_ok=True)

    examples = [
        ("Ground state |0>",             lambda: QuantumCircuit(1)),
        ("Excited state |1>",            lambda: _apply(QuantumCircuit(1), lambda qc: qc.x(0))),
        ("Plus state |+> (H gate)",      lambda: _apply(QuantumCircuit(1), lambda qc: qc.h(0))),
        ("Minus state |-> (H then Z)",   lambda: _apply(QuantumCircuit(1), lambda qc: (qc.h(0), qc.z(0)))),
        ("Bell state (2 qubits)",        lambda: _apply(QuantumCircuit(2), lambda qc: (qc.h(0), qc.cx(0, 1)))),
    ]

    def _apply(qc, fn):
        fn(qc)
        return qc

    for name, builder in examples:
        qc = builder()
        sv = Statevector(qc)
        safe_name = name.lower().replace(" ", "_").replace("|", "").replace(">", "").replace("(", "").replace(")", "")
        filepath = output_dir / f"{safe_name}.png"
        print(f"\n  Generating: {name}")
        save_bloch_sphere(sv, str(filepath), title=name)

    print(f"\n  All Bloch sphere examples saved to: {output_dir}")
