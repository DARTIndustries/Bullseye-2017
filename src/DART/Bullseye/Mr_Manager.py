#!/usr/bin/python3

#DART 10/14/17
#Namespace = DART.Bullseye

import sys
sys.path.insert(0, '../../')
from DART.Bullseye.Networking.NetMessage import NetMessage
from DART.Bullseye.Commands.MotorCommand import MotorCommand

class Mr_Manager:

    def __init__(self, networkQueue):
        self.networkQueue = networkQueue


    def run(self):
        print("test Manager")
        msg = self.networkQueue.get()

        print(msg.getValue())

        test = MotorCommand(0, 1)

        print(test)

