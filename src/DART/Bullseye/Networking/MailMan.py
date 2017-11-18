#!/usr/bin/python3

#DART 10/14/17
#Namespace = DART.Bullseye.Networking

import sys
import socket 
sys.path.insert(0, '../../../')
from DART.Bullseye.Networking.NetMessage import NetMessage
from DART.Bullseye.Networking.MessageUnpacker import MessageUnpacker

messageUnpacker = MessageUnpacker()
IP = "127.0.0.1"
PORT = 5000

class MailMan:
    def __init__(self, networkQueue):
        self.networkQueue = networkQueue


    def run(self):
        sock = socket.socket()
        server = (IP, PORT)
        sock.bind(server)

        sock.listen(1)
        print("Listening on ip:", IP, "port:", PORT)

        connection, address = sock.accept()
        print ("Connection from: " + str(address))
        while True:
            data = connection.recv(1024).decode()
            if not data:
                break
            msg = NetMessage(data)    
            cmds = messageUnpacker.unpack(msg)
            for cmd in cmds:
                print("Adding command")
                self.networkQueue.put(cmd)

        connection.close()
