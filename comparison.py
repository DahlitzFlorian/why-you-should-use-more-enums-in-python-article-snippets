# comparison.py

from enum import IntEnum


class Colour(IntEnum):
    RED = 1
    GREEN = 2
    BLUE = 3


r = Colour.RED
b = Colour.GREEN
print(r < b)
