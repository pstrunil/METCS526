# METCS526
All the assignements and homeworks are uploaded here for the BU MET CS 526 class.


**Problem 1:**


**HOW TO RUN:** Locate the directory with the code and test files then run: 
*python3 bst.py*. Example of outputs (see Example1.1).


As requested, the class Node is implemented. It was done like in the earlier homeworks. Class BST (Binary Sort Tree) is initialized with a root node and comes with its own getter and setter. 


The *add* function requires a recursive helper that takes in a node and a value. If the given value is smaller than that of the given node, then the function looks to the left and tries to add it there. Similarly, if the given value is larger than that of the given node, then the function looks to the right of the node. This recursion continues until we arrive to a position where the value of the node is exactly the provided value, or the node doesn't exist for that value, then the function makes a new node at that location in the tree. The actual *add* function simply runs this recursive helper at root node, with some given value.


The *find* function works similarly. Using a recursive helper, we traverse the tree seeing if the value of a given node is exactly equal to the provided value. If it is, then we return the node that we are at. If the value is smaller, run this function to the left node. Otherwise run it to the right. If we arrive to a leaf and still not find the value, we return none as there is no node with this value. The final *find* function utilizes this helper at root node with some given value.


The *delete* is a bit more complex requiring two helpers: one finding the smallest value and the recursive helper for delete. The method finding the smallest just requires recursing on the left branch, until we reach a node that has no left node. Then the delete method checks if there is a node in the tree, if there isn't then nothing to remove. Otherwise, similarly to the two previous methods, we use recursion to arrive to the leaf where the node with the given value should reside. If the right node is missing, return the left, and vice versa. (Since if that node only has one child, then we return its only child.) If the node has two children, then find the smallest node and use it as the replacement for the node that will be deleted. Then replace the value of the deleted node with the value of the replacement. Then reset the right of the node that will be deleted, the node that will be deleted with the value of the replacement to the right.


The *print* method prints "empty tree" if it is empty. Otherwise it just prints using Breadth First Search. If a node has only one child, the empty child will be represented by a "-" at each level.


Then the code generates a random set of numbers of size 5 to 50, with values 1 to 1000. Then prints the original BST. Then for two numbers not in the set, that are in the range above, we add them and print the updated tree. Then remove the numbers in the set from the tree and print the updated tree. Then we run find for one number in the set, one not in the set, to show that it will find one number successfully, then unsuccessfully.


**Problem 2:**


**HOW TO RUN:** Locate the directory with the code and test files then run: 
*python3 vowel.py vowel_input1.txt*. The output of different input files is shown in the example of outputs (see Example2.1).


First off we make the alphabet of the vowels encoded in morse. The idea of this code is very similar to the tribonacci number problem we had in our previous homework. The key is to cumulatively add up the number of different ways a of morse can  be decomposed into different morse values. Starting by initializing the number of ways as an array of 0s with the size of the code + 1. This is because there is only 1 way to express the starting of the sequence (before any symbol "." or "-" is even placed).
Then we check between the second and the last positions and for letters in the alphabet, if the code of length of the letter is in the alphabet is equal to a letter in the alphabet, then we can add the number of ways to write that length with letters in the alphabet for that position. Then we return the last element of the array get the answer.


**Problem 3:**


**HOW TO RUN:** Locate the directory with the code and test files then run: 
*python3 longseq.py longest_seq1.txt*. The output of different input files is shown in the example of outputs (see Example3.1).


Here the idea is similar to the problem above. We define *best* as the sequence that satisfies the alternating property that we want. After making the placeholders as array of 0 of lengths *a* and *b* (the given sequences). Then for a position *p* over the longest sequence, if the position is less than the length of *a*. Set the initial best sequence is of length 0. Then for positions over the interval *p* to the length of *b*, if the value of *q*th position in sequence *b* is smaller than that of the *p*th position in sequence *a* and the length of the subsequence of *b* is larger than that of initial best sequence, then we can set that length to be  1 + the length of the initial best sequence. The we use the same logic if the position *p* is smaller than the length of *a*. Then we return the max of the best subsequence of *a* plus that of *b*.
