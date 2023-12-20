"""
Advent of Code 2023
Day 16: The Floor Will Be Lava

Problem description: https://adventofcode.com/2023/day/16
"""

from typing import List, Set, Tuple

from rich.console import Console
import typer as ty

CONSOLE = Console()
POSSIBLE_DIRECTIONS = {
    "|": {"^": ((-1, 0), "^"), "v": ((1, 0), "v")},
    "-": {"<": ((0, -1), "<"), ">": ((0, 1), ">")},
    "\\": {
        "^": ((0, -1), "<"),
        "v": ((0, 1), ">"),
        "<": ((-1, 0), "^"),
        ">": ((1, 0), "v"),
    },
    "/": {
        "^": ((0, 1), ">"),
        "v": ((0, -1), "<"),
        "<": ((1, 0), "v"),
        ">": ((-1, 0), "^"),
    },
    ".": {
        "^": ((-1, 0), "^"),
        "v": ((1, 0), "v"),
        "<": ((0, -1), "<"),
        ">": ((0, 1), ">"),
    },
}


def parse_input(input_file: str) -> List[List[str]]:
    """Parse input file into a matrix with the contraption"""
    with open(input_file, "r", encoding="utf8") as f:
        data = f.read()

    data = data.split("\n")
    return [list(line) for line in data]


def part_one(data: List[List[str]]) -> None:
    """Part one of day 16 problem"""
    data_copy = [line.copy() for line in data]
    position, direction, splitters_mirrors = [0, 0], ">", set()
    reflect_beams(data_copy, splitters_mirrors, position, direction)
    energized_tiles = sum(
        sum(1 for char in line if char in "<>^v") for line in data_copy
    )
    energized_tiles += len(splitters_mirrors)
    CONSOLE.print(f"[PART 1] Total number of energized tiles: {energized_tiles}")


def part_two(data: List[List[str]]) -> None:
    """Part two of day 16 problem"""
    results: List[int] = []
    contraption_sides = [data[0], data[-1], list(zip(*data))[0], list(zip(*data))[-1]]
    contraption_directions = ["v", "^", ">", "<"]
    for side, direction in zip(contraption_sides, contraption_directions):
        side_results: List[int] = []
        for pos, _ in enumerate(side):
            position: List[int] = []
            match (direction):
                case "v":
                    position = [0, pos]
                case "^":
                    position = [len(data) - 1, pos]
                case ">":
                    position = [pos, 0]
                case "<":
                    position = [pos, len(data[0]) - 1]

            data_copy = [line.copy() for line in data]
            splitters_mirrors = set()
            reflect_beams(data_copy, splitters_mirrors, position, direction)
            energized_tiles = sum(
                sum(1 for char in line if char in "<>^v") for line in data_copy
            )
            energized_tiles += len(splitters_mirrors)
            side_results.append(energized_tiles)

        results.append(max(side_results))

    CONSOLE.print(f"[PART 2] Total number of energized tiles: {max(results)}")


def reflect_beams(
    data: List[List[str]], splitters_mirrors: Set[Tuple[int, int]], position, direction
) -> None:
    """Follows the beams and reflects them when necessary"""
    try:
        while True:
            x, y = position
            if x < 0 or y < 0:
                raise IndexError

            if (data[x][y] in "<>" and direction in "^v") or (
                data[x][y] in "^v" and direction in "<>"
            ):
                data[x][y] = "."

            elif data[x][y] in "<>v^":
                return

            movement_data = POSSIBLE_DIRECTIONS[data[x][y]].get(direction)

            if data[x][y] == ".":
                data[x][y] = direction

            elif data[x][y] in "|-/\\":
                splitters_mirrors.add((x, y))

            if movement_data:
                position = [
                    x + movement_data[0][0],
                    y + movement_data[0][1],
                ]
                direction = movement_data[1]
                continue

            if data[x][y] == "|":
                reflect_beams(data, splitters_mirrors, [x + 1, y], "v")
                reflect_beams(data, splitters_mirrors, [x - 1, y], "^")
                return

            if data[x][y] == "-":
                reflect_beams(data, splitters_mirrors, [x, y + 1], ">")
                reflect_beams(data, splitters_mirrors, [x, y - 1], "<")
                return

    except IndexError:
        return


def main(input_file: str = ty.Argument(..., help="Input file with problem input")):
    """Main function for day 16 problem"""
    data = parse_input(input_file)
    part_one(data)
    part_two(data)


if __name__ == "__main__":
    ty.run(main)
