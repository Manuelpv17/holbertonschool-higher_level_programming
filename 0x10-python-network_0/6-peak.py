#!/usr/bin/python3
""" Find a peak """


def find_peak(list_of_integers):
    """ Find a peak """
    lenList = len(list_of_integers)
    right = lenList - 1
    left = 0
    if (lenList == 0):
        return None

    while (right > left):
        mid = (right + 1 + left) // 2
        if list_of_integers[mid - 1] > list_of_integers[mid]:
            right = mid - 1
        else:
            left = mid
    return left
