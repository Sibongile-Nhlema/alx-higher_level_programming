#!/usr/bin/python3
''' say_my_name() prints out a full name
    Handles cases of type() == string
    Handles execption if input != string
    '''
def say_my_name(first_name, last_name=""):
    ''' Args:
            first_name: inputted first name
            last_name: "" by default unless user inputs a value
        Return: Full name or just first_name
    '''
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
