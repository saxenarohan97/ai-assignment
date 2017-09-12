# Define a node of a tree


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

        if (self.state == [0, 0] or self.state == [0, 9] or
                self.state == [0, 89] or self.state == [0, 99]):
            return True

        return False

    def successor(self, action):

        child = None

        if action == 'N':
            child = Tree(self.state, self)

        elif action == 'L':
            child = Tree([self.state[0], self.state[1] - 1], self)

        elif action == 'R':
            child = Tree([self.state[0], self.state[1] + 1], self)

        elif action == 'U':
            child = Tree([self.state[0], self.state[1] - 10], self)

        elif action == 'D':
            child = Tree([self.state[0], self.state[1] + 10], self)

        elif action == 'S':

            dirty_cells = self.state[0]
            mask = ~(2 ** self.state[1])

            child = Tree([dirty_cells & mask, self.state[1]], self)

        return child

    def actions(self):

        # Which actions are allowed for a particular state

        dirty_cells, position = self.state
        allowed_actions = ['N']

        if position % 10 != 0:
            allowed_actions.append('L')

        if position % 10 != 9:
            allowed_actions.append('R')

        if position // 10 != 0:
            allowed_actions.append('U')

        if position // 10 != 9:
            allowed_actions.append('D')

        mask = 2 ** position
        mask = dirty_cells & mask

        if mask != 0:
            allowed_actions.append('S')

        return allowed_actions

    def calc_path(self):

        path = []
        node = self

        while node.parent is not None:

            if node.state[0] == node.parent.state[0]:

                if node.state[1] - node.parent.state[1] == -1:
                    path = ['L'] + path

                elif node.state[1] - node.parent.state[1] == 1:
                    path = ['R'] + path

                elif node.state[1] - node.parent.state[1] == -10:
                    path = ['U'] + path

                elif node.state[1] - node.parent.state[1] == 10:
                    path = ['D'] + path

            elif (node.state[1] == node.parent.state[1]):

                dirty_child = node.state[0]
                dirty_parent = node.parent.state[0]

                difference = dirty_child ^ dirty_parent

                if bin(difference).count('1') == 1:
                    path = ['N'] + path

            node = node.parent

        return path
