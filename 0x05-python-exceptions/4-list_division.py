#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """divides two lists element by element
    args:
        my_list_1 (list): the 1st list
        my_list_2 (list): the 2nd list
        list_length (int): number of elements to divide
    Return:
        new list of length list_length containing all dividions
    """
    new_list = []
    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            new_list.append(div)
    return(new_list)
