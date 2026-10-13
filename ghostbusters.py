from read_check import get_input_lines
import sys

def cross(v, u):
    return v[0] * u[1] - v[1] * u[0]
 
def is_parallel(v, u):
    return cross(v, u) == 0


def get_pair_vector(line):
    word = line.split()
    if 'B' != word[0] or 'G' != word[3] or len(word) != 6:
        raise ValueError(f"Expected 'B <x> <y> G <x> <y>' but got '{line}'")
    try:
        bx, by, gx, gy = (int(word[i]) for i in (1,2,4,5))
    except ValueError:
        raise ValueError(f"Coordinate must be an integer in '{line}'")
    if (bx,by) == (gx,gy):
        raise ValueError(f"The ghostbuster and the ghost are at the same spot in '{line}'")
    return bx, by, gx-bx, gy-by #position of buster and difference to the ghost

def elim(vectors):
    v1 = [vectors[0][2],vectors[0][3]]
    checked = []
    for bx, by, dx, dy in vectors:
        if not is_parallel(v1, [dx,dy]): #we compare if the pairs are parallel (only need to wrt v1)
            return False
        offset = cross(v1, [bx, by]) #checks if a different buster is on the same line as the first
        if offset in checked: #if 2 different busters have the same number, then they are collinear
            return False
        checked.append(offset)
    return True


def main():
    try:
        lines = get_input_lines()
        words = [line.strip() for line in lines if line.strip()] #an array of lines without blanks
        if not words:
            raise ValueError("Empty input")
        try:
            n = int(words[0])
        except ValueError:
            print(f"The first line must be the number of ghostbusters, got '{words[0]}'")
        if n < 1:
            raise ValueError("There must be at least one ghostbuster")
        if n != len(words)-1:
            raise ValueError(f"The first line says {n} pairs, but got {len(words) - 1}")
        
        vectors = [get_pair_vector(word) for word in words[1:]]
        print("All Ghosts: " + ("were eliminated" if elim(vectors) else "were not eliminated"))
    except ValueError as err: #catches all the errors
        print(f"Error: {err}", file = sys.stderr)
        sys.exit(65)

if __name__ == "__main__":
    main()