"""
Advent of Code 2023
Day 2: Cube Conundrum

Problem description: https://adventofcode.com/2023/day/2
"""

import typer as ty
from rich.console import Console

CONSOLE = Console()
BAG_CONFIG: dict[str, int] = {"red": 12, "green": 13, "blue": 14}


def parse_input(input_file: str) -> list[dict[str, list[int]]]:
    """Parse input file into a list of dicts with game results"""
    with open(input_file, "r", encoding="utf8") as f:
        data = f.read()
        data = data.split("\n")
        parsed_data = []
        for line in data:
            line = line.split(":")[1]
            line = line.replace(";", "").replace(",", "").split(" ")
            game_results: dict[str, list[int]] = {"red": [], "green": [], "blue": []}
            for i in range(1, len(line), 2):
                game_results[line[i + 1]].append(int(line[i]))

            parsed_data.append(game_results)

        return parsed_data


def part_one(data: list[dict[str, list[int]]]) -> None:
    """Part one of day 2 problem"""
    valid_id_sum = 0
    for game in enumerate(data):
        for color, max_value in BAG_CONFIG.items():
            if any(value > max_value for value in game[1][color]):
                break

        else:
            # CONSOLE.print(f"Game {game[0]+1} is valid")
            valid_id_sum += game[0] + 1

    CONSOLE.print(f"[PART 1] Final valid games ID sum: {valid_id_sum}")


def part_two(data: list[dict[str, list[int]]]) -> None:
    """Part two of day 2 problem"""
    power_sum = 0
    for line in data:
        mins = [max(color) for color in line.values()]
        # CONSOLE.print(f"Minimum number of cubes needed to play game: {mins}")
        power_sum += mins[0] * mins[1] * mins[2]

    CONSOLE.print(f"[PART 2] Final power sum: {power_sum}")


def main(input_file: str = ty.Argument(..., help="Input file with problem input")):
    """Main function for day 2 problem"""
    data = parse_input(input_file)
    part_one(data)
    part_two(data)


if __name__ == "__main__":
    ty.run(main)
