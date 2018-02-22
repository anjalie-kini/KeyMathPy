import Heron

def main():
  sides = [13.0, 14.0, 15.0]
  print ("TriangleArea for " + str(sides) + ": " + str(Heron.TriangleArea(sides)))

  sides = [4.0, 5.0, 6.0]
  print ("TriangleArea for " + str(sides) + ": " + str(Heron.TriangleArea(sides)))

if __name__== "__main__":
  main()
