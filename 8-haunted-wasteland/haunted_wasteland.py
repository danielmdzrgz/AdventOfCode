"""
Advent of Code 2023
Day 8: Haunted Wasteland

Problem description: https://adventofcode.com/2023/day/8
"""

from typing import Dict, List, Tuple
import math
from rich.console import Console
import typer as ty

CONSOLE = Console()


def parse_input(input_file: str) -> Tuple[str, Dict[str, List[str]]]:
    """Parse input file into movements and a network"""
    with open(input_file, "r", encoding="utf8") as f:
        data = f.read()
        data = data.split("\n")

    data = [line for line in data if line != ""]
    movements = data.pop(0)
    network: Dict[str, List[str]] = {}
    for node in data:
        node = node.split("=")
        node_id = node[0].strip()
        node_value = node[1].strip().strip("(").strip(")")
        left, right = node_value.split(",")
        network[node_id] = [left.strip(), right.strip()]

    return movements, network


def part_one(data: Tuple[str, Dict[str, List[str]]]) -> None:
    """Part one of day 8 problem"""
    movements, network = data
    node = "AAA"
    move_index = 0
    steps = 0
    while node != "ZZZ":
        move = movements[move_index]
        node = network[node][0] if move == "L" else network[node][1]
        move_index = (move_index + 1) % len(movements)
        steps += 1

    CONSOLE.print(f"[PART 1] Total steps to reach last node: {steps}")


def part_two(data: Tuple[str, Dict[str, List[str]]]) -> None:
    """Part two of day 8 problem"""
    movements, network = data
    nodes = [node for node in network if node[2] == "A"]
    step_counts = []
    move_index = 0

    for i, node in enumerate(nodes):
        steps = 0
        while node[2] != "Z":
            move = movements[move_index]
            node = network[node][0] if move == "L" else network[node][1]
            nodes[i] = node
            move_index = (move_index + 1) % len(movements)
            steps += 1

        step_counts.append(steps)

    CONSOLE.print(f"[PART 2] Total steps to reach last node: {math.lcm(*step_counts)}")


def main(input_file: str = ty.Argument(..., help="Input file with problem input")):
    """Main function for day 8 problem"""
    data = parse_input(input_file)
    # part_one(data)
    part_two(data)


if __name__ == "__main__":
    ty.run(main)
