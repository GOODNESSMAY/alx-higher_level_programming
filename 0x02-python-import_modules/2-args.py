#!/usr/bin/python3
import sys

def argument_returned():
  number = len(sys.argv) - 1
  if number == 0:
    print("No arguments were passed.")
  elif number == 1:
    print("1 argument was passed:")
    print(sys.argv[1])
  else:
    print(f"{argument_returned} arguments were passed:")
  for arg in sys.argv[1:]:
    print(arg)


argument_returned()
