import sys
from sll import SinglyLinkedList

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
    if len(sys.argv) == 2: #if we have a filename then we can check if its valid
        valid_file(sys.argv[1]) 
        return read_lines(sys.argv[1])
    if len(sys.argv) == 1: #if the filename isn't given (only seen as stream) we use stdin.readlines()
        try:
            return sys.stdin.readlines()
        except UnicodeDecodeError:
            print("Error: input is not readable text", file=sys.stderr)
            sys.exit(65)
    print("Usage: python3 problem2_driver.py [filename.txt]  (or: ... < input.txt)", file=sys.stderr)
    sys.exit(64)

def parse_val(text): #since the file will contain number as text, we convert it to number
    for convert in (int,float):
        try:
            return convert(text)
        except ValueError:
            pass #since we are told to skip if invalid
    return text

def parse_index(text): #checks if the index is an integer for functions like insert
    try:
        return int(text)
    except ValueError:
        raise ValueError(f"index '{text}' is not a whole number")

directives = { #make a dictionary with all the methods that are allowed
    "append": (parse_val,),
    "prepend": (parse_val,),
    "insert": (parse_index, parse_val),
    "get": (parse_index,),
    "find": (parse_val,),
    "len": (),
    "update": (parse_index, parse_val),
    "delete": (parse_val,),
    "delete_at": (parse_index,),
    "print_list": (),
}

result_printed = {"get", "find", "len", "delete_at"} #directives with prited results

def run_driective(list, directive, args):
    parsers = directives[directive] #looks up the directive in the dictionary
    parsed = []
    for parse, arg in zip(parsers,args): #makes an ntuple of directive and arguments
        entry = parse(arg)
        parsed.append(entry)

    #if the directive is len, it gets replased with "__len__", then runs it (if not its just left as is)
    method = getattr(list, "__len__" if directive == "len" else directive)
    out = method(*parsed)

    #map loops over all the parsed and converts them to a string, then join glues them together and separates them with a , giving the result
    if directive in result_printed:
        print(f"{directive}({', '.join(map(str, parsed))}) = {out}")
    elif directive == "delete" and not out: #we check if we can delete the index or not so the out will be a bool. if we can't then we throw error
        raise ValueError(f"Cannot delete {parsed[0]}: not in the list")

    


def main():
    my_list = SinglyLinkedList()
    lines = get_input_lines()

    for lineno, line in enumerate(lines,start=1):
        line = line.strip() #so we only get the subtance of the line and not deadspace
        if not line or line.startswith("#"): ## needs to be skipped
            continue 
        directive, *args = line.split() #assign the directive and arguments to the two

        if directive not in directives:
            print(f"Warning: line '{lineno}': has unknown directive '{directive}'")
        elif len(args) != len(directives[directive]):
            print(f"Warning: line '{lineno}': '{directive}' expects " 
                  f"{len(directives[directive])} arguments, got {len(args)}")
        else:
            try:
                run_driective(my_list,directive, args)
            except (IndexError,TypeError,ValueError) as e:
                print(f"Warning: line '{lineno}': {e}")
    print("Final list: ", end= "")
    my_list.print_list()
        
    
if __name__ == "__main__":
    main()