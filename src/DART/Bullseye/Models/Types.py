import sys
sys.path.insert(0, '../../../')

from typing import NamedTuple

class Coordinate(NamedTuple):
    x: float
    y: float
    z: float

    def toList(self):
        return (self.x, self.y, self.z)
