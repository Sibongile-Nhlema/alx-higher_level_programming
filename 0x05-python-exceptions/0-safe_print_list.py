#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    num_of_elements = 0
    elements_returned = ""
    try:
        for i in my_list:
            num_of_elements += 1
        for i in range(num_of_elements):
            if i < x:
                print(my_list[i], end="")
                num_of_elements = i + 1
        print()
    except TypeError:
        pass
    return num_of_elements
