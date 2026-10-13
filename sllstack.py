from node import Node

class SinglyLinkedStack:
    def __init__(self):
        self.__head = None

    def push(self, value):
        self.__head = Node(value, self.__head)  #the new node points at the old top

    def is_empty(self):
        return self.__head is None
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Nothing to pop")
        top = self.__head
        self.__head = top.getNext()
        top.setNext(None)
        return top.getValue()

    def peek(self):
        if self.is_empty():
            raise IndexError("Nothing to peek at")
        return self.__head.getValue()

    def __list(self, node): #produces the list of contents in the stack
        if node is None:
            return []
        return self.__list(node.getNext()) + [node.getValue()]

    def to_list(self):
        return self.__list(self.__head)

    def __reverse_from(self, node):
        if node is None or node.getNext() is None: #empty or only 1 node
            return node
        new_head = self.__reverse_from(node.getNext()) #reverse everything after node first
        node.getNext().setNext(node) #reset the nodes to popint back
        node.setNext(None)
        return new_head
    
    def reverse(self): #reverses from head
        self.__head = self.__reverse_from(self.__head)