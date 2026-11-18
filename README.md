# METCS526
All the assignements and homeworks are uploaded here for the BU MET CS 526 class.


**Problem 1:**


**HOW TO RUN:** Locate the directory with the code and test files then run: 
*python3 logs.py merge_input1.txt*. Example of outputs [see Example1.1 through Example1.3].


The main idea is to recognize that the smallest sale not yet merged is always the first unused sale of some register, because every log is already sorted. So the next sale of the merged log is the smallest of the k front sales, and there is no need to look at the rest of the logs.


The algorithm is to firstly turn each log into a stack with its earliest sale on top (the log is reversed, so pop() takes the earliest sale). Then the first sale of every non-empty register goes into my priority queue as a pair (time, register). Pairs compare by time first, then by register number, so a tie on time goes to the lower register, as required. Lastly, repeat until the queue is empty. That is, remove the smallest pair, append it to the merged list, then pop the next sale of that same register (if it has one) and put it in the queue.


The priority queue is a binary min-heap stored in a list. *push* adds the entry at the end and moves it up while it is smaller than its parent. *pop* returns the root, moves the last entry to the root and moves it down while a child is smaller.


**Problem 2:**


**HOW TO RUN:** Locate the directory with the code and test files then run: 
*python3 heap.py heap_input1.txt*. Example of outputs [see Example2.1 through Example2.9].


The heap is a binary tree of linked nodes. Each node holds a value and references to its left
child, right child and parent. Keeping the heap order (every node is less than or equal to its children) and complete shape (every level is full except the last, which fills from the left). The heap also keeps a count of its nodes.


The positions are found using the python built in binary method. Which returns the binary of something, in our case it is position of the node in the tree. Positions are numbered from 1 in level order. The binary digits of a position after the leading 1 give the path from the root (0 = left, 1 = right). The next free spot is position size *+ 1* and the last node is position size, so both are found by walking at most *log(n)* steps. The parent of position *p* is position *p//2*.


The methods that were asked to be implemented are:


*insert*: Attaches a new node at position size + 1, then swaps up (swap values with the parent while strictly smaller than it).


*peek*: Return the root's value (IndexError if empty).


*extract_min*: Remember the root's value, cut off the last node, put its value in the root and swap down (swap with the smaller child while a child is smaller). IndexError if empty.


*delete*: Search for a node with the value (a subtree whose root is already bigger than the value is skipped). If none, return False. Otherwise cut off the last node, copy its value into the found node, then swap up and swap down (it may need either, since it came from another branch). Note that both are implemented here since, swap up fixes a value that is too small for its place, like a new insert at the bottom. While swap down fixes a value that is too big for its place, like the last value moved to the root.


*build*: Make a complete tree from the list, then swap down every node from the bottom up.


*heap_sort*: copy the values into a new heap with build, then extract the minimum until it is empty.


*is_empty* and *__len__*: the root is None  and the node count.


*print_heap*: draws the tree with the root at the top and a / or \ above each child.


**Problem 3:**


**HOW TO RUN:** Locate the directory with the code and test files then run: 
*python3 median.py median_input1.txt*. Example of outputs [see Example3.1 through Example3.2].


The main idea is to use two heaps. The heap from the previous problem [See heap.py] to achieve that. The *upper* heap is a normal min-heap holding the larger half of the sales so far. Its root is the smallest of the larger half. The *lower* heap is the smaller half of the sales so far. A min-heap can act as a max-heap if every value is stored negatively, so lower stores -sale. Its root then gives the largest of the smaller half.


The main idea of the algorithm is to add the number into either lower or higher heap. Since they are kept in a way where the *lower* will have a largest number as its root, then the *upper* will have the smallest value as its root, we can *peek* at the *lower* when we added an odd number of elements so far and take the average of the *peek* of both the *lower* and *upper*. More precisely, for each new sale, if *lower* is empty or the sale is at most the largest of *lower*, insert it into *lower*, but negated. Otherwise insert it into *upper*. Then, if lower is two bigger than *upper*, move *lower's* root to *upper*. If *upper* is bigger than *lower*, move *upper's* root to *lower*. Then record the median from the roots.
