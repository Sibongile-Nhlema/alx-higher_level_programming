#!/usr/bin/python3
'''Module to find the peak in a list of unordered integers'''

def find_peak(list_of_integers):
    '''Find the peak in a list of unordered integers using binary search algorithm.

    Args:
        list_of_integers (list): A list of unordered integers.

    Returns:
        int: The peak element in the list.

    Example:
        >>> find_peak([1, 3, 20, 4, 1, 0])
        20
    '''
    if not list_of_integers:  # Check if the list is empty
        return None

    left = 0
    right = len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]
