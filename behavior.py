from time import sleep
import random
import imager2 as IMR
from reflectance_sensors import ReflectanceSensors
from camera import Camera
from motors import Motors
from ultrasonic import Ultrasonic
from zumo_button import ZumoButton

class Behavior():
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
        self.sense_and_act() # Updates the match_degree
        self.weight_update() # Updates the weight