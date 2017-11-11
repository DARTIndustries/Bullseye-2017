#!/usr/bin/python3

#DART 10/14/17
#Namespace = DART.Bullseye.Networking

import sys
sys.path.insert(0, '../../../')
from DART.Bullseye.Networking.NetMessage import NetMessage
from DART.Bullseye.Networking.MessageUnpacker import MessageUnpacker

messageUnpacker = MessageUnpacker()

class MailMan:

    def __init__(self, networkQueue):
        self.networkQueue = networkQueue


    def run(self):
        print("test Mailman")

        msg = NetMessage('{"Do":{"Motor":[127,94,0,0,-94,-127],"Lights":""}}')
        cmds = messageUnpacker.unpack(msg)
        for cmd in cmds:
            print("Adding command")
            self.networkQueue.put(cmd)
