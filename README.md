# METCS526
All the assignements and homeworks are uploaded here for the BU MET CS 526 class.

**Homework 4:**

*Problem 1:*

Preorder is a depth first tree traversal and visits the nodes from right most to left most. So the sequence would look something like:

  A -> B -> E -> H -> F -> I -> C -> D -> G

A BFT visits every node by top down by visiting each level. (Going right first within the level is just a convention) The sequence will the be:

  A -> B -> C -> D -> E -> F -> G -> H -> I

Postorder traversal starts at the left most node and ends at the root, by visiting subtrees by level. So the visiting sequence will be

 H -> E -> I -> F -> B -> C -> G -> D -> A

 Inorder traversal visits the left most tree first starting at the left most node, going depth up. Then the visiting sequence will be
   G -> D -> E -> B -> A -> H -> I -> F -> C


*Problem 2:*
