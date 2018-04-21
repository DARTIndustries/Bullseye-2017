
#DART 10/14/17
#Namespace = DART.Bullseye.Commands
#Motor Command class

import sys

sys.path.insert(0, '../../../')
from DART.Bullseye.Commands.MovementCommand import MovementCommand
from DART.Bullseye.Controllers.MovementController import MovementController


class MotorMovementCommand(MovementCommand):
    def __init__(self, motorNumber, value, isLongRunning=False):
        MovementCommand.__init__(self)
        self.motorNumber = motorNumber
        self.value = value
        self.isLongRunning = isLongRunning

    def execute(self):
        motorController = MovementController.Instance()
        motorController.execute(self)
 