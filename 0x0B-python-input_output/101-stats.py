#!/usr/bin/python3
""" Log parsing
    """
import sys

status = {'200': 0, '301': 0, '400': 0, '401': 0,
          '403': 0, '404': 0, '405': 0, '500': 0}

cont = 0
size = 0
total_size = 0
try:
    for line in sys.stdin:
        cont += 1
        w = line.split()
        status[w[-2]] += 1

        total_size += int(w[-1])
        if cont % 10 == 0:
            print("File size: {}".format(total_size))
            for stat_key, stat_value in status.items():
                if stat_value > 0:
                    print("{}: {}".format(stat_key, stat_value))
    if cont % 10 != 0:
        print("File size: {}".format(total_size))
        for stat_key, stat_value in status.items():
            if stat_value > 0:
                print("{}: {}".format(stat_key, stat_value))
except Exception:
    print("File size: {}".format(total_size))
    for stat_key, stat_value in status.items():
        if stat_value > 0:
            print("{}: {}".format(stat_key, stat_value))
