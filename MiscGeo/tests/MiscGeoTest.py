import unittest

import os, sys, datetime
sys.path.insert(0, os.path.abspath('..'))

import Brahmagupta
import Heron

class MiscGeoTest(unittest.TestCase):
  def test_Brahmagupta(self):
    print ("\n%%%%%%% Testing QuadArea using Brahmagupta formula")

    sides = [13.0, 14.0, 15.0, 16.0]
    result = Brahmagupta.QuadArea(sides)
    expectedResult = 208.9976076
    print ("QuadArea for " + str(sides) + ": " + str(result))
    self.assertAlmostEqual(result, expectedResult, places=6, msg="QuadArea via Brahmagupta formula", delta=None)

    sides = [4.0, 5.0, 6.0, 7.0]
    result = Brahmagupta.QuadArea(sides)
    expectedResult = 28.982753
    print ("QuadArea for " + str(sides) + ": " + str(result))
    self.assertAlmostEqual(result, expectedResult, places=6, msg="QuadArea via Brahmagupta formula", delta=None)

  def test_Heron(self):
    print ("\n%%%%%%% Testing TriangleArea using Heron formula")

    sides = [13.0, 14.0, 15.0]
    result = Heron.TriangleArea(sides)
    expectedResult = 84.0
    print ("TriangleArea for " + str(sides) + ": " + str(result))
    self.assertAlmostEqual(result, expectedResult, places=6, msg="TriangleArea via Heron formula", delta=None)

    sides = [4.0, 5.0, 6.0]
    result = Heron.TriangleArea(sides)
    expectedResult = 9.9215674
    print ("TriangleArea for " + str(sides) + ": " + str(result))
    self.assertAlmostEqual(result, expectedResult, places=6, msg="TriangleArea via Heron formula", delta=None)

if __name__== "__main__":
  testSuite = unittest.TestLoader().loadTestsFromTestCase(MiscGeoTest)
  unittest.TextTestRunner(verbosity=2).run(testSuite)
