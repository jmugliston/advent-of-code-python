import os
import argparse

def parse_data(data):
    bags_raw = data.strip().split("\n")
    bags = {}
    for bag in bags_raw:
        bag = bag.split(" contain ")
        bag_name = bag[0][:-5]
        if bag[1] == "no other bags.":
            bags[bag_name] = []
        else:
            inner_bags_raw = bag[1].split(", ")
            inner_bags = []
            for inner_bag in inner_bags_raw:
                inner_bag = inner_bag.split(" ")
                inner_bags.append((int(inner_bag[0]), " ".join(inner_bag[1:-1])))

            bags[bag_name] = inner_bags
    return bags


def check_bag(bags, bag):
    if not bags[bag]:
        return False
    for inner_bag in bags[bag]:
        if inner_bag[1] == "shiny gold" or check_bag(bags, inner_bag[1]):
            return True
    return False

def count_bags(bags, bag):
    if not bags[bag]:
        return 0
    count = 0
    for inner_bag in bags[bag]:
        next_bags = count_bags(bags, inner_bag[1])
        count += inner_bag[0] + inner_bag[0] * next_bags
    return count

def part1(data):
    bags = parse_data(data)
    return sum([check_bag(bags, bag) for bag in bags])


def part2(data):
    bags = parse_data(data)
    return count_bags(bags, "shiny gold")


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
