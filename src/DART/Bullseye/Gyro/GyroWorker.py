# DART 2018
# Camera Controller

import sys
from abc import ABC
from threading import Thread

sys.path.insert(0, '../../../')
from libs.Singleton import Singleton
from DART.Bullseye.Drivers.GyroDriver import GyroDriver
from DART.Bullseye.Models.GyroData import GyroData


@Singleton
class GyroWorker:
    gyroVal = GyroData()

    def __init__(self):
        self.gyro = GyroDriver()
        self.gyroThread = Thread(target=self.capture)
        self.gyroThread.start()

    def capture(self):
        print("Starting Gyro Capture Thread")

        # Purge before starting to loop
        self.gyro.purgeBuffer()
        while (True):
            GyroWorker.gyroVal = self.gyro.read()  # blocking
