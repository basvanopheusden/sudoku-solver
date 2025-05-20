# Sudoku Solver

This repository contains a minimal Sudoku solving library written in Python.
The `Board` class implements a simple backtracking solver for 9x9 Sudoku
puzzles.

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

To run the test suite:

```bash
pytest
```
