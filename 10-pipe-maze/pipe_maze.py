"""
Advent of Code 2023
Day 10: Pipe Maze

Problem description: https://adventofcode.com/2023/day/10
"""

import math
from typing import Dict, List, Tuple
from rich.console import Console
import typer as ty

CONSOLE = Console()

MOVEMENTS: Dict[str, List[List[int]]] = {
    "S": [[-1, 0], [1, 0], [0, 1], [0, -1]],
    "|": [[1, 0], [-1, 0]],
    "-": [[0, 1], [0, -1]],
    "L": [[-1, 0], [0, 1]],
    "J": [[-1, 0], [0, -1]],
    "7": [[1, 0], [0, -1]],
    "F": [[1, 0], [0, 1]],
    ".": [],
}


def parse_input(input_file: str) -> Tuple[List[List[str]], List[int]]:
    """Parse input file into the board and the starting position"""
    with open(input_file, "r", encoding="utf8") as f:
        data = f.read()
        data = data.split("\n")

    data = [list(line) for line in data]
    s_position: List[int] = []
    for row, line in enumerate(data):
        col = "".join(line).find("S")
        if col != -1:
            s_position = [row, col]
            break

    return data, s_position


def part_one(data: Tuple[List[List[str]], List[int]]) -> List[Tuple[int, int]]:
    """Part one of day 10 problem"""
    board, start_pos = data
    pipes = [row.copy() for row in board]
    change_start_symbol(start_pos, pipes)
    start_pos_tuple = (start_pos[0], start_pos[1])
    loop_elements: List[Tuple[int, int]] = [start_pos_tuple]
    current_pos = get_possible_moves(start_pos_tuple, pipes)[0]
    while True:
        last = loop_elements[-1]
        loop_elements.append((current_pos[0], current_pos[1]))
        pm_1, pm_2 = get_possible_moves(current_pos, pipes)
        if (start_pos_tuple in (pm_1, pm_2)) and last != start_pos_tuple:
            CONSOLE.print(
                f"[PART 1] Steps to farthest position: {math.ceil(len(loop_elements)/2)}"
            )
            return loop_elements

        current_pos = pm_1 if pm_1 != last else pm_2


def part_two(loop_elements: List[Tuple[int, int]]) -> None:
    """Part two of day 10 problem"""
    loop_positions = list(loop_elements)

    loop_area = 0
    for index, pos in enumerate(loop_positions):
        x1, y1 = pos
        x2, y2 = (
            loop_positions[index + 1]
            if index + 1 != len(loop_positions)
            else loop_positions[0]
        )
        loop_area += (x1 * y2) - (x2 * y1)

    loop_area = (1 / 2) * loop_area

    # Another way to calculate the area of the loop with the shoelace formula
    # padded_positions = [*loop_positions, loop_positions[0]]
    # loop_area = (
    #     sum(
    #         x1 * y2 - x2 * y1
    #         for (x1, y1), (x2, y2) in zip(padded_positions, padded_positions[1:])
    #     )
    #     / 2
    # )

    # Pick's theorem
    # A = i + b/2- 1
    # i = A - b/2 + 1
    inside_tiles = int(abs(loop_area) - 0.5 * len(loop_elements) + 1)
    CONSOLE.print(f"[PART 2] Total number of tiles inside of the loop: {inside_tiles}")


def change_start_symbol(start_position: List[int], board: List[List[str]]) -> None:
    """Change the start symbol to the correct one for the loop"""
    row, col = start_position
    next_moves = MOVEMENTS["S"]
    dirs = ["north", "south", "east", "west"]
    symbols: Dict[str, str] = {}
    for directions, move in zip(dirs, next_moves):
        next_row = row + move[0]
        next_col = col + move[1]
        if (
            next_row < 0
            or next_row >= len(board)
            or next_col < 0
            or next_col >= len(board[0])
        ):
            continue

        symbols[directions] = board[next_row][next_col]

    north = symbols.get("north", ".")
    south = symbols.get("south", ".")
    east = symbols.get("east", ".")
    west = symbols.get("west", ".")

    if north in "|7F" and east in "-7J":
        board[start_position[0]][start_position[1]] = "L"
    if north in "|7F" and west in "-LF":
        board[start_position[0]][start_position[1]] = "J"
    if south in "|LJ" and east in "-7J":
        board[start_position[0]][start_position[1]] = "F"
    if south in "|LJ" and west in "-LF":
        board[start_position[0]][start_position[1]] = "7"
    if north in "|7F" and south in "|LJ":
        board[start_position[0]][start_position[1]] = "|"
    if east in "-7J" and west in "-LF":
        board[start_position[0]][start_position[1]] = "-"


def get_possible_moves(
    current_position: Tuple[int, int], board: List[List[str]]
) -> List[Tuple[int, int]]:
    """Get all possible moves from current position"""
    row, col = current_position
    current_symbol = board[row][col]
    return [(row + move[0], col + move[1]) for move in MOVEMENTS[current_symbol]]


def main(input_file: str = ty.Argument(..., help="Input file with problem input")):
    """Main function for day 10 problem"""
    data = parse_input(input_file)
    loop = part_one(data)
    part_two(loop)


if __name__ == "__main__":
    ty.run(main)
