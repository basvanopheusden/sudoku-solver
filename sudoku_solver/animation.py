import os
import time

RESET = "\033[0m"
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"


def _format_grid(grid, prev=None):
    """Return a formatted string representation of ``grid``.

    When ``prev`` is provided, cells that changed compared to the previous
    step are highlighted:

    * New values are shown in green
    * Removed values are shown in red
    * Changed values are shown in yellow
    """

    horizontal = "+-------+-------+-------+"
    lines = [horizontal]
    for r in range(9):
        row_vals = []
        for c in range(9):
            val = grid[r][c]
            prev_val = None if prev is None else prev[r][c]
            cell = str(val) if val != 0 else "."

            if prev is not None and val != prev_val:
                if prev_val == 0 and val != 0:
                    cell = f"{GREEN}{cell}{RESET}"
                elif prev_val != 0 and val == 0:
                    cell = f"{RED}{cell}{RESET}"
                else:
                    cell = f"{YELLOW}{cell}{RESET}"

            row_vals.append(cell)

        chunks = [" ".join(row_vals[i:i + 3]) for i in range(0, 9, 3)]
        lines.append("| " + " | ".join(chunks) + " |")
        if r % 3 == 2:
            lines.append(horizontal)

    return "\n".join(lines)


def animate_steps(steps, delay=0.05):
    """Animate solving steps in the terminal.

    Parameters
    ----------
    steps : list[list[list[int]]]
        Sequence of board states recorded during solving.
    delay : float
        Time in seconds between frames.
    """
    previous = None
    for grid in steps:
        os.system("cls" if os.name == "nt" else "clear")
        print(_format_grid(grid, previous))
        time.sleep(delay)
        previous = grid

