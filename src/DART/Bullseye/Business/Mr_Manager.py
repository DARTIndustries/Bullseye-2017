#!/usr/bin/python3

#DART 10/14/17
#Namespace = DART.Bullseye

import sys
sys.path.insert(0, '../../../')
from DART.Bullseye.Networking.NetMessage import NetMessage
from DART.Bullseye.Commands.MotorCommand import MotorCommand
from DART.Bullseye.Business.DeliveryBoy import DeliveryBoy

class Mr_Manager:

    def run(self):
        #TODO: Add long running commands
        print("MrManager:  waiting for commands")        
        while (True):
            try:
                command = DeliveryBoy.inQueue.get() #blocking
                if (command == "exit"):
                    sys.exit(0)
                command.execute()
            except Exception as e:
                print(" Mr Manager: Top level exception in run. Exception: ", e)
