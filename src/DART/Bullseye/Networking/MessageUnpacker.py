#DART
#11/11/17

import sys
import json
sys.path.insert(0, '../../../')
from DART.Bullseye.Networking.NetMessage import NetMessage
from DART.Bullseye.Commands.MotorCommand import MotorCommand
from DART.Bullseye.Commands.CameraCommand import CameraCommand

class MessageUnpacker:
    def unpack(self, netMessage):
        commands = []

        try:
            rawData = json.loads(netMessage.getValue())
        except ValueError:  # includes simplejson.decoder.JSONDecodeError
            print('Decoding JSON has failed')
            return []

        if ("Do" in rawData):
            do = rawData["Do"]
            if ("Motor" in do):
                commands += self.motorToCommands(do["Motor"])
            if ("Lights" in do):
                commands += self.lightsToCommands(do["Lights"])
            if ("Servo" in do):
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
            commands.append(MotorCommand(i, self.scaleMotorValue(values[i])))
        return commands

    #Convert [-128, 127] to [-1, 1]
    def scaleMotorValue(self, value):
        minVal = 128.0  #negative (abs)
        maxVal = 127.0 

        if (value < 0):
            return value / minVal
        else:
            return value / maxVal

    #Convert [0, 180] to [-1, 1]
    def scaleServoValue(self, value):
        value -= 90
        return value / -90


    #TODO implement lights message unpacker
    def lightsToCommands(self, values):
        commands = []  
        print ("Message Unpacker: LIGHTS NOT IMPLEMENTED")      
        return commands

    #TODO implement servo message unpacker
    def servoToCommands(self, values): 
        angles = values["Angles"]
        commands = []  
        for i in range(len(angles)):
            commands.append(CameraCommand(i, self.scaleServoValue(angles[i])))
        return commands
