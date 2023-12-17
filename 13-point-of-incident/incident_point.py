"""
Advent of Code 2023
Day 13: Point of Incident

Problem description: https://adventofcode.com/2023/day/13
"""

from typing import List, Tuple

from rich.console import Console
import typer as ty

CONSOLE = Console()


def parse_input(input_file: str) -> List[Tuple[List[str], List[str]]]:
    """Parse input file into a a pair of the pattern and its vertical version"""
    with open(input_file, "r", encoding="utf8") as f:
        data = f.read()
        data = data.split("\n")

    parsed_data: List[Tuple[List[str], List[str]]] = []
    pattern: List[str] = []
    for line in data:
        if line == "":
            vertical_pattern = ["".join(v_pattern) for v_pattern in zip(*pattern)]
            parsed_data.append((pattern, vertical_pattern))
            pattern = []
            continue

        pattern.append(line)

    vertical_pattern = [*zip(*pattern)]
    parsed_data.append((pattern, vertical_pattern))
    return parsed_data


def part_one(data: List[Tuple[List[str], List[str]]]) -> None:
    """Part one of day 13 problem"""
    result = 0
    for pattern_pair in data:
        pattern, v_pattern = pattern_pair
        for i in range(len(pattern)):
            row_count = sum(
                char_1 != char_2
                for begin, end in zip(pattern[i - 1 :: -1], pattern[i:])
                for char_1, char_2 in zip(begin, end)
            )

            if row_count == 0:
                result += 100 * i

        for i in range(len(v_pattern)):
            col_count = sum(
                char_1 != char_2
                for begin, end in zip(v_pattern[i - 1 :: -1], v_pattern[i:])
                for char_1, char_2 in zip(begin, end)
            )
            if col_count == 0:
                result += i

    CONSOLE.print(f"[PART 1] Total reflecion sum: {result}")


def part_two(data: List[Tuple[List[str], List[str]]]) -> None:
    """Part two of day 13 problem"""
    result = 0
    for pattern_pair in data:
        pattern, v_pattern = pattern_pair
        for i in range(len(pattern)):
            row_count = sum(
                char_1 != char_2
                for begin, end in zip(pattern[i - 1 :: -1], pattern[i:])
                for char_1, char_2 in zip(begin, end)
            )

            if row_count == 1:
                result += 100 * i

        for i in range(len(v_pattern)):
            col_count = sum(
                char_1 != char_2
                for begin, end in zip(v_pattern[i - 1 :: -1], v_pattern[i:])
                for char_1, char_2 in zip(begin, end)
            )
            if col_count == 1:
                result += i

    CONSOLE.print(f"[PART 2] Total reflecion sum: {result}")


def main(input_file: str = ty.Argument(..., help="Input file with problem input")):
    """Main function for day 13 problem"""
    data = parse_input(input_file)
    part_one(data)
    part_two(data)


if __name__ == "__main__":
    ty.run(main)
