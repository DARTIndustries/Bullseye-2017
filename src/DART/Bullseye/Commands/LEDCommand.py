# DART 10/14/17
# Namespace = DART.Bullseye.Commands
# LED Command class

import sys

sys.path.insert(0, '../../../')
from DART.Bullseye.Commands.Command import Command
from DART.Bullseye.Controllers import LEDController


class LEDCommand(Command):

    def __init__(self, value):
        super().__init__()
        self.value = value

    def execute(self):
        LEDController.LEDController.Instance().execute(self)
        return False

    def isConflicting(self, command):
        print("Conflicting LED Command Not implemented")
        return False
