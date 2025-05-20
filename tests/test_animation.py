import os
import time
import pytest

from sudoku_solver import Board, animate_steps


def test_animate_steps_no_errors(monkeypatch):
    board = Board([[0]*9 for _ in range(9)])
    solved, steps = board.solve(record_steps=True)

    # Avoid clearing the terminal and sleeping during the test
    monkeypatch.setattr('sudoku_solver.animation.os.system', lambda cmd: None)
    monkeypatch.setattr('sudoku_solver.animation.time.sleep', lambda s: None)

    animate_steps(steps, delay=0)
