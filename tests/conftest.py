import sys
from pathlib import Path

# Ensure project root is on sys.path so `sudoku_solver` can be imported when
# running `pytest` via the entrypoint script.
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
