import os
import argparse


def parse_input(data):
    lines = data.strip().split("\n")

    data = []
    for line in lines:
        policy_raw = line.split(":")[0]
        password = line.split(":")[1].strip()
        policy_range = policy_raw.split(" ")[0].split("-")
        data.append(
            {
                "min": int(policy_range[0]),
                "max": int(policy_range[1]),
                "char": policy_raw.split(" ")[1],
                "password": password,
            }
        )

    return data


def part1(data):
    password_data = parse_input(data)

    count = 0
    for item in password_data:
        char_count = item["password"].count(item["char"])
        if char_count >= item["min"] and char_count <= item["max"]:
            count += 1

    return count


def part2(data):
    password_data = parse_input(data)

    count = 0
    for item in password_data:
        char = item["char"]
        pos_a = item["min"] - 1
        pos_b = item["max"] - 1
        if (item["password"][pos_a] == char) ^ (item["password"][pos_b] == char):
            count += 1

    return count


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
