#!/usr/bin/python3

import sys

length = len(sys.argv)
total = 0
if __name__ == "__main__":
    if length == 1:
        total = 0
    else:
        for j in range(1, length):
            total += int(sys.argv[j])
    print("{:d}".format(total))
