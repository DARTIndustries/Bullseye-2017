#!/usr/bin/python3

#DART 10/14/17
#Namespace = DART.Bullseye.Networking

import sys
import socket 
sys.path.insert(0, '../../../')
from DART.Bullseye.Networking.NetMessage import NetMessage
from DART.Bullseye.Networking.MessageUnpacker import MessageUnpacker

messageUnpacker = MessageUnpacker()
IP = "0.0.0.0"
PORT = 5000

class MailMan:
    def __init__(self, networkQueue):
        self.networkQueue = networkQueue


    def run(self):
        sock = socket.socket()
        server = (IP, PORT)
        sock.bind(server)

        sock.listen(5)
        print("Listening on ip:", IP, "port:", PORT)

        while True:
            try: 
                connection, address = sock.accept()
                print ("Connection from: " + str(address))
                conFile = connection.makefile()
                while True:
                    data = conFile.readline()
                    if not data:
                        break
                    print("RECIEVED PACKET:    ", data)
                    msg = NetMessage(data)    
                    cmds = messageUnpacker.unpack(msg)
                    for cmd in cmds:
                        print("Adding command")
                        self.networkQueue.put(cmd)
                connection.close()
            except socket.error:
                print("Socket Connection Error, trying to reaccept")
            except KeyboardInterrupt:
                self.cleanup()
            except Exception as e:
                print("MailMan: Top level exception throw while decrypting packet. Exception: ", e)

        def cleanup(self):
            print("Mailman interrupt")
            networkQueue.put("exit")
            sys.exit(0)