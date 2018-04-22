# DART 2018
# Camera Controller

import sys


sys.path.insert(0, '../../../')
from DART.Bullseye.Controllers.Controller import Controller
from DART.Bullseye.Drivers.LEDDriver import LEDDriver
from libs.Singleton import Singleton

GREEN_PIN = 12
RED_PIN = 13
BLUE_PIN = 14

@Singleton
class LEDController(Controller):
    def __init__(self):
        self.leds = [LEDDriver(GREEN_PIN), LEDDriver(RED_PIN), LEDDriver(BLUE_PIN)]

    def execute(self, command):
        val = self.hex_to_rgb(command.value)

        self.leds[0].setValue(val[0])
        self.leds[1].setValue(val[1])
        self.leds[2].setValue(val[2])

    def hex_to_rgb(self, value):
        value = value.lstrip('#')
        lv = len(value)
        return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def testDriver():
    tester = LEDController.Instance()
    print(tester.hex_to_rgb('#800000'))

if __name__ == "__main__":
    testDriver()
