import unittest

import os, sys, datetime
sys.path.insert(0, os.path.abspath('..'))

import DistanceFormula
import FindLineEqn
import LinesAngle
import LinesIntersection
import PlaneIntersection
import PointLineDistance
import PointPlaneDistance
import Shoelace

class AnalyticGeoTest(unittest.TestCase):
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

    result = DistanceFormula.distanceFormula(1,2,3,4)
    expectedResult =  2.828427
    print ("distanceFormula for (1,2,3,4): " + str(result))
    self.assertAlmostEqual(result, expectedResult, places=6, msg="distanceFormula(1,2,3,4)", delta=None)

    result = DistanceFormula.distanceFormula(5,2,7,0)
    expectedResult =  2.828427
    print ("distanceFormula for (5,2,7,0): " + str(result))
    self.assertAlmostEqual(result, expectedResult, places=6, msg="distanceFormula(5,2,7,0)", delta=None)

    result = DistanceFormula.distanceFormula(23,65,78,63)
    expectedResult = 55.0363516
    print ("distanceFormula for (23,65,78,63): " + str(result))
    self.assertAlmostEqual(result, expectedResult, places=6, msg="distanceFormula(23,65,78,63)", delta=None)

  def test_FindLineEqn(self):
    print ("\n%%%%%%% Testing FindLineEqn")

    result = FindLineEqn.findLineEquation(1,2,3,4)
    expectedResult = [1.0,1.0]
    print ("findLineEquation for (1,2,3,4): " + str(result))
    self.assertAlmostEqualForList(result, expectedResult, places=6, msg="findLineEquation(1,2,3,4)")

    result = FindLineEqn.findLineEquation(5,2,7,0)
    expectedResult = [-1.0,7.0]
    print ("findLineEquation for (5,2,7,0): " + str(result))
    self.assertAlmostEqualForList(result, expectedResult, places=6, msg="findLineEquation(5,2,7,0)")

    result = FindLineEqn.findLineEquation(23,65,78,63)
    expectedResult = [-0.0363636,65.8363636]
    print ("findLineEquation for (23,65,78,63): " + str(result))
    self.assertAlmostEqualForList(result, expectedResult, places=6, msg="findLineEquation(23,65,78,63)")

  def test_LinesAngle(self):
    print ("\n%%%%%%% Testing LinesAngle")

    line1=[1,2]
    line2=[3,4]
    result = LinesAngle.linesAngle(line1, line2)
    expectedResult = 0.4636476
    print ("linesAngle for " + str(line1) + ", " + str(line2) + ": " + str(result))
    self.assertAlmostEqual(result, expectedResult, places=6, msg="linesAngle", delta=None)

    line1=[5,2]
    line2=[7,0]
    result = LinesAngle.linesAngle(line1, line2)
    expectedResult = 0.0554985
    print ("linesAngle for " + str(line1) + ", " + str(line2) + ": " + str(result))
    self.assertAlmostEqual(result, expectedResult, places=6, msg="linesAngle", delta=None)

    line1=[23,65]
    line2=[78,63]
    result = LinesAngle.linesAngle(line1, line2)
    expectedResult = 0.03063108
    print ("linesAngle for " + str(line1) + ", " + str(line2) + ": " + str(result))
    self.assertAlmostEqual(result, expectedResult, places=6, msg="linesAngle", delta=None)

  def test_LinesIntersection(self):
    print ("\n%%%%%%% Testing LinesIntersection")

    line1=[1,2]
    line2=[3,4]
    result = LinesIntersection.linesIntersection(line1, line2)
    expectedResult = [-0.6666666, 1.3333333]
    print ("linesIntersection for " + str(line1) + ", " + str(line2) + ": " + str(result))
    self.assertAlmostEqualForList(result, expectedResult, places=6, msg="linesIntersection")

    line1=[5,2]
    line2=[7,0]
    result = LinesIntersection.linesIntersection(line1, line2)
    expectedResult = [0.4, 4.0]
    print ("linesIntersection for " + str(line1) + ", " + str(line2) + ": " + str(result))
    self.assertAlmostEqualForList(result, expectedResult, places=6, msg="linesIntersection")

    line1=[23,65]
    line2=[78,63]
    result = LinesIntersection.linesIntersection(line1, line2)
    expectedResult = [-1.375, 33.375]
    print ("linesIntersection for " + str(line1) + ", " + str(line2) + ": " + str(result))
    self.assertAlmostEqualForList(result, expectedResult, places=6, msg="linesIntersection")

  def test_PlaneIntersection(self):
    print ("\n%%%%%%% Testing PlaneIntersection")

    plane1=[1,2,3,4]
    plane2=[3,4,5,6]
    result = PlaneIntersection.planeIntersection(plane1, plane2)
    expectedResult = [[-2, 4, -2], [3.0, -2.0, 0]]
    print ("planeIntersection for " + str(plane1) + ", " + str(plane2) + ": " + str(result))
    self.assertAlmostEqualForListOfLists(result, expectedResult, places=6, msg="planeIntersection")

    plane1=[5,2,7,8]
    plane2=[7,0,25,45]
    result = PlaneIntersection.planeIntersection(plane1, plane2)
    expectedResult =  [[50, -76, -14], [-12.0714285, 6.4285714, 0]]
    print ("planeIntersection for " + str(plane1) + ", " + str(plane2) + ": " + str(result))
    self.assertAlmostEqualForListOfLists(result, expectedResult, places=6, msg="planeIntersection")

    plane1=[23,65,87,123]
    plane2=[78,63,97,103]
    result = PlaneIntersection.planeIntersection(plane1, plane2)
    expectedResult =  [[824, 4555, -3621], [1.9953051643192488, -0.29107981220657275, 0]]
    print ("planeIntersection for " + str(plane1) + ", " + str(plane2) + ": " + str(result))
    self.assertAlmostEqualForListOfLists(result, expectedResult, places=6, msg="planeIntersection")

  def test_PointLineDistance(self):
    print ("\n%%%%%%% Testing PointLineDistance")

    point1=[17,92]
    line1=[1,2,11]
    result = PointLineDistance.pointLineDistance(point1[0], point1[1], line1)
    expectedResult = 94.8092822
    print ("pointLineDistance for point " + str(point1) + ", line " + str(line1) + ": " + str(result))
    self.assertAlmostEqual(result, expectedResult, places=6, msg="pointLineDistance", delta=None)

    point1=[0,0]
    line1=[3,4,12]
    result = PointLineDistance.pointLineDistance(point1[0], point1[1], line1)
    expectedResult = 2.4
    print ("pointLineDistance for point " + str(point1) + ", line " + str(line1) + ": " + str(result))
    self.assertAlmostEqual(result, expectedResult, places=6, msg="pointLineDistance", delta=None)

    point1=[1,2]
    line1=[5,2,13]
    result = PointLineDistance.pointLineDistance(point1[0], point1[1], line1)
    expectedResult = 4.0852974
    print ("pointLineDistance for point " + str(point1) + ", line " + str(line1) + ": " + str(result))
    self.assertAlmostEqual(result, expectedResult, places=6, msg="pointLineDistance", delta=None)

  def test_PointPlaneDistance(self):
    print ("\n%%%%%%% Testing PointPlaneDistance")

    point1=[17,92,105]
    plane1=[1,2,3,11]
    result = PointPlaneDistance.pointPlaneDistance(point1[0], point1[1], point1[2], plane1)
    expectedResult = 140.8466744
    print ("pointPlaneDistance for point " + str(point1) + ", plane " + str(plane1) + ": " + str(result))
    self.assertAlmostEqual(result, expectedResult, places=6, msg="pointPlaneDistance", delta=None)

    point1=[0,0,0]
    plane1=[3,4,5,12]
    result = PointPlaneDistance.pointPlaneDistance(point1[0], point1[1], point1[2], plane1)
    expectedResult =  1.6970562
    print ("pointPlaneDistance for point " + str(point1) + ", plane " + str(plane1) + ": " + str(result))
    self.assertAlmostEqual(result, expectedResult, places=6, msg="pointPlaneDistance", delta=None)

    point1=[1,2,3]
    plane1=[5,2,7,13]
    result = PointPlaneDistance.pointPlaneDistance(point1[0], point1[1], point1[2], plane1)
    expectedResult = 4.8687912
    print ("pointPlaneDistance for point " + str(point1) + ", plane " + str(plane1) + ": " + str(result))
    self.assertAlmostEqual(result, expectedResult, places=6, msg="pointPlaneDistance", delta=None)

  def test_Shoelace(self):
    print ("\n%%%%%%% Testing Shoelace")

    corners = [(2.0, 1.0), (4.0, 5.0), (7.0, 8.0)]
    result = Shoelace.PolygonArea(corners)
    expectedResult = 3.0
    print ("PolygonArea(" + str(corners) + ": " + str(result))
    self.assertAlmostEqual(result, expectedResult, places=6, msg="PolygonArea(" + str(corners) + ")", delta=None)

    corners = [(3.0, 4.0), (5.0, 11.0), (12.0, 8.0), (9.0, 5.0), (5.0, 6.0)]
    result = Shoelace.PolygonArea(corners)
    expectedResult = 30.0
    print ("PolygonArea(" + str(corners) + ": " + str(result))
    self.assertAlmostEqual(result, expectedResult, places=6, msg="PolygonArea(" + str(corners) + ")", delta=None)


if __name__== "__main__":
  testSuite = unittest.TestLoader().loadTestsFromTestCase(AnalyticGeoTest)
  unittest.TextTestRunner(verbosity=3).run(testSuite)

