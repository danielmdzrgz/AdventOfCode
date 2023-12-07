"""
Advent of Code 2023
Day 6: Wait For It

Problem description: https://adventofcode.com/2023/day/6
"""

import math as m
from rich.console import Console
import typer as ty

CONSOLE = Console()


def parse_input(input_file: str) -> (list[int], list[int]):
    """Parse input file into a list of numbers and a dictionary of transformations"""
    with open(input_file, "r", encoding="utf8") as f:
        data = f.read()
        data = data.split("\n")
        data = [line.split(":")[1] for line in data]

    times = [int(number) for number in data[0].split(" ") if number != ""]
    records = [int(number) for number in data[1].split(" ") if number != ""]
    return times, records


def part_one(data: (list[int], list[int])) -> None:
    """Part one of day 6 problem"""
    races = list(zip(*data))
    record_breaks = []
    for _, (time, record) in enumerate(races):
        breaks_count = 0
        for speed in range(0, (time // 2) + 1):
            distance = speed * (time - speed)
            if distance > record:
                breaks_count = (
                    breaks_count + 2 if speed != time - speed else breaks_count + 1
                )

        record_breaks.append(breaks_count)

    CONSOLE.print(f"[PART 1] Product of ways of beat records: {m.prod(record_breaks)}")


def part_two(data: (list[int], list[int])) -> None:
    """Part two of day 6 problem"""
    time = int("".join([str(num) for num in data[0]]))
    record = int("".join([str(num) for num in data[1]]))
    breaks_count = 0
    for speed in range(0, (time // 2) + 1):
        distance = speed * (time - speed)
        if distance > record:
            breaks_count = (
                breaks_count + 2 if speed != time - speed else breaks_count + 1
            )

    CONSOLE.print(f"[PART 2] Product of ways of beat the record: {breaks_count}")


def main(input_file: str = ty.Argument(..., help="Input file with problem input")):
    """Main function for day 6 problem"""
    data = parse_input(input_file)
    part_one(data)
    part_two(data)


if __name__ == "__main__":
    ty.run(main)
