import os
import time


def animate_steps(steps, delay=0.1):
    """Simple terminal animation of solving steps.

    Parameters
    ----------
    steps : list[list[list[int]]]
        Sequence of board states recorded during solving.
    delay : float
        Time in seconds between frames.
    """
    for grid in steps:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\n'.join(
            ' '.join(str(c) if c != 0 else '.' for c in row) for row in grid
        ))
        time.sleep(delay)

