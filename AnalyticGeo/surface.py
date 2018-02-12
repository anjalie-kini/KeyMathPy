from math import sqrt, atan

class Point:
	x = None
	y = None

	def __init__(self, x,y):
		self.x = x
		self.y = y

	def distanceFormula(p_other):
		sq1 = pow((self.x - p_other.x) ,2)
		sq2 = pow((self.y - p_other.y), 2)
		return math.sqrt(sq1 + sq2)

	def PointLineDistance(l_other):
		return l_other.PointLineDistance(self)

class Line:
	def __init__(self, p1, p2):
		'''
		'''
		self.getCoef(p1,p2)

	def __init__(self,a,b,c):
		'''
		ax + by + c = 0
		'''
		self.a = a
		self.b = b
		self.c = c

	def getCoef(p1,p2):
		slope = (p2.y-p1.y) / (p2.x - p1.x)
		self.y_intercept = p1.y -  p1.x * slope
		self.c = -1 * self.y_intercept
		self.b = (-1) * slope
		self.a = 1

	def PointLineDistance(p_other):
		denom = math.sqrt( pow(p_other.x,2) + pow(p_other.y,2))
		num = self.a * p_other.x  + self.b * p_other.y + c
		return num / denom

	def linesAngle(l_other):
		theta1 = atan(self.slope)
		theta2 = atan(l_other.slope)
		return abs(theta1 - theta2)

class Plane:
	def __init__(self,p1,line):
		pass



