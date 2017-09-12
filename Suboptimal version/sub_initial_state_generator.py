from random import sample
from random import randint


def generate_initial_state(p):

    # Check the value of p is correct
    assert p >= 0 and p <= 100

    dirty_cells = sample(range(100), p)
    dirty_cells.sort()

    initial_cells = 0

    for i in range(100):

        initial_cells *= 2

        if i in dirty_cells:
            initial_cells += 1

    start_positions = [0, 9, 90, 99]
    random_start = start_positions[randint(0, 3)]

    return [initial_cells, random_start]
