#Buzzer Controller

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

    def execute(self, command):
        pass

    def alternate(self):
        self.isOn = not self.isOn
        if (self.isOn):
            self.buzzer.on()
        else:
            self.buzzer.off()


def curTime():
    return time.time() * 1000


def testDriver():
    buzzerCtrl = BuzzerController.Instance()
    startTimeMillis = curTime()
    while(True):
        if (curTime() - startTimeMillis > TRIGGER_TIME):
            buzzerCtrl.alternate()
            startTimeMillis = curTime()




if __name__ == "__main__":
	testDriver()




