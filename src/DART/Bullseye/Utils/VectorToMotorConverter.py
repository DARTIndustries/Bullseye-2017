import sys
from sympy import *
import numpy

sys.path.insert(0, '../../../')
from DART.Bullseye.Models.Types import Coordinate


class VectorToMotorConverter:

    @staticmethod
    def convert(movementVector: Coordinate, angleVector: Coordinate) -> tuple:
        pass

    @staticmethod
    def movementVals(movementVector: Coordinate) -> tuple:
        #Note .17 = sin(10)
        #Motor Matrix
        #[M0 M1 M4]
        #1   0  -1
        #1   0   1
        #0.17  1  0.17

        #Moore Penrose Pseudo Inverse:
        #0.5    0.5   0
        #0    -.17    1
        #-0.5   0.5   0



        solution = rref[0]
        m0 = solution[3] * norm
        m5 = m0
        m2 = solution[7] * norm
        m3 = m2
        m4 = solution[11] * norm
        m1 = m4

        return (m0, m1, m2, m3, m4, m5)


def testDriver():
    print(VectorToMotorConverter.movementVals(Coordinate(.707, .707, 0)))


if __name__ == "__main__":
    testDriver()
