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

	def testLineConstructor2D(self):
		# y = 2x + 4
		l = Line.fromSlopeInt2D(2,4)
		assert_almost_equal(l.getValueT(2), [2,8,0])
		assert_almost_equal(l.getValueX(-1), [-1,2,0])
		# y = 3x - 2
		l = Line.fromSlopeInt2D(3,-2)
		assert_almost_equal(l.getValueT(4), [4,10,0])
		assert_almost_equal(l.getValueX(2), [2,4,0])





	

if __name__ == '__main__':
	unittest.main()