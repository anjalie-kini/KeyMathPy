import Brahmagupta

def main():
  sides = [13.0, 14.0, 15.0, 16.0]
  print ("QuadArea for " + str(sides) + ": " + str(Brahmagupta.QuadArea(sides)))

  sides = [4.0, 5.0, 6.0, 7.0]
  print ("QuadArea for " + str(sides) + ": " + str(Brahmagupta.QuadArea(sides)))

if __name__== "__main__":
  main()
