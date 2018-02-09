def planeIntersection(plane1, plane2):
    crossedPlanes = []
    crossedPlanes[0] = (plane1[1]*plane2[2]) - (plane1[2]*plane[1])
    crossedPlanes[1] = (plane1[2]*plane2[0]) - (plane1[0]*plane[2])
    crossedPlanes[2] = (plane1[0]*plane2[1]) - (plane1[1]*plane[0])

    x = (plane1[3]*plane2[0] - plane2[3]*plane*plane1[0])/ (plane1[1]*plane2[0] - plane2[0]*plane*plane1[1])
    y = (plane1[3]*plane2[1] - plane2[3]*plane*plane1[1])/ (plane1[0]*plane2[1] - plane2[1]*plane*plane1[0])

    point = []
    point[0] = x
    point[1] = y
    point[2] = 0

    line = []
    line[0] = crossedPlanes
    line[1] = point

    return line 
