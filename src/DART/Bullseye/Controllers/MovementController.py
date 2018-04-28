# DART 2017
# Movement Controller

import sys
import typing

from DART.Bullseye.Gyro.GyroCorrector import GyroCorrector
from DART.Bullseye.Gyro.GyroWorker import GyroWorker
from DART.Bullseye.Models.Types import Coordinate

sys.path.insert(0, '../../../')
from DART.Bullseye.Controllers.Controller import Controller
from DART.Bullseye.Commands.Command import Command
from DART.Bullseye.Commands import VectorMovementCommand
from DART.Bullseye.Commands import MotorMovementCommand
from DART.Bullseye.Utils.VectorToMotorConverter import VectorToMotorConverter
from DART.Bullseye.Drivers.MotorDriver import MotorDriver
from libs.Singleton import Singleton

# NUM_MOTORS = 6
MOTOR_PINS = [
    #  pwm, dir, invert   dir gpio
    (0, 7, False),  # 4   True
    (1, 11, False),  # 17  True
    (2, 12, False),  # 18
    (3, 13, False),  # 27
    (4, 15, True),  # 22
    (5, 16, True),  # 23
]


@Singleton
class MovementController(Controller):

    def __init__(self):
        self.gyroCorrector = GyroCorrector()
        self.isGyroOn = False
        self.motors = []
        self.currHeading = None
        for pins in MOTOR_PINS:
            # self.motors.append("test")
            self.motors.append(MotorDriver(pins[0], pins[1], pins[2]))

    def execute(self, command: Command) -> bool:
        if type(command) is MotorMovementCommand.MotorMovementCommand:
            command = typing.cast(MotorMovementCommand.MotorMovementCommand, command)
            num = command.motorNumber
            val = command.value
            self.motors[num].setValue(val)
            # print("Motor Controller: Set Motor: ", num, " To: ", val)
            return True
        elif type(command) is VectorMovementCommand.VectorMovementCommand:
            command = typing.cast(VectorMovementCommand.VectorMovementCommand, command)

            if self.isGyroOn:
                # Call Gyro Correction
                corrected = self.gyroCorrector.correct(command)
            else:
                corrected = command

            mVals = VectorToMotorConverter.convert(corrected.movementVector, corrected.angularVector)
            for motor, val in zip(self.motors, mVals):
                motor.setValue(val)

            return not self.isGyroOn  # if gyro, not done, else finished
