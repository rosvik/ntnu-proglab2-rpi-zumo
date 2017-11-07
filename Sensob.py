
class UV(Sensob):

    def __init__(self):
        self.sensors = [Ultrasonic()]

    def update(self):
        self.sensors[0].update()

    def get_value(self):
        self.value = self.sensors[0].value

    def reset(self):
        self.sensors[0].reset
=======
        self.sensor.update()




>>>>>>> Stashed changes
