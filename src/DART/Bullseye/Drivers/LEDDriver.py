#!/usr/bin/python3

# LED Driver for Raspberry PI with 16-channel PWM Servo Hat
# For DART 8/26/17
# By Adam Feldscher
# Takes input from -1 to 1 and sets the servo pwm value
# May need to add mid lower and upper configurable parameters

import sys
import time

sys.path.insert(0, '../../../')
from libs.ABE_ServoPi import PWM
from libs.ABE_helpers import ABEHelpers
import RPi.GPIO as GPIO


class LEDDriver:
    def __init__(self, pwmPort):
        # Initialise the PWM device using the default address
        i2c_helper = ABEHelpers()
        bus = i2c_helper.get_smbus()

        self.pwm = PWM(bus, 0x40)
        self.pwm.set_pwm_freq(1000)  # Set frequency to 60 Hz
        self.pwm.output_enable()
        self.pwmPort = pwmPort

        self.upper = 4095  # 0 -> 4095

    # set a value from 0 to 1
    def setValue(self, value):
        inVal = float(value)
        if inVal < 0 or inVal > 255:
            raise Exception("Value out of bounds, [0, 256)")

        outVal = inVal * self.upper / 255
        self.pwm.set_pwm(self.pwmPort, 0, int(outVal))

    # set the LED to off
    def off(self):
        self.pwm.set_pwm(self.pwmPort, 0, 0)

    # set the LED to on
    def on(self):
        self.pwm.set_pwm(self.port, 0, 4095)


# ===Test driver===
def testDriver():
    pwmPort = int(input("Enter a PWM port: "))
    ctrl = LEDDriver(pwmPort)

    while (True):
        value = input("Enter a value from 0 to 255: ")
        if str(value) == "off":
            ctrl.off()
        else:
            ctrl.setValue(float(value))


if __name__ == "__main__":
    testDriver()
