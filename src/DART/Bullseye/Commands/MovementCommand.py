
#DART 10/14/17
#Namespace = DART.Bullseye.Commands
#Movement Command Abstract class
import abc
import sys
sys.path.insert(0, '../../../')
from DART.Bullseye.Commands.Command import Command


class MovementCommand(Command):
    def __init__(self):
        Command.__init__(self)
        self.isLongRunning = False

    @abc.abstractmethod
    def execute(self):
        pass

    def isConflicting(self, command):
        return isinstance(command, MovementCommand)
