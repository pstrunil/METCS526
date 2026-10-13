# METCS526
All the assignements and homeworks are uploaded here for the BU MET CS 526 class.

**Homework 3:**

***Run:***

&nbsp;&nbsp;&nbsp;&nbsp;locate the directory, then run "python3 plaindrome.py filename.txt"
&nbsp;&nbsp;&nbsp;&nbsp;< also works if you want it as stdin. filename.txt is placeholder for instrunctions.
&nbsp;&nbsp;&nbsp;&nbsp;


**Problem 1:** (see: palindrome.py and read_check.py)

This question requires us to construct a palindrome checker, that intakes lines and spits out a sequence of True or Falses as well as the number of True statements.

After noticing a pattern of having to read inputs, I just decided to make a standalone program that checks the validity of a text file and gives out the lines. (See read_check.py). This is pretty much the same checking method I used in the previous homeworks, but this time made into a single file. I also added the case where we read from source, the case where the file name isn't given. Specifically stdin will be read as raw bytes, then decoded into a uft-8 string and split into a list of individual lines. This is done because the usual stdin.readlines() method replaces bytes it can't decode with ones that it can. So to avoid it, we use the utf-8 as it's the global standard for text data and we should be able to read the file. If it does't pass this check, it fails and exists. From now on, this will be used for any future text file validation.

Now onto the actual task at hand. the palindrome checker works rather simply (see palindrome.py). Using the read_check program we obtain a list of lines. To ensure that it runs properly, we strip the list of any empty lines. Then for each non-empty line we remove spaces within the word. Then over the range from first to the middle we compare the chars at positions i and last position -i. (So if i is the first position and n is the last, then we compare char at first position and last position, then second and last position -1 etc.) If any two are different we flag it as not a palindrome, otherwise it is. Thus, we can make an array of booleans and print them out as well as the sum of the True statements.


**Problem 2:** (see substring_print.py and read_check.py)

***Run:***

&nbsp;&nbsp;&nbsp;&nbsp;locate the directory, then run "python3 substring_print.py filename.txt"
&nbsp;&nbsp;&nbsp;&nbsp;< also works if you want it as stdin. filename.txt is placeholder for instrunctions.

This question asks us to find every consecutive substring of a string, then print all of them and say how many strings were there. This has to be recursive.

I was thinking for a bit about this. My first approach was to just make an actual function that would do it. However, I realized I could just traverse a tree recursively from left to right and print it out like that (see substring_print.py). First we have to actually make the tree. I started off with making a Node class that has a value and pointers to left and right nodes, as well as the setters and getters. To construct the tree, I start at a string. Check if the string has something and if it doesn't I don't do anything. If it does, I add it to the visited set of nodes and make a node with the value of the string. I set it's left pointer to a subtree with a substring that is missing its last element, then set its right pointer to a subtree with a substring thats missing its first element. This way I get a binary tree and each leaf will be just one letter and all the branches will be that string missing either left or right. Since we start with a non-empty string, we get that the root is set to be the original strign we gave, then the right child will be missing the first letter and the left child will be missing the last, those will have a similar structure. I return node, since, as said before that will be the root of the tree that has all of its pointers set up to point at its respective subtrees.

&nbsp;&nbsp;&nbsp;&nbsp;To traverse it, I will start at a node, then if its empty, I do nothing. Otherwise, I will add it to a set of nodes that we found. Then I will call the same function, but start to the right of the node and to the left. That way all of children of the root will be found.

&nbsp;&nbsp;&nbsp;&nbsp;Then, I get the string using read_check and strip it to get rid of spaces. If it is an empty line I skip it. Set the root by building out the tree and the found set will be just an empty set that will be filled out by traversing the set. After we sort it alphabetically, we print each substring out and at the end the length of the set found.

&nbsp;&nbsp;&nbsp;&nbsp;In conclusion we completely recursively construct a tree of substrings. We recursively traverse it to make a list of all the substirngs. After sorting them we print each one out.


