#!/usr/bin/python3
""" defines a Node class """


class Node:
    """
    This class defines a Node

    Attribute:
        data : setter / get data
        next_node: setter / get next data
    """

    def __init__(self, data, next_node=None):
        """
        Args:
            data(int): data to add to node class
            next_node: property seeter
        """
        self.__data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = data

    @property
    def next_node(self):
        return self.__next_node

    def next_node(self, value):
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """
    Attributes:
        sorted_insert: inserts a new node into the correct
        sorted position in the list (increasing order)
    """

    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        elif value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while (current.next_node is not None and
                   current.next_node.data < value):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """merge list and seperate using strip()"""
        temp = self.head
        display = ""
        while temp is not None:
            display += str(temp.data) + "\n"
            temp = temp.next_node

        return display.strip()
