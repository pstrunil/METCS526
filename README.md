# METCS526
All the assignements and homeworks are uploaded here for the BU MET CS 526 class.


**Problem 1:**


**HOW TO RUN:** Locate the directory with the code and test files then run: 
*python3 bst.py*. Example of outputs [see Example1.1].


As requested, the class Node is implemented. It was done like in the earlier homeworks. Class BST (Binary Sort Tree) is initialized with a root node and comes with its own getter and setter. 


The *add* function requires a recursive helper that takes in a node and a value. If the given value is smaller than that of the given node, then the function looks to the left and tries to add it there. Similarly, if the given value is larger than that of the given node, then the function looks to the right of the node. This recursion continues until we arrive to a position where the value of the node is exactly the provided value, or the node doesn't exist for that value, then the function makes a new node at that location in the tree. The actual *add* function simply runs this recursive helper at root node, with some given value.


The *find* function works similarly. Using a recursive helper, we traverse the tree seeing if the value of a given node is exactly equal to the provided value. If it is, then we return the node that we are at. If the value is smaller, run this function to the left node. Otherwise run it to the right. If we arrive to a leaf and still not find the value, we return none as there is no node with this value. The final *find* function utilizes this helper at root node with some given value.


The *delete* is a bit more complex requiring two helpers: one finding the smallest value and the recursive helper for delete. The method finding the smallest just requires recursing on the left branch, until we reach a node that has no left node. Then the delete method checks if there is a node in the tree, if there isn't then nothing to remove. Otherwise, similarly to the two previous methods, we use recursion to arrive to the leaf where the node with the given value should reside. If the right node is missing, return the left, and vice versa. (Since if that node only has one child, then we return its only child.) If the node has two children, then find the smallest node and use it as the replacement for the node that will be deleted. Then replace the value of the deleted node with the value of the replacement. Then reset the right of the node that will be deleted, the node that will be deleted with the value of the replacement to the right.


The *print* method prints "empty tree" if it is empty. Otherwise it just prints using Breadth First Search. If a node has only one child, the empty child will be represented by a "-" at each level.


Then the code generates a random set of numbers of size 5 to 50, with values 1 to 1000. Then prints the original BST. Then for two numbers not in the set, that are in the range above, we add them and print the updated tree. Then remove the numbers in the set from the tree and print the updated tree. Then we run find for one number in the set, one not in the set, to show that it will find one number successfully, then unsuccessfully.


**Problem 2:**


**HOW TO RUN:** Locate the directory with the code and test files then run: 
*python3 vowel.py vowel_input1.txt*. The output of different input files is shown in the example of outputs [see Example2.1].
**Note that this program requires the use of read_check.py to get a valid text input.**


First off we make the alphabet of the vowels encoded in morse: A `.-`, E `.`, I `..`, O `---`, U `..-`. The idea of this code is very similar to the tribonacci number problem we had in our previous homework. The answer for a longer input is built from the answers for the shorter ones. We let *ways* to be the number of was the first *i* symbols can be written as a sequence of vowels. The array has the length of the code + 1, so there is an entry for every position from 0 (before any symbol) to the end. All entries start at 0 except *ways[0]* = 1, since there is exactly one way to write nothing: with 0 vowels. For each position *i* from 1 to the end and for each vowel, we check whether the symbols just before position *i* are exactly the Morse code of that vowel. If they are, every way of writing the part before that vowel can be extended by it, so we can add *ways[i - length of vowel's code]* to *ways[i]*. Thus, the last entry *ways[n]* is the cumulative answer.


**Problem 3:**


**HOW TO RUN:** Locate the directory with the code and test files then run: 
*python3 longseq.py longest_seq1.txt*. The output of different input files is shown in the example of outputs [see Example3.1].
**Note that this program requires the use of read_check.py to get a valid text input.**


We want the longest sequence whose values and positions are strictly increasing, such that its elements alternate between elements of sequences *a* and *b*. The idea is similar to the problem above. Let *best_a[p]* be the length of the longest valid sequence that ends with the element at position *p* of *a*, and *best_b[p]* the same for *b*. Both start as arrays of 0 with the lengths of *a* and *b*. We go through the positions *p* from left to right. For *a[p]* we look at the positions *q* of *b* that come before *p*. From those, with *b[q] < a[p]*, we take the largest *best_b[q]* (0 if there is none) and set *best_a[p]* to that value + 1. The same is done for *b[p]* using *a*. The answer is the largest value in *best_a* and *best_b*.
