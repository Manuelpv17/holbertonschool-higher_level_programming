#!/usr/bin/python3
def weight_average(my_list=[]):
    s = 0
    div = 0
    if my_list:
        for item in my_list:
            s += item[0] * item[1]
            div += item[1]
        return(s / div)
    else:
        return(0)
