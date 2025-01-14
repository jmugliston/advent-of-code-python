import os
import argparse


def simulate_moves(labels, moves):
    linked_list = {}
    for i in range(len(labels)):
        linked_list[labels[i]] = labels[(i + 1) % len(labels)]

    current = labels[0]
    for _ in range(moves):
        pick_up = []
        next_cup = current
        for _ in range(3):
            next_cup = linked_list[next_cup]
            pick_up.append(next_cup)

        destination = current - 1
        while destination in pick_up or destination < 1:
            destination -= 1
            if destination < 1:
                destination = max(labels)

        # Link the current cup to the cup after the pick up
        linked_list[current] = linked_list[pick_up[-1]]
        # Link the last pick up cup to the cup after the destination
        linked_list[pick_up[-1]] = linked_list[destination]
        # Link the destination cup to the first pick up cup
        linked_list[destination] = pick_up[0]

        # The current cup is now the cup after the current cup
        current = linked_list[current]

    res = []
    next_cup = 1
    for _ in range(len(labels) - 1):
        next_cup = linked_list[next_cup]
        res.append(next_cup)

    return res

def part1(data):
    labels = [int(label) for label in data.strip()]

    linked_list = {}
    for i in range(len(labels)):
        linked_list[labels[i]] = labels[(i + 1) % len(labels)]

    result = simulate_moves(labels, 100)

    return "".join(map(str, result))


def part2(data, example=False):
    num = 1_000_000

    if example:
        # Reduce size for example (otheriwse tests are quite slow)
        num = 100

    labels = [int(label) for label in data.strip()]

    max_label = max(labels)
    
    labels += list(range(max_label + 1, max_label + num - len(labels) + 1))

    result = simulate_moves(labels, num*10)

    return result[0] * result[1]


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
