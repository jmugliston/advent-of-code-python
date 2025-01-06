import os
import argparse
from itertools import product


def parse_data(data):
    lines = data.strip().split("\n")
    coords = []
    for y in range(len(lines)):
        line = lines[y]
        for x in range(len(line)):
            if line[x] == "#":
                coords.append((x, y, 0))

    return coords

def get_neighbours(coord):
    deltas = [-1, 0, 1]
    neighbours = []
    for delta in product(deltas, repeat=len(coord)):
        if any(delta):
            neighbours.append(tuple(c + d for c, d in zip(coord, delta)))
    return neighbours

def get_max_coords(coords):
    dimensions = len(next(iter(coords)))
    max_coords = [max(coord[i] for coord in coords) for i in range(dimensions)]
    return tuple(max_coords)

def get_min_coords(coords):
    dimensions = len(next(iter(coords)))
    max_coords = [min(coord[i] for coord in coords) for i in range(dimensions)]
    return tuple(max_coords)

def run_boot_sequence(cubes):
    cube_map = {cube: True for cube in cubes}
    dimensions = len(next(iter(cubes)))

    for _ in range(6):
        next_map = {}
        min_coords = get_min_coords(cube_map.keys())
        max_coords = get_max_coords(cube_map.keys())
        ranges = [range(min_coords[i] - 1, max_coords[i] + 2) for i in range(dimensions)]
        
        neighbour_counts = {}
        for coord in product(*ranges):
            if cube_map.get(coord, False):
                for neighbour in get_neighbours(coord):
                    if neighbour not in neighbour_counts:
                        neighbour_counts[neighbour] = 0
                    neighbour_counts[neighbour] += 1

        for coord, count in neighbour_counts.items():
            if cube_map.get(coord, False):
                next_map[coord] = count in [2, 3]
            else:
                next_map[coord] = count == 3

        cube_map = next_map

    return cube_map


def part1(data):
    cubes = parse_data(data)
    
    cube_map = run_boot_sequence(cubes)

    return sum(state for state in cube_map.values())


def part2(data):
    cubes = parse_data(data)

    # Add the 4th dimension to the cubes
    cubes = [(x, y, z, 0) for x, y, z in cubes]

    cube_map = run_boot_sequence(cubes)

    return sum(state for state in cube_map.values())


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
