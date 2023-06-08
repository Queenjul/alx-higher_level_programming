#!/usr/bin/python3

import sys

if __name__ == "__main__":
    count = len(sys.argv)

    if count == 1:
        print("{:d} arguments.".format(count - 1))
    elif count == 2:
        print("{:d} argument:".format(count - 1))
    else:
        print("{:d} arguments:".format(count - 1))
    for j in range(1, count):
        print("{:d}: {:s}".format(j, sys.argv[j]))
