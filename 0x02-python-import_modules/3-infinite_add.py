#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    len_argv = len(argv) - 1
    sum = 0
    for i in range(1, len_argv + 1):
        sum = sum + int(argv[i])
    print("{}".format(sum))
