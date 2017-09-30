#!/usr/bin/python

#Servo Controller for Raspberry PI with 16-channel PWM Servo Hat
#For DART 8/26/17
#By Adam Feldscher
#Takes input from -1 to 1 and sets the servo pwm value
#May need to add mid lower and upper configurable parameters


from Adafruit_PWM_Servo_Driver import PWM
import time
import sys


class ServoController:
	def __init__(self, port):
		# Initialise the PWM device using the default address
		self.pwm = PWM(0x40)
		self.pwm.setPWMFreq(50) # Set frequency to 60 Hz
		self.port = port
			
		#===The Below Values may need to be configurable===
		self.mid = 332
		self.lower = 140
		self.upper = 540


	#set a value from -1 to 1
	def setValue(self, value):
		inVal = float(value)
		outVal = 0
		if (inVal > 1 or inVal < -1):
			raise Exception("Value out of bounds, [-1, 1]")
	
		#==Scale the input using a piecewise function===
		# 0 = mid
		# then  0 -> 1 scale linearly to mid -> upper
		# then -1 -> 0 scale linearly to lower -> mid	

		if (inVal > 0): #upper
			outVal = (inVal * (self.upper - self.mid)) + self.mid
		else: #lower
			outVal = (inVal * (self.mid - self.lower)) + self.mid
	
		#print outVal #<-- for debugging uncomment	
		self.pwm.setPWM(self.port, 0, int(outVal))


	#set the servo to off
	def off(self):
		self.pwm.setPWM(self.port, 0, 0)


#===Test driver to control a servo===
def testDriver():
	port = int(raw_input("Enter a port: "))
	ctrl = ServoController(port)

	while (True):
		value = raw_input("Enter a value from -1 to 1: ")
		if str(value) == "off":
			ctrl.off()
		else:	
			ctrl.setValue(float(value))


if __name__ == "__main__":
	testDriver()


