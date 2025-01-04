import os
import argparse


def parse_data(data):
    instructions_raw = data.strip().split("\n")
    instructions = []
    for instruction in instructions_raw:
        instructions.append((instruction[0], int(instruction[1:])))
    return instructions

def part1(data):
    instructions = parse_data(data)

    direction = 'E'
    x = 0
    y = 0

    directions = ['N', 'E', 'S', 'W']
    for instruction in instructions:
        dir, value = instruction
        if dir in 'NESW':
            if dir == 'N':
                y += value
            elif dir == 'S':
                y -= value
            elif dir == 'E':
                x += value
            elif dir == 'W':
                x -= value
        elif dir in 'LR':
            steps = value // 90
            if dir == 'L':
                steps = -steps
            direction = directions[(directions.index(direction) + steps) % 4]
        elif dir == 'F':
            if direction == 'N':
                y += value
            elif direction == 'S':
                y -= value
            elif direction == 'E':
                x += value
            elif direction == 'W':
                x -= value

    return abs(x) + abs(y)


def part2(data):
    instructions = parse_data(data)

    waypoint_x = 10
    waypoint_y = 1

    x = 0
    y = 0

    for instruction in instructions:
        dir, value = instruction
        if dir in 'NESW':
            if dir == 'N':
                waypoint_y += value
            elif dir == 'S':
                waypoint_y -= value
            elif dir == 'E':
                waypoint_x += value
            elif dir == 'W':
                waypoint_x -= value
        elif dir in 'LR':
            steps = value // 90
            if dir == 'L':
                steps = -steps
            for _ in range(steps % 4):
                waypoint_x, waypoint_y = waypoint_y, -waypoint_x
        elif dir == 'F':
            x += waypoint_x * value
            y += waypoint_y * value

    return abs(x) + abs(y)


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
