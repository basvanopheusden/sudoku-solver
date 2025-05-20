#!/usr/bin/env python
"""Command line helper to solve one of the example Sudoku boards."""

import argparse
from sudoku_solver import Board, example_boards
from sudoku_solver.utils import copy_grid


def main():
    parser = argparse.ArgumentParser(description="Solve an example Sudoku puzzle")
    parser.add_argument(
        "board",
        choices=example_boards.BOARDS.keys(),
        help="Name of the example board to solve",
    )
    args = parser.parse_args()

    grid = copy_grid(example_boards.BOARDS[args.board])
    board = Board(grid)

    print("Initial board:\n")
    print(board)
    print()

    if board.solve():
        print("Solved board:\n")
        print(board)
    else:
        print("No solution found")


if __name__ == "__main__":
    main()
