# METCS526
All the assignements and homeworks are uploaded here for the BU MET CS 526 class.

**Homework 2**

**Problem 1:**
The advantage of a tail pointer is that it reduces the time of appending a node to the end of the list from O(n) to O(1).

**Problem 2:** (see node.py; sll.py; problem2_driver.py)
  these are tested with text files that contain problem2 in their name
  run: python3 problem2_driver.py problem2_filename.txt
    to see the results.
Intro:
  The problem asks us to combine the node and singly linked list (sll) classes to operate a driver program. The idea is that I use the node class to make the sll. Then the driver will receive a file with text (those should be instructions, but not guaranteed), reads them and then enacts the instructions on the sll. Before it does anything, I verify that the instruction file is a text file. I then read the file and look at the instructions there. The driver has a dictionary of allowed methods that can be called. Using the getattr function in python, the driver can separate the method name and the value it contains to then apply it to a sll.

NODE AND SINGLY LINKED LISTS:
  The code makes a class called node (see node.py file). There I used the basic properties of the node, as outlined by given of the problem. The attributes are private, so we make the getters and setters as seen in the code.

  Then I made the SinglyLikedList (see sll.py). There the basic idea is the same as in the node file. The attributes are default to the given of the problem. In addition to the methods that were asked of me, I also added icheck, traverse and rm_at methods.
  
  icheck: Verifies that the received index is an integer and not a boolean (since 1 or 0 are integers) to avoid crashes. This method also allows to check if the index is in bounds of the list. Notice that since there is an insert method that is needed for the solution, so we could add at the end with an insert. This would raise an IndexError since usually, if the index checked was bounded at the length of the list - 1 (since its base 0). So adding at the end would check for the index at the end and thus crash the program. This allows us to still raise an error when using a method like append, and still not raise an error when inserting.
  
  Traverse is a helper function that checks the index and if its valid, then we can iterate to the index that we want to get to.
  
  rm_at is a helper function that does the bulk of the work for required methods delete and delete_at. Since they will be sharing a large portion of the code, I decided to use it to avoid copy-pasting.

  append uses the exact idea in problem 1, we no longer have to travel to the tail to add a node, we can just do it straight away.
  
  insert in an interesting function since it can be used as an append and prepend as well as inserting at the end. If we want to insert at index 0, we just append, if we want to insert at the end of the list, then we can append there. As said above, method like get cant get an index at the end of the list, but you could insert a number at the back of the list, into a place that hasn't been made. I could have made an insert at an index before 0. But that's not necessary and also and index of -1 means that it would be inserted at the back of the list, not in front of the head.

The rest of the methods are pretty standard implementations of the methods required by the problem.

DRIVER (problem2_driver.py):
  The driver first does a check on the file to ensure its a text file. Now all of the code for that is just the submission from the first homework. The only new thing is that i also checked for the stream, if the filename isn't given (see get_input_lines()). If it tries to read standard in and fails it will raise a UnicodeDecodeError, and if there is still an error after the two conditions then it raises a throws UsageError.

  Since we receive a text file, all the numbers will also be text. So we want to get values and indices out of the text. parse_val does exactly that. It check the text and sees if we can get a float or int out of it, if its not possible python will raise its own error, but if that's the case we just want to keep it as text and move on. For index its the same thing, but more restrictive. We just look for integers where we have to see them, so we raise an error of our own.

  As mentioned above, we make a dictionary with all the directives that we are allowed to use and how we can use them. We don't want the user using public methods like icheck and traverse. Now i could have made them private, but it is easier to use them and also if we want to check how they work you could call them. Ultimately I should have worked around that. One the other hand python does not really have strict access modifiers and one could get to private attributes pretty easily, so if we wanted security, we wouldn't be using python (partly joking here, but also what i'm trying to get at isn't exactly wrong).

  Anyway, now that we have a dictionary of allowed methods we look which ones need to be printed and put them in a separate set. When we run the directives we get them out of the dictionary. Then, we make a tuple of the directive and the argument and it automatically has the values parsed, by the functions prior (see run_drictive (yes, i actually made a typo in the file))

  Once we have that done, we we can have the method using the getattr. The only exception being len being called differently since we use len to really mean __len__. Then if they are printed, we print the name of the directive, then what they intake separated by a comma and what the output of that method is.

  Lastly the main. We get the lines of the file and strip them of empty lines and unnecessary spaces, and ignore anything that starts with #. Assign the directive and argument in the line by using the split command. If we notice the directive is not in the dictionary, we raise error. If the number of arguments is different to what the method should get, we also raise an error. Then we try to run the directive, as explained above, and if we encounter any errors, make an exception and print a warning.


