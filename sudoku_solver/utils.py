from typing import Generator, List


def iter_coords() -> Generator[tuple[int, int], None, None]:
    """Yield all coordinates on a 9x9 Sudoku grid."""
    for r in range(9):
        for c in range(9):
            yield r, c


def iter_box_coords(box_row: int, box_col: int) -> Generator[tuple[int, int], None, None]:
    """Yield coordinates within the 3x3 box identified by ``box_row`` and ``box_col``."""
    for r in range(box_row * 3, box_row * 3 + 3):
        for c in range(box_col * 3, box_col * 3 + 3):
            yield r, c


def copy_grid(grid: List[List[int]]) -> List[List[int]]:
    """Return a deep copy of ``grid``."""
    return [row[:] for row in grid]


def create_empty_grid() -> List[List[int]]:
    """Return a new 9x9 grid initialised with zeros."""
    return [[0 for _ in range(9)] for _ in range(9)]


def validate_grid(grid: List[List[int]]):
    """Ensure ``grid`` is a 9x9 matrix with values between 0 and 9 or ``None``."""
    if len(grid) != 9 or any(len(row) != 9 for row in grid):
        raise ValueError("Grid must be 9x9")
    for row in grid:
        for cell in row:
            if cell is not None:
                value = int(cell)
                if value < 0 or value > 9:
                    raise ValueError("Cell values must be between 0 and 9")


def normalize_grid(grid: List[List[int]]) -> List[List[int]]:
    """Return a copy of ``grid`` with ``None`` replaced by 0 and all values cast to ``int``."""
    return [[0 if cell is None else int(cell) for cell in row] for row in grid]
