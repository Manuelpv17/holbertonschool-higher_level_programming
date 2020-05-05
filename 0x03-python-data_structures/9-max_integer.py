#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        num = my_list[0]
        for item in my_list:
            if item > num:
                num = item
        return(num)
    return (None)
