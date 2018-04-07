#DART 2018
#Camera Controller

import sys
sys.path.insert(0, '../../../')
from DART.Bullseye.Controllers.Controller import Controller
from DART.Bullseye.Drivers.ServoDriver import ServoDriver
from libs.Singleton import Singleton


VERT_SERVO_PIN = 8
HORZ_SERVO_PIN = 9

@Singleton
class CameraController(Controller):
    def __init__(self):
        self.servos = [ServoDriver(HORZ_SERVO_PIN), ServoDriver(VERT_SERVO_PIN)]

    def execute(self, command):
        if not command.isLongRunning:
            num = command.servoNum
            val = command.value
            self.servos[num].setValue(val)
            print("Servo Controller: Set Servo: ", num, " To: ", val)
        else:
            print("Servo Controller: No Long running support!")

