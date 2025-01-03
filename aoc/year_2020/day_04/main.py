import os
import argparse

def parse_data(data):
    return [
        dict(field.split(":") for field in passport_raw.split())
        for passport_raw in data.split("\n\n")
    ]

def part1(data):
    passports = parse_data(data)

    num_valid = 0
    required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    for passport in passports:
        if required_fields.issubset(passport):
            num_valid += 1

    return num_valid


def part2(data):
    passports = parse_data(data)

    num_valid = 0

    validation_rules = {
        "byr": lambda x: 1920 <= int(x) <= 2002,
        "iyr": lambda x: 2010 <= int(x) <= 2020,
        "eyr": lambda x: 2020 <= int(x) <= 2030,
        "hgt": lambda x: x[:-2].isdigit() and int(x[:-2]) >= 150 and int(x[:-2]) <= 193 if x.endswith("cm") else x[:-2].isdigit() and int(x[:-2]) >= 59 and int(x[:-2]) <= 76 if x.endswith("in") else False,
        "hcl": lambda x: x[0] == "#" and len(x) == 7 and all(c in "0123456789abcdef" for c in x[1:]),
        "ecl": lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
        "pid": lambda x: x.isdigit() and len(x) == 9,
        "cid": lambda x: True,
    }

    for passport in passports:
        if all(field in passport and rule(passport[field]) for field, rule in validation_rules.items() if field != "cid"):
            num_valid += 1

    return num_valid


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
