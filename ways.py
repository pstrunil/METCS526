def ways(n):
    if n <=1:
        return 1
    if n == 2:
        return 2
    return ways(n-1) + ways(n-2) + ways(n-3)

def main():
    [print(ways(i)) for i in [3,5,10]]
if __name__ == "__main__":
    main()
