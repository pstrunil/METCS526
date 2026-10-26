from math import gcd
import sys
from read_check import get_input_lines


def generator(a, b):
    n = gcd(a, b)
    a //= n
    b //= n
    if a < 0 or (a == 0 and b < 0):
        a, b = -a, -b
    return (a, b)

def triangles(corner, points):
    cx, cy = corner
    on_line = {}
    for x, y in points:
        a, b = x - cx, y - cy
        if a == 0 and b == 0:
            continue
        g = generator(a, b)
        on_line[g] = on_line.get(g, 0) + 1

    tot = 0
    for g, nb_pts in on_line.items():
        orthog = generator(-g[1], g[0])
        if g < orthog:
            tot += nb_pts*on_line.get(orthog, 0)
    return tot


def count_right_triangles(points):
    return sum(triangles(corner, points) for corner in points)

def main():
    try:
        points = get_input_lines()
        words = [points.strip() for points in points if points.strip()]
        if not words:
            raise ValueError("Empty input")
        try:
            n = int(words[0])
        except ValueError:
            raise ValueError(f"The number of points must be a whole number, got '{words[0]}'")
        if n < 1:
            raise ValueError("There must be at least one point")
        if n != len(words) - 1:
            raise ValueError(f"Given {n} points, but got {len(words) - 1}")
        points = []
        for word in words[1:]:
            parts = word.split()
            if len(parts) != 2:
                raise ValueError(f"Expected 2 coordinates but got '{word}'")
            try:
                points.append((int(parts[0]), int(parts[1])))
            except ValueError:
                raise ValueError(f"Coordinates must be whole numbers in '{word}'")
        if len(set(points)) != len(points):
            raise ValueError("The points must be distinct")
        print("The number of right triangles is: " + str(count_right_triangles(points)))
    
    except ValueError as err:
        print(f"Error: {err}", file=sys.stderr)
        sys.exit(65)


if __name__ == "__main__":
    main()