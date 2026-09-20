# METCS526 HW1

Introduction:
  My name Peter. I am an exchange student at BU. At my home university in Geneva, Switzerland, I am in my last year of Economics. In this faculty I have learned Scala and R. I studied Mathematics prior to switching to my current degree, where I learned how to program in C++ (final project was an OOP project that simulated perfect gazes). In my spare time I am working on a data analysis project in Python. 
  While I was in Mathematics, my programming class taught me a bit about algorithms, things like writing pseudo-code and complexity analysis. As for data structure I simply know of stacks and queues, however I haven't really gotten to dig into the details.

Pseudocode:
BEGIN

FUNCTION valid_file(filename):
  IF filename does not end with ".txt"
    print: Error to standard error
    exit: with code 2
  END IF
END FUNCTION

FUNCTION read_lines(filename):
  try:
      open: filename for reading lines <- All lines read from the file
      close: file
      return: lines
    catch: FileNotFound
      print: Error to standard error
      exit: with code 66
    catch: PermissionDenied
      print: Error to standard error
      exit: with code 77
    catch: UnreadableContent
      print: Error to standard error
      exit: with code 65
    END try
END FUNCTION

FUNCTION main():
  IF number of command-line arguments is not 1
    print: Error to standard error
    Exit with code 64
  END IF
  
  filename <- given command-line argument
 
  CALL valid_file(filename)
  lines <- CALL read_lines(filename)
  
  FOR EACH line IN lines DO
      print: line
  END FOR
END FUNCTION

CALL main()
END

Description of pseudocode:
  The idea is that you start by defining a function to check if your file is a text file. If it happens to be some sort of other file, I won't be able to read it. That a key filter that if failed, exits with an error message, saying the program can't read something that isn't text. We put this first since there is no preset error like NotTextFile, so we have to check for it manually.
  The next step is to try and read the file. Once the attempt was made we check for other errors, since at this point we know that it is a text file, but not necessarily something that will give an output. We check the preset errors in python. So then we go with checking if the file even exists, if not then we throw an error saying that it isn't there, hence exit code 66. Similar idea follows for the next errors too. PermissionDenied; if we can't access the file, if it requires permission by the admin. UnreadableContent; if its text, but not something readable like Unicode.
  All the error codes exit to standard error since it wont mix with output and won't be accepted as an input for next steps. Not that it would in the case of this program, but in general a good thing to do.
  Once the checks have passed, we have to assign the file name so that we can call the function defined earlier to read it. In the command-line this means inserting the name of my program, then the name of whatever file we want to read. So if the user inserts 2 files, we wont manage to read both of them and there will be an error. In theory, we could accept a vector of files and apply the process to all of them, but in the task we were specifically asked to read a file, not a collection of files, so that was not implemented. Naturally if the user doesn't insert the file, the issue is the same and we just don't return anything and exit with code 64, the command-line usage error.
  Once all the checks have passed, we deem the file as "good" and in theory should handle it well. So we assign the file name to filename variable and call the above-defined read function. Now python already knows when the line ends so no need to add anything else as it will handle the reading (like we don't specify that it has to go to a particular terminating character). Once the lines have been identified as the list of strings (our lines), then we run a for loop on all of them and print each one. We then end the main and call it.
  Now in theory it has read and printed all the lines, however if we are being technical, I am not actually sure that it prints the very last terminating character, as the last line wont have any characters on it, so the read_lines will probably just ignore it, so in theory we haven't printed exactly the output of our file. However that being said, in terms of providing information to the user about the text itself, we completed our job. 
      
      
