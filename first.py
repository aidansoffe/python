"""
>>> adder(
...   2,
...   multiply(3, 4)
... )
14
"""

def adder(x, y):
  """
  >>> adder(3,9)
  12
  >>> adder(8, -9)
  -1
  >>> adder(2, -33333333)
  -33333331
  """
  return x + y

def multiply(x, y):
  return x * y


class Cat:
  """
  >>> cats_a=Cat("V")
  >>> cats_a.say_hello()
  Meow! My name is V
  >>> cats_d=Cat('Tim')
  >>> cats_d.say_hello()
  Meow! My name is Tim

  >>> Cat(1)
  Traceback (most recent call last):
    ...
  TypeError: Name must be a string
  """

  def __init__(self, name):
    if type(name) != str:
      raise TypeError("Name must be a string")
    self.name = name
  
  def say_hello(self):
    print(f"Meow! My name is {self.name}")


"""
>>> Cat(A)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'A' is not defined
>>> Cat("A")
<__main__.Cat object at 0x7fe0e2232c10>
>>> say_hello(Cat('A')
... )
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'say_hello' is not defined
>>> Cat.say_hello(Cat('A'))
Meow! My name is A
>>> Cat.say_hello(Cat('A'))
KeyboardInterrupt
>>> Cat('A').say_hello()
KeyboardInterrupt
>>> cat_a = Cat('A')
>>> cat_a.say_hello()
Meow! My name is A
>>> 
"""