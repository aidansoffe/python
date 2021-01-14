import arithmetic 
from unittest import TestCase

class AdditionTestCase(TestCase):
  def test_adder(self):
    assert arithmetic.adder(2, 4) == 6

  def test_adder2(self):
    """
    this type of method is better
    """
    self.assertEqual(arithmetic.adder(2,2), 4)
  