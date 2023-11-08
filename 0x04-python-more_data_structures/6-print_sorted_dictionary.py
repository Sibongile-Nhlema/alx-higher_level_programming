#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for key in map(lambda x: x[0], sorted(a_dictionary.items())):
        print(key, ":", a_dictionary[key])
