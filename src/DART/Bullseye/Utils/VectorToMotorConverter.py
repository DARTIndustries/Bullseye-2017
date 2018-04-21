import sys
from sympy import *
sys.path.insert(0, '../../../')
from DART.Bullseye.Models.Types import Coordinate


class VectorToMotorConverter:


    @staticmethod
    def convert(movementVector: Coordinate, angleVector: Coordinate) -> tuple:
        pass


    @staticmethod
    def movementVals(movementVector: Coordinate) -> tuple:
        matrix = Matrix([
            [1, 0, -1, movementVector.x],
            [1, 0, 1, movementVector.y],
            [0.17, 1, 0.17, movementVector.z]
        ])

        rref= matrix.rref()

        if not rref[1] == [0, 1, 2]:
            print("Bad RREF!!!")

        reduced = rref[0]

        m0 = reduced[3]
        m2 = reduced[7]
        m4 = reduced[11]



        # m0 = numpy.dot(movementVector.toList(), (1, 1, 0.17))
        # m1 = numpy.dot(movementVector.toList(), (-1, 1, 0.17))
        # m2 = numpy.dot(movementVector.toList(), (0, 0, 1))
        # m3 = numpy.dot(movementVector.toList(), (0, 0, 1))
        # m4= numpy.dot(movementVector.toList(), (-1, 1, 0.17))
        # m5 = numpy.dot(movementVector.toList(), (1, 1, 0.17))

