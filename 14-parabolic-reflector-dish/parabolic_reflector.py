"""
Advent of Code 2023
Day 14: Paraolic Reflector Dish

Problem description: https://adventofcode.com/2023/day/14
"""

from typing import List

from rich.console import Console
import typer as ty

CONSOLE = Console()


def parse_input(input_file: str) -> List[List[str]]:
    """Parse input file into a platform with the round and square rocks"""
    with open(input_file, "r", encoding="utf8") as f:
        data = f.read()

    data = data.split("\n")
    return [list(line) for line in data]


def part_one(data: List[List[str]]) -> None:
    """Part one of day 14 problem"""
    for i, line in enumerate(data):
        for j, symbol in enumerate(line):
            if symbol == "O":
                k = i
                while k > 0 and data[k - 1][j] not in "#O":
                    data[k][j] = "."
                    data[k - 1][j] = "O"
                    k -= 1

    size = len(data)
    result = sum(line.count("O") * (size - i) for i, line in enumerate(data))
    CONSOLE.print(f"[PART 1] Total load sum: {result}")


def part_two(data: List[List[str]]) -> None:
    """Part two of day 14 problem"""
    size = len(data)

    def tilt_north() -> None:
        for i, line in enumerate(data):
            for j, symbol in enumerate(line):
                if symbol == "O":
                    k = i
                    while k > 0 and data[k - 1][j] not in "#O":
                        data[k][j] = "."
                        data[k - 1][j] = "O"
                        k -= 1

    def tilt_south() -> None:
        for i in range(size - 1, -1, -1):
            line = data[i]
            for j, symbol in enumerate(line):
                if symbol == "O":
                    k = i
                    while k < size - 1 and data[k + 1][j] not in "#O":
                        data[k][j] = "."
                        data[k + 1][j] = "O"
                        k += 1

    def tilt_east() -> None:
        for i, line in enumerate(data):
            line_size = len(line)
            for j in range(line_size - 1, -1, -1):
                symbol = line[j]
                if symbol == "O":
                    k = j
                    while k < size - 1 and data[i][k + 1] not in "#O":
                        data[i][k] = "."
                        data[i][k + 1] = "O"
                        k += 1

    def tilt_west() -> None:
        for i, line in enumerate(data):
            for j, symbol in enumerate(line):
                if symbol == "O":
                    k = j
                    while k > 0 and data[i][k - 1] not in "#O":
                        data[i][k] = "."
                        data[i][k - 1] = "O"
                        k -= 1

    cycle = [tilt_north, tilt_west, tilt_south, tilt_east]
    # c = 0
    for _ in range(1000):
        for tilt in cycle:
            tilt()
            # CONSOLE.print("After tilt:")
            # for line in data:
            #     CONSOLE.print("".join(line))

        # CONSOLE.print(f"After {c+1} cycle:")
        # for line in data:
        #     CONSOLE.print("".join(line))
        # c += 1

    size = len(data)
    result = sum(line.count("O") * (size - i) for i, line in enumerate(data))
    CONSOLE.print(f"[PART 2] Total load sum after 1M cycles: {result}")


def main(input_file: str = ty.Argument(..., help="Input file with problem input")):
    """Main function for day 14 problem"""
    data = parse_input(input_file)
    part_one(data)
    part_two(data)


if __name__ == "__main__":
    ty.run(main)
