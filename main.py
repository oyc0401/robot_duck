from duck import *

create_world()

induck = Duck(orientation="N")
induck.set_trace("blue")
induck.set_pause(0.3)

induck.move()
induck.move()
induck.turn_right()
induck.move()
induck.move()
induck.turn_left()
induck.move()
induck.move()