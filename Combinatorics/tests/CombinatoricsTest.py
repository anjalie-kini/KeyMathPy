import unittest

import os, sys, datetime
sys.path.insert(0, os.path.abspath('..'))

import Catalan
import Combination
import Factorial
import Fibonacci
import Permutation

class CombinatoricsTest(unittest.TestCase):
  def testCatalan(self):
    print ("\n%%%%%%% Testing Catalan")
    expectedResult = 1430
    result = Catalan.catalan(8)
    print("catalan(8)=" + str(result))
    self.assertEqual(result, expectedResult, msg="catalan(8)")

    expectedResult = 35357670
    result = Catalan.catalan(16)
    print("catalan(16)=" + str(result))
    self.assertEqual(result, expectedResult, msg="catalan(16)")

    expectedResult = 343059613650
    result = Catalan.catalan(23)
    print("catalan(23)=" + str(result))
    self.assertEqual(result, expectedResult, msg="catalan(23)")

  def testCombination(self):
    print ("\n%%%%%%% Testing Combination")
    expectedResult = 56
    result = Combination.combination(8,3)
    print("combination(8,3)=" + str(result))
    self.assertEqual(result, expectedResult, msg="combination(8,3)")

    expectedResult = 1
    result = Combination.combination(5,5)
    print("combination(5,5)=" + str(result))
    self.assertEqual(result, expectedResult, msg="combination(5,5)")

    expectedResult = 66
    result = Combination.combination(12,2)
    print("combination(12,2)=" + str(result))
    self.assertEqual(result, expectedResult, msg="combination(12,2)")

  def testFactorial(self):
    print ("\n%%%%%%% Testing Factorial")
    expectedResult = 1307674368000
    result = Factorial.factorial(15)
    print("factorial(15)=" + str(result))
    self.assertEqual(result, expectedResult, msg="factorial(15)")

    expectedResult = 5040
    result = Factorial.factorial(7)
    print("factorial(7)=" + str(result))
    self.assertEqual(result, expectedResult, msg="factorial(7)")

    expectedResult = 8841761993739701954543616000000
    result = Factorial.factorial(29)
    print("factorial(46)=" + str(result))
    self.assertEqual(result, expectedResult, msg="factorial(46)")


  def testFibonacci(self):
    print ("\n%%%%%%% Testing Fibonacci")
    expectedResult = 13
    result = Fibonacci.fibonacci(8)
    print("fibonacci(8)=" + str(result))
    self.assertEqual(result, expectedResult, msg="fibonacci(8)")

    expectedResult = 610
    result = Fibonacci.fibonacci(16)
    print("fibonacci(16)=" + str(result))
    self.assertEqual(result, expectedResult, msg="fibonacci(16)")

    expectedResult = 17711
    result = Fibonacci.fibonacci(23)
    print("fibonacci(23)=" + str(result))
    self.assertEqual(result, expectedResult, msg="fibonacci(23)")


  def testPermutation(self):
    print ("\n%%%%%%% Testing Permutation")

    expectedResult = 336
    result = Permutation.permutation(8,3)
    print("permutation(8,3)=" + str(result))
    self.assertEqual(result, expectedResult, msg="Permutation(8,3)")

    expectedResult = 120
    result = Permutation.permutation(5,5)
    print("permutation(5,5)=" + str(result))
    self.assertEqual(result, expectedResult, msg="Permutation(5,5)")

    expectedResult = 132
    result = Permutation.permutation(12,2)
    print("permutation(12,2)=" + str(result))
    self.assertEqual(result, expectedResult, msg="Permutation(12,2)")

if __name__== "__main__":
  testSuite = unittest.TestLoader().loadTestsFromTestCase(CombinatoricsTest)
  unittest.TextTestRunner(verbosity=3).run(testSuite)
