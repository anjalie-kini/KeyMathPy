import math

from AnalyticGeometry import Point

def PolygonArea(corners):
  n = len(corners) # number of corners
  area = 0.0
  for i in range(n):
    j = (i + 1) % n
    pointI = corners[i]
    pointJ = corners[j]
    area += pointI.getX() * pointJ.getY()
    area -= pointJ.getX() * pointI.getY()
  area = abs(area) / 2.0
  return area

def PolygonSort(corners):
  # calculate centroid of the polygon
  n = len(corners) # number of corners
  sumx = 0.0
  sumy = 0.0
  for i in range(n):
    pointI = corners[i]
    sumx = sumx + pointI.getX()      
    sumy = sumy + pointI.getY()      
  cx = float(sumx) / n
  cy = float(sumy) / n

  # create a new list of corners which includes angles
  cornersWithAngles = []
  for i in range(n):
    pointI = corners[i]
    dx = pointI.getX() - cx
    dy = pointI.getY() - cy
    angel = (math.atan2(dy, dx) + 2.0 * math.pi) % (2.0 * math.pi)
    cornersWithAngles.append((dx, dy, angel))
  # sort list of corners using the angles
  cornersWithAngles.sort(key = lambda tup: tup[2])
  return cornersWithAngles
