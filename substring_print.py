from read_check import get_input_lines
class Node:
    def __init__(self, value, right = None, left = None): 
        self.__value = value
        self.__left = left
        self.__right = right

    def get_value(self): return self.__value #getters
    def get_left(self): return self.__left
    def get_right(self): return self.__right

    def set_value(self, value): self.__value = value #setters
    def set_right(self, right): self.__right = right
    def set_left(self, left): self.__left = left

def is_inside(node, value): #checks if the value is already somewhere in the tree that starts at node
    if node is None:
        return False
    if value == node.get_value():
        return True
    if value < node.get_value():
        return is_inside(node.get_left(), value) #smaller values will be to the left
    return is_inside(node.get_right(), value) #bigger values be to the right

def insert(node, value): #places a value that isnt in the tree into its alphabetical place
    if node is None:
        return Node(value)
    if value < node.get_value(): #if smaller than the node value, go left and try insert again
        node.set_left(insert(node.get_left(), value))
    else:
        node.set_right(insert(node.get_right(), value)) #do the same, but now if its larger
    return node

def build_tree(str, root):
    if not str or is_inside(root, str): #empty or already recorded, then we are at root
        return root
    root = insert(root, str) #place the string alphabetically
    root = build_tree(str[:-1], root) #removes the last char
    return build_tree(str[1:], root) #same but with first

def traverse(node): #prints as it moves
    if node is None: #reached the end, nothing to add
        return 0
    printed = traverse(node.get_left()) #everything smaller goes first
    print(node.get_value())
    return printed + 1 + traverse(node.get_right()) #then bigger

def main():
    for line in get_input_lines(): #get the validated lines
        word = line.strip() #get rid of spaces
        if not word: #if empty line move on
            continue
        print(traverse(build_tree(word,None)))

if __name__ == "__main__":
    main()