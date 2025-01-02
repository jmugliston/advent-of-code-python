import os
import argparse


def parseNumbers(data):
    return [int(line) for line in data.strip().split("\n")]


def part1(data):
    numbers = parseNumbers(data)
    return [x * y for x in numbers for y in numbers if x + y == 2020][0]


def part2(data):
    numbers = parseNumbers(data)
    return [
        x * y * z
        for x in numbers
        for y in numbers
        for z in numbers
        if x + y + z == 2020
    ][0]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--part", type=int, help="part number", choices=[1, 2], default=1
    )

    args = parser.parse_args()

    dir = os.path.dirname(__file__)

    with open(os.path.join(dir, "input/input.txt"), "r") as file:
        data = file.read()

    if args.part == 1:
        print(part1(data))
    else:
        print(part2(data))
