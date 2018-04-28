from DART.Bullseye.Commands import VectorMovementCommand
from DART.Bullseye.Gyro.GyroWorker import GyroWorker
from DART.Bullseye.Models.Types import Coordinate


class GyroCorrector:

    def __init__(self):
        self.currHeading = None

    def correct(self, command: VectorMovementCommand.VectorMovementCommand):
        if command.angularVector.isZero():
            self.currHeading = GyroWorker.gyroVal.angle
            return command
        elif self.currHeading is not None:
            # Find the offset and the angular velocity correction
            x = self.angleDiffCorrection(self.calcAngleDiff(self.currHeading.x, GyroWorker.gyroVal.angle.x))
            y = self.angleDiffCorrection(self.calcAngleDiff(self.currHeading.y, GyroWorker.gyroVal.angle.y))
            z = self.angleDiffCorrection(self.calcAngleDiff(self.currHeading.z, GyroWorker.gyroVal.angle.z))

            # Build the correction vector by taking max, normalizing, then scaling to max
            scale = abs(max(x, y, z, key=abs))
            angles = Coordinate(x, y, z).normalize()
            angles.multiply(scale)

            # Update Command angle vector
            command.angularVector = angles
            return command

    def calcAngleDiff(self, desiredVal: float, gyroVal: float):
        """Takes in angles in deg 0-360 and finds their difference"""
        diff = gyroVal - desiredVal
        sign = 1 if diff >= 0 else -1

        if abs(diff) > 180:
            return (abs(diff) - 360) * sign
        else:
            return diff

    def angleDiffCorrection(self, diff: float) -> float:
        """Takes a diff in degrees and returns an angular velocity -1 to 1 to correct it"""
        sign = 1 if diff >= 0 else -1
        netDiff = abs(diff)
        if netDiff > 30:
            return sign
        else:
            return sign * (0.0012 * netDiff ** 2 - 0.0035 * netDiff + 0.0339)
