from math import sqrt, atan

class Point:
	x = None
	y = None

	def __init__(self, x,y):
		self.x = x
		self.y = y

	def distanceFormula(self,p_other):
		sq1 = pow((self.x - p_other.x) ,2)
		sq2 = pow((self.y - p_other.y), 2)
		return sqrt(sq1 + sq2)

	def pointLineDistance(self,l_other):
		return l_other.PointLineDistance(self)

class Line:
	def __init__(self, p1=None, p2=None,a=None,b=None,c=None):
		'''Creates a Line object using two Point objects, or with coefficients
		Args:
			p1: The 

		'''
		if p1 and p2 and not (a and b and c):
			self.getCoef(p1,p2)
		elif a and b and c:
			self.a = a
			self.b = b
			self.c = c



	def getCoef(self,p1,p2):
		self.slope = (p2.y-p1.y) / (p2.x - p1.x)
		self.y_intercept = p1.y -  p1.x * self.slope
		self.c = -1 * self.y_intercept
		self.b = (-1) * self.slope
		self.a = 1

	def pointLineDistance(p_other):
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



