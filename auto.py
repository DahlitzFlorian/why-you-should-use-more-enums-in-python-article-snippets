# auto.py

from enum import auto
from enum import Enum


class Colour(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()


c = Colour.RED
print(c.value)
