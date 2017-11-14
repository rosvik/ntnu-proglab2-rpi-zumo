from basic_robot.irproximity_sensor import IRProximitySensor
import basic_robot.ultrasonic
from math import floor
from basic_robot.camera import Camera
from basic_robot.ultrasonic import Ultrasonic

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

    #kamera, skal detektere farge og analysere
    def __init__(self, color, threshold = 0.3, CR=(0.5, 0.25, 0, 0.25)):
        super().__init__()
        self.color = color          #rgb tuppel av fargen du skal se for
        self.threshold = threshold  #slingrishmonn tillatt
        self.CR = CR                #cutratio, hvor mye av bilde som skal kuttes før analyseringa
        self.sensor = Camera()

    #tar bilde med kamera + analse av fargeverdiene
    def update(self):
        image = self.sensor.update()
        width, height = image.size

        s0_y = floor(height * self.CR[0])
        s1_y = floor(height * (1-self.CR[2]))
        s0_x = floor(width * self.CR[3])
        s1_x = floor(width * (1-self.CR[1]))

        lower = [self.color[i] - 255*self.threshold for i in range(3)]
        upper = [self.color[i] + 255*self.threshold for i in range(3)]

        #går igjennom hver piksel på bildet og ser om pikselet er nærme nok fargen vi ser etter. if yies, counter
        num_color_pixels = 0
        num_pixels = (s1_x - s0_x) * (s0_y - s1_y)

        for x in range(s0_x, s1_x):
            for y in range(s0_y, s1_y):
                pixel = image.getpixel((x,y))
                for i in range(3):
                    if not lower[i] <= pixel[i] <= upper[i]:
                        break
                    else:
                        num_color_pixels += 1
        self.value = num_color_pixels/num_pixels    #forhold mellom piksler av fargen og totalt antall


        print("updating camera sensor ....")

        return self.value

    """get value - returns the Image object, which is ready to be analyzed and modified using the wide range of PIL methods."""
    def get_value(self):
        #return value to the value

        return self.value
        self.sensors[0].update()

    """reset - set the value slot to None."""
    def reset(self):
        self.sensors[0].reset


class UV(Sensob):

    def __init__(self):
        self.sensors = [Ultrasonic()]

    def update(self):
        self.sensors[0].update()

    def get_value(self):
        self.value = self.sensors[0].value

    def reset(self):
        self.sensors[0].reset
