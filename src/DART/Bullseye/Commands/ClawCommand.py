#DART 10/14/17
#Namespace = DART.Bullseye.Commands
#Camera Command class

import sys

from DART.Bullseye.Controllers.ClawController import ClawController

sys.path.insert(0, '../../../')
from DART.Bullseye.Commands.Command import Command


class ClawCommand(Command):
    def __init__(self, value, isLongRunning=False):
        self.value = value
        self.isLongRunning = isLongRunning


    def execute(self):
        clawController = ClawController.Instance()
        clawController.execute(self)


    def isConflicting(self, command):
        print("Conflicting Claw Command Not implemented")
        return False


 