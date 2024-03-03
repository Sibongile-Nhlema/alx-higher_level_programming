#!/usr/bin/python3
''' Function finds the peak in a list of unordered integers'''

def find_peak(list_of_integers):
    ''' Function finds the peak in a list of unordered integers'''
    left = 0
    right = len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

	if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]

