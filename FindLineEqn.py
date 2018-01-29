def findLineEquation(x1 , y1 , x2 , y2):
    slope = (y1 - y2) / (x1 - x2)
    b = y1 - slope * x1
    return ("y = " + str(slope) + "x + " + str(b))
