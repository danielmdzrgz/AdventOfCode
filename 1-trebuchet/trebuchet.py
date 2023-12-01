"""
Advent of Code 2023
Day 1: Trebuchet?!

Problem description: https://adventofcode.com/2023/day/1
"""

import typer as ty
from rich.console import Console

CONSOLE = Console()
TEXT2NUM = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

# Dictionary for alternative part 2 solution
# TEXT2NUM = {
#     "one": "o1e",
#     "two": "t2o",
#     "three": "t3e",
#     "four": "f4r",
#     "five": "f5e",
#     "six": "s6x",
#     "seven": "s7n",
#     "eight": "e8t",
#     "nine": "n9e"
# }


def parse_input(input_file: str) -> list[str]:
    """Parse input file into a list of strings"""
    with open(input_file, "r", encoding="utf8") as f:
        data = f.read()
        return data.split("\n")


def part_one(data: list[str]) -> None:
    """Part one of day 1 problem"""
    calibration_sum = 0
    for line in data:
        line_numbers = [char for char in line if char.isdigit()]
        # CONSOLE.print(line_numbers)
        calibration_sum += int(line_numbers[0] + line_numbers[-1])

    CONSOLE.print(f"[PART 1] Final calibration sum: {calibration_sum}")


def part_two(data: list[str]) -> None:
    """Part two of day 1 problem"""
    calibration_sum = 0
    for line in data:
        for key, num in TEXT2NUM.items():
            key_position = line.find(key)
            while key_position != -1:
                line = line[0:key_position+1] + num + line[key_position:]
                key_position = line.find(key, key_position+len(key))

        # Alternative solution using replace
        # for key, num in TEXT2NUM.items():
        #     if key in line:
        #         line = line.replace(key, num)

        # CONSOLE.print(line)
        line_numbers = [char for char in line if char.isdigit()]
        calibration_sum += int(line_numbers[0] + line_numbers[-1])

    CONSOLE.print(f"[PART 2] Final calibration sum: {calibration_sum}")


def main(input_file: str = ty.Argument(..., help="Input file with problem input")):
    """Main function for day 1 problem"""
    data = parse_input(input_file)
    # part_one(data)
    part_two(data)


if __name__ == "__main__":
    ty.run(main)
