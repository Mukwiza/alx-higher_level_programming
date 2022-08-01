#!/usr/bin/python3
"""
Module: 1-my_list
"""


class MyList(list):
    """
    Reperesents MyList class
    """


    def print_sorted(self):
        """
        prints the list, but sorted one.
        """
        print (sorted(self))
