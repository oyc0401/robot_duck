from duck import *

create_world()

induck = Duck(orientation="N")
induck.set_trace("blue")
induck.set_pause(0.3)


def move_9():
    for i in range(9):
        induck.move()


def zigzag():
    move_9()
    induck.turn_right()
    induck.move()
    induck.turn_right()
    move_9()


def zig():
    zigzag()
    induck.turn_left()
    induck.move()
    induck.turn_left()


zig()
zig()
zig()
zig()
zigzag()
