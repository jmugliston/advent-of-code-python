import os
import argparse

def parse_data(data):
    instructions_raw = data.strip().split("\n")
    instructions = []
    for instruction in instructions_raw:
        op, arg = instruction.split(" ")
        instructions.append((op, int(arg)))
    return instructions

def run_program(instructions):
    acc = 0
    pointer = 0
    visited = set()

    while pointer not in visited:
        visited.add(pointer)
        op, arg = instructions[pointer]
        if op == "acc":
            acc += arg
            pointer += 1
        elif op == "jmp":
            pointer += arg
        elif op == "nop":
            pointer += 1

        if pointer == len(instructions):
            return acc, True

    return acc, False

def part1(data):
    instructions = parse_data(data)

    acc, _ = run_program(instructions)

    return acc


def part2(data):
    instructions = parse_data(data)

    for i, (op, arg) in enumerate(instructions):
        if op == "acc":
            continue

        new_instructions = instructions.copy()
        new_instructions[i] = ("nop", arg) if op == "jmp" else ("jmp", arg)

        acc, finished = run_program(new_instructions)
        if finished:
            return acc


    return None


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
