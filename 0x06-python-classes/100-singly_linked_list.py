#!/usr/bin/python3
""" file part for node class"""


class Node:
    """node class"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @property
    def next_node(self):
        return self.__next_node

    @data.setter
    def data(self, value):
        dataType = type(value)
        if dataType is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        nnodeType = type(value)
        if nnodeType is not None and not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


""" file part for singlylinkedlist class"""


class SinglyLinkedList:
    """Singly linked list class"""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        aux = self.__head
        while aux.next_node is not None and value > aux.next_node.data:
            aux = aux.next_node
        new_node.next_node = aux.next_node
        aux.next_node = new_node

    def __str__(self):
        existingNode = self.__head
        list = ""
        while existingNode is not None:
            list += str(existingNode.data)
            if existingNode.next_node is not None:
                list += '\n'
            existingNode = existingNode.next_node
        return list
