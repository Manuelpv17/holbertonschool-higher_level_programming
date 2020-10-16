#!/usr/bin/python3
""" Find a peak """


def find_peak(list_of_integers):
    """ Find a peak """
    lenList = len(list_of_integers)
    if lenList == 0:
        return None
    return recursionPeak(list_of_integers, 0, lenList - 1)


def recursionPeak(intList, left, right):
    if (left == right):
        return intList[left]
    mid = (left + right) // 2
    if (intList[mid] > intList[mid + 1]) and (mid == left or intList[mid] > intList[mid - 1]):
        return intList[mid]
    elif intList[mid] < intList[mid + 1]:
        return recursionPeak(intList, mid + 1, right)
    else:
        return recursionPeak(intList, left, mid - 1)
