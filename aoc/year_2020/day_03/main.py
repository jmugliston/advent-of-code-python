import os
import argparse

from aoc.utils import *


def count_trees(grid, right, down):
    trees = 0
    r = right
    d = down
    while True:
        if grid[d][r % len(grid[0])] == "#":
            trees += 1
        r += right
        d += down
        if d >= len(grid):
            break
    return trees


def part1(data):
    grid = parse_grid(data)
    return count_trees(grid, 3, 1)


def part2(data):
    grid = parse_grid(data)

    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    ans = 1
    for slope in slopes:
        ans *= count_trees(grid, slope[0], slope[1])

    return ans


def main(part, example=False):
    file_name = "example.txt" if example else "input.txt"
    file_path = os.path.join(os.path.dirname(__file__), f"input/{file_name}")
    with open(file_path, "r") as file:
        data = file.read()
    return part1(data) if part == 1 else part2(data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--part", type=int, choices=[1, 2], default=1, help="part number"
    )
    parser.add_argument("--example", action="store_true", help="use the example data")
    args = parser.parse_args()
    print(main(args.part, args.example))
