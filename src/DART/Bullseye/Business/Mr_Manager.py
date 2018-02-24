#!/usr/bin/python3

#DART 10/14/17
#Namespace = DART.Bullseye

import sys
sys.path.insert(0, '../../../')
from DART.Bullseye.Networking.NetMessage import NetMessage
from DART.Bullseye.Commands.Command import Command
from DART.Bullseye.Business.DeliveryBoy import DeliveryBoy



class Mr_Manager:
    longList = []

    def processor(self):
        #TODO: Add locks
        print("MrManager:  waiting for commands")        
        while (True):
            try:
                command = DeliveryBoy.inQueue.get() #blocking
                if (command == "exit"):
                    sys.exit(0)
                
                newList = []
                for(longCommand : self.longList):
                    if not command.isConflicting(longCommand):
                        newList.append(command)
                
                self.longList = newList
                
                
                if command.isLongRunning():
                    self.longList.append(longCommand)
                else:
                    command.execute()
                        
                    
            except Exception as e:
                print(" Mr Manager: Top level exception in run. Exception: ", e)

    def executer(self):
        newList = []
        for(command : longList):
            isDone = command.execute()
            if not isDone:
                newList.append(command)
        self.longList = newList


