from math import sqrt

# Finds the shortest distance between a point and a line
def pointLineDistance(x1, y1, line1):
    denom = math.sqrt(line1[0] * line1[0] + line1[1] * line1[1])
    num = line1[0] * x1 + line1[1] * y1 + line1[2]
    return (num/denom)
