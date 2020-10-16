#!/usr/bin/python3
""" Test function find_peak """
find_peak = __import__('6-peak').find_peak

a = [1, 2, 4, 6, 3]
print(find_peak(a), a)
a = [4, 2, 1, 2, 3, 1]
print(find_peak(a), a)
a = [2, 2, 2]
print(find_peak(a), a)
a = []
print(find_peak(a), a)
a = [-2, -4, 2, 1]
print(find_peak(a), a)
a = [4, 2, 1, 2, 2, 2, 3, 1]
print(find_peak(a), a)
a = [1, 2, 3, 4, 5]
print(find_peak(a), a)
a = [5, 4, 3, 2, 1]
print(find_peak(a), a)
a = [1, 4, 6, 2, 1]
print(find_peak(a), a)
a = [5, 4, 6, 2, 1, 4, 5, 2]
print(find_peak(a), a)
