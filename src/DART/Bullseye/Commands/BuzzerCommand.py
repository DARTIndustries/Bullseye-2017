# DART 10/14/17
# Namespace = DART.Bullseye.Commands
# Camera Command class

import sys

from DART.Bullseye.Controllers.BuzzerController import BuzzerController

sys.path.insert(0, '../../../')
from DART.Bullseye.Commands.Command import Command


class BuzzerCommand(Command):
    def __init__(self, state: bool):
        self.state = state
        self.isLongRunning = True

    def execute(self):
        buzzerController = BuzzerController.Instance()
        buzzerController.execute(self)

    def isConflicting(self, command) -> bool:
        if type(command) is BuzzerCommand:
            return command.state != self.state  # Conflicting if not equal
        return False
