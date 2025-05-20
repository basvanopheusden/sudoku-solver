import os
import sys
import time
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from board import Board
from animation import animate_steps


def test_animate_steps_no_errors(monkeypatch):
    board = Board([[0]*9 for _ in range(9)])
    solved, steps = board.solve(record_steps=True)

    # Avoid clearing the terminal and sleeping during the test
    monkeypatch.setattr('animation.os.system', lambda cmd: None)
    monkeypatch.setattr('animation.time.sleep', lambda s: None)

    animate_steps(steps, delay=0)
