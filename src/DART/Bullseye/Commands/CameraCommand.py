#DART 10/14/17
#Namespace = DART.Bullseye.Commands
#Camera Command class

import sys
import abc
sys.path.insert(0, '../../../')
from DART.Bullseye.Commands.Command import Command
from DART.Bullseye.Controllers.CameraController import CameraController


class CameraCommand(Command):
    def __init__(self, servoNum, value, isLongRunning=False):
        self.servoNum = servoNum
        self.value = value
        self.isLongRunning = isLongRunning


    def execute(self):
        cameraController = CameraController.Instance()
        cameraController.execute(self)


    def isConflicting(self, command):
        print("Conflicting Servo Command Not implemented")
        return False


 