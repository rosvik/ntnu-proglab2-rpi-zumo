from time import sleep
import random
import basic_robot.imager2 as IMR
from basic_robot.reflectance_sensors import ReflectanceSensors
from basic_robot.camera import Camera
from motors import Motors
from ultrasonic import Ultrasonic
from zumo_button import ZumoButton

class Behavior:
    def __init__(self, bbcon):
        self.bbcon = bbcon
        self.sensobs = []
        self.motor_rec = []
        self.active_flag = False
        self.halt_request = False
        self.priority = 1.0
        self.match_degree = 0
        self.weight = 0

    def consider_deactivation(self):
        # When a behavior is active (active_flag = True), the behavior must consider deactivation each timestep
        pass

    def consider_activation(self):
        # When a behavior is inacvtive (active_flag = False), it must consider activation
        pass

    def sense_and_act(self):
        # The core computations that use sensob readings to produce motor recommendations and halt requests
        self.match_degree = something

    def weight_update(self):
        self.weight = self.priority*self.match_degree

    def update(self):
        if self.active_flag:
            self.consider_deactivation()
        else:
            self.consider_activation()
        self.sense_and_act() # Updates the match_degree and motor_rec
        self.weight_update() # Updates the weight

class UV_behavior(Behavior):
    def __init__(self, bbcon):
        self.sensobs.append(UV())
        self.active_flag = True

    def sense_and_act(self):
        dist = sensob[0].get_value()
        if dist >= 10:
            self.motor_rec = ['F', 0.25, 0.3]
            self.match_degree = 0.5
            self.weight_update()
        else:
            self.motor_rec.append['S', 0, 0]
            self.match_degree = 0.7
            self.weight_update()

class camera_behavior(Behavior):
    #skrive oppførselen vi vil den skal gjøre her.
    def __init__(self, bbcon):
        self.sensobs.append(CameraSensob())


class proximity_behavior(Behavior):
    def __init__(self, bbcon):
        self.sensobs.append(Proximity())
        self.active_flag = True

    def sense_and_act(self):
        val = self.sensobs[0].get_value()
        if val[0] == True:
            self.motor_rec = ['R', 0.25, 1]
            self.match_degree = 1
        elif val[1] == True:
            self.motor_rec = ['L', 0.25, 1]
            self.match_degree = 1
        else:
            self.motor_rec = ['S', 0.25, 1]
            self.match_degree = 0
