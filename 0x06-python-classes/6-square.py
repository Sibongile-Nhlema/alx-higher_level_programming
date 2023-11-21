#!/usr/bin/python3
''' Module for the Square definition'''


class Square:
    ''' Defines a new square '''
    def __init__(self, size=0, position=(0, 0)):
        ''' Constructor.
        Args:
            size: width and height of the Square
            position: position of the square created
        '''
        if isinstance(size, int):
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        ''' Retrieves the private instance attribute size '''
        return self.__size

    @size.setter
    def size(self, value):
        ''' Sets the Size attribute.
        Args:
            value:size of new value of the square
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        ''' Retrieves the position of the square '''
        return self.__position

    @position.setter
    def position(self, value):
        ''' Sets the Positin attribute.
        Args:
            value: new value as a tuple with 2 elements
        '''
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    # moved area to after setter so that it uses updated values

    def area(self):
        ''' Calculates the area of Object Square.
        Return:
            the current square area
        '''
        return (self.__size * self.__size)

    def my_print(self):
        ''' Prints in Stdout the square with the character # '''
        if self.__size == 0:
            print()
        else:
            for k in range(0, self.__position[0]):
                print(" ")
            for i in range(self.__size):
                for j in range(1, self.__size):
                    print("#", end="")
                print("#")
