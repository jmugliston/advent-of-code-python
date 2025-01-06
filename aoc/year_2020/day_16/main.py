import os
import argparse
from itertools import permutations

def parse_data(data):
    sections = data.strip().split("\n\n")
    fields = {
        field.split(": ")[0]: [list(map(int, r.split("-"))) for r in field.split(": ")[1].split(" or ")]
        for field in sections[0].split("\n")
    }
    your_ticket = list(map(int, sections[1].split("\n")[1].split(",")))
    nearby_tickets = [list(map(int, ticket.split(","))) for ticket in sections[2].split("\n")[1:]]
    return fields, your_ticket, nearby_tickets


def invalid_tickets(fields, tickets):
    invalid_tickets = []
    invalid_nums = []
    for idx, ticket in enumerate(tickets):
        for value in ticket:
            valid = False
            for ranges in fields.values():
                for r in ranges:
                    if r[0] <= value <= r[1]:
                        valid = True
                        break
            if not valid:
                invalid_tickets.append(idx)
                invalid_nums.append(value)

    return invalid_tickets, invalid_nums


def part1(data):
    fields, _, nearby_tickets = parse_data(data)
    _, invalid_nums = invalid_tickets(fields, nearby_tickets)
    return sum(invalid_nums)


def part2(data):
    fields, my_ticket, nearby_tickets = parse_data(data)
    
    invalid, _ = invalid_tickets(fields, nearby_tickets)

    valid = [ticket for idx, ticket in enumerate(nearby_tickets) if idx not in invalid]

    field_list = list(fields.keys())

    # For each valid ticket, get all the values for each position
    field_values = {}
    for ticket in valid:
        for idx, value in enumerate(ticket):
            if idx not in field_values:
                field_values[idx] = []
            field_values[idx].append(value)
    
    # Check each value for each position to see if it could be a certain field
    possible_fields = {}
    for idx, values in field_values.items():
        for field in field_list:
            valid = True
            for value in values:
                ranges = fields[field]
                if not any(r[0] <= value <= r[1] for r in ranges):
                    valid = False
                    break
            if valid:
                if idx not in possible_fields:
                    possible_fields[idx] = []
                possible_fields[idx].append(field)

    while True:
        # Eliminate fields that can't be in a certain position
        for idx, fields in possible_fields.items():
            if len(fields) == 1:
                field = fields[0]
                for i in possible_fields:
                    if i != idx and field in possible_fields[i]:
                        possible_fields[i].remove(field)

        # Check if all fields have been assigned
        if all(len(fields) == 1 for fields in possible_fields.values()):
            break

    departure_field_idxs = [idx for idx, fields in possible_fields.items() if fields[0].startswith("departure")]

    ans = 1
    for idx in departure_field_idxs:
        ans *= my_ticket[idx]
    
    return ans


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
