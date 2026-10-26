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


**HOW TO RUN:** Locate the directory with the code and test files then run:
*python3 smallestNumber.py <TestFilename>.txt*


**For examples of the output see Example2.1.png and Example2.2.png**


The tasks provides a list of elements and a target value. It then asks to find the lowest amount of elements that sum to a value that is larger than the target value.


The algorithm then takes the values, ensures that the problem is well-specified. That is, the input is readable, it then ensures that there are at least three input lines. Then it ensures that the count > 0, target and the values are integers, such that, the sum of the elements are larger than the target. Once the set up is confirmed, it sorts the values and adds the largest values together, while that sum is smaller than the target. Each iteration of the loop is counted and the result is the final count.

*Problem 3:*


**HOW TO RUN:** Locate the directory with the code and test files then run:
*python3 rightTriangles.py <TestFilename>.txt*


**For examples of the output see Example3.1.png, Examples3.2.png and Example3.3.png**


The task provides a list of points and asks us to find the number of right triangles that are created by these points.

The algorithm ensures that the provided values are well-specified. That is, the input is readable, it checks that the input is non-empty; the number of points provided > 0 and the coordinates themselves are integers; the number of points coincides with the actual number of points provided; the number of coordinates per point is exactly 2; and that the points are distinct.


The algorithm requires a few parts. The first is finding the generating vector. In particular, it finds vectors that identify points lying on the same line. That is the points (2,4), (-1,-2) and (1,2) really lie on the same line. The values get scaled to a single generating vector (1,2). (Done by the *generator* function)


Moreover, the algorithm uses a dictionary with a key being the generating vector and the value it stores is originally 0, but if we find another vector that has the same generating vector, then it adds 1 to the value in the dictionary assigned to the generating vector.


Once the inputs pass the verification step explained above, it takes any fixed point from the set of points, call it the corner point, and creates an empty dictionary. Then for any point in the set is finds the difference vector between the corner point and any other point in the set. If the difference is 0, we ignore it (since we just compare the corner point to itself). It finds the generating vector of the difference vector and increases the value of that generating vector in the dictionary by 1.


After the dictionary was updated for all points with respect to the corner, for each element of the dictionary, the algorithm sets its orthogonal (that is if the generating vector is (a,b), its orthogonal is (-b,a) as (a,b)*(-b,a) = 0). It compares the generator pair and orthogonal pair values. By checking if the first coordinate of the generator is smaller than that of the orthogonal, if so, it is true. If they are equal, it compares the second coordinates. If generator is "smaller" than the orthogonal, then the number of triangles is increased by the value in the dictionary of associated to the generating vector, times the value associated to the orthogonal vector. 


This is a way to eliminate double counting when finding the total number of triangles. Suppose we have 2 points that have a generating vector (1,0) and 3 that have its orthogonal (0,1). Then (1,0) < (0,1) fails, but (0,1) < (1,0) passes and the total is increased by 2*3. Therefore, it only count the pairs once. The increase in the number of triangles is given by that product, since each point on a line can connect to the points on the orthogonal line to form a right triangle. The algorithm then sets each point as the corner point, thus running the previous section for all points.


The final time complexity of the algorithm is O(n^2log(m)). The verification step already sets us to O(n). Gdc has a complexity of O(log(m)), where m is the largest coordinate difference. Since we run it for each corner and for each point, we then get that our final time complexity is O(n^2log(m)). The brute force method is O(n^3).
