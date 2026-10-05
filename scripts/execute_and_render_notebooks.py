"""Execute all notebooks and save full output in .ipynb format for submission."""
from __future__ import annotations

import sys
import os
import shutil
import time
from pathlib import Path
import nbformat
from nbclient import NotebookClient
import jupytext

ROOT = Path(__file__).resolve().parents[1]
NB_DIR = ROOT / "notebooks"
SUBMISSION_NB_DIR = ROOT / "submission" / "notebooks"
SUBMISSION_NB_DIR.mkdir(parents=True, exist_ok=True)

def main():
    py_files = sorted(p for p in NB_DIR.glob("[0-9]*.py"))
    print(f"Found {len(py_files)} notebooks to execute and render.")

    for py_path in py_files:
        nb_name = py_path.stem
        ipynb_name = f"{nb_name}.ipynb"
        ipynb_path = NB_DIR / ipynb_name
        dest_ipynb = SUBMISSION_NB_DIR / ipynb_name

        print(f"\n--- Processing {nb_name} ---")
        # Load from .py using jupytext
        nb = jupytext.read(py_path)

        # Execute using NotebookClient
        client = NotebookClient(nb, timeout=600, kernel_name="python3", resources={"metadata": {"path": str(NB_DIR)}})
        t0 = time.perf_counter()
        client.execute()
        dt = time.perf_counter() - t0
        print(f"Executed {nb_name} in {dt:.1f}s")

        # Write executed notebook to NB_DIR and SUBMISSION_NB_DIR
        with open(ipynb_path, "w", encoding="utf-8") as f:
            nbformat.write(nb, f)
        with open(dest_ipynb, "w", encoding="utf-8") as f:
            nbformat.write(nb, f)
        print(f"Saved executed notebook to {dest_ipynb}")

    print("\nAll notebooks executed and saved successfully!")

if __name__ == "__main__":
    main()
