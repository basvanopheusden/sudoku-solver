def find_determined_squares(board):
    """Return all cells with exactly one possible value.

    Each entry in the returned list is a ``(row, col, value)`` tuple.
    """
    moves = []
    for r in range(9):
        for c in range(9):
            if board.grid[r][c] == 0:
                opts = board.valid_values_for(r, c)
                if len(opts) == 1:
                    moves.append((r, c, opts[0]))
    return moves


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
            self.grid = [[0 if cell is None else int(cell) for cell in row] for row in grid]

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

    def valid_values_for(self, row, col):
        """Return all valid values for the given empty cell."""
        if self.grid[row][col] != 0:
            return []
        return [v for v in range(1, 10) if self.is_valid_move(row, col, v)]

    def determined_actions(self):
        """Return a list of all logically forced moves.

        Each action is a ``(row, col, value)`` tuple describing a placement
        that is forced by the current state of the board. This includes cells
        that have only one possible value as well as values that can only
        appear in one cell of a row, column or 3x3 box.
        """

        possible = [[self.valid_values_for(r, c) for c in range(9)] for r in range(9)]
        actions = set()

        # Cells with a single possible value
        for r in range(9):
            for c in range(9):
                if len(possible[r][c]) == 1:
                    actions.add((r, c, possible[r][c][0]))

        # Unique position for a value in any row
        for r in range(9):
            for value in range(1, 10):
                cells = [c for c in range(9) if value in possible[r][c]]
                if len(cells) == 1:
                    actions.add((r, cells[0], value))

        # Unique position for a value in any column
        for c in range(9):
            for value in range(1, 10):
                cells = [r for r in range(9) if value in possible[r][c]]
                if len(cells) == 1:
                    actions.add((cells[0], c, value))

        # Unique position for a value in any 3x3 box
        for box_row in range(3):
            for box_col in range(3):
                coords = [
                    (r, c)
                    for r in range(box_row * 3, box_row * 3 + 3)
                    for c in range(box_col * 3, box_col * 3 + 3)
                ]
                for value in range(1, 10):
                    cells = [(r, c) for r, c in coords if value in possible[r][c]]
                    if len(cells) == 1:
                        r, c = cells[0]
                        actions.add((r, c, value))

        return sorted(actions)

    def find_empty(self):
        """Return the coordinates of the next empty cell or None if full."""
        for r in range(9):
            for c in range(9):
                if self.grid[r][c] == 0:
                    return r, c
        return None

    def solve(self, record_steps=False, _steps=None, counter=None):
        """Solve the board using backtracking with simple heuristics.

        If ``record_steps`` is True, every intermediate board state is appended
        to a list which is returned together with the solve result. This can be
        used to visualise the solving process.
        """

        if record_steps and _steps is None:
            # Start the step list with a deep copy of the initial grid so
            # callers receive a sequence of full board states rather than a
            # mix of rows and grids.
            _steps = [[row[:] for row in self.grid]]

        def apply_determined():
            actions = []
            while True:
                moves = find_determined_squares(self)
                progress = False
                for r, c, v in moves:
                    if self.grid[r][c] == 0 and self.is_valid_move(r, c, v):
                        self.grid[r][c] = v
                        actions.append((r, c))
                        if record_steps:
                            _steps.append([row[:] for row in self.grid])
                        progress = True
                if not progress:
                    break
            return actions

        actions_applied = apply_determined()

        empties = []
        for r in range(9):
            for c in range(9):
                if self.grid[r][c] == 0:
                    options = self.valid_values_for(r, c)
                    if not options:
                        for ar, ac in actions_applied:
                            self.grid[ar][ac] = 0
                            if record_steps:
                                _steps.append([row[:] for row in self.grid])
                        return (False, _steps) if record_steps else False
                    empties.append((len(options), r, c, options))

        if not empties:
            solved = self.is_solved()
            return (solved, _steps) if record_steps else solved

        empties.sort(key=lambda x: x[0])
        _, row, col, options = empties[0]
        for value in options:
            if not self.is_valid_move(row, col, value):
                continue
            self.grid[row][col] = value
            if record_steps:
                _steps.append([row[:] for row in self.grid])
            if counter is not None:
                counter[0] += 1
            result = self.solve(record_steps=record_steps, _steps=_steps, counter=counter)
            solved = result[0] if record_steps else result
            if solved:
                return (True, _steps) if record_steps else True
            self.grid[row][col] = 0
            if record_steps:
                _steps.append([row[:] for row in self.grid])

        for ar, ac in actions_applied:
            self.grid[ar][ac] = 0
            if record_steps:
                _steps.append([row[:] for row in self.grid])
        return (False, _steps) if record_steps else False

    def __str__(self):
        rows = []
        for r in range(9):
            row = " ".join(str(val) if val != 0 else "." for val in self.grid[r])
            rows.append(row)
        return "\n".join(rows)

    def is_solved(self):
        """Return ``True`` if the board is completely and validly solved."""
        digits = set(range(1, 10))
        for r in range(9):
            if set(self._row_values(r)) != digits:
                return False
        for c in range(9):
            if set(self._column_values(c)) != digits:
                return False
        for br in range(0, 9, 3):
            for bc in range(0, 9, 3):
                values = [
                    self.grid[r][c]
                    for r in range(br, br + 3)
                    for c in range(bc, bc + 3)
                ]
                if set(values) != digits:
                    return False
        return True

    def solve_with_counter(self):
        """Solve the board and return a tuple of (solved, count)."""
        counter = [0]
        solved = self.solve(counter=counter)
        return solved, counter[0]
