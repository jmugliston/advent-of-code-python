import os
import argparse

def parse_input(data):
    wire_1_raw, wire_2_raw = data.strip().split("\n")
    wire_1 = wire_1_raw.split(",")
    wire_2 = wire_2_raw.split(",")
    return wire_1, wire_2

def get_points(wire):
    points = []
    x, y = 0, 0
    directions = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    for move in wire:
        direction = directions[move[0]]
        distance = int(move[1:])
        for _ in range(distance):
            x += direction[0]
            y += direction[1]
            points.append((x, y))
    return points


def manhattan_distance(point):
    return abs(point[0]) + abs(point[1])


def part1(data):
    wire_1, wire_2 = parse_input(data)
    
    wire_1_points = get_points(wire_1)
    wire_2_points = get_points(wire_2)

    intersections = set(wire_1_points) & set(wire_2_points)

    min_distance = min(manhattan_distance(intersection) for intersection in intersections)

    return min_distance


def part2(data):
    wire_1, wire_2 = parse_input(data)
    
    wire_1_points = get_points(wire_1)
    wire_2_points = get_points(wire_2)

    intersections = set(wire_1_points) & set(wire_2_points)

    min_steps = min(wire_1_points.index(intersection) + wire_2_points.index(intersection) + 2 for intersection in intersections)

    return min_steps
    


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
