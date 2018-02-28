import math

from AnalyticGeometry import Point

# Implements Shoelace Formula to find area of a polygon given its coordinates
def PolygonArea(corners):
  n = len(corners)
  area = 0.0
  for i in range(n):
    j = (i + 1) % n
    pointI = corners[i]
    pointJ = corners[j]
    area += pointI.getX() * pointJ.getY()
    area -= pointJ.getX() * pointI.getY()
  area = abs(area) / 2.0
  return area

# Sorts corners into correct order to be inputted into shoelace
# (Corners must be listed in clockwise order)
def cornerSort(corners):
  n = len(corners)
  sumx = 0.0
  sumy = 0.0
  for i in range(n):
    pointI = corners[i]
    sumx = sumx + pointI.getX()      
    sumy = sumy + pointI.getY()      
  cx = float(sumx) / n
  cy = float(sumy) / n

  sortedCorners = []
  for i in range(n):
    pointI = corners[i]
    dx = pointI.getX() - cx
    dy = pointI.getY() - cy
    angel = (math.atan2(dy, dx) + 2.0 * math.pi) % (2.0 * math.pi)
    sortedCorners.append((dx, dy, angel))
  sortedCorners.sort(key = lambda tup: tup[2])
  return sortedCorners
