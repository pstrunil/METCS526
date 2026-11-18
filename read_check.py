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

def get_input_lines():
    if len(sys.argv) == 2: #if a filename was given run the full file checks
        valid_file(sys.argv[1])
        return read_lines(sys.argv[1])
    if len(sys.argv) == 1: #if the filename isn't given (only seen as stream) we use stdin.readlines()
            try: #sys.stdin.readlines() replaces bytes it cant decode, so we decode it instead uft-8 is the windows default
                return sys.stdin.buffer.read().decode("utf-8").splitlines()
            except:
                print("Error: input is not readable text", file=sys.stderr)
                sys.exit(65)
    print("Usage: python3 program.py [filename.txt] or: < input.txt", file=sys.stderr)
    sys.exit(64)
