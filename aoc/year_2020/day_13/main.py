import os
import argparse

def part1(data):
    data = data.strip().split("\n")
    t = int(data[0])
    buses = [int(x) for x in data[1].split(",") if x != "x"]

    min_wait = float("inf")
    min_bus = None
    for bus in buses:
        wait = bus - (t % bus)
        if wait < min_wait:
            min_wait = wait
            min_bus = bus

    return min_wait * min_bus


def part2(data):
    data = data.strip().split("\n")
    buses = [(i, int(x)) for i, x in enumerate(data[1].split(",")) if x != "x"]

    d = 1
    i = 0
    for idx, bus in buses:
        while True:
            i += d
            if (i + idx) % bus == 0:
                d = d * bus
                break

    return i
        


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
