import sys
from math import sin
from math import radians

sys.path.insert(0, '../../../')
from DART.Bullseye.Models.Types import Coordinate

SIN10 = sin(radians(10))


class VectorToMotorConverter:

    @staticmethod
    def convert(movementVector: Coordinate, angleVector: Coordinate) -> tuple:
        pass

    @staticmethod
    def movementVals(movementVector: Coordinate) -> tuple:
        # Note .17 = sin(10)
        # Motor Matrix
        # [M0 M1 M4]
        # 1   0  -1
        # 1   0   1
        # 0.17  1  0.17

        # Moore Penrose Pseudo Inverse:
        # 0.5    0.5   0
        # 0    -.17    1
        # -0.5   0.5   0

        mag = movementVector.norm()
        dirV = movementVector.normalize()

        # Compute raw values for left side of robot
        # Note: these aren't scaled correctly, but they are proportional
        m0Raw = (0.5 * dirV.x) + (0.5 * dirV.y)
        m2Raw = (-SIN10 * dirV.y) + dirV.z
        m4Raw = (-0.5 * dirV.x) + 0.5 * dirV.y

        maxRaw = max(m0Raw, m2Raw, m4Raw)  # used for scaling
        scaleFactor = mag / maxRaw  # used to scale raw values. Convert to -1 to 1, then scale by magnitude

        # Convert to motor percentage
        m0 = m0Raw * scaleFactor
        m2 = m2Raw * scaleFactor
        m4 = m4Raw * scaleFactor

        # match corresponding equal motors
        m1 = m4
        m3 = m2
        m5 = m0

        return m0, m1, m2, m3, m4, m5

    @staticmethod
    def rotationVals(rotationVector: Coordinate) -> tuple:
        # Note .17 = sin(10)
        # x = pitch m0, m1,  m4, m5
        # y = roll m2, m3
        # z = yaw  m0, m1, m4, m5  and m2, m3 to cancel the 10deg

        # Rotational Motor Matrix:
        # .17  .17  0  0  -.17  -.17
        # 0     0   1  -1   0     0
        # 1    -1   0   0   1    -1

        # Pseudo Inverse:
        #    1.4397   0.0000   0.2500
        #    1.4397   0.0000  -0.2500
        #    0.0000   0.5000   0.0000
        #   -0.0000  -0.5000  -0.0000
        #   -1.4397   0.0000   0.2500
        #   -1.4397   0.0000  -0.2500

        rVect = rotationVector.normalize()
        mag = rotationVector.norm()

        # Compute Motor Values
        m0Raw = (0.5 * rVect.x) + (0.5 * rVect.z)
        m1Raw = (0.5 * rVect.x) - (0.5 * rVect.z)
        m2Raw = rVect.y - (SIN10 * rVect.z)
        m3Raw = -rVect.y + (SIN10 * rVect.z)
        m4Raw = (-0.5 * rVect.x) + (0.5 * rVect.z)
        m5Raw = (-0.5 * rVect.x) + (-0.5 * rVect.z)

        # m0Raw = (1.4397 * rVect.x) + (0.25 * rVect.z)
        # m1Raw = (1.4397 * rVect.x) - (0.25 * rVect.z)
        # m2Raw = 0.5 * rVect.y
        # m3Raw = -0.5 * rVect.y
        # m4Raw = (-1.4397 * rVect.x) + (0.25 * rVect.z)
        # m5Raw = (-1.4397 * rVect.x) - (0.25 * rVect.z)

        # m0Raw = (0.25 * rVect.x) + (0.25 * rVect.z)
        # m1Raw = (0.25 * rVect.x) - (0.25 * rVect.z)
        # m2Raw = 0.5 * rVect.y
        # m3Raw = -0.5 * rVect.y
        # m4Raw = (-0.25 * rVect.x) + (0.25 * rVect.z)
        # m5Raw = (-0.25 * rVect.x) - (0.25 * rVect.z)

        maxRaw = max(m0Raw, m1Raw, m2Raw, m3Raw, m4Raw, m5Raw)  # used for scaling
        scaleFactor = mag / maxRaw  # used to scale raw values. Convert to -1 to 1, then scale by magnitude

        # Convert to Motor Perception
        m0 = m0Raw * scaleFactor
        m1 = m1Raw * scaleFactor
        m2 = m2Raw * scaleFactor
        m3 = m3Raw * scaleFactor
        m4 = m4Raw * scaleFactor
        m5 = m5Raw * scaleFactor

        return m0, m1, m2, m3, m4, m5


def testDriver():
    print(VectorToMotorConverter.rotationVals(Coordinate(0, 0, 1)))


if __name__ == "__main__":
    testDriver()
