
#DART 10/14/17
#Namespace = DART.Bullseye.Commands
#Command Abstract class

import sys
import abc
sys.path.insert(0, '../../../')

class Command(metaclass=abc.ABCMeta):
    def __init__(self):
        isLongRunning = False

    @abc.abstractmethod
    def execute(self):
        """Execute a command"""

    @abc.abstractmethod
    def isConflicting(self, command):
        """Check if a command is conflicting"""






 