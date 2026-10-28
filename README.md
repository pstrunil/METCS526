# METCS526
All the assignements and homeworks are uploaded here for the BU MET CS 526 class.

***MIDTERM:*** Note that all the code assumes a well specified input for the code. Furthermore the algorithms used programs from previous homeworks, in particular, read_check.


**Problem 1:**


**HOW TO RUN:** Locate the directory with the code and test files then run: 
*python3 snowfall.py snowfall_input1.txt*. Note that different input files could be used as seen in the example of outputs (see Example1.1).


Since the snowfall is cumulative, to find the snowfall of three consecutive days, we take the difference between the current day and one that was three days ago. Then to see if its larger than half of the total snowfall, we take the last snowfall day in the set and divide it by two. Note that if there are fewer than 3 days, then the output will necessarily be false. This is also the reason behind why the loop starts at day three, rather than the first day. The loop returns true if the condition above is satisfied and false if the condition is never satisfied.


The program then gets the lines using the read_check program, fixes ensures that each line can be worked with, obtains the values from the lines 1 onwards, then runs the algorithm on the values, to obtain the result.


**Problem 2:**


**HOW TO RUN:** Locate the directory with the code and test files then run: 
*python3 pandemic.py pandemic_input1.txt*. Note that different input files could be used as seen in the example of outputs (see Example2.1).


The algorithm is initialized with a set of infected counties and a size of the column n. Begin by initializing the directions in which neighbors are, which is to the right; left; above; below, the current position. 


The heart of the algorithm requires an originally empty dictionary and a while loop. The list called "today", identifies the set of infected counties as of the current iteration. It gets initialized with the patient zero set given by the input. While the set today is not empty, the loop will run over the elements in today's set. The set tomorrow is initialized as empty in the beginning of the loop. Then using nested for loops the algorithm iterates over the coordinates of the counties in the infected today set and over the directions of neighbors. 


If the county which is a neighbor of the infected county is within the bounds of the grid and not in already infected set, it gets added to the dictionary and is increased in value by 1. If through out the nested for loops, the county reaches a value of 2, it will be added to the set of counties that will be infected tomorrow. 


The set of all infected counties gets updated with the newly infected counties and the set of today's infections will be reinitialized as the set of newly infected counties, so that the next iteration will be on the newly infected counties. 


As mentioned prior, if all the counties have been infected, then there are no more counties to infect and tomorrows's set will be empty, thus the while loop exits with the set of all infected counties. If the infection stops due to the structure of the patient zeros, then tomorrow's set will also be empty and the loops exits with the same set described above. If the size set of infected counties is equal to the size of the grid, then all the counties have been infected. Otherwise, there are some healthy counties left.

The program then gets the input lines with read_check, formats them accordingly and gets the dimension of the board. Then makes a set of patient zeros, (since that set will be continuously worked on as the infected set, so all the changes must be recorded. Then, gets the points form line one onwards and sets the coordinates into the patient zero set. Then the algorithm is run on the board of size n and the patient zero set, to obtain the final result.

**Problem 3:**


**HOW TO RUN:** Locate the directory with the code and test files then run: 
*python3 sudoku.py puzzle_game_input1.txt*. Note that different input files could be used as seen in the example of outputs (see Example3.1).


The first part of the algorithm makes a dictionary of with each key being one of n symbols that are given in the puzzle. The value is the coordinates of the symbol, that is the row and column of the symbol. It then reads through the board by row and column in the row. If the element is a ".", it is skipped as it is considered empty. 


If the board contains an element that isn't a key in the dictionary, then the board is considered invalid. Then for each symbol make its position into three lists: the row, the column and the quadrant number. The quadrant is the splitting of the grid into smaller grids, of sizes square root of n, call it k. So the quadrant coordinate will be the row-quadrant coordinate times k, plus the quadrant column coordinate. That way we can order the whole grid into unique quadrants for a valid board.


Then for each triple defined above, we check if for each triple the size of the set of that triple is equal to the size of that triple. This will tell us if there exist repeats in the list. As the triple will first check the symbols appearances in rows, then columns then quadrants. If for any element of the triple, the set size is smaller than the list size for any symbol, then the board will be invalid. Otherwise we return true.


Then the program takes the input lines via the read_check program, gets the dimension of the grid, (since the grid is a square), gets the symbols and sets the board to be empty. Then fills in the board row by row and checks if the board is valid.
