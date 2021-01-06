from typing import Dict, List, Set

from utils import elapsed_time, print_results


class Food:
    def __init__(self, line: str):
        self._init_line = line.strip()
        ingredients_str, allergens_str = line.strip().split(' (contains ')
        self.ingredients: Set[str] = set(ingredients_str.split())
        self.allergens: Set[str] = set(allergens_str.strip(')').split(', '))

    def __repr__(self):
        return f"{__class__.__name__}('{self._init_line}')"


def read_foods(filename: str) -> List[Food]:
    return [Food(line) for line in open(filename)]


def part1(filename: str) -> int:
    foods = read_foods(filename)
    allergens: Set[str] = set.union(*(food.allergens for food in foods))
    todo: Set[str] = allergens.copy()
    solved: Dict[str, str] = {}
    while todo:
        print(f"{len(todo)} allergens remaining to identify...")
        allergen = todo.pop()
        print(f"working on '{allergen}'...")
        possible_ingredients: Set[str] = set.intersection(*(
            food.ingredients
            for food in foods
            if allergen in food.allergens
        ))
        possible_ingredients.difference_update(solved)
        if len(possible_ingredients) == 1:
            solved[possible_ingredients.pop()] = allergen
        else:
            todo.add(allergen)
    return sum(ingredient not in solved
               for food in foods
               for ingredient in food.ingredients)


def part2(filename: str) -> int:
    pass


if __name__ == '__main__':
    puzzle_input = 'input_day21.txt'
    print_results(elapsed_time(part1, puzzle_input),  # 2573
                  elapsed_time(part2, puzzle_input))
