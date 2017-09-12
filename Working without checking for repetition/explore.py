from status import *
from initial_state_generator import generate_initial_state
from grid import draw_path, fill_dirt_in_grid

explored_states = []


def depth_limited_search(node, limit):

    if node.goal_check():
        return node

    elif limit == 0:
        return 'cutoff'

    else:

        cutoff = False

        for action in node.actions():

            child = node.successor(action)

            result = depth_limited_search(child, limit - 1)

            if result == 'cutoff':
                cutoff = True

            elif result != 'failure':
                return result

        if cutoff:
            return 'cutoff'

        else:
            return 'failure'


def iterative_deepening(node):

    depth = 0

    while True:

        result = depth_limited_search(node, depth)

        if result != 'cutoff':
            return result

        depth += 1


node = Tree(129, None)

fill_dirt_in_grid(node.state)

result = iterative_deepening(node)

path = result.calc_path()

print path

draw_path(split_state(node.state)[1], path)

close = 'n'

while close != 'y':
    close = raw_input('Close(y/n): ')
