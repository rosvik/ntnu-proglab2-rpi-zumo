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

class BBCON:
    def __init__(self):
        self.behaviors = []
        self.active_behaviors = []
        self.inactive_behaviors = []
        self.sensobs = []
        self.motobs = []
        self.current_timestep = 0
        self.arbitrator = Arbitrator(self, False)

        # Adds all behaviors to the BBCON
        self.add_behavior(UV_behavior(self))
        self.add_behavior(camera_behavior(self))
        self.add_behavior(proximity_behavior(self))

        # Adds all the sensobs used by the behaviors to the BBCON
        for behavior in self.behaviors:
            for sensob in self.behavior.sensobs:
                if sensob not in self.sensobs:
                    self.add_sensob(sensob)

        # Adds motob
        self.motobs = [Wheels()]

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
        for j in range(len(self.behaviors)):
            self.behaviors[j].update()
        self.motobs[0].update(self.arbitrator.choose_action().motor_rec)
        sleep[0.5]
        for sensob in self.sensobs:
            sensob.reset()

if __name__ == '__main__':
    main()

def main():
    bbcon = BBCON()
    x = False
    while x == False:
        bbcon.run_one_timestep()