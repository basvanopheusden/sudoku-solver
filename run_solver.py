#!/usr/bin/env python
"""Command line helper to solve one of the example Sudoku boards."""

import argparse
from copy import deepcopy

from board import Board
import example_boards


def main():
    parser = argparse.ArgumentParser(description="Solve an example Sudoku puzzle")
    parser.add_argument(
        "board",
        choices=example_boards.BOARDS.keys(),
        help="Name of the example board to solve",
    )
    args = parser.parse_args()

    grid = deepcopy(example_boards.BOARDS[args.board])
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
