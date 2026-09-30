"""
Quick runner: execute any experiment by its number or name.

Usage:
    uv run python run.py 1          # runs foundations/01_single_qubit/main.py
    uv run python run.py 03         # runs foundations/03_measurement/main.py
    uv run python run.py grover     # runs algorithms/grover_search/main.py
    uv run python run.py            # lists all available experiments
"""

import sys
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent

# Scan all stage directories for folders containing main.py
STAGES = ["foundations", "algorithms", "applications", "hardware"]


def find_experiments():
    """Returns a dict mapping short keys to main.py paths."""
    experiments = {}
    for stage in STAGES:
        stage_dir = ROOT / stage
        if not stage_dir.is_dir():
            continue
        for folder in sorted(stage_dir.iterdir()):
            main_py = folder / "main.py"
            if main_py.exists():
                # Extract number prefix if it exists (e.g., "01" from "01_single_qubit")
                name = folder.name
                parts = name.split("_", 1)

                # Register by full folder name
                experiments[name] = main_py

                # Register by number (e.g., "1", "01")
                if parts[0].isdigit():
                    num = parts[0]
                    experiments[num] = main_py
                    experiments[str(int(num))] = main_py  # "01" -> also "1"

                # Register by short keyword (e.g., "grover" matches "grover_search")
                for word in name.replace("_", " ").split():
                    if not word.isdigit() and len(word) > 2:
                        experiments[word.lower()] = main_py

    # Add standalone utilities
    bloch_script = ROOT / "utils" / "bloch.py"
    if bloch_script.exists():
        experiments["bloch"] = bloch_script

    return experiments


def list_experiments():
    """Prints all available experiments grouped by stage."""
    print("\n  Available experiments:\n")
    for stage in STAGES:
        stage_dir = ROOT / stage
        if not stage_dir.is_dir():
            continue
        folders = sorted(
            f for f in stage_dir.iterdir()
            if (f / "main.py").exists()
        )
        if not folders:
            continue

        print(f"  {stage.upper()}")
        for folder in folders:
            name = folder.name
            parts = name.split("_", 1)
            if parts[0].isdigit():
                shortcut = parts[0].lstrip("0") or "0"
                label = parts[1].replace("_", " ").title() if len(parts) > 1 else name
                print(f"    {shortcut:>3}  {label}")
            else:
                print(f"        {name.replace('_', ' ').title()}")
        print()

    print("  UTILITIES")
    print("    bloch  Generate sample 3D Bloch sphere diagrams")
    print()
    print("  Usage:  uv run python run.py <number or keyword>")
    print("          .\\run <number or keyword>    (in PowerShell)\n")


def main():
    if len(sys.argv) < 2:
        list_experiments()
        return

    key = sys.argv[1].lower().strip()
    experiments = find_experiments()

    if key in experiments:
        path = experiments[key]
        print(f"\n  Running: {path.relative_to(ROOT)}\n", flush=True)
        result = subprocess.run([sys.executable, str(path)], cwd=str(ROOT))
        sys.exit(result.returncode)
    else:
        print(f"\n  No experiment found for '{key}'.")
        print(f"  Try: uv run python run.py\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
