# Sudoku Solver

This repository contains a minimal Sudoku solving library written in Python.
The `Board` class implements a simple backtracking solver for 9x9 Sudoku
puzzles.

## Installation

Install the dependencies with:

```bash
pip install -r requirements.txt
```

## Usage

```python
from board import Board

# 0 represents an empty cell
puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

board = Board(puzzle)
board.solve()
print(board)

# Find logically determined actions
actions = board.determined_actions()
print(actions)
```

## Command line helpers

Several small scripts are provided for experimenting with the solver without
writing code:

- `run_solver.py` solves one of the example puzzles.  Use `--help` to see the
  available board names (``easy``, ``medium`` and ``hard``) and run, for
  example:

  ```bash
  python run_solver.py medium
  ```

- `animate_solver.py` visualises how the solver progresses on the ``hard``
  puzzle by animating each recorded board state in the terminal.

- `iterative_removal.py` repeatedly removes numbers from a solved puzzle while
  measuring the amount of backtracking required to keep solving it.  This
  script can be used to get a feel for the solver's efficiency.

You can also record solving steps programmatically using
``board.solve(record_steps=True)`` and pass the resulting step list to
``animation.animate_steps`` for custom animations.

To run the test suite, first install the dependencies and then execute:

```bash
pip install -r requirements.txt
pytest
```
