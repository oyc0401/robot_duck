from robotLib.cs1robot_ducks import *


class Duck(Robot):
    def turn_right(self):
        for i in range(3):
            self.turn_left()

    def speak(self):
        print("꽥꽥")
