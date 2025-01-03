def parse_lines_of_text(input):
    return input.split("\n")


def parse_lines_of_numbers(input):
    return [int(x) for x in input.split("\n")]


def parse_grid(input):
    return [list(x) for x in input.split("\n")]
