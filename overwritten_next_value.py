# overwritten_next_values.py

from enum import auto
from enum import Enum


class AutoName(Enum):
    def _generate_next_value_(name, start, count, last_values):
        if len(last_values) > 0:
            return last_values[-1] * 2
        return 2


class Colour(AutoName):
    RED = auto()
    GREEN = auto()
    BLUE = auto()


c = Colour.RED
g = Colour.GREEN
b = Colour.BLUE
print(c.value)
print(g.value)
print(b.value)
