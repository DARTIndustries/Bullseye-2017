#!/usr/bin/python3

# Servo Driver for Raspberry PI with 16-channel PWM Servo Hat
# For DART 8/26/17
# By Adam Feldscher
# Takes input from -1 to 1 and sets the servo pwm value
# May need to add mid lower and upper configurable parameters

import sys
import time

sys.path.insert(0, '../../../')

from libs.ABE_ServoPi import PWM
from libs.ABE_helpers import ABEHelpers


class ServoDriver:
    def __init__(self, port):
        # Initialise the PWM device using the default address
        i2c_helper = ABEHelpers()
        bus = i2c_helper.get_smbus()

        self.pwm = PWM(bus, 0x40)
        self.pwm.set_pwm_freq(50)  # Set frequency to 60 Hz
        self.pwm.output_enable()
        self.port = port

        # ===The Below Values may need to be configurable===
        self.lower = 200
        self.mid = 306
        self.upper = 415

    # set a value from -1 to 1
    def setValue(self, value):
        inVal = float(value)
        outVal = 0
        if (inVal > 1 or inVal < -1):
            raise Exception("Value out of bounds, [-1, 1]")

        # ==Scale the input using a piecewise function===
        # 0 = mid
        # then  0 -> 1 scale linearly to mid -> upper
        # then -1 -> 0 scale linearly to lower -> mid

        if (inVal > 0):  # upper
            outVal = (inVal * (self.upper - self.mid)) + self.mid
        else:  # lower
            outVal = (inVal * (self.mid - self.lower)) + self.mid

        # print outVal #<-- for debugging uncomment
        self.pwm.set_pwm(self.port, 0, int(outVal))

    # set the servo to off
    def off(self):
        self.pwm.set_pwm(self.port, 0, 0)

    # set the servo to 5v
    def on(self):
        self.pwm.set_pwm(self.port, 0, 4095)


# ===Test driver to control a servo===
def testDriver():
    port = int(input("Enter a port: "))
    ctrl = ServoDriver(port)

    while (True):
        value = input("Enter a value from -1 to 1: ")
        if str(value) == "off":
            ctrl.off()
        elif str(value) == "on":
            ctrl.on()
        else:
            ctrl.setValue(float(value))


if __name__ == "__main__":
    testDriver()
