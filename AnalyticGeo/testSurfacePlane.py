import unittest
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from AnalyticGeo.surface import Point, Line, Plane
from numpy.testing import assert_almost_equal

# class PlaneTestCase(unittest.TestCase):
#     def testPlaneIntersection(self): #add when planeIntersection is fixed
