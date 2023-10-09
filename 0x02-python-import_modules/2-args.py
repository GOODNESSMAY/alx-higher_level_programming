#!/usr/bin/python3
import sys

number = len(sys.argv) - 1
if number == 0:
    print("0 arg.")
elif number == 1:
    print("1 arg:")
else:
    print("{} arg:".format(number))
for m in range(number):
    print("{}: {}".format(m + 1, sys.argv[m + 1]))
