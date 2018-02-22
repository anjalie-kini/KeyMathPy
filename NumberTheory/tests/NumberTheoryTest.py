import CheckPrime
import FindFactors
import Gcd
import Lcm
import PrimeFactors
import unittest

class NumberTheoryTest(unittest.TestCase):
  def testCheckPrime(self):
    print ("\n%%%%%%% Testing CheckPrime")
    result = CheckPrime.checkPrime(15349)
    expectedResult = True
    print ("checkPrime(15349)=" + str(result))
    self.assertEqual(result, expectedResult, msg="checkPrime(15349)")

    result = CheckPrime.checkPrime(850453)
    expectedResult = True
    print ("checkPrime(850453)=" + str(result))
    self.assertEqual(result, expectedResult, msg="checkPrime(850453)")

    result = CheckPrime.checkPrime(2943)
    expectedResult = False
    print ("checkPrime(2943)=" + str(result))
    self.assertEqual(result, expectedResult, msg="checkPrime(2943)")

    result = CheckPrime.checkPrime(373587911)
    expectedResult = True
    print ("checkPrime(373587911)=" + str(result))
    self.assertEqual(result, expectedResult, msg="checkPrime(373587911)")

    result = CheckPrime.checkPrime(32980549)
    expectedResult = False
    print ("checkPrime(32980549)=" + str(result))
    self.assertEqual(result, expectedResult, msg="checkPrime(32980549)")
  
  def testFindFactors(self):
    print ("\n%%%%%%% Testing FindFactors")
    result = FindFactors.findFactors(8)
    expectedResult = [8,1,2,4]
    print ("findFactors(8)=" + str(result))
    self.assertCountEqual(result, expectedResult, msg="findFactors(8)")

    result = FindFactors.findFactors(108)
    expectedResult = [1,2,3,4,6,9,12,18,27,36,54,108]
    print ("findFactors(108)=" + str(result))
    self.assertCountEqual(result, expectedResult, msg="findFactors(108)")

    result = FindFactors.findFactors(23)
    expectedResult = [1,23]
    print ("findFactors(23)=" + str(result))
    self.assertCountEqual(result, expectedResult, msg="findFactors(23)")
  
  def testGcd(self):
    print ("\n%%%%%%% Testing Gcd")
    result = Gcd.gcd(15, 12)
    expectedResult = 3
    print ("gcd(15,12)=" + str(result))
    self.assertEqual(result, expectedResult, msg="gcd(15,12)")

    result = Gcd.gcd(24,36)
    expectedResult = 12
    print ("gcd(24,36)=" + str(result))
    self.assertEqual(result, expectedResult, msg="gcd(24,36)")

    result = Gcd.gcd(2,3)
    expectedResult = 1
    print ("gcd(2,3)=" + str(result))
    self.assertEqual(result, expectedResult, msg="gcd(2,3)")

  def testLcm(self):
    print ("\n%%%%%%% Testing Lcm")
    result = Lcm.lcm(15,12)
    expectedResult = 60
    print ("lcm(15,12)=" + str(result))
    self.assertEqual(result, expectedResult, msg="lcm(15,12)")

    result = Lcm.lcm(24,36)
    expectedResult = 72
    print ("lcm(24,36)=" + str(result))
    self.assertEqual(result, expectedResult, msg="lcm(24,36)")

    result = Lcm.lcm(2,3)
    expectedResult = 6
    print ("lcm(2,3)=" + str(result))
    self.assertEqual(result, expectedResult, msg="lcm(2,3)")

  def testPrimeFactors(self):
    print ("\n%%%%%%% Testing PrimeFactors")
    result = PrimeFactors.primeFactors(8)
    expectedResult = [2,2,2]
    print("primeFactors(8)=" + str(result))
    self.assertCountEqual(result, expectedResult, msg="primefactors(8)")

    result = PrimeFactors.primeFactors(108)
    expectedResult = [2,2,3,3,3]
    print("primeFactors(108)=" + str(result))
    self.assertCountEqual(result, expectedResult, msg="primefactors(108)")

    result = PrimeFactors.primeFactors(23)
    expectedResult = [23]
    print("primeFactors(23)=" + str(result))
    self.assertCountEqual(result, expectedResult, msg="primefactors(23)")


if __name__== "__main__":
  testSuite = unittest.TestLoader().loadTestsFromTestCase(NumberTheoryTest)
  unittest.TextTestRunner(verbosity=3).run(testSuite)
