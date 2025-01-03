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
