import os
import argparse

def parse_data(data):
    instructions = []

    for line in data.strip().split("\n"):
        next_instruction = []
        previous_char = ""
        for char in line:
            if char in ["e", "w"]:
                next_instruction.append(previous_char + char)
                previous_char = ""
            else:
                previous_char = char
        instructions.append(next_instruction)

    return instructions


def get_tile_in_direction(tile, direction):
    x, y = tile

    if direction == "e":
        x += 1
    elif direction == "w":
        x -= 1
    elif direction == "ne":
        y -= 1
        if y % 2 == 0:
            x += 1
    elif direction == "nw":
        y -= 1
        if y % 2 != 0:
            x -= 1
    elif direction == "se":
        y += 1
        if y % 2 == 0:
            x += 1
    elif direction == "sw":
        y += 1
        if y % 2 != 0:
            x -= 1

    return x, y


"""
Tiles are hexagonal with sides (e, w, ne, nw, se, sw)
"""
def flip_tiles(tiles, instructions):
    for instruction in instructions:
        x, y = 0, 0
        for direction in instruction:
            x, y = get_tile_in_direction((x, y), direction)
        tiles[(x, y)] = not tiles.get((x, y), False)

    return tiles


"""
Get all the neighbors of a tile
"""
def get_tile_neighbors(tile):
    neighbours = []
    for direction in ["e", "w", "ne", "nw", "se", "sw"]:
        neighbours.append(get_tile_in_direction(tile, direction))
    return neighbours

def next_day(tiles):
    neighbour_map = {}

    # Get the neighbors of the current tiles
    for tile in tiles:
        neighbour_map[tile] = get_tile_neighbors(tile)

    # Add any additional tiles that are neighbors of the current tiles
    for _, neighbours in neighbour_map.items():
        for neighbour in neighbours:
            if neighbour not in tiles:
                tiles[neighbour] = False

    # Get the neighbors of the new tiles
    for tile in tiles:
        if tile not in neighbour_map:
            neighbour_map[tile] = get_tile_neighbors(tile)

    # Flip tiles according to the rules
    new_tiles = {}
    for tile in tiles:
        black_neighbours = 0
        for neighbour in neighbour_map[tile]:
            if tiles.get(neighbour, False):
                black_neighbours += 1

        if tiles[tile] and (black_neighbours == 0 or black_neighbours > 2):
            new_tiles[tile] = False
        elif not tiles[tile] and black_neighbours == 2:
            new_tiles[tile] = True
        else:
            new_tiles[tile] = tiles[tile]
            
    return new_tiles


def part1(data):
    instructions = parse_data(data)

    tiles = {
        (0, 0): False,
    }

    tiles = flip_tiles(tiles, instructions)

    return sum(tiles.values())


def part2(data, example=False):
    instructions = parse_data(data)

    tiles = {
        (0, 0): False,
    }

    tiles = flip_tiles(tiles, instructions)

    for _ in range(10 if example else 100):
        tiles = next_day(tiles)

    return sum(tiles.values())


def main(part, example=False):
    file_name = "example.txt" if example else "input.txt"
    file_path = os.path.join(os.path.dirname(__file__), f"input/{file_name}")
    with open(file_path, "r") as file:
        data = file.read()
    return part1(data) if part == 1 else part2(data, example)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--part", type=int, choices=[1, 2], default=1, help="part number"
    )
    parser.add_argument("--example", action="store_true", help="use the example data")
    args = parser.parse_args()
    print(main(args.part, args.example))
