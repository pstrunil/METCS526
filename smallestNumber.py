from read_check import get_input_lines
import sys

def counter(target, values):
    ordered = sorted(values)
    count = 0
    tot = 0
    while tot <= target:
        tot = tot + ordered.pop()
        count += 1
    return count



def main():
    try:
        lines = get_input_lines()
        words = [line.strip() for line in lines if line.strip()]
        if len(words) != 3:
            raise ValueError(f"Expected 3 lines, but got {len(words)}")
        try:
            n = int(words[0])
            target = int(words[1])
            values = [int(element) for element in words[2].split()]
            ans = counter(target, values)
        except ValueError:
            print(f"The count, target and every value, must be whole numbers")
        if n < 1:
            raise ValueError("There must be at least one value")
        if n != len(values):
            raise ValueError(f"The first line says {n} values, but got {len(words)}")
        if sum(values) <= target:
            raise ValueError("The sum of all the values must be larger than the target")
        print("Input: " + ",".join(str(v) for v in values)+ " Target: "+ str(target) + " Answer: " + str(ans))
    
    except ValueError as err:
        print(f"Error: {err}", file = sys.stderr)
        sys.exit(65)    

if __name__ == "__main__":
    main()