#!/usr/bin/python3
for g in range(0, 8):
    for p in range(g + 1, 10):
        print("{:d}{:d}".format(g, p), end=', ')
print("{:d}{:d}".format(g + 1, p))
