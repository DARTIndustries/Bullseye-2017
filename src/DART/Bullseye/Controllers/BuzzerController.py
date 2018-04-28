# Buzzer Controller

import time
import sys


sys.path.insert(0, '../../../')
from DART.Bullseye.Controllers.Controller import Controller
from DART.Bullseye.Drivers.ServoDriver import ServoDriver
from libs.Singleton import Singleton

TRIGGER_TIME = 250


@Singleton
class BuzzerController(Controller):
    def __init__(self):
        self.buzzer = ServoDriver(11)
        self.isOn = False
        self.startTimeMillis = 0

    def execute(self, command) -> bool:
        if command.state:  # buzz
            self.buzzPattern()
            return False
        else:  # turn off
            self.buzzer.off()
            self.isOn = False
            return True  # command done

    def alternate(self):
        self.isOn = not self.isOn
        if self.isOn:
            self.buzzer.on()
        else:
            self.buzzer.off()

    def buzzPattern(self):
        if curTime() - self.startTimeMillis > TRIGGER_TIME:
            self.alternate()
            self.startTimeMillis = curTime()


def curTime():
    return time.time() * 1000


def testDriver():
    buzzerCtrl = BuzzerController.Instance()
    while True:
        buzzerCtrl.buzzPattern()
        time.sleep(0.005)


if __name__ == "__main__":
    testDriver()
