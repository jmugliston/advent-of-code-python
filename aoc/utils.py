import math

def parse_lines_of_text(input):
    return input.strip().split("\n")


def parse_grid(input):
    return [list(x) for x in input.strip().split("\n")]


def print_grid(grid):
    for row in grid:
        print("".join(row))


def manahattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)
