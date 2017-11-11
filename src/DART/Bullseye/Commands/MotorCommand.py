
#DART 10/14/17
#Namespace = DART.Bullseye.Commands
#Motor Command class

import sys
import abc
sys.path.insert(0, '../../../')
from DART.Bullseye.Commands.Command import Command
from DART.Bullseye.Controllers.MotorController import MotorController


class MotorCommand(Command):
    def __init__(self, motorNumber, value, isLongRunning=False):
        self.motorNumber = motorNumber
        self.value = value
        self.isLongRunning = isLongRunning


    def execute(self):
        print("command message")
        motorController = MotorController.Instance()
        motorController.execute(self)


    def isConflicting(self, command):
        print("Conflicting Motor Command Not implemented")
        return False


 