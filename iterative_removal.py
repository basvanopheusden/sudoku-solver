#!/usr/bin/env python
"""Iteratively remove numbers from a solved board and measure solver effort."""

import random

from sudoku_solver import Board
from sudoku_solver.utils import copy_grid

# Solved board taken from tests
SOLVED = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
]


def main():
    puzzle = copy_grid(SOLVED)
    cells = [(r, c) for r in range(9) for c in range(9)]
    random.shuffle(cells)

    removed = 0
    while cells:
        r, c = cells.pop()
        puzzle[r][c] = 0
        removed += 1

        board = Board(copy_grid(puzzle))
        solved, count = board.solve_with_counter()
        assert solved, "Board became unsolvable"
        assert board.is_solved(), "Solved board is invalid"

        print(f"Blanks: {removed:2d}, backtracking steps: {count}")

    print("Finished. Board is empty.")


if __name__ == "__main__":
    main()
