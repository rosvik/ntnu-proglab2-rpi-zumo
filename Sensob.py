from basic_robot.irproximity_sensor import IRProximitySensor
import basic_robot.ultrasonic
from math import floor
from basic_robot.camera import Camera
from basic_robot.ultrasonic import Ultrasonic
from time import sleep
from basic_robot.imager2 import Imager
from PIL import Image
import RPi.GPIO as GPIO

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
        return self.value

    def reset(self):
        self.sensors[0].reset()

    def update(self):
        self.sensors[0].update()
        self.value = self.sensors[0].get_value()



class CameraSensob(Sensob):

    #kamera, skal detektere farge og analysere
    def __init__(self, threshold = 0.4, CR=(0.5, 0.25, 0, 0.25)):
        super().__init__()
        self.threshold = threshold  #slingrishmonn tillatt
        self.CR = CR                #cutratio, hvor mye av bilde som skal kuttes før analyseringa
        self.sensors = [Camera()]
        self.value = []


    #tar bilde med kamera + analse av fargeverdiene
    def update(self):
        image = self.sensors[0].update()

        width, height = image.size

        # Get largest pixel
        def wta(p):
            w = max(p)
            l = list(p)
            i = l.index(w)
            g = [0,0,0]
            g[i] = 255
            return tuple(g)

        for h in range(height):
            for w in range(width):
                p = image.getpixel((w,h))
                image.putpixel((w,h),wta(p))


        # går igjennom hver piksel på bildet og 
        num_color_pixels = 0
        num_pixels = [0,0,0]

        for x in range(width):
            for y in range(height):
                pixel = list(image.getpixel((x,y)))
                num_pixels[pixel.index(255)] += 1

        color_fraction = [0.0, 0.0, 0.0]
        pixel_amount = width*height
        for c in range(len(num_pixels)):
            color_fraction[c] = num_pixels[c] / pixel_amount

        # self.value = num_color_pixels/num_pixels    #forhold mellom piksler av fargen og totalt antall
        self.value = color_fraction

    """get value - returns the Image object, which is ready to be analyzed and modified using the wide range of PIL methods."""
    def get_value(self):
        #return value to the value

        return self.value
        self.sensors[0].update()

    """reset - set the value slot to None."""
    def reset(self):
        self.sensors[0].reset()


class UV(Sensob):

    def __init__(self):
        self.sensors = [Ultrasonic()]

    def update(self):
        self.sensors[0].update()
        self.value = self.sensors[0].value

    def get_value(self):
        return self.value

    def reset(self):
        self.sensors[0].reset()


def main():
    try:
        p = Proximity()
        u = UV()
        c = CameraSensob()
        while True:    
            p.update()
            u.update()
            c.update()
            print("Camera: ", c.get_value())
            print("Proximity: ", p.get_value())
            print("UV: ", u.get_value())
            sleep(0.5)
    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
