import os
import argparse

def find_num(nums, window_size):
    for i in range(window_size, len(nums)):
        found = False
        for j in range(i - window_size, i):
            for k in range(j + 1, i):
                if nums[j] + nums[k] == nums[i]:
                    found = True
                    break
            if found:
                break
        if not found:
            return nums[i]
    return 0

def find_contiguous_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 2, len(nums)):
            if sum(nums[i:j]) == target:
                return min(nums[i:j]) + max(nums[i:j])

def part1(data, example=False):
    nums = list(map(int, data.strip().split("\n")))
    window_size = 5 if example else 25
    return find_num(nums, window_size)


def part2(data, example=False):
    nums = list(map(int, data.strip().split("\n")))
    window_size = 5 if example else 25
    num = find_num(nums, window_size)
    return find_contiguous_sum(nums, num)


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
