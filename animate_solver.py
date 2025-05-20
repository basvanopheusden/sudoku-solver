#!/usr/bin/env python
"""Solve the hard example board and animate the solving steps."""

from copy import deepcopy

from board import Board
from animation import animate_steps
import example_boards


def main():
    grid = deepcopy(example_boards.HARD)
    board = Board(grid)

    solved, steps = board.solve(record_steps=True)
    animate_steps(steps)

    if solved:
        print("Solved board:\n")
        print(board)
    else:
        print("No solution found")


if __name__ == "__main__":
    main()
