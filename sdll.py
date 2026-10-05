from node4 import Node

class SortedDoublyLinkedList:
    def __init__(self): #initialize the properties of the linked list
            self.__head = None
            self.__tail = None
            self.__count = 0

    def add(self, val):
        newNode = Node(val)
        
        if self.__head is None: #if list is empty add the node
            self.__head = newNode
            self.__tail = newNode

        elif val < self.__head.getValue(): #if the value is less than the first element
            newNode.setNext(self.__head) #newnode points to current head
            self.__head.setPrev(newNode) #current head points back at newnode
            self.__head = newNode #make new node the new head

        elif val >= self.__tail.getValue(): #same idea as above, but now with tail
            newNode.setPrev(self.__tail)
            self.__tail.setNext(newNode)
            self.__tail = newNode
        
        else: #takes on a middle value
            prior = self.__head
            while prior.getNext().getValue() <= val: #cycle through values until you find one that is larger than val
                prior = prior.getNext()
            following = prior.getNext() #set the following node to be the one thats just above the value (we found it with the cycle)      

            newNode.setPrev(prior) #set up the pointers so that the newnode points at the prior and following nodes and those point back at newnode
            newNode.setNext(following)
            prior.setNext(newNode)
            following.setPrev(newNode)

        self.__count += 1

    def delete(self, val):
        if self.__head is None: #if the list is empty, nothing to remove
            return False
        
        elif val < self.__head.getValue() or val > self.__tail.getValue(): #if the value is outside the list bounds, nothing to remove
            return False

        else:
            current = self.__head
            while current.getValue() != val: #cycle through until you find a node equal to that value
                if current == self.__tail: #if none are equal and you cylced to the end, then nothing to remove
                    return False
                current = current.getNext()

            prior = current.getPrev() #get the neighbors to reset pointers
            following = current.getNext()

            if prior is None: #means that current is the head, so node after is is the new head
                self.__head = following
            else: #otherwise proceed as normal and just set the prior to point at the following
                prior.setNext(following)

            if following is None: #means that the current is tail, so node prior to it is the new tail
                self.__tail = prior
            else: #otherwise proceed as normal and make the following point back at the prior
                following.setPrev(prior)

            current.setNext(None) #reset the current pointers to None
            current.setPrev(None)
            
            self.__count -= 1
            return True

    def __find(self, node, val):
            if node is None:
                return False
            elif node.getValue() == val:
                return True
            elif node.getValue() > val:
                return False
            return self.__find(node.getNext(), val)
    
    
    def exists(self, val):
        return self.__find(self.__head, val)

    def __printer(self, node):
        print(node.getValue(), end= "") #prints the node's value
        if node.getNext() is not None: #if its not the last term, prints arrows and sees how to print the next
            print(" <-> ", end = "")
            self.__printer(node.getNext())
    
    def print_list(self):
        if self.__head is None: #if empty list
            print("(empty)")
        else: #uses printer from head
            self.__printer(self.__head)
            print()

    def __sigma(self, node): #like the sigma notation we just add the current term to the next
        if node is None:
            return 0
        return node.getValue() + self.__sigma(node.getNext())
    
    def total(self):
        return self.__sigma(self.__head)

    def __counter(self, node, val):
        if node is None or node.getValue() > val: #if are out of bounds
            return 0
        if node.getValue() == val: #matches the value and keeps continues to add
            return 1 + self.__counter(node.getNext(), val)
        return self.__counter(node.getNext(), val) # if value is smaller than val, continues walking
    
    def count(self, val):
        return self.__counter(self.__head, val)

    def __getMiddle(self):
        current = self.__head
        mid = self.__count//2
        if self.__count%2 == 0:
            for _ in range(mid-1):
                current = current.getNext()
            return [current,current.getNext()]
        for i in range(mid):
            current = current.getNext()
        return [current]
    
    def median(self):
        if self.__count == 0:
            raise ValueError("No median in an empty list")
        middle = self.__getMiddle()
        if len(middle) == 1:
            return middle[0].getValue()
        return (middle[0].getValue() + middle[1].getValue()) / 2 #finds the value in the middle be it even or odd and divides it by its legnth

    def sum_middle_three(self):
        if self.__count < 3:
            raise ValueError("Needs at least 3 nodes")
        middle = self.__getMiddle()
        first = middle[0]
        if len(self.__getMiddle()) == 1:
            return first.getPrev().getValue() + first.getNext().getValue() + first.getValue()
        return first.getPrev().getValue() + first.getValue() +middle[1].getValue()