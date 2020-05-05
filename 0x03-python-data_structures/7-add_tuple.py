#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    for i in range(2):
        if i >= len(tuple_a):
            aux1 = 0
        elif i < len(tuple_a):
            aux1 = tuple_a[i]
        if i >= len(tuple_b):
            aux2 = 0
        elif i < len(tuple_b):
            aux2 = tuple_b[i]
        if i == 0:
            sum1 = aux1 + aux2
        else:
            return(sum1, aux1 + aux2)
