#!/usr/bin/python3
def best_score(a_dictionary):
    num = 0
    n_key = None
    if not a_dictionary:
        return (None)
    for key, value in a_dictionary.items():
        if value > num:
            num = value
            n_key = key
    return(n_key)
