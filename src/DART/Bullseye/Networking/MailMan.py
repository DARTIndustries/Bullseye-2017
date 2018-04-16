#!/usr/bin/python3

#DART 10/14/17
#Namespace = DART.Bullseye.Networking

import sys
import socket 
sys.path.insert(0, '../../../')
from DART.Bullseye.Networking.NetMessage import NetMessage
from DART.Bullseye.Networking.MessageUnpacker import MessageUnpacker
from DART.Bullseye.Business.DeliveryBoy import DeliveryBoy
import json

messageUnpacker = MessageUnpacker()
LISTEN_IP = "0.0.0.0"
REMOTE_IP=""
PORT = 5000

class MailMan:

    def send(self):
        sock = socket.socket()
        sock.connect((REMOTE_IP, PORT))

        while True:
            try:
                data = DeliveryBoy.outQueue.get()
                print("SENDING PACKET:    ", data)
                jsonData = json.dumps(data)
                sock.send(jsonData)
            except socket.error:
                print("Socket Connection Error, trying to reaccept")
            except KeyboardInterrupt:
                self.cleanup()
            except Exception as e:
                print("MailMan: Top level exception throw while decrypting packet. Exception: ", e)
        sock.close()
        
    def receive(self):
        sock = socket.socket()
        server = (LISTEN_IP, PORT)
        sock.bind(server)

        sock.listen(5)
        print("Listening on ip:", LISTEN_IP, "port:", PORT)

        while True:
            try: 
                connection, address = sock.accept()
                print ("Connection from: " + str(address))
                conFile = connection.makefile()
                while True:
                    data = conFile.readline()
                    if not data:
                        break
                    print("RECEIVED PACKET:    ", data)
                    msg = NetMessage(data)    
                    cmds = messageUnpacker.unpack(msg)
                    for cmd in cmds:
                        print("Adding command")
                        DeliveryBoy.inQueue.put(cmd)
                connection.close()
            except socket.error:
                print("Socket Connection Error, trying to reaccept")
            except KeyboardInterrupt:
                self.cleanup()
            except Exception as e:
                print("MailMan: Top level exception throw while decrypting packet. Exception: ", e)

    def cleanup(self):
        print("Mailman interrupt")
        DeliveryBoy.inQueue.put("exit")
        sys.exit(0)
