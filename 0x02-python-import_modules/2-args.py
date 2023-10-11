#!/usr/bin/python3

if__name__ == "__main__":

    import sys

    number = len(sys.argv) - 1
    if number == 0:
        print("0 arguments.")
    elif number == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(number))
    for m in range(number):
        print("{}: {}".format(m + 1, sys.argv[m + 1]))

