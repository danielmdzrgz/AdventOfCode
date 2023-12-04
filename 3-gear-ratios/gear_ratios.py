"""
Advent of Code 2023
Day 3: Gear Ratios

Problem description: https://adventofcode.com/2023/day/3
"""

import math
import re

from rich.console import Console
import typer as ty

CONSOLE = Console()


def parse_input(input_file: str) -> list[int]:
    """Parse input file into a list of numbers"""
    with open(input_file, "r", encoding="utf8") as f:
        data = f.read()
        data = data.split("\n")

    rows = len(data)
    cols = len(data[0])
    symbols = {
        (row, col): (data[row][col], [])
        for row in range(rows)
        for col in range(cols)
        if data[row][col] not in "0123456789."
    }

    for line, row in enumerate(data):
        for number in re.finditer(r"\d+", row):
            edge = {
                (line, col)
                for line in (line - 1, line, line + 1)
                for col in range(number.start() - 1, number.end() + 1)
            }

            # Makes union between edge and symbols keys to get the symbols that are in the edge
            for symbol in edge & symbols.keys():
                symbols[symbol][1].append(int(number.group()))

    CONSOLE.print(symbols)
    return symbols


def part_one(data) -> None:
    """Part one of day 3 problem"""
    engine_parts_sum = sum(sum(numbers[1]) for numbers in data.values())
    CONSOLE.print(f"[PART 1] Final engine parts sum: {engine_parts_sum}")


def part_two(data: list[list[str]]) -> None:
    """Part two of day 3 problem"""
    gear_ratios = sum(
        math.prod(numbers[1])
        for numbers in data.values()
        if numbers[0] == "*" and len(numbers[1]) == 2
    )
    CONSOLE.print(f"[PART 2] Final gear ratios: {gear_ratios}")


def main(input_file: str = ty.Argument(..., help="Input file with problem input")):
    """Main function for day 2 problem"""
    data = parse_input(input_file)
    part_one(data)
    part_two(data)


if __name__ == "__main__":
    ty.run(main)
