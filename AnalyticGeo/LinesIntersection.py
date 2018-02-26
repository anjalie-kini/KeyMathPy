#Finds the intersection point between two lines
def linesIntersection(line1, line2):
    x = (line1[0]-line2[0])/(line2[1]-line1[0])
    y = line1[0] * x + line1[1]

    line = []
    line.append(x)
    line.append(y)
    # print ("(" + str(x) + "," + str(y) + ")")
    return line
