from unittest import TestCase
from algorithm import reverse_str, isPalindrome, factorial

class AlgorithmTestCase(TestCase):
  def test_reverse_str(self):
    self.assertEqual(reverse_str("hello"), "olleh")
    self.assertEqual(reverse_str("Apple"), "elppA")

  def test_isPalindrome(self):
    self.assertEqual(isPalindrome("lol"), True)
    self.assertTrue(isPalindrome("racecar"))
    self.assertFalse(isPalindrome("Apple"))

  def test_factorial(self):
    self.assertEqual(factorial(5), 120)
    self.assertRaises(ValueError, factorial, -5)