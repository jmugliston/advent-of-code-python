import os
import argparse

def parse_input(data):
    lines = data.strip().split("\n")

    player_1 = []
    player_2 = []

    player = player_1
    for line in lines:
        if line == "Player 1:":
            player = player_1
        elif line == "Player 2:":
            player = player_2
        elif line == "":
            continue
        else:
            player.append(int(line))

    return player_1, player_2


def calculate_score(player):
    score = 0
    for i, card in enumerate(player):
        score += card * (len(player) - i)
    return score


def play_game(player_1, player_2):
    while len(player_1) > 0 and len(player_2) > 0:
        player_1_card = player_1.pop(0)
        player_2_card = player_2.pop(0)

        if player_1_card > player_2_card:
            player_1.append(player_1_card)
            player_1.append(player_2_card)
        else:
            player_2.append(player_2_card)
            player_2.append(player_1_card)

    winning_player = player_1 if len(player_1) > 0 else player_2

    score = calculate_score(winning_player)
    
    return 1 if player_1 else 2, score


def part1(data):
    player_1, player_2 = parse_input(data)

    _, score = play_game(player_1, player_2)

    return score


cache = {}

def play_recursive_game(player_1, player_2):
    if (tuple(player_1), tuple(player_2)) in cache:
        return cache[(tuple(player_1), tuple(player_2))]

    previous_rounds = set()
    while player_1 and player_2:
        if (tuple(player_1), tuple(player_2)) in previous_rounds:
            cache[(tuple(player_1), tuple(player_2))] = (1, calculate_score(player_1))
            return 1, calculate_score(player_1)
        previous_rounds.add((tuple(player_1), tuple(player_2)))

        player_1_card, player_2_card = player_1.pop(0), player_2.pop(0)

        if len(player_1) >= player_1_card and len(player_2) >= player_2_card:
            winner, _ = play_recursive_game(player_1[:player_1_card], player_2[:player_2_card])
        else:
            winner = 1 if player_1_card > player_2_card else 2

        if winner == 1:
            player_1.extend([player_1_card, player_2_card])
        else:
            player_2.extend([player_2_card, player_1_card])

    winner = 1 if player_1 else 2

    score = calculate_score(player_1 if player_1 else player_2)

    cache[(tuple(player_1), tuple(player_2))] = (winner, score)

    return winner, score

def part2(data):
    player_1, player_2 = parse_input(data)
    
    _, score = play_recursive_game(player_1, player_2)

    return score


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
