import unittest
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from AnalyticGeo.surface import Point, Line, Plane
from numpy.testing import assert_almost_equal


class LineTestCase(unittest.TestCase):
	def testLineConstructor2D(self):
		# y = 2x + 4
		l = Line.fromSlopeInt2D(2,4)
		assert_almost_equal(l.getValueT(2), [2,8,0])
		assert_almost_equal(l.getValueX(-1), [-1,2,0])
		# y = 3x - 2
		l = Line.fromSlopeInt2D(3,-2)
		assert_almost_equal(l.getValueT(4), [4,10,0])
		assert_almost_equal(l.getValueX(2), [2,4,0])


	def testLineConstructor3D(self):
		l = Line(coef=[1,2,3],p=[9,7,6])
		self.assertListEqual(l.getValueT(2), [11,11,12])
		self.assertListEqual(l.getValueT(0), [9,7,6])


	def testPointLineDistance(self):
		p = Point([2,3])
		l = Line(coef=[1,2,3], p=[9,7,6])
		l.pointLineDistance(p)



if __name__ == '__main__':
	unittest.main()