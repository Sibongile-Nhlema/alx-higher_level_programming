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
                list_dictionaries(dict): list of dicts
            Return: None if empty or json string
        '''
        if list_dictionaries is not None or list_dictionaries != []:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        ''' writes JSON string representation of list_objs to file
            Args:
                cls(obj): class
                list_objects(list): list of instances who inherits Base
        '''
        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write([])
            else:
                # to_json_string taks dict as a paramater
                list_of_dicts = []
                for i in list_objs:
                    list_of_dicts.append(i.to_dictionary())
                f.write(Base.to_json_string(list_of_dicts))
