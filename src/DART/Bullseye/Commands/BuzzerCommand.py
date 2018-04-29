# DART 10/14/17
# Namespace = DART.Bullseye.Commands
# Camera Command class

import sys

from DART.Bullseye.Controllers import BuzzerController

sys.path.insert(0, '../../../')
from DART.Bullseye.Commands.Command import Command


class BuzzerCommand(Command):
    def __init__(self, state: bool):
        self.state = state
        self.isLongRunning = True

    def execute(self):
        buzzerController = BuzzerController.BuzzerController.Instance()
        return buzzerController.execute(self)

    def isConflicting(self, command) -> bool:
        if type(command) is BuzzerCommand:
            return True
        return False
