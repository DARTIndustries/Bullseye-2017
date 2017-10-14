#!/usr/bin/python3

#Motor Driver for Raspberry PI with 16-channel PWM Servo Hat
#For DART 8/26/17
#By Adam Feldscher
#Takes input from -1 to 1 and sets the servo pwm value
#May need to add mid lower and upper configurable parameters

import sys
import time

sys.path.insert(0, '../../../')
from libs.ABE_ServoPi import PWM
from libs.ABE_helpers import ABEHelpers
import RPi.GPIO as GPIO

class MotorDriver:
	def __init__(self, pwmPort, dirPort):
		# Initialise the PWM device using the default address
		i2c_helper = ABEHelpers()
		bus = i2c_helper.get_smbus()
		
		self.pwm = PWM(bus, 0x40)
		self.pwm.set_pwm_freq(50) # Set frequency to 60 Hz
		self.pwm.output_enable()
		self.pwmPort = pwmPort
		self.dirPort = dirPort
	
		self.upper = 4095  #0 -> 4095

		#init GPIO
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(dirPort, GPIO.OUT)
		

	#set a value from -1 to 1
	def setValue(self, value):
		inVal = float(value)
		outVal = 0
		if (inVal > 1 or inVal < -1):
			raise Exception("Value out of bounds, [-1, 1]")
	
		outVal = abs(inVal) * self.upper

		#Set Direction
		GPIO.output(self.dirPort, (inVal < 0))


		#print outVal #<-- for debugging uncomment	
		self.pwm.set_pwm(self.pwmPort, 0, int(outVal))


	#set the motor to off
	def off(self):
		self.pwm.set_pwm(self.pwmPort, 0, 0)


#===Test driver to control a servo===
def testDriver():
	pwmPort = int(input("Enter a PWM port: "))
	dirPort = int(input("Enter a dir port: "))
	ctrl = MotorDriver(pwmPort, dirPort)

	while (True):
		value = input("Enter a value from -1 to 1: ")
		if str(value) == "off":
			ctrl.off()
		else:	
			ctrl.setValue(float(value))


if __name__ == "__main__":
	testDriver()


