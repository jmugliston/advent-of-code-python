import os
import argparse

def parse_input(data):
    lines = data.strip().split("\n")
    return int(lines[0]), int(lines[1])


def find_loop_size(subject, target, divider):
    value, loop_size = 1, 0
    while value != target:
        value = (value * subject) % divider
        loop_size += 1
    return loop_size

def part1(data):
    card, door = parse_input(data)

    divider = 20201227

    card_loop = find_loop_size(7, card, divider)

    encryption_key = pow(door, card_loop, divider)
    
    return encryption_key


def part2():
    return -1


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
