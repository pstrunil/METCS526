from node import Node

class SinglyLinkedList:
    def __init__(self): #initialize the properties of the linked list
        self.__head = None
        self.__tail = None
        self.__count = 0

    def icheck(self, index, wend = False): #validate the index
        if not isinstance(index,int) or isinstance(index,bool):
            raise TypeError("Index must be an integer") #ensures the index is an integer
        upper = self.__count if wend else self.__count - 1 #necessary for insert since we can add at the end with it
        if index < 0 or index > upper: #ensures the index is a non-negative integer
            raise IndexError("Index out of bounds")
            
    
    def traverse(self, index):
        self.icheck(index) #sometimes we will have that this is called twice within the function, but its okay because it will for sure not be misused, but is only constant time, so wont make things more complex
        current = self.__head
        for _ in range(index):
            current = current.getNext()
        return current

    def __rm_at(self,index):
            if index == 0:
                rm = self.__head
                self.__head = rm.getNext()
                if self.__head is None: #sets the list to empty
                    self.__tail = None
            else:
                current = self.traverse(index - 1) #get to the node before the one you want to delete
                rm = current.getNext()
                current.setNext(rm.getNext())
                if rm is self.__tail: #removed last node
                    self.__tail = current
            rm.setNext(None)
            self.__count -= 1
            return rm.getValue()
    
    def append(self, val):
        newNode = Node(val) #creates a new node
        if self.__head is None: #then the list is empty and head and tail are the same
            self.__head = newNode #only something assigned to head, tail remains None
        else:
            self.__tail.setNext(newNode) #so that the node knows where the next node is
        self.__tail = newNode #so that the list knows where the tail is
        self.__count += 1

    def prepend(self, val):
        newNode = Node(val, self.__head)  # new node points at the old head
        self.__head = newNode
        if self.__tail is None:  # list was empty
            self.__tail = newNode
        self.__count += 1
   
    def insert(self, index, val):
        self.icheck(index, True) # checks the validity of index
        if index == 0:
            self.prepend(val)
        elif index == self.__count:
            self.append(val)
        else:
            current = self.traverse(index - 1) #traverse to the node before the index
            current.setNext(Node(val,current.getNext())) #points the current to a new node that itself has a val and points at the current's previous next
            self.__count += 1

    def get(self, index): #traverses until the index and returns the value at that index
        return self.traverse(index).getValue()

    def find(self, val):
        current = self.__head
        index = 0
        while current is not None: #traverse the list until you find the index with the associated value
            if current.getValue() == val:
                return index
            index += 1
            current = current.getNext()
        return -1

    def __len__(self):
        return self.__count

    def update(self, index, val): # traverses to get to the node at the index and changes its value
        self.traverse(index).setValue(val) 

    def delete(self, val):
        index = self.find(val) #no checks here since find does it for you
        if index == -1:
            return False
        self.__rm_at(index)
        return True

    def delete_at(self, index):
        self.icheck(index)
        return self.__rm_at(index)
    

    def print_list(self):
        current = self.__head
        if current is None:
            print("(empty)")
            return
        else:
            while current is not None:
                if current.getNext() is None:
                    print(current.getValue())
                    break
                print(current.getValue(), end = " -> ")
                current = current.getNext()