#!/usr/bin/python3
def best_score(a_dictionary):
    num = 0
    if not a_dictionary:
        return (None)
    for value in a_dictionary.values():
        if value > num:
            num = value
    return(num)
