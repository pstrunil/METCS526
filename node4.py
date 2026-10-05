class Node:
    def __init__(self, val, next = None, prev = None): 
        self.__value = val
        self.__next = next
        self.__prev = prev

    def getValue(self): return self.__value #getters
    def getPrev(self): return self.__prev
    def getNext(self): return self.__next

    def setValue(self, setvalue): self.__value = setvalue #setters
    def setNext(self, setnext): self.__next = setnext
    def setPrev(self, setprev): self.__prev = setprev