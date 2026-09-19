import sys

def valid_file(filename):
    if not filename.endswith(".txt"): #Checks if the file is a .txt
        print("Error: File must be a .txt file", file = sys.stderr)
        sys.exit(2)

def read_lines(filename):
    try:
        with open(filename,"r") as file: #Attempts to open and read the file
           lines =file.readlines()
    except FileNotFoundError: #If the file isn't found in the directory
        print(f"Error: File '{filename}' not found", file = sys.stderr)
        sys.exit(66)
    except PermissionError: # If the user doesn't have access to the file
        print(f"Error: Access denied to file '{filename}'", file = sys.stderr)
        sys.exit(77)
    except UnicodeDecodeError: #If content of the .txt file is not readable
        print(f"Error: File '{filename}' is not a readable text", file = sys.stderr)
        sys.exit(65)
    return lines

def main():
    if len(sys.argv) != 2: #Ensures that user provides one argument to run.
        print("Usage: python script.py <filename>", file = sys.stderr)
        sys.exit(64)

    filename = sys.argv[1]
    valid_file(filename)
    lines = read_lines(filename)
    for line in lines:
        print(line, end="") #Prints the lines of the file
        
if __name__ == "__main__":
    main()