#!/usr/bin/env python3
def no_c(my_string):
    new = ""
    for letter in my_string:
        if letter != 'c' and letter != 'C':
            new = new + letter
    return(new)
