# DART
# 11/11/17

import sys
import json
from typing import List

from DART.Bullseye.Commands import Command
from DART.Bullseye.Commands.BuzzerCommand import BuzzerCommand
from DART.Bullseye.Networking.NetMessage import NetMessage

sys.path.insert(0, '../../../')
from DART.Bullseye.Commands.LEDCommand import LEDCommand
from DART.Bullseye.Commands.MotorMovementCommand import MotorMovementCommand
from DART.Bullseye.Commands.VectorMovementCommand import VectorMovementCommand
from DART.Bullseye.Commands.CameraCommand import CameraCommand
from DART.Bullseye.Commands.ClawCommand import ClawCommand
from DART.Bullseye.Models.Types import Coordinate


class MessageUnpacker:
    def unpack(self, netMessage: NetMessage):
        commands = []

        try:
            rawData = json.loads(netMessage.getValue())
        except ValueError:  # includes simplejson.decoder.JSONDecodeError
            print('Decoding JSON has failed')
            return []

        if "Do" in rawData:
            do = rawData["Do"]
            if "Motor" in do:
                commands += self.motorToCommands(do["Motor"])
            elif "MotorVector" in do:
                commands += self.motorVectorToCommands(do["MotorVector"])

            if "Lights" in do:
                commands += self.lightsToCommands(do["Lights"])
            if "Camera" in do:
                commands += self.cameraToCommands(do["Camera"])
            if "Claw" in do:
                commands += self.clawToCommands(do["Claw"])
            if "Buzzer" in do:
                commands += self.buzzerToCommands(do["Buzzer"])

        elif "Request" in rawData:
            print("MailMan Request Not Implemented")
        else:
            print("Mailman, invalid packet recieved:    ", rawData)
        # TODO: Response type
        return commands

    def motorToCommands(self, values):
        commands = []
        for i in range(len(values)):
            commands.append(MotorMovementCommand(i, self.scaleMotorValue(values[i])))
        return commands

    def motorVectorToCommands(self, values):
        mvmt = self.vectorToCoor(values["Velocity"])
        angle = self.vectorToCoor(values["AngularVelocity"])
        return [VectorMovementCommand(mvmt, angle)]

    def vectorToCoor(self, vector) -> Coordinate:
        return Coordinate(self.scaleMotorValue(vector[0]), self.scaleMotorValue(vector[1]),
                          self.scaleMotorValue(vector[2]))

    def scaleMotorValue(self, value):
        """Convert [-128, 127] to [-1, 1]"""
        minVal = 128.0  # negative (abs)
        maxVal = 127.0

        if (value < 0):
            return value / minVal
        else:
            return value / maxVal

    def scaleCameraValue(self, value):
        """Convert [0, 180] to [-1, 1]"""
        value -= 90
        return value / -90

    def lightsToCommands(self, value):
        return [LEDCommand(value)]

    def cameraToCommands(self, values):
        angles = values["Angles"]
        commands = []
        for i in range(len(angles)):
            commands.append(CameraCommand(i, self.scaleCameraValue(angles[i])))
        return commands

    def clawToCommands(self, values):
        return [ClawCommand(self.scaleCameraValue(values["Angle"]))]

    def buzzerToCommands(self, values):
        return [BuzzerCommand(values["State"])]
