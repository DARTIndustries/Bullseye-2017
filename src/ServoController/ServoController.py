#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time
import sys


class ServoController:
	def __init__(self, port):
		# Initialise the PWM device using the default address
		self.pwm = PWM(0x40)
		self.pwm.setPWMFreq(50) # Set frequency to 60 Hz
		self.port = port
		self.mid = 332
		self.lower = 140
		self.upper = 540

	def setValue(self, value):
		inVal = float(value)
		outVal = 0
		if (inVal > 1 or inVal < -1):
			raise Exception("Value out of bounds, [-1, 1]")
		
		if (inVal > 0):
			outVal = (inVal * (self.upper - self.mid)) + self.mid
		else:
			outVal = (inVal * (self.mid - self.lower)) + self.mid
	
		print outVal	
		self.pwm.setPWM(self.port, 0, int(outVal))


def testDriver():
	port = input("Enter a port: ")
	ctrl = ServoController(port)

	while (True):
		value = input("Enter a value from -1 to 1: ")	
		ctrl.setValue(value)

if __name__ == "__main__":
	testDriver()

