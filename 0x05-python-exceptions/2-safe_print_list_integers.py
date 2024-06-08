#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """print the first x element of a list that are integers

    Args:
        my_list (list): the list to print elements from
        x (in): the number of elements of my_list to print
        Return:
            the number of elements printed
    """
    num = 0
    for items in range(x):
        try:
            print("{:d}".format(my_list[items]), end= '')
            num += 1
        except (ValueError, TypeError, IndexError):
            pass
        print()
        return num
