from basic_robot/irproximity_sensor import IRProximitySensor

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
        self.sensor = IRProximitySensor()

    def get_value(self):
        self.update() # TODO: Is this needed?

        # True means something is close
        # Boolean array, with one value for each sensor
        self.value = self.sensor.value

    def reset(self):
        self.sensor.reset()

    def update(self):
        self.sensor.update()
