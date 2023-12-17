"""
Advent of Code 2023
Day 12: Hot Springs

Problem description: https://adventofcode.com/2023/day/12
"""

from functools import cache
from itertools import groupby, product
from typing import List, Tuple

from rich.console import Console
import typer as ty

CONSOLE = Console()


def parse_input(input_file: str) -> List[Tuple[str, List[int]]]:
    """Parse input file into a dictionary of the groupings in each line of the file"""
    with open(input_file, "r", encoding="utf8") as f:
        data = f.read()
        data = data.split("\n")

    data = [line.split(" ") for line in data]
    parsed_data: List[Tuple[str, List[int]]] = []
    for line in data:
        parsed_data.append((line[0], [int(num) for num in line[1].split(",")]))

    return parsed_data


def part_one(strings: List[str], counts: List[List[int]]) -> None:
    """Part one of day 12 problem"""
    permutations: List[List[str]] = []
    for i, string in enumerate(strings):
        string_permutations: List[str] = []
        positions = [i for i, char in enumerate(string) if char == "?"]

        for combination in product(["#", "?"], repeat=len(positions)):
            new_str = list(string)
            for j, char in zip(positions, combination):
                new_str[j] = char

            if new_str.count("#") != sum(counts[i]):
                continue

            string_permutations.append("".join(new_str))

        permutations.append(string_permutations)

    arrangements_count = 0
    for index, (string, count) in enumerate(zip(strings, counts)):
        if len(permutations[index]) == 1:
            arrangements_count += 1
            continue

        for possibility in permutations[index]:
            if all(
                len(k) == l
                for k, l in zip(
                    [list(g) for k, g in groupby(possibility) if k == "#"], count
                )
            ):
                arrangements_count += 1

    CONSOLE.print(f"[PART 1] Total arrangements: {arrangements_count}")


def part_two(strings: List[str], counts: List[List[int]]) -> None:
    """Part two of day 12 problem"""
    arrangements_count = 0
    for i, _ in enumerate(strings):
        strings[i] = "?".join([strings[i]] * 5)
        counts[i] *= 5
        arrangements_count += get_arrangements_count(strings[i], tuple(counts[i]))

    CONSOLE.print(f"[PART 2] Total arrangements: {arrangements_count}")


@cache
def get_arrangements_count(string, count, result=0):
    """Recursively get the number of arrangements for a given string"""
    if not count:
        return "#" not in string

    current, count = count[0], count[1:]
    for i in range(len(string) - sum(count) - len(count) - current + 1):
        if "#" in string[:i]:
            break

        if (
            (nxt := i + current) <= len(string)
            and "." not in string[i:nxt]
            and string[nxt : nxt + 1] != "#"
        ):
            result += get_arrangements_count(string[nxt + 1 :], count)

    return result


def main(input_file: str = ty.Argument(..., help="Input file with problem input")):
    """Main function for day 12 problem"""
    data = parse_input(input_file)
    strings = [string for string, _ in data]
    counts = [count for _, count in data]
    part_one(strings, counts)
    part_two(strings, counts)


if __name__ == "__main__":
    ty.run(main)
