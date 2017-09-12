'''
When cleaner does nothing, we will update cost and path, and keep state as it
is, we will not keep another node for do_nothing part
'''
from sub_status import *
from sub_initial_state_generator import generate_initial_state
from sub_grid import draw_path

path = []   # Consists of actions 'U', 'D', 'L', 'R', 'S', 'N'
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


random_initial_state = generate_initial_state(5)

node = Tree([1, 29], None)

result = iterative_deepening(node)

path = result.calc_path()

print(path)

draw_path(node.state[1], path)
