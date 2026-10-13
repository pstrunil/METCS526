from arraystack import ArrayStack
from sllstack import SinglyLinkedStack
from dllstack import DoublyLinkedStack


def show(name, stack):
    for number in range(1, 11): #push 1 to 10
        stack.push(number)
    print(name)
    print("Before: " + ", ".join(map(str, stack.to_list()))) #prints the original sequnce
    stack.reverse()
    print("After: " + ", ".join(map(str, stack.to_list()))) #prints reversed sequence


def main():
    show("Array stack", ArrayStack())
    show("Singly linked list stack", SinglyLinkedStack())
    show("Doubly linked list stack", DoublyLinkedStack())


if __name__ == "__main__":
    main()