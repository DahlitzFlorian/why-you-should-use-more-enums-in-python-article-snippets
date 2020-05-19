# iterate.py

from enum import Enum


class Colour(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


for name, member in Colour.__members__.items():
    print(name, member)
