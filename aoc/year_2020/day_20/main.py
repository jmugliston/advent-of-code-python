import os
import argparse
import math

def parse_data(data):
    raw_tiles = data.strip().split("\n\n")

    tiles = {}
    for raw_tile in raw_tiles:
        split_tile = raw_tile.split("\n")
        id = int(split_tile[0].split(" ")[1][:-1])
        tile = list(split_tile[1:])
        tiles[id] = tile

    return tiles


'''
Return top, right, bottom, left edges of a tile
'''
def get_edges(tile):
    return tile[0], "".join(row[-1] for row in tile), tile[-1], "".join(row[0] for row in tile)


'''
Return all the variations of rotating/flipping a tile
'''
def get_edge_options(edges):
    variations = []
    # All variations of flipped edges
    variations.append([edges[0], edges[1], edges[2], edges[3]])
    # Flip vertical
    variations.append([edges[2], edges[1][::-1], edges[0], edges[3][::-1]])
    # Flip horizontal
    variations.append([edges[0][::-1], edges[3], edges[2][::-1], edges[1]])
    return variations


'''
Return a map of all the adjacent tiles
'''
def get_adjacent_tiles(tiles):
    tile_edge_options = {}
    for id, tile in tiles.items():
        edges = get_edges(tile)
        tile_edge_options[id] = get_edge_options(edges)

    seen = set()
    adjacent_tile_map = {}
    for id, options in tile_edge_options.items():
        for id2, options2 in tile_edge_options.items():
            if id == id2:
                continue
            for option in options:
                for option2 in options2:
                    matches = [edge in option2 for edge in option]
                    if sum(matches) == 1:
                        if (id, id2) not in seen and (id2, id) not in seen:
                            seen.add((id, id2))
                            adjacent_tile_map.setdefault(id, []).append(id2)
                            adjacent_tile_map.setdefault(id2, []).append(id)

    return adjacent_tile_map


'''
Return a neested list of tile ids in the correct positions
e.g. [[1, 2], [3, 4]] would be a 2x2 grid with tile 1 in the top left, 2 in the top right, 3 in the bottom left, and 4 in the bottom right
'''
def place_tiles(start, adjacent_tile_map, tiles):
    positions = [[None for _ in range(int(math.sqrt(len(tiles))))] for _ in range(int(math.sqrt(len(tiles))))]

    # Place the top left corner
    positions[0][0] = start
    positions[0][1] = adjacent_tile_map[start][0]
    positions[1][0] = adjacent_tile_map[start][1]

    placed = set()
    placed.add(start)
    placed.add(positions[0][1])
    placed.add(positions[1][0])

    remaining = [x for x in tiles if x not in [start, positions[0][1], positions[1][0]]]

    while len(remaining) > 0:
        for x in range(len(positions)):
            for y in range(len(positions[x])):
                if positions[x][y] is None:
                    neighbours = [
                        positions[x-1][y] if x > 0 else None,
                        positions[x][y-1] if y > 0 else None,
                        positions[x+1][y] if x < len(positions) - 1 else None,
                        positions[x][y+1] if y < len(positions[x]) - 1 else None
                    ]
                    neighbours = [n for n in neighbours if n is not None]
                    
                    adj_neighbour_sets = []
                    for neighbour in neighbours:
                        adj_neighbours_not_placed = [x for x in adjacent_tile_map[neighbour] if x not in placed]
                        adj_neighbour_sets.append(adj_neighbours_not_placed)
                    
                    if len(adj_neighbour_sets) == 0:
                        continue

                    common_neighbours = set.intersection(*map(set, adj_neighbour_sets))

                    if len(common_neighbours) == 1:
                        next_placement = common_neighbours.pop()
                        positions[x][y] = next_placement
                        placed.add(next_placement)
                        remaining.remove(next_placement)
    

    # Now that we have mapped the position of all the tiles, we can get the actual tiles

    tile_positions = [[None for _ in range(int(math.sqrt(len(tiles))))] for _ in range(int(math.sqrt(len(tiles))))]

    for y in range(len(positions)):
        for x in range(len(positions[y])):
            tile_positions[y][x] = tiles[positions[y][x]]

    return tile_positions


'''
Rotate a tile n times (90 degrees clockwise)
'''
def rotate_tile(tile, rotations):
    for _ in range(rotations):
        tile = ["".join(row) for row in zip(*tile[::-1])]
    return tile


'''
Return all the variations of rotating/flipping a tile
'''
def get_tile_options(tile):
    options = []

    for i in range(4):
        rotated = rotate_tile(tile.copy(), i)
        flipped_horizontally = [row[::-1] for row in rotated]
        flipped_vertically = rotated[::-1]
        options.append(rotated)
        options.append(flipped_horizontally)
        options.append(flipped_vertically)
    
    return options


