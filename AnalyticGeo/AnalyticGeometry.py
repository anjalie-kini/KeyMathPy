import math 

class Point:
  def __init__(self, x, y, z=None):
    '''
    Creates a 2D or 3D Point object using x, y, z coords
    '''
    self.x = x
    self.y = y
    self.z = z

  def __str__(self):
    return ("Point X(" + str(self.getX()) + "), Y(" + str(self.getY()) + "), Z(" + str(self.getZ()) + ")")

  def __repr__(self):
    return ("Point Coordinates X(" + str(self.getX()) + "), Y(" + str(self.getY()) + "), Z(" + str(self.getZ()) + ")")

  def getX(self):
    return self.x

  def getY(self):
    return self.y

  def getZ(self):
    return self.z

  def distance2D(self,other):
    sq1 = pow((self.getX() - other.getX()), 2)
    sq2 = pow((self.getY() - other.getY()), 2)
    return math.sqrt(sq1 + sq2)

  def findLineEquation(self, other):
    slope = (self.getY() - other.getY()) / (self.getX() - other.getX())
    b = self.getY() - slope * self.getX()

    return Line(slope, b)

  def pointLineDistance(self,line):
    return line.PointLineDistance(self)

  def pointPlaneDistance(self,plane):
    return plane.PointLineDistance(self)


class Line:
  def __init__(self, m, b):
    '''
    Creates a Line object using the coefficients of 
    the slope-intercept form: y = mx + b
    '''
    self.slope = m
    self.y_intercept = b

  def __str__(self):
    return ("Line S(" + str(self.getSlope()) + ") I(" + str(self.getIntercept()) + ")")

  def __repr__(self):
    return ("Line Slope(" + str(self.getSlope()) + ") Intercept(" + str(self.getIntercept()) + ")")


  def getStandard(self):
    '''
    Convert our slope-intercept form to standard form
    ax + by = c
    '''
    standard = []
    standard.append(-1 * self.slope)
    standard.append(1)
    standard.append(self.y_intercept)
    return standard

  def setFromStandard(self, a, b, c):
    '''
    Sets the slope and intercept from the coefficients of 
    the standard form: ax + by = c
    '''
    self.slope = -(a/b)
    self.y_intercept = (c/b)
    print("setFromStandard: " + self)

  def getSlope(self):
    return self.slope

  def getIntercept(self):
    return self.y_intercept

  def pointLineDistance(self, point):
    """
    For lines in two dimensions (XY)
    """
    standard = self.getStandard()
    denom = math.sqrt(pow(standard[0],2) + pow(standard[1],2))
    num = standard[0]*point.getX() + standard[1]*point.getY() - standard[2]
    return abs(num / denom)

  def linesAngle(self,other):
    """
    Finds angles between 2 lines
    """
    theta1 = math.atan(self.getSlope())
    theta2 = math.atan(other.getSlope())
    return abs(theta1 - theta2)

  def linesIntersection(self,other):
    """
    Intersection point between 2 lines
    """
    s1 = self.getStandard()
    s2 = other.getStandard()

    determinant = s1[0]*s2[1] - s2[0]*s1[1];
    if (determinant == 0):
        raise Exception("Lines " + str(self) + " and " + str(other) + " are parallel")

    x = (s2[1]*s1[2] - s1[1]*s2[2])/determinant
    y = (s1[0]*s2[2] - s2[0]*s1[2])/determinant

    intersectionPoint = Point(x, y)
    return intersectionPoint



class Plane:
  def __init__(self, a, b, c, d):
    '''
    Creates a Plane object using the coefficients of
    the standard form: ax + by + cz = d
    '''
    self.a = a
    self.b = b
    self.c = c
    self.d = d

  def __str__(self):
    return ("Plane A(" + str(self.getA()) + "), B(" + str(self.getB()) + "), C(" + str(self.getC()) + "), D(" + str(self.getD()) + ")")

  def __repr__(self):
    return ("Plane Standard Form A(" + str(self.getA()) + "), B(" + str(self.getB()) + "), C(" + str(self.getC()) + "), D(" + str(self.getD()) + ")")


  def getA(self):
    return self.a

  def getB(self):
    return self.b

  def getC(self):
    return self.c

  def getD(self):
    return self.d


  def planeIntersection(self, other):
    crossedPlanes = []
    crossedPlanes.append((self.getB()*other.getC()) - (self.getC()*other.getB()))
    crossedPlanes.append((self.getC()*other.getA()) - (self.getA()*other.getC()))
    crossedPlanes.append((self.getA()*other.getB()) - (self.getB()*other.getA()))

    x = (self.getD()*other.getA() - other.getD()*self.getA()) / (self.getB()*other.getA() - self.getA()*other.getB())
    y = (self.getD()*other.getB() - other.getD()*self.getB()) / (self.getA()*other.getB() - self.getB()*other.getA())

    point = []
    point.append(x)
    point.append(y)
    point.append(0)

    line = []
    line.append(crossedPlanes)
    line.append(point)
    return line 


  def pointPlaneDistance(self, point1):
    denom = math.sqrt(pow(self.getA(),2) + pow(self.getB(),2) + pow(self.getC(),2))
    num = self.getA()*point1.getX() + self.getB()*point1.getY() + self.getC()*point1.getZ() + self.getD()
    return (num/denom)

