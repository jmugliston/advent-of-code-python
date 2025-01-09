import os
import argparse
import math
from collections import Counter

def parse_data(data):
    raw_tiles = data.strip().split("\n\n")

    tiles = {}
    for raw_tile in raw_tiles:
        split_tile = raw_tile.split("\n")
        id = int(split_tile[0].split(" ")[1][:-1])
        tile = list(split_tile[1:])
        tiles[id] = tile

    return tiles


def get_edges(tile):
    top = tile[0]
    bottom = tile[-1]
    left = "".join([row[0] for row in tile])
    right = "".join([row[-1] for row in tile])
    return top, right, bottom, left


def flip_edge(edge):
    return edge[::-1]

def get_all_variations(edges):
    variations = []
    # All variations of flipped edges
    variations.append([edges[0], edges[1], edges[2], edges[3]])
    # Flip vertical
    variations.append([edges[2], edges[1][::-1], edges[0], edges[3][::-1]])
    # Flip horizontal
    variations.append([edges[0][::-1], edges[3], edges[2][::-1], edges[1]])
    return variations


def get_adjacent_tiles(tile_edge_options):
    seen = set()
    adjacent_tiles = []
    for id, options in tile_edge_options.items():
        for id2, options2 in tile_edge_options.items():
            if id == id2:
                continue
            for optIdx, option in enumerate(options):
                for opt2Idx, option2 in enumerate(options2):
                    matches = [edge in option2 for edge in option]
                    if sum(matches) == 1:
                        if (id, id2) not in seen:
                            seen.add((id, id2))
                            seen.add((id2, id))
                            adjacent_tiles.append((id, id2, [optIdx, opt2Idx, matches.index(True)]))

    return adjacent_tiles


def part1(data):
    tiles = parse_data(data)

    tile_edge_options = {}
    for id, tile in tiles.items():
        tile_edge_options[id] = get_all_variations(get_edges(tile))


    adjacent_tiles = get_adjacent_tiles(tile_edge_options)
    
    tile_matches = Counter(tile for pair in adjacent_tiles for tile in set(pair[:2]))
    
    corner_tiles = [tile for tile, matches in tile_matches.items() if matches == 2]
    edge_tiles = [tile for tile, matches in tile_matches.items() if matches == 3]
    middle_tiles = [tile for tile, matches in tile_matches.items() if matches == 4]

    res = 1
    for tile, matches in tile_matches.items():
        if matches == 2:
            res *= tile

    return res


def part2(data):
    return -1


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
