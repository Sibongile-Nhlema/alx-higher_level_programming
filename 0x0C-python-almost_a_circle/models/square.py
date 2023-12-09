#!/usr/bin/python3
''' Defines a Square '''
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    ''' Defines a square instance br inheriting from
        the Rectangle class
        Args:
            Rectangle: class it inherits from
    '''
    def __init__(self, size, x=0, y=0, id=None):
        ''' Initialises a square instance
            Args:
                size(int): the length of the edges
                x: x co-ordinates of the square
                y: y co-ordinates of the square
                id: the unque number given to the instance
        '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''prints a string representation of the square '''
        return "[{}] ({}) {}/{} - {}".format(Square.__name__, self.id,
                                             self.x, self.y, self.height)

    @property
    def size(self):
        ''' gets the width of the square '''
        return self.width

    @size.setter
    def size(self, value):
        ''' sets the size of the square '''
        self.width = value
        self.height = value

