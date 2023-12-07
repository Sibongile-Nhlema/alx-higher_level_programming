#!/usr/bin/python3
''' Defines a rectangle '''
from models.base import Base


class Rectangle(Base):
    ''' Defines a retangle by inheriting from the Base class
        Arsg:
            Base: class it inherits from
    ''' 
    def __init__(self, width, height, x=0, y=0, id=None):
        ''' initialises a rectangle instance
            Args:
                width(int): width of the rectangle
                height(int): height of the rectangle
                x(int): unknown
                y(int): unknown
        '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def set_width(self):
        ''' gets the width attr '''
        return self.__width

    @set_width.setter
    def set_width(self, value):
        ''' sets the width attr '''
        self.__width = value

    @property
    def set_height(self):
        ''' gets the height attr '''
        return self.__height

    @set_height.setter
    def set_height(self, value):
        ''' sets the height attr '''
        self.__height = value

    @property
    def set_x(self):
        ''' gets the x attr '''
        return self.__x

    @set_x.setter
    def set_x(self, value):
        ''' sets the x attr '''
        self.__x = value

    @property
    def set_y(self):
        ''' gets the y attr '''
        return self.__y

    @set_y.setter
    def set_y(self):
        ''' sets the y attr '''
        self.__y = value

