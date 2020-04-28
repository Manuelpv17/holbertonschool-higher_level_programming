#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
aux = abs(number) % 10
if aux > 5:
    str = "and is greater than 5"
elif aux == 0:
    str = "and is 0"
else:
    str = "and is less than 6 and not 0"

if (number < 0):
    print("Last digit of {:d} is {} {}".format(
        number, -aux, str))
else:
    print("Last digit of {:d} is {} {}".format(number, aux, str))
