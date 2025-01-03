def parse_lines_of_text(input):
    return input.strip().split("\n")


def parse_grid(input):
    return [list(x) for x in input.strip().split("\n")]


def print_grid(grid):
    for row in grid:
        print("".join(row))
