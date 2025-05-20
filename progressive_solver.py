from copy import deepcopy
from board import Board

# Fully solved Sudoku grid used as the baseline solution
SOLUTION = [
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
    grid = deepcopy(SOLUTION)
    cells = [(r, c) for r in range(9) for c in range(9)]

    step = 0
    while cells:
        r, c = cells.pop(0)
        grid[r][c] = 0

        board = Board(deepcopy(grid))
        solved = board.solve()
        if not solved:
            raise RuntimeError("Solver failed on generated puzzle")

        correct = board.grid == SOLUTION
        print(
            f"Removed {step + 1:2d} cells | backtracking steps: {board.backtrack_count:4d} | correct: {correct}"
        )
        step += 1

    print("Reached empty board")


if __name__ == "__main__":
    main()
