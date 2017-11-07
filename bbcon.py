import random
import imager2 as IMR
import Sensob
import Arbitrator
import behavior
from reflectance_sensors import ReflectanceSensors
from camera import Camera
from motors import Motors
from ultrasonic import Ultrasonic
from zumo_button import ZumoButton
from time import sleep

class BBCON():
    def __init__(self):
        self.behaviors = []
        self.active_behaviors = []
        self.inactive_behaviors = []
        self.sensobs = []
        self.motobs = []
        self.current_timestep = 0
        self.arbitrator = Arbitrator()

        self.add_sensob(UV())
        self.add_sensob(Proximity())
        self.add_sensob(CameraSensob())

    def add_behavior(behavior):
        self.behaviors.append(behavior)

    def add_sensob(sensob):
        self.sensobs.append(sensob)

    def activate_behavior(behavior):
        if behavior not in self.active_behaviors:
            self.active_behaviors.append(behavior)

    def deactivate_behavior(behavior):
        if behavior in self.active_behaviors:
            self.active_behaviors.pop(behavior)

    def run_one_timestep():
        for i in range(len(self.sensobs)):
            self.sensobs[i].update()
        for j in range(len(self.active_behaviors)):
            self.active_behaviors[j].update()
        self.arbitrator.choose_action()