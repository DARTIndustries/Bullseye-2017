#DART 2018
#Camera Controller

import sys
sys.path.insert(0, '../../../')
from DART.Bullseye.Controllers.Controller import Controller
from DART.Bullseye.Drivers.ServoDriver import ServoDriver
from libs.Singleton import Singleton


SERVO_PIN = 11 #TODO SET PIN NUM

@Singleton
class ClawController(Controller):
    def __init__(self):
        self.servo = ServoDriver(SERVO_PIN)

    def execute(self, command):
        if not command.isLongRunning:
            val = command.value
            self.servo.setValue(val)
            print("Camera Controller: Set Claw To: ", val)
        else:
            print("Camera Controller: No Long running support!")

