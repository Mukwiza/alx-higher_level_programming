#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    i, a = 0, 0
    j = (len(my_list) - 1)
    while i < j:
        if my_list[a] < my_list[i+1]:
            i += 1
            a += 1
        x = my_list[a]
        i += 1
    return x
