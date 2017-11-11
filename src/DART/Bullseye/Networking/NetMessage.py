#!/usr/bin/python3

#DART 10/14/17
#Namespace = DART.Bullseye.Networking


import sys
sys.path.insert(0, '../../../')

class NetMessage:
    def __init__(self):
        self.value = ""

    def __init__(self, value):
        self.value = value


    def getValue(self):
        return self.value