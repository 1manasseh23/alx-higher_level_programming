#!/usr/bin/python3


"""
This Write a class Node that defines
a node of a singly linked list
"""


class Node:
    """
    Instantiation with data and next_node
     Attribute:
        data: Private instance attribute
        next_node: Private instance attribute
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node
    """
    property to retrieve
    Attribute:
        __data
    """
    @property
    def data(self):
        return self.__data
    """
    property setter to set
    Attribute:
        value
    """
    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value
    """
    property to retrieve
    Attribute:
        __next_node
    """
    @property
    def next_node(self):
        return self.__next_node
    """
    property setter to set
    Attribute:
        value
    """
    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""
This And, write a class SinglyLinkedList that
defines a singly linked list
"""


class SinglyLinkedList:

    """
    Simple instantiation should be printable
    Attribute:
        None
    """
    def __init__(self):
        self.head = None
    """
    Public instance method that inserts a new Node
    into the correct sorted
    Attribute:
        value
    """
    def sorted_insert(self, value):
        new_node = Node(value)
        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while (
                    current.next_node is not None and
                    current.next_node.data < value
                    ):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
    """
    This method is a special method It returns the
    string representation of the object.
    Attribute:
        self.head
    """
    def __str__(self):
        propst = []
        current = self.head
        while current:
            propst.append(str(current.data))
            current = current.next_node
        return '\n'.join(propst)
