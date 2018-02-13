import unittest
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from AnalyticGeo.surface import Point, Line, Plane

class PointTestCase(unittest.TestCase):

	def testPointDistanceFormula(self):
		p = Point(2,3)
		p2 = Point(5,6)
		self.assertAlmostEqual(4.242640687, p.distanceFormula(p2))
		p = Point(-2,-3)
		p2 = Point(-3,-4)
		self.assertAlmostEqual(1.414213562, p.distanceFormula(p2))
		p2 = Point(3,4)
		self.assertAlmostEqual(8.602325267, p.distanceFormula(p2))
		p2 = Point(100, 200)
		self.assertAlmostEqual(227.1849467, p.distanceFormula(p2))

	def testLineConstructor(self):
		l = Line(p1=Point(2,3), p2=Point(3,4))
		self.assertEqual(1,l.a)
		self.assertEqual(-1,l.b)
		self.assertEqual(-1,l.c)
		self.assertEqual(1, l.y_intercept)
		self.assertEqual(1,l.slope)


if __name__ == '__main__':
	unittest.main()