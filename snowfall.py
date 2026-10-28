from read_check import get_input_lines

def consec(values):
    if len(values) < 3:
        return False
    for i in range(3,len(values)):
        if 2*(values[i]- values[i-3]) > values[-1]:
            return True
    return False

def main():
    lines = get_input_lines()
    words = [line.strip() for line in lines if line.strip()]
    values = [int(element) for element in words[1].split()]
    out = consec(values)
    print(" ".join(str(v) for v in values) + " solution: " + ("YES" if out else "NO"))
if __name__ == "__main__":
    main()