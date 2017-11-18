#DART
#11/11/17

import sys
import json
sys.path.insert(0, '../../../')
from DART.Bullseye.Networking.NetMessage import NetMessage
from DART.Bullseye.Commands.MotorCommand import MotorCommand

class MessageUnpacker:
    def unpack(self, netMessage):
        commands = []

        try:
            rawData = json.loads(netMessage.getValue())
        except ValueError:  # includes simplejson.decoder.JSONDecodeError
            print 'Decoding JSON has failed'
            return []

        if ("Do" in rawData):
            do = rawData["Do"]
            if ("Motor" in do):
                commands += self.motorToCommands(do["Motor"])
            elif ("Lights" in do):
                commands += self.lightsToCommands(do["Lights"])
            elif ("Servo" in do):
                commands += self.servoToCommands(do["Servo"])
        elif ("Request" in rawData):
            print("MailMan Request Not Implemented")
        else :
            print("Mailman, invalid packet recieved:    ", rawData)
        #TODO: Response type
        return commands


    def motorToCommands(self, values):
        commands = []
        for i in range(len(values)):
            commands.append(MotorCommand(i, values[i]))
        return commands

    #TODO implement lights message unpacker
    def lightsToCommands(self, values):
        commands = []  
        print ("Message Unpacker: LIGHTS NOT IMPLEMENTED")      
        return commands

    #TODO implement servo message unpacker
    def servoToCommands(self, values): 
        commands = []  
        print ("Message Unpacker: SERVO NOT IMPLEMENTED")      
        return commands
