#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    i, a = 0, 0 
    while i < (len(my_list) - 1):
        if my_list[a] < my_list[i+1]:
            a += 1
            i += 1
        elif my_list[a] > my_list[i+1]:
            x = my_list[a]
        i += 1
    return x
