#!/usr/bin/python3
''' Defines the "Base" of all other classes '''
import json


class Base:
    ''' "Base" of all other classes '''
    __nb_objects = 0

    def __init__(self, id=None):
        ''' Constructor.
            Args:
                id(int): id
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' returns the JSON string representation of list_dictionaries
            Args:
                list_dictionaries: list of dicts
            Return: None if empty or json string
        '''
        if list_dictionaries is not None or list_dictionaries != []:
            return json.dumps(list_dictionaries)
        else:
            return "[]"
