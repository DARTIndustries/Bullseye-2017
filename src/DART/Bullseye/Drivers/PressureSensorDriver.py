import sys

sys.path.insert(0, '../../../')
from libs import ms5837


class PressureSensorDriver:
    def __init__(self):
        self.sensor = ms5837.MS5837_30BA()  # Default I2C bus is 1 (Raspberry Pi 3)

        if not self.sensor.init():
            print("Sensor could not be initialized")

    def getTemperature(self):
        if not self.sensor.read():
            print("Sensor read failed!")

        return self.sensor.temperature(ms5837.UNITS_Centigrade)

    def getDepth(self):
        if not self.sensor.read():
            print("Sensor read failed!")

        return self.sensor.temperature(ms5837.UNITS_Centigrade)

    def getPressureAtm(self):
        if not self.sensor.read():
            print("Sensor read failed!")

        return self.sensor.pressure(ms5837.UNITS_atm)


def testDriver():
    sensor = PressureSensorDriver()

    while (True):
        input("Press Enter... ")
        print("Temperature: ", sensor.getTemperature(), "C")
        print("Pressure: ", sensor.getPressureAtm(), "atm")
        print("Depth: ", sensor.getDepth(), "m")




if __name__ == "__main__":
    testDriver()
