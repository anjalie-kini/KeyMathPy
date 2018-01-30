from math import *

def linesAngle(line1, line2):
    theta1 = math.atan(line1[0])
    theta2 = math.atan(line2[0])

    return (math.abs(theta1 - theta2))
