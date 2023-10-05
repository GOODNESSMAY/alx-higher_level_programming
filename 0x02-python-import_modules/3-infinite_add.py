#!/usr/bin/python3
from sys import argv
add = 0
for g in argv[1:]:
    add += int(g)
print("{:d}".format(add))
