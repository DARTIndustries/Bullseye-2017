import sys

sys.path.insert(0, '../../../')
from DART.Bullseye.Models.Types import Coordinate


class VectorToMotorConverter:
    @staticmethod
    def convert(movementVector: Coordinate, angleVector: Coordinate) -> tuple:
        pass
