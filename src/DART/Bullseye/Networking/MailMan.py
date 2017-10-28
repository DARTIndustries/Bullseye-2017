#!/usr/bin/python3

#DART 10/14/17
#Namespace = DART.Bullseye.Networking

import sys
sys.path.insert(0, '../../../')
from NetMessage import NetMessage


class MailMan:

    def __init__(self, networkQueue):
        self.networkQueue = networkQueue


    def run(self):
        print("test Mailman")

        tmp = NetMessage("testMsgValue")
        self.networkQueue.put(tmp)
