#DART 2017
#Abstract Controller

import sys
import abc

sys.path.insert(0, '../../../')

class Controller(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def execute(self, command):
        """Execute a command"""