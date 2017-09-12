from random import sample
from random import randint


def generate_initial_state(p):

    # Check the value of p is correct
    assert p >= 0 and p <= 100

    dirty_cells = sample(range(100), p)
    dirty_cells.sort()

    initial_cells = 0

    for i in range(100):

        initial_cells = initial_cells << 1

        if i in dirty_cells:
            initial_cells += 1

    random_start = randint(0, 99)

    initial_state = (initial_cells << 7) | random_start

    return initial_state
