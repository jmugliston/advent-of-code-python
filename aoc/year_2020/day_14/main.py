import os
import argparse

def parse_data(data):
    data = data.strip().split("\n")
    instructions = []
    for line in data:
        if line.startswith("mask"):
            instructions.append(("mask", line.split(" = ")[1]))
            continue
        split = line.split(" = ")
        mem_address = split[0].split("[")[1][:-1]
        mem_value = int(split[1])
        instructions.append((mem_address, mem_value))
    return instructions


def apply_mask(mask, value):
    value = list(bin(value)[2:].zfill(len(mask)))
    for i, bit in enumerate(mask):
        if bit != "X":
            value[i] = bit
    return "".join(value)

def apply_memory_mask(mask, value):
    value = list(bin(value)[2:].zfill(len(mask)))
    for i, bit in enumerate(mask):
        if bit != "0":
            value[i] = bit

    x_count = value.count("X")

    # Generate all possible combinations of the floating bits
    options = []
    for i in range(2 ** x_count):
        options.append(bin(i)[2:].zfill(x_count))

    addresses = []
    for option in options:
        address = value[:]
        for bit in option:
            address[address.index("X")] = bit
        addresses.append("".join(address))
        

    return addresses


def part1(data):
    instructions = parse_data(data)

    mask = ""
    memory = {}
    for mem_address, mem_value in instructions:
        if mem_address == "mask":
            mask = mem_value
            continue
        memory[mem_address] = apply_mask(mask, mem_value)

    return sum(int(value, 2) for value in memory.values())


def part2(data):
    instructions = parse_data(data)

    mask = ""
    memory = {}
    for mem_address, mem_value in instructions:
        if mem_address == "mask":
            mask = mem_value
            continue
        memory_locations = apply_memory_mask(mask, int(mem_address))
        for location in memory_locations:
            memory[location] = "".join(bin(mem_value)[2:].zfill(len(mask)))

    return sum(int(value, 2) for value in memory.values())



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
