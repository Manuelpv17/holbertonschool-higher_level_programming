#!/usr/bin/python3
def weight_average(my_list=[]):
    sum = 0
    div = 0
    if my_list:
        for item in my_list:
            sum += (item[0] * item[1])
            div += item[1]
            return(sum / div)
    else:
        return(0)
