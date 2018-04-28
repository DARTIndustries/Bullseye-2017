import sys
from math import sin
from math import radians
from operator import add

sys.path.insert(0, '../../../')
from DART.Bullseye.Models.Types import Coordinate

SIN10 = sin(radians(10))


class VectorToMotorConverter:

    @staticmethod
    def convert(movementVector: Coordinate, rotationVector: Coordinate) -> tuple:
        mvmtVals = VectorToMotorConverter.movementVals(movementVector)
        rotVals = VectorToMotorConverter.rotationVals(rotationVector)

        maxMvmt = abs(max(mvmtVals, key=abs))
        maxRot = abs(max(rotVals, key=abs))
        maxOrig = abs(max(maxRot, maxMvmt, key=abs))

        combined = tuple(map(add, mvmtVals, rotVals))
        maxComb = abs(max(combined, key=abs))
        return tuple((i * maxOrig / maxComb) for i in combined) if maxComb != 0 else combined

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

        # Convert to -1 to 1, then scale by magnitude
        maxRaw = abs(max(m0Raw, m2Raw, m4Raw, key=abs))  # scales to -1 to 1
        scaleFactor = mag / maxRaw if maxRaw != 0 else 1

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

        rVect = rotationVector.normalize()
        mag = rotationVector.norm()

        # Compute Motor Values
        m0Raw = (0.5 * rVect.x) + (0.5 * rVect.z)
        m1Raw = (0.5 * rVect.x) - (0.5 * rVect.z)
        m2Raw = rVect.y - (SIN10 * rVect.z)
        m3Raw = -rVect.y + (SIN10 * rVect.z)
        m4Raw = (-0.5 * rVect.x) + (-0.5 * rVect.z)
        m5Raw = (-0.5 * rVect.x) + (0.5 * rVect.z)

        # Convert to -1 to 1, then scale by magnitude
        maxRaw = abs(max(m0Raw, m1Raw, m2Raw, m3Raw, m4Raw, m5Raw, key=abs))  # scales -1 to 1
        scaleFactor = mag / maxRaw if maxRaw != 0 else 1

        # Convert to Motor Perception
        m0 = m0Raw * scaleFactor
        m1 = m1Raw * scaleFactor
        m2 = m2Raw * scaleFactor
        m3 = m3Raw * scaleFactor
        m4 = m4Raw * scaleFactor
        m5 = m5Raw * scaleFactor

        return m0, m1, m2, m3, m4, m5


def testDriver():
    print(VectorToMotorConverter.convert(Coordinate(0, 1, 0), Coordinate(0, 0, 0.2)))


if __name__ == "__main__":
    testDriver()
