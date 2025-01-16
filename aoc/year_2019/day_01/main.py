import os
import argparse


def part1(data):
    nums = [int(num) for num in data.strip().split("\n") if num]

    return sum(map(lambda x: x // 3 - 2, nums))


def part2(data):
    nums = [int(num) for num in data.strip().split("\n") if num]

    total = 0
    for num in nums:
        while num > 0:
            num = num // 3 - 2
            total += max(num, 0)
    
    return total


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
