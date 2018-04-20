#!/usr/bin/python3

import sys
sys.path.insert(0, '../../../')
from DART.Bullseye.Models.Types import Coordinate


# <timeMS>, <accelX>, <accelY>, <accelZ>, <gyroX>, <gyroY>, <gyroZ>, <magX>, <magY>, <magZ>, <angleX>, <angleY>, <angleZ>

class GyroData:
    def __init__(self):
        self.time = 0
        self.accel: Coordinate = Coordinate(0.0, 0.0, 0.0)
        self.gyro: Coordinate = Coordinate(0.0, 0.0, 0.0)
        self.mag: Coordinate = Coordinate(0.0, 0.0, 0.0)
        self.angle: Coordinate = Coordinate(0.0, 0.0, 0.0)

    def __str__(self) -> str:
        return "GyroData:\n  accel: {0}\n  gyro: {1}\n  mag: {2}\n  angle: {3})".format(self.accel, self.gyro, self.mag,
                                                                                        self.angle)


