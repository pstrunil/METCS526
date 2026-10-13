class ArrayStack:
    def __init__(self): #define it as an empty array
        self.__items = []

    def push(self, value): #push appends values
        self.__items.append(value)

    def is_empty(self):
        return len(self.__items) == 0
    
    def pop(self): #pop just uses pop to remove
        if self.is_empty():
            raise IndexError("Nothing to pop")
        return self.__items.pop()
    
    def peek(self):
        if self.is_empty(): #gives the last value added
            raise IndexError("Nothing to peek at")
        return self.__items[-1]

    def __list(self,i): #produces the list of the contents in the stack
        if i == len(self.__items):
            return []
        return [self.__items[i]] + self.__list(i+1)

    def to_list(self):
        return self.__list(0)

    def list(self):
        return list(self.__items)

    def __reverse_in(self, low, high): #swap the two ends, then everything in between
        if low >= high: # cant swap one or no elements.
            return
        self.__items[low], self.__items[high] = self.__items[high], self.__items[low]
        self.__reverse_in(low + 1, high - 1) #iterates on the next inner items
    
    def reverse(self):
        self.__reverse_in(0, len(self.__items) - 1)