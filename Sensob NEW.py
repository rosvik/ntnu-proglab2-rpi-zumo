from basic_robot/irproximity_sensor import IRProximitySensor
import basic_robot/ultrasonic

class Sensob:

    #serves as an interface between one or more sensors and bbcon behav
    def __init__(self):
        self.sensors = []
        self.value = None

    def get_value(self):
        return self.value

    def update(self):
        return

    def reset(self):
        #resets

        for sensor in self.sensors:
            sensor.reset()


class Proximity(Sensob):

    def __init__(self):
        self.sensors = [IRProximitySensor()]
        self.value = None

    def get_value(self):
        # True means something is close
        # Boolean array, with one value for each sensor
        self.value = self.sensors[0].value

    def reset(self):
        self.sensors[0].reset()

    def update(self):
        self.sensors[0].update()


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
        self.sensors[0].update()


class UV(Sensob):

    def __init__(self):
        self.sensors = [Ultrasonic()]

    def update(self):
        self.sensors[0].update()

    def get_value(self):
        self.value = self.sensors[0].value

    def reset(self):
        self.sensors[0].reset
