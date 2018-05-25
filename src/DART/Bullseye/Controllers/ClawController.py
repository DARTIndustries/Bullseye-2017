#DART 2018
#Claw Controller

import sys
sys.path.insert(0, '../../../')
from DART.Bullseye.Controllers.Controller import Controller
from DART.Bullseye.Drivers.VexMotorDriver import VexMotorDriver
from libs.Singleton import Singleton


SERVO_PIN = 10

@Singleton
class ClawController(Controller):
    def __init__(self):
        self.driver = VexMotorDriver(SERVO_PIN)

    def execute(self, command):
        if not command.isLongRunning:
            val = command.value
            self.driver.setValue(val)
            # print("Claw Controller: Set Claw To: ", val)
        else:
            print("Claw Controller: No Long running support!")

