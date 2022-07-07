#!/usr/bin/python3
def best_score(a_dictionary):
    if  a_dictionary is None:
        return None 

    y = []
    y = list(a_dictionary.values())
    x = max(y)

    for k, v in a_dictionary.items():
        if v == x:
            return k
