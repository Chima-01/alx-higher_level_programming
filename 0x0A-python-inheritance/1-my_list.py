#!/usr/bin/python3
"""
    Create a class called MyList to inherit from
    list
"""


class MyList(list):
    """ class inherits class list """
    pass

    def print_sorted(self):
        """ prints list in sorted format """
        new_list = sorted(self)
        try:
          return print("{}".format(new_list))
        except Exception as e:
            print(e)
