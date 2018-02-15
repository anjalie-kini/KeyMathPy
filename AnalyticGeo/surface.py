from math import sqrt, atan

class Point:
	x = None
	y = None
	z = None

	def __init__(self, x,y,z=0):
		self.x = x
		self.y = y
		self.z = z

	def distanceFormula(self,other):
		sq1 = pow((self.x - other.x) ,2)
		sq2 = pow((self.y - other.y), 2)
		sq3 = pow((self.z - other.z), 2)
		return sqrt(sq1 + sq2 + sq3)

	def pointLineDistance(self,l_other):
		return l_other.PointLineDistance(self)

class Line:
	def __init__(self, coef=None, p=None):
		'''Creates a Line object using its slope and a point
		Lines go up to 3D and are stored in parametric form:
			r(t) = <x1,y1,z1> + t<a,b,c>
		where (x1,y1,z1) is p1, a point on the line and
		coef is <a,b,c> is coef
		'''
		if len(coef) == 2:
			coef[2] = 0
		self.coef = coef
		if len(p) == 2:
			point[2] = 0
		self.point = p
		print(str(len(p)) + "   " + str(len(coef)))

	@classmethod
	def fromSlopeInt2D(cls, slope, y_int):
		coef = [1,slope,0]
		point = [0,y_int,0]
		return cls(coef,point)


	def getValue(self,t):
		"""
		Returns the value of the line at the specified point t
		"""

		p = []
		for index, val in enumerate(self.coef):
			p.append(val * t + self.point[index]) 
			# p[1] = val * t + self.point[index]
			# p[2] = val * t + self.point[index]
		return p


	def getCoef(self,p1,p2):
		self.slope = (p2.y-p1.y) / (p2.x - p1.x)
		self.y_intercept = p1.y -  p1.x * self.slope
		self.c = -1 * self.y_intercept
		self.b = (-1) * self.slope
		self.a = 1

	# def pointLineDistance(p_other):
	# 	denom = math.sqrt(pow(p_other.x,2) + pow(p_other.y,2))
	# 	num = self.a * p_other.x  + self.b * p_other.y + c
	# 	return num / denom

	# def linesAngle(l_other):
	# 	theta1 = atan(self.slope)
	# 	theta2 = atan(l_other.slope)
	# 	return abs(theta1 - theta2)

class Plane:
	def __init__(self,normal, point):
		"""Constructs a Plane object
		Params:
			normal: the normal vector to the plane, list form
			point: A point on the plane, list form
		"""
		self.normal = normal
		if point:
			self.point = point
		else:
			self.point = [0,0,0]
		self.d = 0
		for index, elem in enumerate(point):
			self.d += elem * normal[index]


	def planeIntersection(other):
		"""
		Cross `self` with other
		NOT FINISHED
		"""
		crossedPlanes = crossProduct(self.normal, other.normal)

		x = ((self.d*other.normal[0] - other.d*plane*self.normal[0])/ 
			(self.normal[1]*other.normal[0] - other.normal[0]*plane*self.normal[1]))
		y = ((self.d*other.normal[1] - other.d*plane*self.normal[1])/
		 (self.normal[0]*other.normal[1] - other.normal[1]*plane*self.normal[0]))
		point = []
    	# point[0] = x.point[1] y,point[2] = 0


	@staticmethod
	def crossProduct(normal1, normal2):
		cross = []
		cross[0] = normal1[1]*normal2[2] - normal1[2]*noraml2[1]
		cross[1] = normal1[2]*normal2[0] - normal1[0]*normal2[2]
		cross[2] = normal1[0]*normal2[1] - normal1[1]*normal2[0]
		return cross












