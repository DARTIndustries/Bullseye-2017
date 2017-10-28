#!/usr/bin/python3

#DART 10/14/17
#Namespace = DART.Bullseye

import sys
sys.path.insert(0, '../../')
from DART.Bullseye.Networking.NetMessage import NetMessage

class Mr_Manager:

    def __init__(self, networkQueue):
        self.networkQueue = networkQueue


    def run(self):
        print("test Manager")
        msg = self.networkQueue.get()

        print(msg.getValue())
