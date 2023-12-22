"""
Advent of Code 2023
Day 17: Clumsy Crucible

Problem description: https://adventofcode.com/2023/day/17
"""

from __future__ import annotations
import heapq
from typing import List, Tuple

from rich.console import Console
import typer as ty

CONSOLE = Console()

def parse_input(input_file: str) -> List[List[int]]:
    """Parse input file into a matrix with the heat-loss map"""
    with open(input_file, "r", encoding="utf8") as f:
        data = f.read()

    data = data.split("\n")
    return [[int(value) for value in line] for line in data]


def part_one(data: List[List[int]]) -> None:
    """Part one of day 17 problem"""
    heat_loss = dijkstra_search(data, (0, 0), (len(data) - 1, len(data[0]) - 1))
    CONSOLE.print(f"[PART 1] Minimum heat loss: {heat_loss}")


def part_two(data: List[List[int]]) -> None:
    """Part two of day 17 problem"""
    heat_loss = dijkstra_search(data, (0, 0), (len(data) - 1, len(data[0]) - 1), True)
    CONSOLE.print(f"[PART 2] Minimum heat loss: {heat_loss}")


def dijkstra_search(
    data: List[List[int]],
    start: Tuple[int, int],
    goal: Tuple[int, int],
    part2: bool = False,
) -> int:
    """Dijkstra search algorithm"""
    rows, cols = len(data), len(data[0])
    steps_count = [[0 for _ in range(cols)] for _ in range(rows)]

    def is_valid(x, y, prev_steps, steps, same_dir):
        in_limits = 0 <= x < rows and 0 <= y < cols
        valid_part_1 = steps <= 3
        valid_part_2 = steps <= 10 and (prev_steps >= 4 or same_dir or prev_steps == -1)
        valid = valid_part_2 if part2 else valid_part_1
        return in_limits and valid

    visited = {}
    heap = [(0, start, (0, 0), -1)]
    heapq.heapify(heap)
    while heap:
        current_distance, current_node, prev_direction, steps = heapq.heappop(heap)
        x, y = current_node
        steps_count[x][y] = steps
        if (current_node, prev_direction, steps) in visited:
            continue

        visited[(current_node, prev_direction, steps)] = current_distance
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            next_x, next_y = x + dx, y + dy
            pdx, pdy = prev_direction
            next_steps = steps + 1 if (pdx, pdy) == (dx, dy) else 1
            same_dir = (dx, dy) == (pdx, pdy)
            valid = is_valid(next_x, next_y, steps, next_steps, same_dir)
            if not valid or (dx, dy) == (-pdx, -pdy):
                continue

            if ((next_x, next_y), (dx, dy), next_steps) in visited:
                continue

            new_distance = current_distance + data[next_x][next_y]
            heapq.heappush(heap, (new_distance, (next_x, next_y), (dx, dy), next_steps))

    result = int(1e10)
    for (position, _, steps), cost in visited.items():
        if position == goal and (steps >= 4 or not part2):
            result = min(result, cost)

    return result


def main(input_file: str = ty.Argument(..., help="Input file with problem input")):
    """Main function for day 17 problem"""
    data = parse_input(input_file)
    part_one(data)
    part_two(data)


if __name__ == "__main__":
    ty.run(main)
