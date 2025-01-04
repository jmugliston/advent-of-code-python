import os
import argparse
from ...utils import parse_grid, print_grid

def simulate_round(grid):
    next_grid = []

    for i in range(len(grid)):
        row = []
        for j in range(len(grid[i])):
            if grid[i][j] == ".":
                row.append(".")
                continue

            occupied = 0
            for x in range(-1,2):
                for y in range(-1,2):
                    if x == 0 and y == 0:
                        continue
                    if i+x < 0 or i+x >= len(grid):
                        continue
                    if j+y < 0 or j+y >= len(grid[i]):
                        continue
                    if grid[i+x][j+y] == "#":
                        occupied += 1
            
            if occupied == 0:
                row.append("#")
            elif occupied >= 4:
                row.append("L")
            else:
                row.append(grid[i][j])

        next_grid.append(row)

    return next_grid

def simulate_round_alt(grid):
    next_grid = []

    for i in range(len(grid)):
        row = []
        for j in range(len(grid[i])):
            if grid[i][j] == ".":
                row.append(".")
                continue

            occupied = 0
            for x in range(-1,2):
                for y in range(-1,2):
                    if x == 0 and y == 0:
                        continue

                    x_dir = x
                    y_dir = y
                    while True:
                        if i+x_dir < 0 or i+x_dir >= len(grid):
                            break
                        if j+y_dir < 0 or j+y_dir >= len(grid[i]):
                            break
                        if grid[i+x_dir][j+y_dir] == "L":
                            break
                        if grid[i+x_dir][j+y_dir] == "#":
                            occupied += 1
                            break
                        x_dir += x
                        y_dir += y
            
            if occupied == 0:
                row.append("#")
            elif occupied >= 5:
                row.append("L")
            else:
                row.append(grid[i][j])

        next_grid.append(row)

    return next_grid



def count_seats(grid):
    count = 0
    for row in grid:
        count += row.count("#")
    return count

def part1(data):
    grid = parse_grid(data)

    while True:
        next_grid = simulate_round(grid)
        if next_grid == grid:
            break
        grid = next_grid

    return count_seats(grid)


def part2(data):
    grid = parse_grid(data)

    while True:
        next_grid = simulate_round_alt(grid)
        if next_grid == grid:
            break
        grid = next_grid

    return count_seats(grid)


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
