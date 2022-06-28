#!/usr/bin/python3
a = 97
while a < 123:
    if (a == 101) or (a == 113):
        a += 1
        continue
    else:
        b = chr(a)
        print("{}".format(b), end="")
        a += 1
