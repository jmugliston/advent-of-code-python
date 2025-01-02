import os
import argparse


def part1(data):
    return -1


def part2(data):
    return -1


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
