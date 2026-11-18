import sys
from read_check import get_input_lines

class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent

class Heap:
    def __init__(self):
        self.root = None
        self.size = 0

    def __node_at(self, position): #locating the node with binary
        node = self.root
        for bit in bin(position)[3:]:
            node = node.left if bit == "0" else node.right
        return node

    def __sift_up(self, node): #swapping the nodes. Small goes up
        while node.parent is not None and node.value < node.parent.value:
            node.value, node.parent.value = node.parent.value, node.value
            node = node.parent

    def __sift_down(self, node): #swapping the nodes. Large goes down
        while True:
            smallest = node
            if node.left is not None and node.left.value < smallest.value:
                smallest = node.left
            if node.right is not None and node.right.value < smallest.value:
                smallest = node.right
            if smallest is node: #if not larger than either child, done
                return
            node.value, smallest.value = smallest.value, node.value
            node = smallest

    def __remove_last(self):
        last = self.__node_at(self.size)
        if last.parent is None:
            self.root = None
        elif last.parent.left is last:
            last.parent.left = None
        else:
            last.parent.right = None
        self.size -= 1
        return last

    def insert(self, value):
        self.size += 1
        if self.size == 1:
            self.root = Node(value)
            return
        parent = self.__node_at(self.size//2) #the parent of position p is position p//2
        new = Node(value, parent)
        if self.size% 2 == 0: #even positions are left children
            parent.left = new
        else:
            parent.right = new
        self.__sift_up(new)

    def peek(self):
        if self.root is None:
            raise IndexError("empty heap")
        return self.root.value

    def extract_min(self):
        if self.root is None:
            raise IndexError("empty heap")
        smallest = self.root.value
        last = self.__remove_last()
        if self.root is not None: #the last node's value takes the root's place and sinks down
            self.root.value = last.value
            self.__sift_down(self.root)
        return smallest

    def __find(self, node, value):
        if node is None or value < node.value:
            return None
        if node.value == value:
            return node
        return self.__find(node.left, value) or self.__find(node.right, value)

    def delete(self, value):
        target = self.__find(self.root, value)
        if target is None:
            return False
        last = self.__remove_last()
        if last is not target: #the last node's value fills the position, then moves up or down as needed
            target.value = last.value
            self.__sift_up(target)
            self.__sift_down(target)
        return True

    def build(self, values):
        self.size = len(values)
        self.root = self.__make(values, 1, None)
        self.__heapify(self.root)

    def __make(self, values, position, parent):
        if position > len(values):
            return None
        node = Node(values[position - 1], parent)
        node.left = self.__make(values, 2 * position, node)
        node.right = self.__make(values, 2 * position + 1, node)
        return node

    def __heapify(self, node):
        if node is not None:
            self.__heapify(node.left) #children first, so both subtrees are heaps before this node sinks
            self.__heapify(node.right)
            self.__sift_down(node)

    def __collect(self, node, values):
        if node is not None:
            values.append(node.value)
            self.__collect(node.left, values)
            self.__collect(node.right, values)

    def heap_sort(self):
        values = []
        self.__collect(self.root, values)
        copy = Heap()
        copy.build(values)
        result = []
        while not copy.is_empty():
            result.append(copy.extract_min())
        return result

    def is_empty(self):
        return self.root is None

    def __len__(self):
        return self.size

    def __draw(self, node):
        text = str(node.value)
        if node.left is None:
            return [text], len(text) // 2
        left, left_center = self.__draw(node.left)
        left_width = len(left[0])
        if node.right is None:
            rows = left
            slashes = {left_center + 1: "/"}
            middle = left_center + 2
        else:
            right, right_center = self.__draw(node.right)
            right_width = len(right[0])
            offset = max(left_width + 1, left_center - right_center + 4)
            rows = []
            for i in range(max(len(left), len(right))):
                a = left[i] if i < len(left) else " " * left_width
                b = right[i] if i < len(right) else " " * right_width
                rows.append(a + " " * (offset - left_width) + b)
            slashes = {left_center + 1: "/", offset + right_center - 1: "\\"}
            middle = (left_center + 1 + offset + right_center - 1) // 2
        start = middle - len(text) // 2
        shift = max(0, -start)
        width = max(len(rows[0]) + shift, start + shift + len(text), max(slashes) + shift + 1)
        slash_line = [" "] * width
        for column, mark in slashes.items():
            slash_line[column + shift] = mark
        lines = [" " * (start + shift) + text, "".join(slash_line)] + [" " * shift + row for row in rows]
        return [line.ljust(width) for line in lines], middle + shift

    def print_heap(self):
        if self.root is None:
            print("  (empty heap)")
            return
        lines, _ = self.__draw(self.root)
        for line in lines:
            print("  " + line.rstrip())

def parse_values(lines):
    text = " ".join(lines).replace("[", " ").replace("]", " ").replace(",", " ")
    return [int(word) for word in text.split()]

def main():
    try:
        values = parse_values(get_input_lines())
    except ValueError:
        print("Error: the input must be a list of whole numbers", file=sys.stderr)
        sys.exit(65)
    print("Input values:", values)
    heap = Heap()
    for value in values:
        heap.insert(value)
        print()
        print(f"After insert({value}):")
        heap.print_heap()

if __name__ == "__main__":
    main()