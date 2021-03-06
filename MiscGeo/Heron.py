import math

# Finds the area of a triangle, given the lengths of its sides
def TriangleArea(sides):
    area = 0.0
    perimeter = 0.0
    for i in range(len(sides)):
        perimeter += sides[i]
    semiperimeter = perimeter/2.0
    area = math.sqrt(semiperimeter * (semiperimeter - sides[0]) * (semiperimeter - sides[1]) * (semiperimeter - sides[2]))
    return area
