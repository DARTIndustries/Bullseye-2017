# DART 10/14/17
# Namespace = DART.Bullseye.Commands
# Motor Command class

import sys

sys.path.insert(0, '../../../')
from DART.Bullseye.Commands.MovementCommand import MovementCommand
from DART.Bullseye.Commands.Command import Command
from DART.Bullseye.Controllers.MovementController import MovementController


class MotorMovementCommand(MovementCommand):
    def __init__(self, movementVector, angularVector):
        MovementCommand.__init__(self)
        self.movementVector = movementVector
        self.angularVector = angularVector
        self.isLongRunning = True

    def execute(self):
        motorController = MovementController.Instance()
        motorController.execute(self)
