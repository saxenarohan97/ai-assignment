# Define a node of a tree


def merge_state(dirty_cells, position):

    dirty_cells = dirty_cells << 7

    state = dirty_cells | position

    return state


def split_state(state):

    mask = 0b1111111
    position = state & mask

    mask = -1 << 7
    dirty_cells = state & mask
    dirty_cells = dirty_cells >> 7

    return [dirty_cells, position]


class Tree(object):

    def __init__(self, state, parent):

        self.state = state      # Contains [grid, pos] for current node
        self.left = None        # Node when robot goes left
        self.right = None       # Node when robot goes right
        self.up = None          # Node when robot goes up
        self.down = None        # Node when robot goes down
        self.suck = None        # Node when robot sucks the dirt
        self.parent = parent    # Stores the parent of the node for path
        # self.nothing = None     # Node when robot does nothing

    def goal_check(self):

        if (self.state == 0 or self.state == 9 or
                self.state == 89 or self.state == 99):
            return True

        return False

    def successor(self, action):

        child = None
        dirty_cells, position = split_state(self.state)

        if action == 'N':
            child = Tree(self.state, self)

        elif action == 'L':
            child = Tree(merge_state(dirty_cells, position - 1), self)

        elif action == 'R':
            child = Tree(merge_state(dirty_cells, position + 1), self)

        elif action == 'U':
            child = Tree(merge_state(dirty_cells, position - 10), self)

        elif action == 'D':
            child = Tree(merge_state(dirty_cells, position + 10), self)

        elif action == 'S':

            mask = ~(1 << position)

            child = Tree(merge_state(dirty_cells & mask, position), self)

        return child

    def actions(self):

        # Which actions are allowed for a particular state

        dirty_cells, position = split_state(self.state)
        allowed_actions = ['N']

        if position % 10 != 0:
            allowed_actions.append('L')

        if position % 10 != 9:
            allowed_actions.append('R')

        if position // 10 != 0:
            allowed_actions.append('U')

        if position // 10 != 9:
            allowed_actions.append('D')

        mask = 1 << position
        mask = dirty_cells & mask

        if mask != 0:
            allowed_actions.append('S')

        return allowed_actions

    def calc_path(self):

        path = []
        node = self

        while node.parent is not None:

            dirty_child, position_child = split_state(node.state)
            dirty_parent, position_parent = split_state(node.parent.state)

            if dirty_child == dirty_parent:

                if position_child - position_parent == -1:
                    path = ['L'] + path

                elif position_child - position_parent == 1:
                    path = ['R'] + path

                elif position_child - position_parent == -10:
                    path = ['U'] + path

                elif position_child - position_parent == 10:
                    path = ['D'] + path

            elif (position_child == position_parent):

                difference = dirty_child ^ dirty_parent

                if bin(difference).count('1') == 1:
                    path = ['N'] + path

            node = node.parent

        return path
