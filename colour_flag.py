# colour_flag.py

from enum import auto
from enum import Flag


class Colour(Flag):
    RED = auto()
    GREEN = auto()
    BLUE = auto()
    WHITE = RED | GREEN | BLUE


print(Colour.WHITE.name, Colour.WHITE.value)
