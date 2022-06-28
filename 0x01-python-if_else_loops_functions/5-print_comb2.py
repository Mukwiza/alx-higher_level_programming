#!/usr/bin/python3
a = 0
while a < 100:
    if a == 99:
        print("{:02}".format(a))
        break
    else:
        print("{:02}, ".format(a), end="")
        a += 1
