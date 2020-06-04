#!/usr/bin/python3
""" Log parsing
    """
import sys

cont_200 = 0
cont_301 = 0
cont_400 = 0
cont_401 = 0
cont_403 = 0
cont_404 = 0
cont_405 = 0
cont_500 = 0
total_size = 0
cont = 0

try:
    for line in sys.stdin:
        cont += 1
        w = line.split()
        if w[-2] == "200":
            cont_200 += 1
        if w[-2] == "301":
            cont_301 += 1
        if w[-2] == "400":
            cont_400 += 1
        if w[-2] == "401":
            cont_401 += 1
        if w[-2] == "403":
            cont_403 += 1
        if w[-2] == "404":
            cont_404 += 1
        if w[-2] == "405":
            cont_405 += 1
        if w[-2] == "500":
            cont_500 += 1

        total_size += int(w[-1])
        if cont % 10 == 0:
            print("File size: {}".format(total_size))
            if cont_200 > 0:
                print("200: {}".format(cont_200))
            if cont_301 > 0:
                print("301: {}".format(cont_301))
            if cont_400 > 0:
                print("400: {}".format(cont_400))
            if cont_401 > 0:
                print("401: {}".format(cont_401))
            if cont_403 > 0:
                print("403: {}".format(cont_403))
            if cont_404 > 0:
                print("404: {}".format(cont_404))
            if cont_405 > 0:
                print("405: {}".format(cont_405))
            if cont_500 > 0:
                print("500: {}".format(cont_500))
except KeyboardInterrupt:
    sys.exit()
