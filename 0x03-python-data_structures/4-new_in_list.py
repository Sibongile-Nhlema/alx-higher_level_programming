#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return (my_list)
    elif idx > len(my_list):
        return (my_list)
    else:
        list_copy = my_list.copy()
        list_copy.insert(idx, element)
        list_copy.pop(idx + 1)
        return (list_copy)
