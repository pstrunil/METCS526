from read_check import get_input_lines

def longest_alternating(a, b):
    best_a = [0]*len(a)
    best_b = [0]*len(b)
    for p in range(max(len(a), len(b))): #positions from left to right
        if p < len(a):
            before = 0
            for q in range(min(p, len(b))):
                if b[q] < a[p] and best_b[q] > before:
                    before = best_b[q]
            best_a[p] = 1 + before
        if p < len(b):
            before = 0
            for q in range(min(p, len(a))):
                if a[q] < b[p] and best_a[q] > before:
                    before = best_a[q]
            best_b[p] = 1 + before
    return max(best_a + best_b)


def main():
    lines = get_input_lines()
    a = [int(elt) for elt in lines[2].split()]
    b = [int(elt) for elt in lines[3].split()]
    print("Longest Sequence: " + str(longest_alternating(a, b)))

if __name__ == "__main__":
    main()