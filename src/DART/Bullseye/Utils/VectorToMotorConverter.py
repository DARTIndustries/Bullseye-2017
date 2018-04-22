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
        norm = movementVector.norm()  # magnitude
        unitVector = movementVector.normalize()

        # matrix = Matrix([
        #     [0.707, 0, -0.707, movementVector.x],
        #     [0.707, 0, 0.707, movementVector.y],
        #     [0.169, 0.971, 0.169, movementVector.z]
        # ])

        matrix = Matrix([
            [.5, 0, -.5, unitVector.x],
            [.5, 0, .5, unitVector.y],
            [0.17, 1, 0.17, unitVector.z]
        ])

        # matrix = Matrix([
        #     [1, 0, -1, movementVector.x],
        #     [1, 0, 1, movementVector.y],
        #     [0.17, 1, 0.17, movementVector.z]
        # ])

        rref = matrix.rref()
        if not rref[1] == (0, 1, 2):
            print("No solution to RREF!")

        # Get coefficients and multiply by the magnitude
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
