#!/usr/bin/python3
"""defines the class square"""


class Node:
    """represents the node"""

    def __init__(self, data, next_node=None):
        """data initialized"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """retrieve the data"""
        return self.__data

    @data.setter
    def data(self, value):
        """sets the data"""
        if type(value) != int:
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """retrieve that data"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """sets the next node"""
        if type(value) != Node and value is not None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """singly linked list"""

    def __init__(self):
        """linked list initialized"""
        self.head = None

    def __repr__(self):
        string = ''
        a = self.head
        while a:
            string += str(a.data) + '\n'
            a = a.next_node
        return string[:-1]

    def sorted_insert(self, value):
        """inserts a new node"""
        b = Node(value)
        a = self.head
        if a is None:
            self.head = b
            return
        if a.data > value:
            b.next_node = self.head
            self.head = b
            return
        while a.next_node is not None:
            if a.next_node.data > value:
                break
            a = a.next_node
        b.next_node = a.next_node
        a.next_node = b
        return
