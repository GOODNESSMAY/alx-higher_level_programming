#!/usr/bin/python3
for m in range(97, 123):
    if chr(m) == 'q' or chr(m) == 'e':
        continue
    print(chr(m).format(m), end='')
