def planeIntersection(plane1, plane2):
    crossedPlanes = []
    crossedPlanes.append((plane1[1]*plane2[2]) - (plane1[2]*plane2[1]))
    crossedPlanes.append((plane1[2]*plane2[0]) - (plane1[0]*plane2[2]))
    crossedPlanes.append((plane1[0]*plane2[1]) - (plane1[1]*plane2[0]))

    x = (plane1[3]*plane2[0] - plane2[3]*plane1[0])/ (plane1[1]*plane2[0] - plane1[0]*plane2[1])
    y = (plane1[3]*plane2[1] - plane2[3]*plane1[1])/ (plane1[0]*plane2[1] - plane1[1]*plane2[0])

    point = []
    point.append(x)
    point.append(y)
    point.append(0)

    line = []
    line.append(crossedPlanes)
    line.append(point)

    return line 