**Problem 3:** (see ways.py)
    For this one, just run the code as is, it takes in nothing.
  (base conditions)
  The idea here is pretty simple. We ask ourselves, how many way to climb 1 stair? (one way). How many ways to go down 2 steps? (2, once with just single steps, once with one big one). How many ways to go down 0 stairs? Now that's more interesting, mathematically there could be 0 ways of climbing it since there is nothing to climb, or infinity ways since every way will get you from 0 to 0. But ignoring the philosophical dilemma, we think about it from a rational point of view and conclude that there is 1 way to climb this non-existent set of 0 stairs, which is by doing nothing. We stick with that approach. If we were to climb a set of stairs with only one or two steps at a time, we have the Fibonacci sequence that tells us what the answer will be. 
  (recursion)
  Placing ourselves at the top of the stair case our first move could be to take one, two or three step down. Once we do any of those we can do the same. So on and so on till we get to our well defined case with 2, 1 and 0 steps.
  Putting the two elements together we get our solution.

**Problem 4:**
  these are tested with text files that contain problem4 in their name
  run: python3 problem4_driver.py problem4_filename.txt
    to see the results.

The idea here is similar to problem 2.
Make the node class like in problem 2, but now add a pointer to previous.
Make the sorteddoublylinkedlist (sdll).
  This is where it gets a bit different. When adding a node, we have to check if the value is larger than the tail or smaller than the head, that way we know where to add it. Adding one to an empty list is trivial. If the value is somewhere in the middle we have to use a while to get to traverse to the value just right before it to get the value before the new node value and one after it (prior and following in the code). Then set up the pointers accordingly. Note that I use the >= on purpose since that will allow us to duplicate the values and put it after its equals.

  delete works in a similar manner. Check the conditions if before head and tail, then use the while to get to the node with the value that needs to be deleted. Then we set the pointers to point at the prior and following values of the current node (the one we want to delete). Here we can't forget to check if there is a prior or a following (in the case of head and tail). Then remove the pointers of the current node to delete it.

  I defined a method called find that finds the node with a value. It does it by checking the base conditions if the node is none, if the value of the node is equal to the value, or if the value of the node is larger than the value we are looking for. Then the method is called as a return if these conditions are not satisfied we do the same idea, but now with the next node. The method exists, uses exactly that idea, but just starts at the head.

  the function print list relies on the recursive helper printer. That one prints the current node value. Then if the next node isn't none, then it prints arrows and calls itself. Then the print_list uses that method to print anything that isn't empty. The empty list prints out empty.

  total uses another recursive helper that sums the value of the current node with the out of itself when the next node gets called. Total uses that helper, but starts at head, instead of any arbitrary node.

count also gets a helper, counter. The counter doesn't add anything if the value is larger than the one we have or if the node is none. If it is equal to the one we have, then it adds one to the output of counter of the next node. If the value is smaller than the one we have, we just continue the walk. Then count just applies the counter to the head of the list.

median and sum middle three rely on the same mechanism, which is fining the middle. That is done by checking if the length of the list is even or odd. If it is odd we just travel to the node at the floor of half length index and return it as an array. If it is even, we travel to the index that is the floor of half the floor of the length -1. Then we return the array of that node and the one after it.
  The median then ensures that our count isn't 0, otherwise we raise and error, and gets the middle for us. If the length of the array is 1, then we return the value of the node in that array. If the length is 2 then we find the average of the 2 values and return that. We use array precisely because we can see if we need to average out the numbers or not by just looking at the length of the array.
  The sum middle three uses the similar idea. First checks that we have at least 3 nodes, then find the middle. If the length of the array is one, then we get the two values around it. If the length is 2 then we get the sum of the two values already in the array and add the value of the node before the first node in the array.

  Coming back to the note about private methods: all the helpers were made private as they should be to ensure good encapsulation. 

One additional note. These recursions are not the best since a very long list, that will run a recursion on a single node 1000 times will reach maximum recursion depth set by python. We could make it longer manually, but for our purposes here, it should be fine. 

DRIVER:
This driver is essentially a copy of the driver in problem 2, it does exactly the same thing, except it tweaks the dictionary, what is printed and how its printed to suit the output a bit better.
