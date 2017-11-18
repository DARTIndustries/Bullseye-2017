#!/usr/bin/python3

#DART 10/14/17
#Namespace = DART.Bullseye

import sys
sys.path.insert(0, '../../')
from DART.Bullseye.Networking.NetMessage import NetMessage
from DART.Bullseye.Commands.MotorCommand import MotorCommand

class Mr_Manager:

    def __init__(self, networkInQueue):
        self.networkInQueue = networkInQueue


    def run(self):
        #TODO: Add long running commands
        print("MrManager:  waiting for commands")        
        while (True):
            command = self.networkInQueue.get() #blocking
            command.execute()
