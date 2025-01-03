import os
import argparse

from aoc.utils import parse_grid


def part1(data):
    return -1


def part2(data):
    return -1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--part", type=int, help="part number", choices=[1, 2], default=1
    )
    parser.add_argument(
        "--example", action=argparse.BooleanOptionalAction, help="use the example data"
    )

    args = parser.parse_args()

    dir = os.path.dirname(__file__)

    file_name = "input.txt"
    if args.example:
        file_name = "example.txt"

    with open(os.path.join(dir, f"input/{file_name}"), "r") as file:
        data = file.read()

    if args.part == 1:
        print(part1(data))
    else:
        print(part2(data))
