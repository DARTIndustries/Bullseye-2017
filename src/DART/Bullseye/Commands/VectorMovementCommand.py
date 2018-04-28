# DART 10/14/17
# Namespace = DART.Bullseye.Commands
# Motor Command class

import sys


sys.path.insert(0, '../../../')
from DART.Bullseye.Commands.MovementCommand import MovementCommand
from DART.Bullseye.Controllers import MovementController
from DART.Bullseye.Models.Types import Coordinate


class VectorMovementCommand(MovementCommand):
    def __init__(self, movementVector: Coordinate, angularVector: Coordinate):
        MovementCommand.__init__(self)
        self.movementVector = movementVector
        self.angularVector = angularVector
        self.isLongRunning = True

    def execute(self):
        motorController = MovementController.MovementController.Instance()
        return motorController.execute(self)
