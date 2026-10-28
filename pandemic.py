from read_check import get_input_lines

neighbor_directions = ((1,0),(-1,0),(0,1),(0,-1)) #direction of neighbors

def spread(n, infected):
    seen = {} #infected neighbors of a county
    today = list(infected) #counties infected today
    while today:
        tomorrow = []
        for row, col in today:
            for drow, dcol in neighbor_directions:
                a, b = row + drow, col + dcol
                if 0 <= a < n and 0 <= b < n and (a,b) not in infected:
                    seen[(a,b)] = seen.get((a, b), 0) + 1 #for that uninfected county add 1
                    if seen[(a,b)] == 2: #if that uninfected county has 2 infected neighbors, it will be infected tomorrow
                        tomorrow.append((a,b))
        infected.update(tomorrow)
        today = tomorrow
    return infected
   
def main():
    lines = get_input_lines()
    words = [line.strip() for line in lines if line.strip()]
    n = int(words[0])
    pzero = set()
    for word in words[1:]:
        point = word.split()
        row, col = int(point[0]), int(point[1])
        pzero.add((row,col))
    final = spread(n,pzero)
    if len(final) == n*n:
        print("There are no healthy counties left")
    else:
        print("There are healthy counties left")
    
if __name__ == "__main__":
    main()