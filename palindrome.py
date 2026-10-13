from read_check import get_input_lines

def is_palindrome(word):
    chars = word.replace(" ", "") #since "g e e k" is a palindrome when geek is
    last = len(chars) - 1
    for i in range(len(chars) // 2): #check if the first half is equal to the second
        if chars[i] != chars[last - i]: #check chars, since case matters
            return False
    return True

def pld_check(words): #get an array of T/F for each word
    return [is_palindrome(word) for word in words]

def main():
    lines = get_input_lines()
    words = [line.strip() for line in lines if line.strip()] #an array of lines without blanks
    outs = pld_check(words)
    for out in outs: #print the sequence of T/F and the sum of Ts
        print(out)          
    print(sum(outs))

if __name__ == "__main__":
    main()