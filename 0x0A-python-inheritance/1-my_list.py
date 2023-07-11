#!/usr/bin/python3
"""
    Create a class called MyList to inherit from
    list
"""


class MyList(list):
    """ class inherits class list """

    def print_sorted(self):
        """ prints list in sorted format """

        print(sorted(self))
