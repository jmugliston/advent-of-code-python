import os
import argparse
from collections import Counter

def parse_input(data):
    split = data.strip().split("-")
    return int(split[0]), int(split[1])


def meets_criteria(range_start, range_end, part2=False):
    meets_criteria = 0
    for i in range(range_start, range_end + 1):
        # Must be 6 digits
        if i < 100000 or i > 999999:
            continue

        # Must always be increasing
        digits = [int(d) for d in str(i)]
        if digits != sorted(digits):
            continue

        # Must have at least one adjacent pair
        has_adjacent = False
        for j in range(1, len(digits)):
            if digits[j] == digits[j - 1]:
                has_adjacent = True
                break

        if not has_adjacent:
            continue
        
        # Must have at least one adjacent pair that is not part of a larger group
        if part2 and 2 not in Counter(digits).values():
            continue

        meets_criteria += 1
    
    return meets_criteria

def part1(data):
    range_start, range_end = parse_input(data)
    return meets_criteria(range_start, range_end)


def part2(data):
    range_start, range_end = parse_input(data)
    return meets_criteria(range_start, range_end, part2=True)


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
