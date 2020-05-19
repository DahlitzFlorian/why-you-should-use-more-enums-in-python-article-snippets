# permissions.py

from enum import IntFlag


class Permission(IntFlag):
    R = 4
    W = 2
    X = 1


RW = Permission.R | Permission.W
print(RW)
print(Permission.R + Permission.W)
print(Permission.R in RW)
