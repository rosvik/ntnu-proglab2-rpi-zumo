from Sensob import *
from camera import *

class CameraSensob(Sensob):

    #kamera

    def __init__(self):
        super(CameraSensob, self).__init__()
        self.sonsor = Camera()
        self.sensors.append(self.sensor)
        self.value = None

    def update(self):

        #updates the values

        print("updating camera sensor ....")
        self.sensors[0].update()
        self.value = self.sensors[0].get_value()
        return self.value

    def get_value(self):

        #return value to the value

        return self.value
