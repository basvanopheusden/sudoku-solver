import pytest

from sudoku_solver import Board, example_boards, _format_grid, GREEN, RED, YELLOW


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


def test_valid_values_for_empty_and_filled_cell():
    board = Board(example_boards.MEDIUM)
    assert board.valid_values_for(0, 0) == []
    assert board.valid_values_for(0, 2) == [1, 2, 4]


def test_is_valid_move_rejects_out_of_range_values():
    board = Board(example_boards.MEDIUM)
    assert not board.is_valid_move(0, 2, 0)
    assert not board.is_valid_move(0, 2, 10)
    assert not board.is_valid_move(0, 2, -1)


def test_board_initializes_none_as_empty():
    board = Board([[None] * 9 for _ in range(9)])
    for row in board.grid:
        assert all(val == 0 for val in row)


def test_solve_with_counter_returns_steps():
    board = Board(example_boards.MEDIUM)
    solved, count = board.solve_with_counter()
    assert solved
    assert isinstance(count, int) and count >= 0
    assert board.grid == EXPECTED_SOLUTION


def test_format_grid_highlights_changes():
    prev = [[0] * 9 for _ in range(9)]
    cur = [[0] * 9 for _ in range(9)]
    prev[0][0] = 1
    cur[0][0] = 2  # changed value
    cur[0][1] = 3  # new value
    prev[0][2] = 4
    # value removed at (0,2)
    out = _format_grid(cur, prev)
    assert GREEN in out
    assert RED in out
    assert YELLOW in out

