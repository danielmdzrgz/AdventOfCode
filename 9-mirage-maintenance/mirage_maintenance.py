"""
Advent of Code 2023
Day 9: Mirage Maintenance

Problem description: https://adventofcode.com/2023/day/9
"""

from typing import List
from rich.console import Console
import typer as ty

CONSOLE = Console()


def parse_input(input_file: str) -> List[List[int]]:
    """Parse input file into movements and a network"""
    with open(input_file, "r", encoding="utf8") as f:
        data = f.read()
        data = data.split("\n")

    return [[int(num) for num in line.split(" ")] for line in data]


def part_one(data: List[List[int]]) -> None:
    """Part one of day 9 problem"""
    extrapolated_values: List[int] = []
    for history in data:
        differences: List[int] = []
        extrapolated_value = 0
        for i in range(len(history) - 1):
            differences.append(history[i + 1] - history[i])

        difference_step: List[List[int]] = [differences]
        while any(value != 0 for value in differences):
            next_differences: List[int] = []
            for i in range(len(differences) - 1):
                next_differences.append(differences[i + 1] - differences[i])

            differences = next_differences
            difference_step.append(differences)

        for i in range(len(difference_step) - 2, -1, -1):
            extrapolated_value += difference_step[i][-1]

        extrapolated_values.append(extrapolated_value + history[-1])

    values_sum = 0
    for value in extrapolated_values:
        values_sum += value

    CONSOLE.print(f"[PART 1] Sum of extrapolated values: {values_sum}")


def part_two(data: List[List[int]]) -> None:
    """Part two of day 9 problem"""
    extrapolated_values: List[int] = []
    for history in data:
        differences: List[int] = []
        extrapolated_value = 0
        for i in range(len(history) - 1):
            differences.append(history[i + 1] - history[i])

        difference_step: List[List[int]] = [differences]
        while any(value != 0 for value in differences):
            next_differences: List[int] = []
            for i in range(len(differences) - 1):
                next_differences.append(differences[i + 1] - differences[i])

            differences = next_differences
            difference_step.append(differences)

        sign = 1 if len(difference_step) % 2 != 0 else -1
        for i in range(len(difference_step) - 2, -1, -1):
            extrapolated_value += difference_step[i][0] * sign
            sign *= -1

        extrapolated_values.append(history[0] + extrapolated_value)

    values_sum = 0
    for value in extrapolated_values:
        values_sum += value

    CONSOLE.print(f"[PART 2] Sum of backward-extrapolated values: {values_sum}")


def main(input_file: str = ty.Argument(..., help="Input file with problem input")):
    """Main function for day 9 problem"""
    data = parse_input(input_file)
    part_one(data)
    part_two(data)


if __name__ == "__main__":
    ty.run(main)
