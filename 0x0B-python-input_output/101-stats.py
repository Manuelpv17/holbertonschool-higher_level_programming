#!/usr/local/bin/python3
""" Log parsing
    """
import sys


def print_format():
    print("File size: {:d}".format(total_size))
    for i in range(8):
        if values[i] > 0:
            print("{}: {:d}".format(status[i], values[i]))


status = ['200', '301', '400', '401',
          '403', '404', '405', '500']
values = [0, 0, 0, 0, 0, 0, 0, 0]

cont = 0
total_size = 0

try:
    for line in sys.stdin:
        w = line.split()

        for i, elem in enumerate(status):
            if w[-2] == elem:
                values[i] += 1
                total_size += int(w[-1])
        cont += 1
        if cont % 10 == 0:
            print_format()

except KeyboardInterrupt:
    print_format()
    raise

print_format()
