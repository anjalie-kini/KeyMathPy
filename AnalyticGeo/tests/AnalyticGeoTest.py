import unittest

import os, sys, datetime
sys.path.insert(0, os.path.abspath('..'))

from AnalyticGeometry import Line,Plane,Point
import Shoelace

class AnalyticGeoTest(unittest.TestCase):
  def assertAlmostEqualForPoint(self, p1, p2, places, msg):
    self.assertAlmostEqual(p1.getX(), p2.getX(), places=places, msg=msg + " (X)", delta=None)
    self.assertAlmostEqual(p1.getY(), p2.getY(), places=places, msg=msg + " (Y)", delta=None)
    self.assertAlmostEqual(p1.getZ(), p2.getZ(), places=places, msg=msg + " (Z)", delta=None)
      
  def assertAlmostEqualForLine(self, l1, l2, places, msg):
    self.assertAlmostEqual(l1.getSlope(), l2.getSlope(), places=places, msg=msg + " (slope)", delta=None)
    self.assertAlmostEqual(l1.getIntercept(), l2.getIntercept(), places=places, msg=msg + " (intercept)", delta=None)
      
  def assertAlmostEqualForList(self, l1, l2, places, msg):
    if (len(l1) != len(l2)):
      return False
    for i in range(len(l1)):
      self.assertAlmostEqual(l1[i], l2[i], places=places, msg=msg, delta=None)
      
  def assertAlmostEqualForListOfLists(self, l1, l2, places, msg):
    if (len(l1) != len(l2)):
      return False
    for i in range(len(l1)):
      if (len(l1[i]) != len(l2[i])):
        return False
      for j in range(len(l1[i])):
        self.assertAlmostEqual(l1[i][j], l2[i][j], places=places, msg=msg, delta=None)
      

  def test_DistanceFormula(self):
    print ("\n%%%%%%% Testing DistanceFormula")

    point1 = Point(1,3)
    point2 = Point(2,4)
    result = point1.distance2D(point2)
    expectedResult =  1.4142135
    print ("distanceFormula for " + str(point1) + ", " + str(point2) + ":" + str(result))
    self.assertAlmostEqual(result, expectedResult, places=6, msg="distanceFormula for " + str(point1) + ", " + str(point2), delta=None)

    point1 = Point(5,7)
    point2 = Point(2,0)
    result = point1.distance2D(point2)
    expectedResult =   7.6157731
    print ("distanceFormula for " + str(point1) + ", " + str(point2) + ":" + str(result))
    self.assertAlmostEqual(result, expectedResult, places=6, msg="distanceFormula for " + str(point1) + ", " + str(point2), delta=None)

    point1 = Point(23,78)
    point2 = Point(65,63)
    result = point1.distance2D(point2)
    expectedResult =  44.5982062
    print ("distanceFormula for " + str(point1) + ", " + str(point2) + ":" + str(result))
    self.assertAlmostEqual(result, expectedResult, places=6, msg="distanceFormula for " + str(point1) + ", " + str(point2), delta=None)


  def test_FindLineEqn(self):
    print ("\n%%%%%%% Testing FindLineEqn")

    point1 = Point(1, 3)
    point2 = Point(2, 4)
    result = point1.findLineEquation(point2)
    expectedResult = Line(1.0,2.0)
    print ("findLineEquation for " + str(point1) + ", " + str(point2) + ": " + str(result))
    self.assertAlmostEqualForLine(result, expectedResult, places=6, msg="findLineEquation for " + str(point1) + ", " + str(point2))

    point1 = Point(5, 7)
    point2 = Point(2, 0)
    result = point1.findLineEquation(point2)
    expectedResult = Line(2.3333333,-4.6666666)
    print ("findLineEquation for " + str(point1) + ", " + str(point2) + ": " + str(result))
    self.assertAlmostEqualForLine(result, expectedResult, places=6, msg="findLineEquation for " + str(point1) + ", " + str(point2))

    point1 = Point(23, 78)
    point2 = Point(65, 63)
    result = point1.findLineEquation(point2)
    expectedResult = Line(-0.3571428, 86.2142857)
    print ("findLineEquation for " + str(point1) + ", " + str(point2) + ": " + str(result))
    self.assertAlmostEqualForLine(result, expectedResult, places=6, msg="findLineEquation for " + str(point1) + ", " + str(point2))


  def test_LinesAngle(self):
    print ("\n%%%%%%% Testing LinesAngle")

    line1=Line(1,2)
    line2=Line(3,4)
    result = line1.linesAngle(line2)
    expectedResult = 0.4636476
    print ("linesAngle for " + str(line1) + ", " + str(line2) + ": " + str(result))
    self.assertAlmostEqual(result, expectedResult, places=6, msg="linesAngle", delta=None)

    line1=Line(5,2)
    line2=Line(7,0)
    result = line1.linesAngle(line2)
    expectedResult = 0.0554985
    print ("linesAngle for " + str(line1) + ", " + str(line2) + ": " + str(result))
    self.assertAlmostEqual(result, expectedResult, places=6, msg="linesAngle", delta=None)

    line1=Line(23,65)
    line2=Line(78,63)
    result = line1.linesAngle(line2)
    expectedResult = 0.03063108
    print ("linesAngle for " + str(line1) + ", " + str(line2) + ": " + str(result))
    self.assertAlmostEqual(result, expectedResult, places=6, msg="linesAngle", delta=None)


  def test_LinesIntersection(self):
    print ("\n%%%%%%% Testing LinesIntersection")

    line1=Line(3,1)
    line2=Line(-1,0)
    result = line1.linesIntersection(line2)
    expectedResult = Point(-0.25, 0.25)
    print ("linesIntersection for " + str(line1) + ", " + str(line2) + ": " + str(result))
    self.assertAlmostEqualForPoint(result, expectedResult, places=6, msg="linesIntersection")

    line1=Line(3,-3)
    line2=Line(2.3,4)
    result = line1.linesIntersection(line2)
    expectedResult = Point(10, 27)
    print ("linesIntersection for " + str(line1) + ", " + str(line2) + ": " + str(result))
    self.assertAlmostEqualForPoint(result, expectedResult, places=6, msg="linesIntersection")

    # Parallel lines do not intersect
    line1=Line(0.5,-3)
    line2=Line(0.5,8)
    with self.assertRaises(Exception) as context:
      result = line1.linesIntersection(line2)
      print ("linesIntersection for " + str(line1) + ", " + str(line2) + ": SHOULD NOT REACH HERE due to raised Exception")


  def test_PlaneIntersection(self):
    print ("\n%%%%%%% Testing PlaneIntersection")

    plane1=Plane(1,2,3,4)
    plane2=Plane(3,4,5,6)
    result = plane1.planeIntersection(plane2)
    expectedResult = [[-2, 4, -2], [3.0, -2.0, 0]]
    print ("planeIntersection for " + str(plane1) + ", " + str(plane2) + ": " + str(result))
    self.assertAlmostEqualForListOfLists(result, expectedResult, places=6, msg="planeIntersection")

    plane1=Plane(5,2,7,8)
    plane2=Plane(7,0,25,45)
    result = plane1.planeIntersection(plane2)
    expectedResult =  [[50, -76, -14], [-12.0714285, 6.4285714, 0]]
    print ("planeIntersection for " + str(plane1) + ", " + str(plane2) + ": " + str(result))
    self.assertAlmostEqualForListOfLists(result, expectedResult, places=6, msg="planeIntersection")

    plane1=Plane(23,65,87,123)
    plane2=Plane(78,63,97,103)
    result = plane1.planeIntersection(plane2)
    expectedResult =  [[824, 4555, -3621], [1.9953051643192488, -0.29107981220657275, 0]]
    print ("planeIntersection for " + str(plane1) + ", " + str(plane2) + ": " + str(result))
    self.assertAlmostEqualForListOfLists(result, expectedResult, places=6, msg="planeIntersection")


  def test_PointLineDistance(self):
    print ("\n%%%%%%% Testing PointLineDistance")

    point1=Point(17,92)
    # StandardForm: 1, 2, 11
    line1=Line(-0.5, -5.5)
    result = line1.pointLineDistance(point1)
    expectedResult = 94.8092822
    print ("pointLineDistance for " + str(point1) + ", " + str(line1) + ": " + str(result))
    self.assertAlmostEqual(result, expectedResult, places=6, msg="pointLineDistance", delta=None)

    point1=Point(0,0)
    # StandardForm: 3, 4, 12
    line1=Line(-0.75, -3)
    result = line1.pointLineDistance(point1)
    expectedResult = 2.4
    print ("pointLineDistance for " + str(point1) + ", " + str(line1) + ": " + str(result))
    self.assertAlmostEqual(result, expectedResult, places=6, msg="pointLineDistance", delta=None)

    point1=Point(1,2)
    # StandardForm: 5, 2, 13
    line1=Line(-2.5, -6.5)
    result = line1.pointLineDistance(point1)
    expectedResult = 4.0852974
    print ("pointLineDistance for " + str(point1) + ", " + str(line1) + ": " + str(result))
    self.assertAlmostEqual(result, expectedResult, places=6, msg="pointLineDistance", delta=None)

  def test_PointPlaneDistance(self):
    print ("\n%%%%%%% Testing PointPlaneDistance")

    point1=Point(17,92,105)
    plane1=Plane(1,2,3,11)
    result = plane1.pointPlaneDistance(point1)
    expectedResult = 140.8466744
    print ("pointPlaneDistance for point " + str(point1) + ", plane " + str(plane1) + ": " + str(result))
    self.assertAlmostEqual(result, expectedResult, places=6, msg="pointPlaneDistance", delta=None)

    point1=Point(0,0,0)
    plane1=Plane(3,4,5,12)
    result = plane1.pointPlaneDistance(point1)
    expectedResult =  1.6970562
    print ("pointPlaneDistance for point " + str(point1) + ", plane " + str(plane1) + ": " + str(result))
    self.assertAlmostEqual(result, expectedResult, places=6, msg="pointPlaneDistance", delta=None)

    point1=Point(1,2,3)
    plane1=Plane(5,2,7,13)
    result = plane1.pointPlaneDistance(point1)
    expectedResult = 4.8687912
    print ("pointPlaneDistance for point " + str(point1) + ", plane " + str(plane1) + ": " + str(result))
    self.assertAlmostEqual(result, expectedResult, places=6, msg="pointPlaneDistance", delta=None)

  def test_Shoelace(self):
    print ("\n%%%%%%% Testing Shoelace")

    point1 = Point(2.0, 1.0)
    point2 = Point(4.0, 5.0)
    point3 = Point(7.0, 8.0)
    corners = [point1, point2, point3]
    result = Shoelace.PolygonArea(corners)
    expectedResult = 3.0
    print ("PolygonArea(" + str(corners) + ": " + str(result))
    self.assertAlmostEqual(result, expectedResult, places=6, msg="PolygonArea(" + str(corners) + ")", delta=None)

    point1 = Point(3.0, 4.0)
    point2 = Point(5.0, 11.0)
    point3 = Point(12.0, 8.0)
    point4 = Point(9.0, 5.0)
    point5 = Point(5.0, 6.0)
    corners = [point1, point2, point3, point4, point5]
    result = Shoelace.PolygonArea(corners)
    expectedResult = 30.0
    print ("PolygonArea(" + str(corners) + ": " + str(result))
    self.assertAlmostEqual(result, expectedResult, places=6, msg="PolygonArea(" + str(corners) + ")", delta=None)

    # result = Shoelace.PolygonSort(corners)
    # print ("PolygonSort(" + str(corners) + ": " + str(result))

if __name__== "__main__":
  testSuite = unittest.TestLoader().loadTestsFromTestCase(AnalyticGeoTest)
  unittest.TextTestRunner(verbosity=3).run(testSuite)

