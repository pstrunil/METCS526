import sys
from heap import Heap
from heap import parse_values
from read_check import get_input_lines

def running_medians(sales):
    lower = Heap() #the smaller will be made negative and its minimum is the largest value of that half
    upper = Heap() #the larger half is the minimum is the smallest value of that half
    medians = []
    for sale in sales:
        if lower.is_empty() or sale <= -lower.peek():
            lower.insert(-sale)
        else:
            upper.insert(sale)
        if len(lower) > len(upper) + 1: #keep the halves within 1 of each other, lower never smaller
            upper.insert(-lower.extract_min())
        elif len(upper) > len(lower):
            lower.insert(-upper.extract_min())
        if len(lower) > len(upper):
            medians.append(float(-lower.peek()))
        else:
            medians.append((-lower.peek() + upper.peek())/2)
    return medians

def main():
    try:
        sales = parse_values(get_input_lines())
    except ValueError:
        print("Error: the input must be a list of whole numbers", file=sys.stderr)
        sys.exit(65)
    print(running_medians(sales))

if __name__ == "__main__":
    main()