import math

def QuadArea(sides):
    area = 0.0
    perimeter = 0.0
    for i in range(n):
        perimeter += sides[i]
    semiperimeter = perimeter/2.0
    area = math.sqrt((semiperimeter - sides[0]) * (semiperimeter - sides[1]) * (semiperimeter - sides[2]) * (semiperimeter - sides[3]))
    return area

def main():
  # examples
  sides = [13.0, 14.0, 15.0, 16.0]
  print QuadArea(sides)
  sides = [4.0, 5.0, 6.0, 7.0]
  print QuadArea(sides)

if __name__== "__main__":
  main()
