from read_check import get_input_lines

class PriorityQueue:
    def __init__(self):
        self.__items = []

    def size(self): return len(self.__items)
    def is_empty(self): return len(self.__items) == 0

    def push(self, entry):
        items = self.__items
        child = len(items) #original size before adding entry
        items.append(entry)
        while child > 0:
            parent = (child - 1)//2 #depth of parent given the child's depth
            if items[child] < items[parent]: #if the value of child is less than the parent, swap them
                items[child], items[parent] = items[parent], items[child]
                child = parent #after values were swapped, child gets the parent's depth and vice versa
            else:
                break

    def pop(self): #remove and return the smallest entry
        items = self.__items
        if not items:
            raise IndexError("pop from an empty priority queue")
        smallest = items[0] #since sorted in the log
        last = items.pop() #the last entry is removed
        if items:
            items[0] = last #last entry takes the top spot
            parent = 0
            while True: #then swaps while a child is smaller
                left, right = 2 * parent + 1, 2 * parent + 2 #assigning the debth index to children
                smallest_child = parent
                if left < len(items) and items[left] < items[smallest_child]:
                    smallest_child = left #if the left of the parent is smaller than the parent, then left is the smallest child
                if right < len(items) and items[right] < items[smallest_child]:
                    smallest_child = right #same logic, but now with right
                if smallest_child == parent:
                    break
                items[parent], items[smallest_child] = items[smallest_child], items[parent]
                parent = smallest_child #then swap the positions of parent with the smallest child's and their values 
        return smallest


def merge_logs(logs):
    stacks = [log[::-1] for log in logs] #reverse the logs to pop of the end of the list
    queue = PriorityQueue()
    for register, stack in enumerate(stacks, start=1):
        if stack: #pairing the lowest time and the register number for each register
            queue.push((stack.pop(), register))

    merged = []
    while not queue.is_empty():
        time, register = queue.pop() #the smallest sale left anywhere
        merged.append((time, register)) #add the next lowest time and register to the output
        stack = stacks[register - 1]
        if stack: #register's next sale takes the popped sale's place in the queue
            queue.push((stack.pop(), register))
    return merged


def main():
    logs = []
    for line in get_input_lines():
        line = line.strip()
        if not line:
            continue
        inside = line.strip("[]")
        log = [int(elt) for elt in inside.split(",") if elt.strip()]
        logs.append(log)
    print("Registers: ", len(logs))
    print("Total sales: ", sum(len(log) for log in logs))
    print("Merged logs: ", merge_logs(logs))

if __name__ == "__main__":
    main()