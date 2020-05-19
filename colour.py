# color.py

from enum import Enum


class Colour(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


c = Colour.RED
print(c)
print(c.name)
print(c.value)
print(c is Colour.RED)
print(c is Colour.BLUE)
