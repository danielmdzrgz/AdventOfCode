"""
Advent of Code 2023
Day 11: Cosmic Expansion

Problem description: https://adventofcode.com/2023/day/11
"""

from itertools import combinations
from typing import List

from rich.console import Console
import typer as ty

CONSOLE = Console()


def parse_input(input_file: str) -> List[List[str]]:
    """Parse input file into a grid with the galaxies"""
    with open(input_file, "r", encoding="utf8") as f:
        data = f.read()
    return [list(row) for row in data.split("\n")]


def part_one(data: List[List[str]]) -> None:
    """Part one of day 11 problem"""
    universe_row_expansion = [i for i, row in enumerate(data) if set(row) == {"."}]
    universe_col_expansion = [
        j for j in range(len(data[0])) if {row[j] for row in data} == {"."}
    ]

    galaxy_positions = [
        (x, y) for x, row in enumerate(data) for y, col in enumerate(row) if col == "#"
    ]
    distances: int = 0
    for pair in list(combinations(galaxy_positions, 2)):
        (x1, y1), (x2, y2) = pair
        distances += abs(x1 - x2) + abs(y1 - y2)
        distances += sum(
            1 for r in universe_row_expansion if r in range(min(x1, x2), max(x1, x2))
        )
        distances += sum(
            1 for c in universe_col_expansion if c in range(min(y1, y2), max(y1, y2))
        )

    CONSOLE.print(f"[PART 1] Total distance sum between galaxies: {distances}")


def part_two(data: List[List[str]]) -> None:
    """Part two of day 11 problem"""
    universe_row_expansion = [i for i, row in enumerate(data) if set(row) == {"."}]
    universe_col_expansion = [
        j for j in range(len(data[0])) if {row[j] for row in data} == {"."}
    ]

    galaxy_positions = [
        (x, y) for x, row in enumerate(data) for y, col in enumerate(row) if col == "#"
    ]
    distances: int = 0
    for pair in list(combinations(galaxy_positions, 2)):
        (x1, y1), (x2, y2) = pair
        distances += abs(x1 - x2) + abs(y1 - y2)
        distances += sum(
            999999
            for r in universe_row_expansion
            if r in range(min(x1, x2), max(x1, x2))
        )
        distances += sum(
            999999
            for c in universe_col_expansion
            if c in range(min(y1, y2), max(y1, y2))
        )

    CONSOLE.print(f"[PART 2] Total distance sum between galaxies: {distances}")


def main(input_file: str = ty.Argument(..., help="Input file with problem input")):
    """Main function for day 11 problem"""
    data = parse_input(input_file)
    part_one(data)
    part_two(data)


if __name__ == "__main__":
    ty.run(main)
