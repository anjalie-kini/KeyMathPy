import math

def pointPlaneDistance(x1, y1, z1, plane1):
    denom = math.sqrt(plane1[0] * plane1[0] + plane1[1] * plane1[1] + plane1[2] * plane1[2])
    num = plane1[0] * x1 + plane1[1] * y1 + plane1[2] * z1 + plane1[3]
    return (num/denom)
