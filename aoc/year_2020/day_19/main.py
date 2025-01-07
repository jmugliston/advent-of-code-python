import os
import argparse

def parse_data(data):
    split = data.strip().split("\n\n")

    rules = {}
    for rule in split[0].split("\n"):
        key, value = rule.split(": ")

        if "|" in value:
            value = value.split(" | ")
            a = value[0].split(" ")
            b = value[1].split(" ")
            value = [a, b]
        else:
            value = value.replace('"', "").split(" ")

        rules[key] = value

    messages = split[1].split("\n")

    return rules, messages

def check_rule(rules, message, current_rule, pos=0):
    if pos >= len(message):
        return False, pos

    if len(current_rule) == 1 and current_rule[0] in ["a", "b"]:
        if pos < len(message) and message[pos] == current_rule[0]:
            return True, pos + 1
        else:
            return False, pos

    if all(isinstance(sub_rule, list) for sub_rule in current_rule):
        for sub_rule in current_rule:
            valid, new_pos = check_rule(rules, message, sub_rule, pos)
            if valid:
                return True, new_pos
        return False, pos

    initial_pos = pos
    for rule in current_rule:
        valid, pos = check_rule(rules, message, rules[rule], pos)
        if not valid:
            return False, initial_pos

    return True, pos


def part1(data):
    rules, messages = parse_data(data)

    start_rule = rules["0"]

    valid_messages = 0
    for message in messages:
        is_valid, final_idx = check_rule(rules, message, start_rule)
        if final_idx < len(message):
            is_valid = False
        if is_valid:
            valid_messages += 1

    return valid_messages


def part2(data):
    rules, messages = parse_data(data)

    rules["8"] = [["42"], ["42", "8"]]
    rules["11"] = [["42", "31"], ["42", "11", "31"]]

    start_rule = rules["0"]

    valid_messages = 0
    for message in messages:
        is_valid, final_idx = check_rule(rules, message, start_rule)
        if final_idx < len(message):
            is_valid = False
        if is_valid:
            valid_messages += 1

    return valid_messages


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

