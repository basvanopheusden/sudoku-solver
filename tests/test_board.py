import os
import sys
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from board import Board


def create_puzzle():
    return [
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


EXPECTED_SOLUTION = [
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


def test_invalid_grid_size():
    with pytest.raises(ValueError):
        Board([[0] * 8 for _ in range(9)])


def test_find_empty_and_valid_move():
    board = Board(create_puzzle())
    # First empty cell should be at row 0, col 2
    assert board.find_empty() == (0, 2)
    assert board.is_valid_move(0, 2, 2)
    # Value already in row
    assert not board.is_valid_move(0, 2, 5)


def test_board_str_uses_dot_for_zero_cells():
    puzzle = create_puzzle()
    board = Board(puzzle)
    expected_str = "\n".join(
        " ".join(str(c) if c != 0 else "." for c in row) for row in puzzle
    )
    assert str(board) == expected_str


def test_solver_succeeds_and_board_representation():
    board = Board(create_puzzle())
    assert board.solve()
    assert board.grid == EXPECTED_SOLUTION
    # After solving, there should be no empty cell
    assert board.find_empty() is None
    # Verify string representation uses spaces and newlines
    expected_str = "\n".join(
        " ".join(str(c) for c in row) for row in EXPECTED_SOLUTION
    )
    assert str(board) == expected_str


def test_record_steps_returns_sequence_of_grids():
    board = Board(create_puzzle())
    solved, steps = board.solve(record_steps=True)
    assert isinstance(steps, list)
    assert steps  # at least the initial board
    for grid in steps:
        assert isinstance(grid, list) and len(grid) == 9
        for row in grid:
            assert isinstance(row, list) and len(row) == 9


def test_is_solved_method():
    unsolved = Board(create_puzzle())
    assert not unsolved.is_solved()
    solved_board = Board(EXPECTED_SOLUTION)
    assert solved_board.is_solved()
    unsolved.solve()
    assert unsolved.is_solved()
