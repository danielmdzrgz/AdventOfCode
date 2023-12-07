"""
Advent of Code 2023
Day 5: If You Give A Seed A Fertilizer

Problem description: https://adventofcode.com/2023/day/5
"""

import threading
from rich.console import Console
import typer as ty

CONSOLE = Console()


def parse_input(input_file: str) -> (list[int], list[dict[tuple[int, int], int]]):
    """Parse input file into a list of numbers and a dictionary of transformations"""
    with open(input_file, "r", encoding="utf8") as f:
        data = f.read()
        data = data.split("\n")

    seeds = []
    transformations = []
    transformation = {}
    for line in data:
        line = line.split(" ")
        if line[0] == "seeds:":
            content = line[1:]
            seeds.extend([int(number) for number in content if number != ""])
            continue

        if line == [""] and transformation:
            transformations.append(transformation)
            transformation = {}
            continue

        if not any(char.isdigit() for char in line):
            continue

        destintation_start = int(line[0])
        source_start = int(line[1])
        transform_range = int(line[2])
        transformation[
            (source_start, source_start + transform_range)
        ] = destintation_start

    transformations.append(transformation)
    return seeds, transformations


def part_one(data: list[list[list[int]]]) -> None:
    """Part one of day 5 problem"""
    seeds, transformations = data
    result_locations = []
    for seed in seeds:
        for transformation in transformations:
            for src_start, dest_start in transformation.items():
                if src_start[0] <= seed < src_start[1]:
                    seed = dest_start + (seed - src_start[0])
                    break

        result_locations.append(seed)

    CONSOLE.print(f"[PART 1] Lowest seed location: {min(result_locations)}")


def part_two(data: list[list[list[int]]]) -> None:
    """Part two of day 5 problem"""
    seeds, transformations = data
    seed_ranges = []
    for i in range(0, len(seeds) - 1, 2):
        seed_ranges.append((seeds[i], seeds[i] + seeds[i + 1]))

    result_locations = []
    threads = []

    def thread_function(seed_range: tuple[int, int]):
        result_locations.extend(transform_seeds(seed_range, transformations))

    for s_range in seed_ranges:
        thread = threading.Thread(target=thread_function, args=(s_range,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    CONSOLE.print(f"[PART 2] Lowest seed location: {min(result_locations)[0]}")


def transform_seeds(
    seed_range: tuple[int, int], transformations: list[dict[int, int]]
) -> list[tuple[int, int]]:
    """Transform seeds using the given transformations"""
    ranges = [seed_range]
    for transformation in transformations:
        transformed_ranges, pending_ranges = get_new_ranges(ranges, transformation)
        while pending_ranges:
            extra_ranges, pending_ranges = get_new_ranges(
                pending_ranges, transformation
            )
            transformed_ranges.extend(extra_ranges)

        ranges = transformed_ranges

    return ranges


def get_new_ranges(
    ranges: list[tuple[int, int]], transformation: dict[tuple[int, int], int]
) -> (list[tuple[int, int]], list[tuple[int, int]]):
    """Get new ranges from the given ranges and transformation"""
    transformed_ranges = []
    pending_ranges = []

    for s_range in ranges:
        start, end = s_range
        if not any(
            src_end >= start and src_start < end
            for src_start, src_end in transformation.keys()
        ):
            transformed_ranges.append(s_range)
            continue

        for (src_r_start, src_r_end), dest_start in transformation.items():
            if src_r_start <= start and end <= src_r_end:
                transformed_ranges.append(
                    (
                        dest_start + (start - src_r_start),
                        dest_start + (end - src_r_start),
                    )
                )
                break

            if start < src_r_start and src_r_end <= end:
                pending_ranges.append((start, src_r_start))
                transformed_ranges.append(
                    (dest_start, dest_start + (src_r_end - src_r_start))
                )
                pending_ranges.append((src_r_end, end))
                break

            if src_r_start <= start < src_r_end <= end:
                transformed_ranges.append(
                    (
                        dest_start + (start - src_r_start),
                        dest_start + (src_r_end - src_r_start),
                    )
                )
                pending_ranges.append((src_r_end, end))
                break

            if start < src_r_start < end <= src_r_end:
                pending_ranges.append((start, src_r_start))
                transformed_ranges.append(
                    (
                        dest_start + (src_r_start - src_r_start),
                        dest_start + (end - src_r_start),
                    )
                )
                break

    return transformed_ranges, pending_ranges


def main(input_file: str = ty.Argument(..., help="Input file with problem input")):
    """Main function for day 5 problem"""
    data = parse_input(input_file)
    part_one(data)
    part_two(data)


if __name__ == "__main__":
    ty.run(main)
