import os
import argparse

def parse_input(data):
    lines = data.strip().split("\n")

    parsed = []
    for line in lines:
        parts = line.split(" (contains ")
        ingredients = parts[0].split(" ")
        allergens = parts[1][:-1].split(", ")
        parsed.append((ingredients, allergens))

    return parsed

def get_ingredients_without_allergens(ingredients_and_allergens):
    allergen_to_ingredients = {}
    for ingredients, allergens in ingredients_and_allergens:
        for allergen in allergens:
            if allergen not in allergen_to_ingredients:
                allergen_to_ingredients[allergen] = set(ingredients)
            else:
                # Find the intersection of the ingredients that contain the allergen
                allergen_to_ingredients[allergen] &= set(ingredients)

    all_ingredients = set()
    for ingredients, _ in ingredients_and_allergens:
        # Union of all ingredients
        all_ingredients |= set(ingredients)

    # Find the ingredients that do not contain any allergens
    safe_ingredients = all_ingredients.copy()
    for ingredients in allergen_to_ingredients.values():
        safe_ingredients -= ingredients

    return safe_ingredients

def part1(data):
    ingredients_and_allergens = parse_input(data)

    safe_ingredients = get_ingredients_without_allergens(ingredients_and_allergens)

    count = 0
    for ingredients, _ in ingredients_and_allergens:
        for ingredient in ingredients:
            if ingredient in safe_ingredients:
                count += 1

    return count

def part2(data):
    ingredients_and_allergens = parse_input(data)

    safe_ingredients = get_ingredients_without_allergens(ingredients_and_allergens)

    allergen_to_ingredients = {}
    for ingredients, allergens in ingredients_and_allergens:
        for allergen in allergens:
            if allergen in safe_ingredients:
                continue
            if allergen not in allergen_to_ingredients:
                allergen_to_ingredients[allergen] = set(ingredients)
                continue
            # Find the intersection of the ingredients that contain the allergen
            allergen_to_ingredients[allergen] &= set(ingredients)

    # Find the allergen that has only one ingredient
    while any(len(ingredients) > 1 for ingredients in allergen_to_ingredients.values()):
        for allergen, ingredients in allergen_to_ingredients.items():
            if len(ingredients) == 1:
                for other_allergen in allergen_to_ingredients:
                    if other_allergen == allergen:
                        continue
                    allergen_to_ingredients[other_allergen] -= ingredients

    # Sort the allergens and get the ingredients
    allergens = sorted(allergen_to_ingredients.keys())
    ingredients = [allergen_to_ingredients[allergen].pop() for allergen in allergens]

    return ",".join(ingredients)


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
