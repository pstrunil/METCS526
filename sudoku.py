from read_check import get_input_lines
from math import sqrt

def is_valid(n, symbols, board):
    k = int(sqrt(n))
    place = {symbol: [] for symbol in symbols}

    for r, row in enumerate(board):
        for c, value in enumerate(row):
            if value == ".":
                continue
            if value not in place:
                return False
            place[value].append((r,c))
    for places in place.values():
        rows = [r for r, c in places]
        cols =[c for r, c in places]
        quadrants = [(r//k)*k + (c//k) for r, c in places]    
        for triple in (rows, cols, quadrants):
            if len(set(triple)) != len(triple):
                return False
    return True

def main():
    lines = get_input_lines()
    words = [line.strip() for line in lines if line.strip()]
    n = int(words[0])
    
    symbols = [part.strip() for part in words[1].split(",")]
    
    board = []
    for word in words[2:]:
        row = [part.strip() for part in word.split(",")]
        board.append(row)

    print("The board is valid" if is_valid(n, symbols, board) else "The board is invalid")
   
if __name__ == "__main__":
    main()