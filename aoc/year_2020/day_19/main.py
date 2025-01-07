import os
import argparse

def parse_data(data):
    split = data.split('\n\n')

    rules = {}
    for line in split[0].split('\n'):
        if not line:
            break

        rule_id, options = line.split(': ')
        rule_id = int(rule_id)

        if '"' in options:
            rule = options[1:-1]
        else:
            rule = []
            for option in options.split('|'):
                rule.append(list(map(int, option.split())))

        rules[rule_id] = rule
		
    messages = split[1].split('\n')

    return rules, messages


def check_rule(rules, message, rule=0, pos=0):
    if pos == len(message):
        return []

    rule = rules[rule]
    if type(rule) is str:
        if message[pos] == rule:
            return [pos + 1]
        return []

    matches = []
    for option in rule:
        sub_matches = [pos]
        for sub_rule in option:
            new_matches = []
            for idx in sub_matches:
                new_matches += check_rule(rules, message, sub_rule, idx)
            sub_matches = new_matches

        matches += sub_matches

    return matches


def part1(data):
    rules, messages = parse_data(data)

    valid_messages = 0
    for message in messages:
        if len(message) in check_rule(rules, message):
            valid_messages += 1

    return valid_messages


def part2(data):
    rules, messages = parse_data(data)

    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]

    valid_messages = 0
    for message in messages:
        if len(message) in check_rule(rules, message):
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

