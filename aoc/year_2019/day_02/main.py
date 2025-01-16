import os
import argparse

def run_program(intcode):
    memory = {}
    instruction_pointer = 0

    for i, value in enumerate(intcode):
        memory[i] = value

    while True:
        opcode = intcode[instruction_pointer]
        if opcode == 99:
            instruction_pointer += 1
            break
        elif opcode == 1:
            a = memory.get(intcode[instruction_pointer + 1], 0)
            b = memory.get(intcode[instruction_pointer + 2], 0)
            memory[intcode[instruction_pointer + 3]] =  a + b
        elif opcode == 2:
            a = memory.get(intcode[instruction_pointer + 1], 0)
            b = memory.get(intcode[instruction_pointer + 2], 0)
            memory[intcode[instruction_pointer + 3]] = a * b

        instruction_pointer += 4
    
    return memory[0]


def set_input(intcode, noun, verb):
    output = intcode.copy()
    output[1] = noun
    output[2] = verb
    return output


def part1(data, example=False):
    intcode = list(map(int, data.strip().split(",")))

    if not example:
        intcode = set_input(intcode, 12, 2)

    return run_program(intcode)


def part2(data):
    intcode = list(map(int, data.strip().split(",")))

    target_output = 19690720

    for i in range(0, 99):
        for j in range(0, 99):
            result = run_program(set_input(intcode, i, j))
            if result == target_output:
                return 100 * i + j
            
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
