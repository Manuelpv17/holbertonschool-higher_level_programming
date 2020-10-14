#!/usr/bin/python3
""" Find a peak """


def find_peak(list_of_integers):
    lenList = len(list_of_integers)
    if lenList == 0:
        return None
    for i in range(0, lenList):
        if (i + 1 >= lenList or list_of_integers[i] > list_of_integers[i+1]) and (i == 0 or list_of_integers[i] > list_of_integers[i-1]):
            return list_of_integers[i]

    return list_of_integers[0]
