import unittest
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from AnalyticGeo.surface import Point, Line, Plane
from numpy.testing import assert_almost_equal

class PointTestCase(unittest.TestCase):

	def testPointDistanceFormula(self):
		p = Point([2,3,0])
		p2 = Point([5,6,0])
		self.assertAlmostEqual(4.242640687, p.distanceFormula(p2))
		p = Point([-2,-3,0])
		p2 = Point([-3,-4,0])
		self.assertAlmostEqual(1.414213562, p.distanceFormula(p2))
		p2 = Point([3,4,0])
		self.assertAlmostEqual(8.602325267, p.distanceFormula(p2))
		p2 = Point([100,200,0])
		self.assertAlmostEqual(227.1849467, p.distanceFormula(p2))



	def testLineConstructor3D(self):
		pass

	def testPointLineDistance(self):
		pass





	

if __name__ == '__main__':
	unittest.main()