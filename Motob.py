from basic_robot.motors import *

class Motob:

    def __init__(self):
        self.motors = [Motors()]
        self.value = None

    #receive a new motor recommendation, load it into the value slot, and operationalize it
    def update(self, rec):
        pass



    #convert a motor recommendation into one or more motor settings, which are sent to the corresponding motor(s)
    def operationalize(self):
        pass




