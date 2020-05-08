#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    new = []
    for item in my_list:
        flag = 0
        for new_item in new:
            if new_item == item:
                flag = 1
        if flag == 0:
            new.append(item)
            sum += item
    return(sum)
