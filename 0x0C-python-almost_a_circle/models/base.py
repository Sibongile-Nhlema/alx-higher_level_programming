#!/usr/bin/python3
''' Defines the "Base" of all other classes '''


class Base:
    ''' "Base" of all other classes '''
    __nb_objects = 0
    def __init__(self, id=None):
        ''' Constructor.
            Args:
                id(int): id 
        '''
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
