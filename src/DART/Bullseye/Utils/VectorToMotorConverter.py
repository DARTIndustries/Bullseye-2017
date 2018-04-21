import sys
import numpy as np
sys.path.insert(0, '../../../')
from DART.Bullseye.Models.Types import Coordinate


class VectorToMotorConverter:


    @staticmethod
    def convert(movementVector: Coordinate, angleVector: Coordinate) -> tuple:
        pass


    @staticmethod
    def movementVals(movementVector: Coordinate) -> tuple:
        m0 = np.dot(movementVector.toList(), (1, 1, 0.17))
        m1 = np.dot(movementVector.toList(), (-1, 1, 0.17))
        m2 = np.dot(movementVector.toList(), (0, 0, 1))
        m3 = np.dot(movementVector.toList(), (0, 0, 1))
        m4= np.dot(movementVector.toList(), (-1, 1, 0.17))
        m5= np.dot(movementVector.toList(), (1, 1, 0.17))

