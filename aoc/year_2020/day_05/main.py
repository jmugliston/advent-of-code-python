import os
import argparse

def search(data, upper, lower, upper_char):
    for char in data:
        mid = (upper + lower) // 2
        if char == upper_char:
            lower = mid + 1
        else:
            upper = mid
    return lower

def part1(data):
    passes = data.strip().split("\n")

    ans = 0
    for p in passes:
        row = search(p[:7], 127, 0, "B")
        col = search(p[7:], 7, 0, "R")
        ans = max(ans, row * 8 + col)

    return ans


def part2(data):
    passes = data.strip().split("\n")

    rows = []
    for i in range(128):
        rows.append([0] * 8)

    for p in passes:
        row = search(p[:7], 127, 0, "B")
        col = search(p[7:], 7, 0, "R")
        rows[row][col] = 1

    ans = 0
    for i in range(128):
        for j in range(1, 7):
            if rows[i][j] == 0 and rows[i][j-1] == 1 and rows[i][j+1] == 1:
                ans = i * 8 + j
                break

    return ans


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
