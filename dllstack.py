from node4 import Node


class DoublyLinkedStack:
    def __init__(self):
        self.__head = None #bottom of the stack
        self.__tail = None #top of the stack

    def push(self, value):
        node = Node(value, None, self.__tail) #points back at the old top
        if self.__tail is None:  #first element is both bottom and top
            self.__head = node
        else:
            self.__tail.setNext(node)
        self.__tail = node

    def is_empty(self):
        return self.__head is None
   
    def pop(self):
        if self.is_empty():
            raise IndexError("Nothing to pop")
        top = self.__tail
        below = top.getPrev()
        if below is None:  #that was the only element
            self.__head = None
        else:
            below.setNext(None)
        self.__tail = below
        top.setPrev(None)
        return top.getValue()

    def peek(self):
        if self.is_empty():
            raise IndexError("Nothing to peek at")
        return self.__tail.getValue()

    def __list(self, node): #produces the list of contents in the stack
        if node is None:
            return []
        return [node.getValue()] + self.__list(node.getNext())

    def to_list(self):
        return self.__list(self.__head)
    
    def __swapLinks(self, node):
        if node is None:
            return
        following = node.getNext() #remember the old next
        node.setNext(node.getPrev()) #set the next to point at previous
        node.setPrev(following) #set the previous to point at the old next
        self.__swapLinks(following) #do this for all follwoing nodes
    
    def reverse(self):
        self.__swapLinks(self.__head) #the old top is now the bottom, and vice versa
        self.__head, self.__tail = self.__tail, self.__head