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

def build_tree(str, visited):
    if not str or str in visited: #nothing to add or the substring already has a node
        return None
    visited.add(str)
    node = Node(str) #set up the root
    node.set_left(build_tree(str[:-1], visited)) #make things left of it one letter off the end
    node.set_right(build_tree(str[1:], visited)) #make things right of it one letter off the start
    return node

def traverse(node, found):
    if node is None: #if no node, then nothing to add to the found collection
        return
    found.append(node.get_value()) #if there is, then we record it
    traverse(node.get_right(), found) #then traverse to the right of the node and do that for each branch
    traverse(node.get_left(), found) #same idea, but now going left

def main():
    for line in get_input_lines(): #get the validated lines
        word = line.strip() #get rid of spaces
        if not word: #if empty line move on
            continue
        root = build_tree(word, set()) #set up the tree with the string and an empty set
        found = []
        traverse(root,found) #traverse the tree

        for sstr in sorted(found): #once we sort the tree we get our out
            print(sstr)
        print(len(found)) #get the number of nodes

if __name__ == "__main__":
    main()