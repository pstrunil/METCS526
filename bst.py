import random

class Node:
    def __init__(self, value, right = None, left = None):
        self.__value = value
        self.__left = left
        self.__right = right

    def get_value(self): return self.__value
    def get_left(self): return self.__left
    def get_right(self): return self.__right

    def set_value(self, value): self.__value = value
    def set_right(self, right): self.__right = right
    def set_left(self, left): self.__left = left


class BST:
    def __init__(self, root = None):
        self.__root = root

    def get_root(self): return self.__root
    def set_root(self, root): self.__root = root

    def add(self, value):
        self.__root = self.__add(self.__root, value)

    def __add(self, node, value):
        if node is None:
            return Node(value)
        if value < node.get_value():
            node.set_left(self.__add(node.get_left(), value))
        elif value > node.get_value():
            node.set_right(self.__add(node.get_right(), value))
        return node

    def find(self, value):
        return self.__find(self.__root, value)

    def __find(self, node, value):
        if node is None:
            return None
        if value == node.get_value():
            return node
        if value < node.get_value():
            return self.__find(node.get_left(), value)
        return self.__find(node.get_right(), value)

    def __smallest(self, node):
        if node.get_left() is None:
            return node
        return self.__smallest(node.get_left())
    
    def __delete(self, node, value):
        if node is None:
            return None
        if value < node.get_value(): #get to the node you want to delete
            node.set_left(self.__delete(node.get_left(), value))
        elif value > node.get_value():
            node.set_right(self.__delete(node.get_right(), value))
        else: #got to the node that needs to be deleted
            if node.get_left() is None: #if no left child, right takes its place
                return node.get_right()
            if node.get_right() is None: #same logic as above
                return node.get_left()
            successor = self.__smallest(node.get_right()) # if two children, then next larger value moves up to this node, then removed from where it was
            node.set_value(successor.get_value())
            node.set_right(self.__delete(node.get_right(), successor.get_value()))
        return node

    def delete(self, value):
        if self.find(value) is None:
            return False
        self.__root = self.__delete(self.__root, value)
        return True

    def print_tree(self):
        if self.__root is None:
            print("empty tree")
            return
        level = [self.__root]
        depth = 0
        while any(node is not None for node in level):
            print("Level " + str(depth) + ": " + " ".join("-" if node is None else str(node.get_value()) for node in level))
            next_level = []
            for node in level:
                if node is not None:
                    next_level.append(node.get_left())
                    next_level.append(node.get_right())
            level = next_level
            depth += 1


def show(bst, message):
    print(message)
    bst.print_tree()
    print()


def random_number(bst, in_tree): #will find numbers not yet in the tree to show how adding / finding works
    while True:
        number = random.randint(1, 1000)
        if (bst.find(number) is not None) == in_tree:
            return number


def main():
    values = random.sample(range(1, 1001), random.randint(5, 50))  # distinct numbers between 1 and 1000
    print("Input set: " + ", ".join(map(str, values)))
    print()

    bst = BST()
    for value in values:
        bst.add(value)
    show(bst, "Initial tree:")

    for _ in range(2): #add two numbers not yet in the tree
        value = random_number(bst, False)
        bst.add(value)
        show(bst, "Add " + str(value) + ":")

    for _ in range(2):  #deleting two numbers that are in the tree
        value = random_number(bst, True)
        bst.delete(value)
        show(bst, "Delete " + str(value) + ":")

    for in_tree in (True, False): #one successful and failed find
        value = random_number(bst, in_tree)
        print("Find " + str(value) + ": " + ("found" if bst.find(value) is not None else "not found"))


if __name__ == "__main__":
    main()