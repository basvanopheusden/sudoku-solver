"""Simple Sudoku solver using backtracking."""

from __future__ import annotations

from typing import List, Optional, Tuple

Grid = List[List[int]]


def find_empty(grid: Grid) -> Optional[Tuple[int, int]]:
    """Return coordinates of the next empty cell or None if full."""
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                return r, c
    return None


def is_valid(grid: Grid, row: int, col: int, value: int) -> bool:
    """Check whether placing value at (row, col) is valid."""
    if value in grid[row]:
        return False
    if value in [grid[r][col] for r in range(9)]:
        return False
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    for r in range(box_row, box_row + 3):
        for c in range(box_col, box_col + 3):
            if grid[r][c] == value:
                return False
    return True


def solve_sudoku(grid: Grid) -> bool:
    """Solve the Sudoku puzzle in-place using backtracking."""
    empty = find_empty(grid)
    if empty is None:
        return True
    row, col = empty
    for value in range(1, 10):
        if is_valid(grid, row, col, value):
            grid[row][col] = value
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0
    return False

