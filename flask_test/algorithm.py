def reverse_str(s):
  return s[::-1]


def isPalindrome(s):
  reverse = reverse_str(s)
  return s.lower() == reverse.lower()


def factorial(n):
  """Calculate factorial iteratively"""
  if not(isinstance(n, int) and n >= 0):
      raise ValueError("'n' must be a non-negative integer.")
  result = 1
  for i in range(2, n+1):
      result *= i
  return result