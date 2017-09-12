import turtle as t
from status import split_state


def draw_grid():

    for i in range(5):

        t.fd(600)
        t.left(90)
        t.fd(60)
        t.left(90)

        t.fd(600)
        t.right(90)
        t.fd(60)
        t.right(90)

    t.fd(600)
    t.right(90)

    for i in range(5):

        t.fd(600)
        t.right(90)
        t.fd(60)
        t.right(90)

        t.fd(600)
        t.left(90)
        t.fd(60)
        t.left(90)

    t.fd(600)
    t.left(90)

    t.right(180)


def fill_dirt_in_cell(cell):

    t.color('brown')
    t.begin_fill()
    x_cord = -270 + 60 * (cell % 10)
    y_cord = 250 - 60 * (cell // 10)
    t.penup()
    t.setposition(x_cord, y_cord)
    t.setheading(0)
    t.pendown()
    t.circle(20)

    t.end_fill()
    t.color('black')


def get_coords(position):

    x = -270 + 60 * (position % 10)
    y = 270 - 60 * (position // 10)

    return [x, y]


def fill_dirt_in_grid(initial_state):

    dirty_cells, initial_position = split_state(initial_state)

    temp = dirty_cells
    i = 0

    while temp != 0:

        if temp % 2 == 1:
            fill_dirt_in_cell(i)

        i += 1
        temp = temp >> 1

    t.penup()
    x, y = get_coords(initial_position)
    t.setposition(x, y)
    t.pendown()


def draw_path(initial_position, path):

    t.speed(3)
    t.penup()
    t.setposition(get_coords(initial_position))
    t.pendown()
    t.color('red')

    for action in path:

        if action == 'L':
            t.setheading(180)

        if action == 'R':
            t.setheading(0)

        if action == 'U':
            t.setheading(90)

        if action == 'D':
            t.setheading(270)

        if action != 'N':
            t.forward(60)

        t.setheading(0)

    t.speed(0)


t.speed(0)
t.pensize(4)
t.shape('turtle')
t.setposition(300, 300)
t.clear()
t.setheading(180)

draw_grid()
