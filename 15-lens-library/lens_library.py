"""
Advent of Code 2023
Day 15: Lens Library

Problem description: https://adventofcode.com/2023/day/15
"""

from typing import Dict, List, Tuple

from rich.console import Console
import typer as ty

CONSOLE = Console()


def parse_input(input_file: str) -> List[str]:
    """Parse input file into a list with the initialization sequence"""
    with open(input_file, "r", encoding="utf8") as f:
        data = f.read()

    data = data.replace("\n", "").split(",")
    return [line.strip() for line in data]


def part_one(data: List[str]) -> None:
    """Part one of day 15 problem"""
    hash_sum = 0
    for string in data:
        hash_sum += hash_algorithm(string)

    CONSOLE.print(f"[PART 1] Sum of results of hashing sequence: {hash_sum}")


def part_two(data: List[str]) -> None:
    """Part two of day 15 problem"""
    lens_boxes: Dict[int, List[Tuple[str, int]]] = {}
    for string in data:
        op = "=" if "=" in string else "-"
        hashable_str, label = string.split(op)
        box = hash_algorithm(hashable_str)
        if op == "=":
            box_content = lens_boxes.get(box)
            if box_content:
                old_lens = [
                    i
                    for i, pair in enumerate(lens_boxes[box])
                    if hashable_str in pair[0]
                ]
                if old_lens:
                    lens_boxes[box].pop(old_lens[0])
                    lens_boxes[box].insert(old_lens[0], (hashable_str, int(label)))
                    continue

                lens_boxes[box].append((hashable_str, int(label)))
                continue

            lens_boxes[box] = [(hashable_str, int(label))]

        else:
            box_content = lens_boxes.get(box)
            if not box_content:
                continue

            lens = [
                i for i, pair in enumerate(lens_boxes[box]) if hashable_str in pair[0]
            ]
            if lens:
                lens_boxes[box].pop(lens[0])

    focusing_power = 0
    for box, lens in lens_boxes.items():
        for slot, (_, focal_l) in enumerate(lens):
            focusing_power += (box + 1) * (slot + 1) * focal_l

    CONSOLE.print(f"[PART 2] Resulting focusing power: {focusing_power}")


def hash_algorithm(input_str: str) -> int:
    """Applies the hash algorithm of the guide book"""
    ascii_codes = [ord(char) for char in input_str]
    current_value = 0
    for code in ascii_codes:
        current_value += code
        current_value *= 17
        current_value %= 256

    return current_value


def main(input_file: str = ty.Argument(..., help="Input file with problem input")):
    """Main function for day 15 problem"""
    data = parse_input(input_file)
    part_one(data)
    part_two(data)


if __name__ == "__main__":
    ty.run(main)
