#!/usr/bin/python3
''' Module for the BaseGeometry class '''


class BaseGeometry:
    ''' defines base geometry '''

    def area(self):
        ''' calculates the area of a shape '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        ''' validates whether the value is a positive int '''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
