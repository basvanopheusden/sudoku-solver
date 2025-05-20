class Board:
    """Represents a 9x9 sudoku board and provides a simple solver."""

    def __init__(self, grid=None):
        """Initialize the board with a 9x9 grid.

        Args:
            grid (list[list[int]] | None): Initial grid. None values are treated
                as 0 which means empty.
        """
        if grid is None:
            self.grid = [[0 for _ in range(9)] for _ in range(9)]
        else:
            if len(grid) != 9 or any(len(row) != 9 for row in grid):
                raise ValueError("Grid must be 9x9")
            self.grid = [[int(cell) for cell in row] for row in grid]

    def _row_values(self, row):
        return self.grid[row]

    def _column_values(self, col):
        return [self.grid[row][col] for row in range(9)]

    def _box_values(self, row, col):
        """Return the values in the 3x3 box for (row, col)."""
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        return [
            self.grid[r][c]
            for r in range(box_row, box_row + 3)
            for c in range(box_col, box_col + 3)
        ]

    def is_valid_move(self, row, col, value):
        """Check if placing value at (row, col) is valid."""
        if value < 1 or value > 9:
            return False
        if self.grid[row][col] != 0:
            return False
        if value in self._row_values(row):
            return False
        if value in self._column_values(col):
            return False
        if value in self._box_values(row, col):
            return False
        return True

    def find_empty(self):
        """Return the coordinates of the next empty cell or None if full."""
        for r in range(9):
            for c in range(9):
                if self.grid[r][c] == 0:
                    return r, c
        return None

    def solve(self):
        """Attempt to solve the board using backtracking."""
        empty = self.find_empty()
        if empty is None:
            return True
        row, col = empty
        for value in range(1, 10):
            if self.is_valid_move(row, col, value):
                self.grid[row][col] = value
                if self.solve():
                    return True
                self.grid[row][col] = 0
        return False

    def __str__(self):
        rows = []
        for r in range(9):
            row = " ".join(str(val) if val != 0 else "." for val in self.grid[r])
            rows.append(row)
        return "\n".join(rows)
