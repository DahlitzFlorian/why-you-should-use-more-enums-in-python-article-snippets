# extending.py

from enum import Enum


class Colour(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

    def __str__(self):
        return self.name

    def colorize(self):
        return f"Let's paint everything in {self.name.lower()}"


c = Colour.RED
print(c)
print(c.colorize())