'''
Check if the edges of two tiles match
'''
def does_edge_match(tile1, tile2, edge):
    if edge == "top":
        return tile1[0] == tile2[-1]
    elif edge == "bottom":
        return tile1[-1] == tile2[0]
    elif edge == "left":
        return "".join([row[0] for row in tile1]) == "".join([row[-1] for row in tile2])
    elif edge == "right":
        return "".join([row[-1] for row in tile1]) == "".join([row[0] for row in tile2])


'''
Combine the tiles into a single image (without borders)
'''
def make_image_from_tiles(tiles):
    image = ""
    
    for tile_row in tiles:
        row = ""
        for i in range(len(tiles[0][0])-2):
            for tile in tile_row:
                row += tile[i+1][1:-1]
            row += "\n"
        image += row

    return image


'''
Set the correct rotation/flip for the corners (and adjacent tiles)
'''
def set_corners(tile_positions):
    corners = [
        (0, 0, "right", "bottom"),
        (0, -1, "left", "bottom"),
        (-1, 0, "right", "top"),
        (-1, -1, "left", "top")
    ]

    for y, x, edge1, edge2 in corners:
        for option1 in get_tile_options(tile_positions[y][x]):
            for option2 in get_tile_options(tile_positions[y][x + (1 if x == 0 else -1)]):
                for option3 in get_tile_options(tile_positions[y + (1 if y == 0 else -1)][x]):
                    if does_edge_match(option1, option2, edge1) and does_edge_match(option1, option3, edge2):
                        tile_positions[y][x] = option1
                        tile_positions[y][x + (1 if x == 0 else -1)] = option2
                        tile_positions[y + (1 if y == 0 else -1)][x] = option3
                        break

'''
Set the remaining positions (after corners have been set)
'''
def set_remaining_positions(tile_positions):
    max = len(tile_positions[0]) - 1

    # Corner positions are already set
    set_positions = [
        (0, 0),
        (0, max),
        (max, 0),
        (max, max)
    ]

    for y in range(len(tile_positions)):
        for x in range(len(tile_positions[y])):
            if (y, x) in set_positions:
                continue

            # Get neighbours that have been set already
            neighbours = [
                (y-1, x) if y > 0 else None,
                (y, x-1) if x > 0 else None,
                (y+1, x) if y < len(tile_positions) - 1 else None,
                (y, x+1) if x < len(tile_positions[y]) - 1 else None
            ]
            set_neighbours = [n for n in neighbours if n in set_positions]

            # Match the edge to each set neighbour
            for set_neighbour in set_neighbours:
                edge_to_match = "top" if set_neighbour[0] < y else "bottom" if set_neighbour[0] > y else "left" if set_neighbour[1] < x else "right"
                for option in get_tile_options(tile_positions[y][x]):
                    set_option = tile_positions[set_neighbour[0]][set_neighbour[1]]
                    if does_edge_match(option, set_option, edge_to_match):
                        tile_positions[y][x] = option
                        set_positions.append((y, x))
                        break

'''
Find sea monsters in the image
'''
def find_sea_monsters(image):
    image = [list(row) for row in image]

    sea_monster = [
        "                  # ",
        "#    ##    ##    ###",
        " #  #  #  #  #  #   "
    ]

    sea_monster_positions = []
    for y in range(len(image) - len(sea_monster)):
        for x in range(len(image[y]) - len(sea_monster[0])):
            found = True
            for y2 in range(len(sea_monster)):
                for x2 in range(len(sea_monster[y2])):
                    if sea_monster[y2][x2] == "#" and image[y + y2][x + x2] != "#":
                        found = False
                        break
                if not found:
                    break
            if found:
                sea_monster_positions.append((y, x))
    
    return sea_monster_positions


def part1(data):
    tiles = parse_data(data)

    adjacent_tile_map = get_adjacent_tiles(tiles)

    corners = [x for x in adjacent_tile_map if len(adjacent_tile_map[x]) == 2]

    return corners[0] * corners[1] * corners[2] * corners[3]


def part2(data):
    tiles = parse_data(data)

    adjacent_tile_map = get_adjacent_tiles(tiles)

    corners = [x for x in adjacent_tile_map if len(adjacent_tile_map[x]) == 2]
    
    tile_positions = place_tiles(corners[0], adjacent_tile_map, tiles)

    set_corners(tile_positions)

    set_remaining_positions(tile_positions)

    image = make_image_from_tiles(tile_positions)

    options = get_tile_options(image.strip().split("\n"))

    water_roughness = 0
    for option in options:
        sea_monsters = len(find_sea_monsters(option))
        if sea_monsters > 0:
            total_hashes = sum([row.count("#") for row in option])
            water_roughness = total_hashes - (sea_monsters * 15)
            break

    return water_roughness


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
