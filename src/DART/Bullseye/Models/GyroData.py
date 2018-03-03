#!/usr/bin/python3

import sys
sys.path.insert(0, '../../../')

#<timeMS>, <accelX>, <accelY>, <accelZ>, <gyroX>, <gyroY>, <gyroZ>, <magX>, <magY>, <magZ>, <angleX>, <angleY>, <angleZ>

class GyroData:
    def __init__(self):
        self.time = 0
        self.accel = [0.0, 0.0, 0.0]
        self.gyro = [0.0, 0.0, 0.0]
        self.mag = [0.0, 0.0, 0.0]
        self.angle = [0.0, 0.0, 0.0]

    def __str__(self):
        return "GyroData:\n  accel: {0}\n  gyro: {1}\n  mag: {2}\n  angle: {3})".format(self.accel, self.gyro, self.mag, self.angle)