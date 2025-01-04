import os
import argparse
from collections import Counter


def part1(data):
    adapters = sorted([int(x) for x in data.strip().split("\n")])

    # Add the charging outlet
    adapters = [0] + adapters
    
    diffs = Counter(adapters[i] - adapters[i - 1] for i in range(1, len(adapters)))

    diff_1 = diffs[1]
    diff_3 = diffs[3]

    return diff_1 * (diff_3 + 1)


def count_arrangements(adapters, i, memo):
    if i == len(adapters) - 1:
        return 1

    if i in memo:
        return memo[i]

    count = 0
    for j in range(i + 1, len(adapters)):
        if adapters[j] - adapters[i] <= 3:
            count += count_arrangements(adapters, j, memo)

    memo[i] = count
    return count


def part2(data):
    adapters = sorted([int(x) for x in data.strip().split("\n")])

    # Add the charging outlet
    adapters = [0] + adapters

    return count_arrangements(adapters, 0, {})


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
