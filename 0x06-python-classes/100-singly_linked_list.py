#!/usr/bin/python3
''' Module for Singly List '''

class Node:
    ''' defines a node of a singly linked list '''
    def __init__(self, data, next_node=None):
        ''' 
        Args:
            data: value of node
            next_node: address of the next node
        '''
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        ''' Retrievse data from node'''
        return self.__data

    @data.setter
    def data(self, value):
        ''' Sets new value of node's data
            Args:
                value: new data inserted
        '''
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        ''' Retrievse next node's address'''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        ''' Sets new value of node's data
            Args:
                value: new data inserted
        '''
        if not isinstance(value, Node) or next_node != None:
            raise TypeError("next_node must be a Node object")

class SinglyLinkedList:
    '''  defines a singly linked list '''
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        ''' Inserts a new node in a certain position.
            Args:
                value: new node
        '''