**Problem 3:** (see node4.py; node.py; arraystack.py; sllstack.py; dllstack.py; stack_reversal.py)


***Run:***
&nbsp;&nbsp;&nbsp;&nbsp;locate the directory, then run "python3 stack_reversl.py"


We are tasked with running a recursion on an implementation of a stack. Implementation via array, singly linked list and doubly linked list. Each must support particular methods and reverse the stack in place.



*Array:* (see arraystack.py)

&nbsp;&nbsp;&nbsp;&nbsp;I begun by making a class ArrayStack that contains items (by default an empty array).
Push appends the array


is_empty inspects the length of the array, if its 0, then its empty.


pop checks if the stack is empty. If it is, then nothing to remove or return. Otherwise, it pops the array.


peek checks if its empty, since if it were to be, then nothing to look at. Otherwise just returns the last item in the array, since the last element added is located at the back.


to_list is a method I implemented to actually list out the stack for the output. It works via a recursive helper that takes an index and if the index is at the end of the array we return an empty array. If it isn't, then we return an array with the item at that index and add the next index by calling the function but at the following adjacent index. (Think of it as like a recursive summation.)
&nbsp;&nbsp;&nbsp;&nbsp;Then to_list just sets the index at 0 and call the recursion for the whole list. We, thus, end up with an array of all the items.


reverse function has the same logic as the list, in terms of recursion. The helper takes 2 ends of the array (so 2 indices). If the value at the lower end is larger or equal to the one at the higher end, we return nothing. Otherwise we swap the positions of these values. Then the function calls itself, but now with positions, one above the lower end and one below the higher end. Then the reverse function just starts at index 0 and ends with the last index.


*Singly Linked List:* (see sllstack.py)
&nbsp;&nbsp;&nbsp;&nbsp;Note: I will refer to singly linked list as sll


The elements will be added to the front of the sll list.


We begin by initializing the class Node (which was reused from the previous homework (see node.py)). Then initialize the sll class with a head.


push just sets the head node to the node with value and a pointer to the previous head.


is_empty tells us if the head is a null pointer.


pop checks if the list is empty, then sets the top to a temporary variable ('old' head), sets the current head as the next node of the temporary variable, sets the old head to none and returns the value of the new head.


peek checks if the list is empty, then returns the value of the head of the list, since that's where the newest addition of the stack is.


to_list is identical in logic to the to_list of the array stack, but now just done with the helper that starts at a node, rather than an index and returns an array of elements. Important difference, is that since stacks are LIFO, then we need to call the recursion first before we add the element (as the value 1 is actually stored at the tail). So by calling the recursion first we end up adding the tail value to the beginning of the array first and the head last, as the addition after recursion gets called is executed last.
&nbsp;&nbsp;&nbsp;&nbsp;Then to_list calls the helper function and starts at head.


reverse calls the helper, similarly to the array stack. It takes in a node. First it checks if it the list has 0 or 1 nodes (since in those cases, there is nothing to do). Then we call the reverse from method until we reach the base case. Since 1 is at the end of the list, we just leave it as is. On nodes with values 1 and 2, we make 1 point at 2, then set 2 to point to nothing. Then we look at nodes with values 2 and 3. We make 2 point at 3 (since we have already freed up the 2 pointer), then make 3 point at nothing. We repeat this process until we get to 9 which will be set to point at 10, then 10 will be pointing at nothing. Thus we have successfully reversed the list. The actual reverse function just calls reverse from head.


*Doubly Linked List:* (see dllstack.py)

&nbsp;&nbsp;&nbsp;&nbsp;Note: I will refer to singly linked list as dll


Now the new elements will be added at the back of the dll.


The set up starts with us using the node class which I made for a previous homework (see node4.py).


Defining the dll class is done by setting the head and the tail to none.


push takes makes a new node with a value and a single pointer that points to the tail of the list. If the tail is none, then the list is empty and we just set the head to be the node with that value. Otherwise, we set the old tail to point at the new node and set the set the new tail to be the node. We can do that since we have a dll so we can work with the tail, without traversing to it.


