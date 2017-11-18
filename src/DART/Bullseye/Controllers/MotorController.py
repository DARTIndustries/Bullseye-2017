#DART 2017
#Motor Controller

import sys
from abc import ABC
sys.path.insert(0, '../../../')
from DART.Bullseye.Controllers.Controller import Controller
from DART.Bullseye.Drivers.MotorDriver import MotorDriver
from libs.Singleton import Singleton

#NUM_MOTORS = 6
MOTOR_PINS = [ 
#  pwm, dir   dir gpio
    (0, 7),    #4
    (1, 11),   #17
    (2, 12),   #18
    (3, 13),   #27
    (4, 15),   #22
    (5, 16),   #23
]

@Singleton
class MotorController(Controller):

    def __init__(self):
        self.motors = []
        for pins in MOTOR_PINS:
            self.motors.append(MotorDriver(pins[0], pins[1]))       

    
    def execute(self, command):
        if not command.isLongRunning:
            num = command.motorNumber
            val = command.value
            self.motors[num].setValue(val)
            print("Motor Controller: Set Motor: ", num, " To: ", val)
        else:
            print("Motor Controller: No Long running support!")


