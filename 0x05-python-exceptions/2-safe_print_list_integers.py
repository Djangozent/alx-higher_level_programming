#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """print the first x element of a list that are integers

    Args:
        my_list (list): the list to print elements from
        x (in): the number of elements of my_list to print
        Return:
            the number of elements printed
    """
    ret = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
        print("")
        return (ret)