is_empty is identical to the sll.


pop checks if its empty. Makes temporaries for the tail and element before the tail. If tail was the only element, then we set head to none, since we just remove that one node. Otherwise, we set the penultimate node to point at nothing, new tail to be this penultimate node and set the old tails pointer to nothing, then return the value of the new tail.


peek checks if the list is empty. Then returns the value of the tail.


listing is a mix of array and sll. Like in sll we traverse over the nodes, but like in array, we first return the value of the current node, then run the recursion, since again, we add the new element to the back of the list.


reverse uses a recursive helper. This helper takes in a node, if its empty, then return nothing. We take the node and take its next adjacent. We make the node next-pointer to point at the previous adjacent and its past-pointer point at the next adjacent. (Even though its pointing 2 ways going forward and backwards have different implications, its not the same as just moving somewhere). We then do this procedure with the next adjacent node.

&nbsp;&nbsp;&nbsp;&nbsp;Once the helper has been established, we start swapping at the head and travel to the tail then we reset the head and tail of the list to be the inverse.


*Stack Reversal:* (see stack_reversal.py)


We import the 3 classes that we have made and then show them. Since they all share a to_list and reverse methods, we can just call those shared methods.
&nbsp;&nbsp;&nbsp;&nbsp;We load the stacks with numbers 1 through 10, then print using the list method. This ensures that even though our stack implementation has added these numbers to the stack in different ways, the output will be the same. Then reverse them, keeping their individual structures. We then show how the output looks for each one.



**Problem 4:** (see ghostbusters.py)


***Run:***

&nbsp;&nbsp;&nbsp;&nbsp;locate the directory, then run "python3 ghostbusters.py"


What the problem really wants from us is to check if the lines are parallel or not, and if they are parallel, then they are distinct. This makes everything much clearer. It is well known that if 2 lines are parallel, then their cross product will be 0. This will be our main method of verification. The hard part was to realize what to do when a 2 pairs of ghostbusters and ghost were collinear. However, this can be done by looking at an arbitrary vector between a ghost and ghostbuster and the vector position of another ghostbuster. Since the cross product of those, will give a value and it will be unique. If there are 2 such ghostbusters where their vector positions give the same value with the vector between a ghostbuster and a ghost, this will mean that they stand somewhere on the same line. This means that we have to check for each vector between ghostbuster and ghost.


Understanding all of that, gives the key to the solution. First we define and 2 dimensional cross product and with that a method is_parallel, as explained above.

&nbsp;&nbsp;&nbsp;&nbsp;Then, we ensure that the input is correctly formatted. That is that the coordinate of a buster comes first, then the ghost and that their coordinates are of the right dimensions, are integers, and that a ghost and ghostbuster do not share a location. This function will the do two things; output the vector between the ghostbuster and the ghost (from the coordinates), and the position of the buster (since we need it to check the collinearity condition).

&nbsp;&nbsp;&nbsp;&nbsp;elimination will take an arbitrary vector (I simply picked the first one) between the first ghostbuster and ghost. Then we check if any other vector, from the list of coordinates that we got, is nonparallel, if it isn't, we already know that all ghosts wont be eliminated in one shot. However, if that pair of ghostbuster and ghost are parallel, we don't yet move onto the next pair. We calculate the residual between the first vector and the vector position of any other ghostbuster, and add it to a checked array. If there are at least 2 any other vectors that have the same residual, we know that all the ghosts won't be eliminated in one shot (as described above). After all of that, we will have a value, wither true or false for the situation that we are in.

The main just gets the lines (again see read_check), strips them of any empty lines, and sees if there are any more lines left. It then checks if the number of pairs is a positive integer, corresponding to the actual number of pairs. Then using the methods above, it makes the vectors between the pairs of ghostbusters and ghosts, as well as, recording the vector positions of the busters and prints whether or not the ghosts were eliminated or not. All the errors are caught at the end. 
