#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    array = []
    for key, val in a_dictionary.items():
        if val == value:
            array.append(key)

    for item in array:
        del a_dictionary[item]

    return(a_dictionary)
