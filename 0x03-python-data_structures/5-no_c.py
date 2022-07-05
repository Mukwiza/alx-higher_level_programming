#!/usr/bin/python3
def no_c(my_string):
    string = ""
    for i in my_string:
        if i!= chr(99) and i!= chr(67):
          string += i

    return string
