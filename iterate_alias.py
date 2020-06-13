# iterate_alias.py

from enum import Enum


class Colour(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    ALIAS_RED = 1


for name, member in Colour.__members__.items():
    print(name, member)

print("="*20)

for member in Colour:
    print(member.name, member)
