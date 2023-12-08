#!/usr/bin/python3
''' Defines a rectangle '''
from models.base import Base


class Rectangle(Base):
    ''' Defines a retangle by inheriting from the Base class
        Args:
            Base: class it inherits from
    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        ''' initialises a rectangle instance
            Args:
                width(int): width of the rectangle
                height(int): height of the rectangle
                x(int): x-coordinates of the rectangle
                y(int): y-coordinates of the rectangle
        '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
       ''' gets the width attr '''
       return self.__width

    @width.setter
    def width(self, value):
        ''' sets the width attr '''
        self.__width = value

    @property
    def height(self):
       ''' gets the height attr '''
       return self.__height

    @height.setter
    def height(self, value):
        ''' sets the height attr '''
        self.__height = value

    @property
    def x(self):
        ''' gets the x attr '''
        return self.__x

    @x.setter
    def x(self, value):
       ''' sets the x attr '''
       self.__x = value

    @property
    def y(self):
        ''' gets the y attr '''
        return self.__y

    @y.setter
    def y(self, value):
        ''' sets the y attr '''
        self.__y = value
