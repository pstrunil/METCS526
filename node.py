class Node:
    def __init__(self, val, nextNode = None): 
        self.__value = val
        self.__next = nextNode

    def getValue(self): return self.__value #getters
    def getNext(self): return self.__next

    def setValue(self, setvalue): self.__value = setvalue #setters
    def setNext(self, setnext): self.__next = setnext