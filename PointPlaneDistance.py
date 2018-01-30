from math import sqrt

def pointPlaneDistance(x1, y1, z1, line1):
    denom = math.sqrt(line1[0] * line1[0] + line1[1] * line1[1] + line1[2] * line1[2])
    num = line1[0] * x1 + line1[1] * y1 + line1[2] * z1 + line2[3]
    return (num/denom)
