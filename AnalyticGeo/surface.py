from math import sqrt, atan

class Point:

	def __init__(self, vals):
		self.vals = vals

	def distanceFormula(self,other):
		sq1 = pow((self.vals[0] - other.vals[0]) ,2)
		sq2 = pow((self.vals[1] - other.vals[1]), 2)
		sq3 = pow((self.vals[2] - other.vals[2]), 2)
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

	@classmethod
	def fromSlopeInt2D(cls, slope, y_int):
		coef = [1,slope,0]
		point = [0,y_int,0]
		return cls(coef,point)


	def getValueT(self,t=None):
		"""
		Returns the value of the line at the specified t
		"""

		p = []
		for index, val in enumerate(self.coef):
			p.append(val * t + self.point[index]) 
			# p[1] = val * t + self.point[index]
			# p[2] = val * t + self.point[index]
		return p

	def getValueX(self,x=0):
		"""
		Returns the value of the line at the specified x-value. 
		NOTE: Only for lines in two dimensions
		"""
		t_value = (x - self.point[0]) / self.coef[0]
		return self.getValueT(t_value)

	def pointLineDistance(self,p_other):
		"""
		Currently only functional for lines in two dimensions (XY)
		"""
		a = -1 * self.coef[0]
		b = 1
		c = self.point[1]

		denom = sqrt(pow(p_other.vals[0],2) + pow(p_other.vals[1],2))
		num = a * p_other.vals[0] + b * p_other.vals[1] + c
		return num / denom

	def linesAngle(l_other):
		"""
		For both lines in the 2D and 3D space
		"""
		dot = 0
		for index, val in enumerate(self.coef):
			dot += val * l_other.coef[index]
		mag1 = sqrt(math.pow(self.coef[0],2) + math.pow(self.coef[1],2) + math.pow(self.coef[2],2))
		mag2 = sqrt(math.pow(l_other.coef[0],2), math.pow(l_other.coef[1],2), math.pow(l_other.coef[2],2))
		return dot / (mag1 * mag2)

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












