#!/usr/bin/python3
# 100-print_tebahpla.py
for Q in range(26):
    if Q % 2 == 0:
        print('{:c}'.format(122 - Q), end='')
    else:
        print('{:c}'.format(90 - Q), end='')
