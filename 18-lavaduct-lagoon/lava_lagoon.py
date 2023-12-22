"""
Advent of Code 2023
Day 18: Lavaduct Lagoon

Problem description: https://adventofcode.com/2023/day/18
"""

from typing import List, Tuple

from rich.console import Console
import typer as ty

CONSOLE = Console()
POSSIBLE_DIRECTIONS = {
    "U": complex(-1, 0),
    "D": complex(1, 0),
    "L": complex(0, -1),
    "R": complex(0, 1),
}
DIRECTION_CODIFICATION = {"0": "R", "1": "D", "2": "L", "3": "U"}


def parse_input(input_file: str) -> List[Tuple[str, int, str]]:
    """Parse input file into a list with the digging instructions"""
    with open(input_file, "r", encoding="utf8") as f:
        data = f.read()

    data = data.split("\n")
    return [
        (row.split(" ")[0], int(row.split(" ")[1]), row.split(" ")[2][1:-1])
        for row in data
    ]


def part_one(data: List[Tuple[str, int, str]]) -> None:
    """Part one of day 18 problem"""
    trench_positions: List[complex] = [complex(0, 0)]
    border_length = 0
    for instruction in data:
        direction, distance, _ = instruction
        border_length += distance
        movement = POSSIBLE_DIRECTIONS[direction] * distance
        trench_positions.append(trench_positions[-1] + movement)

    trench_area = (
        sum(
            x.real * y.imag - x.imag * y.real
            for x, y in zip(trench_positions, trench_positions[1:])
        )
        / 2
    )
    lagoon_interior = int(abs(trench_area) + 1 - (0.5 * border_length))
    lagoon_area = lagoon_interior + border_length
    CONSOLE.print(f"[PART 1] Cubic meters of lava: {lagoon_area}")


def part_two(data: List[Tuple[str, int, str]]) -> None:
    """Part two of day 18 problem"""
    decoded_instructions: List[Tuple[str, int]] = []
    for instruction in data:
        _, _, code = instruction
        distance_code = code[1:-1]
        direction_code = code[-1]
        direction = DIRECTION_CODIFICATION[direction_code]
        distance = int(distance_code, 16)
        decoded_instructions.append((direction, distance))


    trench_positions: List[complex] = [complex(0, 0)]
    border_length = 0
    for instruction in decoded_instructions:
        direction, distance = instruction
        border_length += distance
        movement = POSSIBLE_DIRECTIONS[direction] * distance
        trench_positions.append(trench_positions[-1] + movement)

    trench_area = (
        sum(
            x.real * y.imag - x.imag * y.real
            for x, y in zip(trench_positions, trench_positions[1:])
        )
        / 2
    )
    lagoon_interior = int(abs(trench_area) + 1 - (0.5 * border_length))
    lagoon_area = lagoon_interior + border_length
    CONSOLE.print(f"[PART 1] Cubic meters of lava: {lagoon_area}")


def main(input_file: str = ty.Argument(..., help="Input file with problem input")):
    """Main function for day 18 problem"""
    data = parse_input(input_file)
    part_one(data)
    part_two(data)


if __name__ == "__main__":
    ty.run(main)
