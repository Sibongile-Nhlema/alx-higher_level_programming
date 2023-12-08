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
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
       ''' gets the height attr '''
       return self.__height

    @height.setter
    def height(self, value):
        ''' sets the height attr '''
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        ''' gets the x attr '''
        return self.__x

    @x.setter
    def x(self, value):
       ''' sets the x attr '''
       if type(value) != int:
           raise TypeError("x must be an integer")
       if value < 0:
           raise ValueError("x must be >= 0")
       self.__x = value

    @property
    def y(self):
        ''' gets the y attr '''
        return self.__y

    @y.setter
    def y(self, value):
        ''' sets the y attr '''
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        ''' defines area value of the Rectangle instance '''
        return self.__width * self.__height

    def display(self):
        ''' prints in stdout the rectangle instance '''
        for i in range(self.__height):
            for j in range(1, self.__width):
                print("#", end="")
            print("#")
