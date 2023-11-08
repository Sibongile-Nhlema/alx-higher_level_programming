#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if not a_dictionary:
        return
    for key in map(lambda x: x[0], sorted(a_dictionary.items())):
        print("{} : {}".format(key, a_dictionary[key]))
