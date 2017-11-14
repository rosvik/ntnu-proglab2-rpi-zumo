from basic_robot.motors import *
from Motob import *

class Wheels(Motob):
    def __init__(self):
        Motob.__init__(self)


    def update(self, rec):
        self.value = rec
        self.operationalize()

    def operationalize(self):

        if self.value[0] == 'F':
            self.motors[0].forward(speed=self.value[1], dur=self.value[2])
        elif self.value[0] == 'B':
            self.motors[0].backward(speed=self.value[1], dur=self.value[2])
        elif self.value[0] == 'S':
            self.motors[0].stop()
        elif self.value[0] == 'R':
            self.motors[0].right(speed=self.value[1], dur=self.value[2])
        elif self.value[0] == 'L':
            self.motors[0].left(speed=self.value[1], dur=self.value[2])








