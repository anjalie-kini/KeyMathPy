def findLineEquation(x1 , y1 , x2 , y2):
    slope = (y1 - y2) / (x1 - x2)
    b = y1 - slope * x1
    line = []
    line [0] = slope
    line[1] = b
    print ("y = " + str(slope) + "x + " + str(b))
    return line
