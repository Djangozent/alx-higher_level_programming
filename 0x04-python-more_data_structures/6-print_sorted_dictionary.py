#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """A function that prints a dictionary by ordered keys"""

    j = sorted(a_dictionary)
    for i in j:
        print("{}: {}".format(i, a_dictionary[i]))

