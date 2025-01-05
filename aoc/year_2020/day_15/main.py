import os
import argparse

def calculate_last_spoken(nums, final_idx=2020):
    spoken = {num: idx + 1 for idx, num in enumerate(nums)}
    last_spoken = nums[-1]

    for idx in range(len(nums), final_idx):
        if last_spoken in spoken:
            new_spoken = idx - spoken[last_spoken]
        else:
            new_spoken = 0
        spoken[last_spoken] = idx
        last_spoken = new_spoken

    return last_spoken


def part1(data):
    nums = [int(x) for x in data.strip().split(",")]
    return calculate_last_spoken(nums)


def part2(data, example=False):
    nums = [int(x) for x in data.strip().split(",")]
    # Use a smaller number of iterations for the example because my code is a bit slow! :D
    return calculate_last_spoken(nums, 2020 if example else 30000000)


def main(part, example=False):
    file_name = "example.txt" if example else "input.txt"
    file_path = os.path.join(os.path.dirname(__file__), f"input/{file_name}")
    with open(file_path, "r") as file:
        data = file.read()
    return part1(data) if part == 1 else part2(data, example=example)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--part", type=int, choices=[1, 2], default=1, help="part number"
    )
    parser.add_argument("--example", action="store_true", help="use the example data")
    args = parser.parse_args()
    print(main(args.part, args.example))
