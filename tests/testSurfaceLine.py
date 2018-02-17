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

		# y = - 10x + 3
		l = Line.fromSlopeInt2D(-10,3)
		assert_almost_equal(l.getValueT(-2), [-2,23,0])
		assert_almost_equal(l.getValueX(-3), [-3,33,0])

		# y = - 7.5x - 11.1
		l = Line.fromSlopeInt2D(-7.5,-11.1)
		assert_almost_equal(l.getValueT(-1), [-1,-3.6,0])
		assert_almost_equal(l.getValueX(.3), [.3,-13.35,0])



	def testLineConstructor3D(self):
		l = Line(coef=[1,2,3],p=[9,7,6])
		self.assertListEqual(l.getValueT(2), [11,11,12])
		self.assertListEqual(l.getValueT(0), [9,7,6])

		l = Line(coef=[-1,4,.1],p=[-5,4,1.75])
		self.assertListEqual(l.getValueT(-1), [-4,0,1.65])
		self.assertListEqual(l.getValueT(.45), [-5.45,5.8,1.795])

		l = Line(coef=[-3.7, 3.001, 38],p=[-5,.03, -7])
		assert_almost_equal(l.getValueT(12), [-49.4,36.042,449]) #approximation here because of float values
		assert_almost_equal(l.getValueT(-10), [32,-29.98,-387])


	# def testPointLineDistance(self): #uncomment when PointLineDistance fixed
	# 	p = Point([2,3])
	# 	l = Line(coef=[1,2], p=[9,7])
	# 	self.assertListEqual(l.pointLineDistance(p), 8/math.pow(3,1/2));


	# def linesAngleTest(self): #uncomment when linesAngleTest fixed
		# l1 = Line(coef=[1,2,3], p =[9,7,6])
		# l2 = Line(coef=[4,5,6], p=[1,4,2])
		# l3 = Line(coef=[1,2,1], p=[0,0,0])
		# assert_almost_equal(l1.linesAngle(l2), 0)
		# assert_almost_equal(l1.linesAngle(l2), math.acos(4/sqrt(21)))




if __name__ == '__main__':
	unittest.main()
