#DART 2018
#Camera Controller

import sys
sys.path.insert(0, '../../../')
from DART.Bullseye.Controllers.Controller import Controller
from DART.Bullseye.Drivers.LEDDriver import LEDDriver
from libs.Singleton import Singleton


GREEN_PIN = 12
RED_PIN = 13
BLUE_PIN = 14

@Singleton
class CameraController(Controller):
    def __init__(self):
        self.leds = [LEDDriver(GREEN_PIN), LEDDriver(RED_PIN), LEDDriver(BLUE_PIN)]

    def execute(self, command):
        val = self.hex_to_rgb(command.value)

        self.leds[0] = val[0]
        self.leds[1] = val[1]
        self.leds[2] = val[2]

    def hex_to_rgb(value):
        value = value.lstrip('#')
        lv = len(value)
        return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))