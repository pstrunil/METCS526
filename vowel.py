import sys
from read_check import get_input_lines

alphabet = {"A": ".-", "E": ".", "I": "..", "O": "---", "U": "..-"}


def vowel_seq(code):
    ways = [0] * (len(code) + 1) #initialize a list to store number of ways to decode up to each index
    ways[0] = 1  #with no elements, nothing to count, so 1 way
    for end in range(1, len(code) + 1): #index until wich we check
        for morse in alphabet.values(): #letter in the alphabet
            start = end - len(morse) #define starting index
            if start >= 0 and code[start:end] == morse: #if the starting index is valid and the substring matches the letter
                ways[end] += ways[start] #we can increase the number of ways to decode up to the ending index by the number of way to decode up to the starting index
    return ways[len(code)] #the last index is the cummulative nummber of way to decode up to the last index


def main():
    try:
        words = [line.strip() for line in get_input_lines() if line.strip()]
        if len(words) != 2:
            raise ValueError(f"Expected 2 lines, but got {len(words)}")
        code = words[1]
        if not all(c in ".-" for c in code):
            raise ValueError(f"The line must contain only '.' and '-', but got '{code}'")
    except ValueError as err:
        print(f"Error: {err}", file=sys.stderr)
        sys.exit(65)
    print("The Number of Vowel combinations is:  " + str(vowel_seq(code)))


if __name__ == "__main__":
    main()