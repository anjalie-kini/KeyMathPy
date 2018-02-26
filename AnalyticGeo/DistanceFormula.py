import math

def distanceFormula(x1 , y1 , x2 , y2):
    sq1 = (x1 - x2) * (x1 - x2)
    sq2 = (y1 - y2) * (y1 - y2)
    return math.sqrt(sq1 + sq2)
