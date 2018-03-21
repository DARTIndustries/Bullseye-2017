#!/usr/bin/python3

#Gyro Driver -- Read via USB

import os, sys
import serial
import time
sys.path.insert(0, '../../../')
from DART.Bullseye.Models.GyroData import GyroData

#<timeMS>, <accelX>, <accelY>, <accelZ>, <gyroX>, <gyroY>, <gyroZ>, <magX>, <magY>, <magZ>, <angleX>, <angleY>, <angleZ>

class GyroDriver:
    def __init__(self):
        self.port = "/dev/ttyACM0"
        self.baud = 115200
        self.con = serial.Serial(self.port, self.baud, timeout = 5)

    def readLatest(self):
        """Purge and read the newest value from the gyro"""        
        self.con.flushInput()
        return self.read()        

    def read(self):
        """Read a set of values from the gyro. Blocking."""
        line = self.con.readline()

        if len(line) == 0:
            print("Error Reading from gyro")
            return None

        try:
            vals = line.decode().split(',')
            obj = GyroData()
            obj.time = float(vals[0])
            obj.accel = [float(vals[1]), float(vals[2]), float(vals[3])]
            obj.gyro = [float(vals[4]), float(vals[5]), float(vals[6])]
            obj.mag = [float(vals[7]), float(vals[8]), float(vals[9])]
            obj.angle = [float(vals[10]), float(vals[11]), float(vals[12])]
            return obj            
        except ValueError: 
            print("Invalid Gyro Record")
            return None



#===Test driver to read gyro values===
def testDriver():
    gyro = GyroDriver()
    while (True):
        #time.sleep(1)
        print(gyro.read())


if __name__ == "__main__":
    testDriver()


