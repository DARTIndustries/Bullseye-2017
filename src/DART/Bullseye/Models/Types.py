import sys
import math

sys.path.insert(0, '../../../')

from typing import NamedTuple


class Coordinate(NamedTuple):
    x: float
    y: float
    z: float

    def toList(self) -> tuple:
        return (self.x, self.y, self.z)

    def normalize(self):
        norm = self.norm()
        if norm == 0:
            return Coordinate(0, 0, 0)
        return Coordinate(self.x / norm, self.y / norm, self.z / norm)

    def norm(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
