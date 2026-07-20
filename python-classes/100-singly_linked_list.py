#!/usr/bin/python3
"""Module that defines a singly linked list."""


class Node:
    """Defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve node data."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set node data."""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set next node."""
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list."""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new node in sorted order."""
        new_node = Node(value)

        if self.__head is None:
            self.__head = new_node
            return

        if value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head

        while (current.next_node is not None and
               current.next_node.data < value):
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """Print linked list."""
        values = []
        current = self.__head

        while current:
            values.append(str(current.data))
            current = current.next_node

        return "\n".join(values)
