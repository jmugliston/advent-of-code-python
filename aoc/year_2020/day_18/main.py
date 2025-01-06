import os
import argparse


# Evaluate left to right
def calculate(input):
    def eval_expr(expr):
        total = 0
        current = 0
        op = "+"
        for char in expr:
            if char.isdigit():
                current = current * 10 + int(char)
            elif char in "+*":
                total = total + current if op == "+" else total * current
                op = char
                current = 0
        return total + current if op == "+" else total * current

    while "(" in input:
        start = input.rfind("(")
        end = input.find(")", start)
        input = input[:start] + str(eval_expr(input[start + 1:end])) + input[end + 1:]

    return eval_expr(input)

# Evaluate addition before multiplication
def calculate_alt(input):
    def eval_addition(expression):
        parts = expression.split('+')
        return sum(int(part) for part in parts)

    i = 0
    while "(" in input:
        start = input.rfind("(")
        end = input.find(")", start)
        input = input[:start] + str(calculate_alt(input[start + 1:end])) + input[end + 1:]

    parts = input.split('*')
    res = 1
    for part in parts:
        res *= eval_addition(part)
    
    return res


def part1(data):
    input = [x.replace(" ", "") for x in data.strip().split("\n")]
    return sum(calculate(line) for line in input)


def part2(data):
    input = [x.replace(" ", "") for x in data.strip().split("\n")]
    return sum(calculate_alt(line) for line in input)


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
