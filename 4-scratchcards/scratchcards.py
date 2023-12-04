"""
Advent of Code 2023
Day 4: Scratchcards

Problem description: https://adventofcode.com/2023/day/4
"""

from rich.console import Console
import typer as ty

CONSOLE = Console()


def parse_input(input_file: str) -> list[list[list[int]]]:
    """Parse input file into a list of lists of lists of numbers"""
    with open(input_file, "r", encoding="utf8") as f:
        data = f.read()
        data = data.split("\n")

    data = [line.split(":")[1].split("|") for line in data]
    parsed_data = []
    for line in data:
        line[0] = line[0].strip()
        line[1] = line[1].strip()
        winning_numbers = [int(number) for number in line[0].split(" ") if number != ""]
        card_numbers = [int(number) for number in line[1].split(" ") if number != ""]
        parsed_data.append([winning_numbers, card_numbers])

    CONSOLE.print(parsed_data)
    return parsed_data


def part_one(data: list[list[list[int]]]) -> None:
    """Part one of day 4 problem"""
    punctuation = 0
    for card in data:
        if not any(number in card[1] for number in card[0]):
            continue

        points = 1
        for number in card[0]:
            points = points * 2 if number in card[1] else points

        punctuation += points // 2
    CONSOLE.print(f"[PART 1] Total points: {punctuation}")


def part_two(data: list[list[list[int]]]) -> None:
    """Part two of day 4 problem"""
    matches = 0
    cards = {card_num: 1 for card_num, _ in enumerate(data)}
    for card_num, card in enumerate(data):
        matches = 0
        if not any(number in card[1] for number in card[0]):
            continue

        for number in card[0]:
            matches = matches + 1 if number in card[1] else matches

        for next_card in range(matches):
            cards[card_num + next_card + 1] += cards[card_num]

    total_cards = sum(cards.values())
    CONSOLE.print(f"[PART 2] Final number of scratchcards: {total_cards}")


def main(input_file: str = ty.Argument(..., help="Input file with problem input")):
    """Main function for day 4 problem"""
    data = parse_input(input_file)
    part_one(data)
    part_two(data)


if __name__ == "__main__":
    ty.run(main)
