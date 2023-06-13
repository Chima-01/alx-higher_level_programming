#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    _tuple = (0,)

    if len(tuple_a) == 1:
        tuple_a = tuple_a + _tuple
    elif len(tuple_a) == 0:
        tuple_a = _tuple + _tuple

    if len(tuple_b) == 1:
        tuple_b = tuple_b + _tuple
    elif len(tuple_b) == 0:
        tuple_b = _tuple + _tuple

    new_tuple_a = tuple_a[0] + tuple_b[0]
    new_tuple_b = tuple_a[1] + tuple_b[1]
    new_tuple = (new_tuple_a, new_tuple_b)

    return new_tuple
