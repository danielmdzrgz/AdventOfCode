"""
Advent of Code 2023
Day 7: Camel Cards

Problem description: https://adventofcode.com/2023/day/7
"""

from typing import List
from collections import Counter
from functools import cmp_to_key
from rich.console import Console
import typer as ty

CONSOLE = Console()
TYPES_STRENGTH = {
    "fivekind": 6,
    "fourkind": 5,
    "full": 4,
    "threekind": 3,
    "doblepair": 2,
    "pair": 1,
    "high": 0,
}


def parse_input(input_file: str) -> List[List[str]]:
    """Parse input file into a list of strings"""
    with open(input_file, "r", encoding="utf8") as f:
        data = f.read()
        data = data.split("\n")
        data = [line.split(" ") for line in data]

    return data


def part_one(data: List[List[str]]) -> None:
    """Part one of day 7 problem"""
    card_strength = {
        "A": 12,
        "K": 11,
        "Q": 10,
        "J": 9,
        "T": 8,
        "9": 7,
        "8": 6,
        "7": 5,
        "6": 4,
        "5": 3,
        "4": 2,
        "3": 1,
        "2": 0,
    }

    hands_strength = []
    for line in data:
        hand, bid = line
        counts = {}
        for card in card_strength:
            counts[card] = hand.count(card)

        if not any(card_count > 1 for card_count in counts.values()):
            hands_strength.append((TYPES_STRENGTH["high"], hand, int(bid)))

        if any(card_count == 5 for card_count in counts.values()):
            hands_strength.append((TYPES_STRENGTH["fivekind"], hand, int(bid)))
            continue

        if any(card_count == 4 for card_count in counts.values()):
            hands_strength.append((TYPES_STRENGTH["fourkind"], hand, int(bid)))
            continue

        if any(card_count == 3 for card_count in counts.values()):
            if any(card_count == 2 for card_count in counts.values()):
                hands_strength.append((TYPES_STRENGTH["full"], hand, int(bid)))
                continue

            hands_strength.append((TYPES_STRENGTH["threekind"], hand, int(bid)))
            continue

        if any(card_count == 2 for card_count in counts.values()):
            if list(counts.values()).count(2) == 2:
                hands_strength.append((TYPES_STRENGTH["doblepair"], hand, int(bid)))
                continue

            hands_strength.append((TYPES_STRENGTH["pair"], hand, int(bid)))
            continue

    def compare_hands(hand, other_hand) -> int:
        htype = hand[0]
        other_htype = other_hand[0]
        rank_diff = htype - other_htype
        if rank_diff != 0:
            return rank_diff

        for card, other_card in zip(hand[1], other_hand[1]):
            cstrength = card_strength[card]
            other_cstrength = card_strength[other_card]
            if cstrength != other_cstrength:
                return cstrength - other_cstrength

        return 0

    sorted_hands = sorted(hands_strength, key=cmp_to_key(compare_hands))
    # CONSOLE.print(sorted_hands)
    result = 0
    for weight, hand in enumerate(sorted_hands):
        result += (weight + 1) * hand[2]

    CONSOLE.print(f"[PART 1] Total winnings: {result}")


def part_two(data: List[List[str]]) -> None:
    """Part two of day 7 problem"""
    card_strength = {
        "A": 12,
        "K": 11,
        "Q": 10,
        "T": 9,
        "9": 8,
        "8": 7,
        "7": 6,
        "6": 5,
        "5": 4,
        "4": 3,
        "3": 2,
        "2": 1,
        "J": 0,
    }

    hands_strength = []
    for line in data:
        hand, bid = line
        counts = Counter(hand)
        jokers: int = 0
        if counts.get("J"):
            joker_count = counts.get("J")
            if joker_count is not None and joker_count != 5:
                jokers = joker_count
                counts.pop("J")

        counts += Counter(counts.most_common(1)[0][0] * jokers)
        for _, count in counts.most_common():
            match count:
                case 5:
                    hands_strength.append((TYPES_STRENGTH["fivekind"], hand, int(bid)))
                    break

                case 4:
                    hands_strength.append((TYPES_STRENGTH["fourkind"], hand, int(bid)))
                    break

                case 3:
                    if list(counts.values()).count(2) == 1:
                        hands_strength.append((TYPES_STRENGTH["full"], hand, int(bid)))
                        break

                    hands_strength.append((TYPES_STRENGTH["threekind"], hand, int(bid)))
                    break

                case 2:
                    if list(counts.values()).count(2) == 2:
                        hands_strength.append(
                            (TYPES_STRENGTH["doblepair"], hand, int(bid))
                        )
                        break

                    hands_strength.append((TYPES_STRENGTH["pair"], hand, int(bid)))
                    break

        else:
            hands_strength.append((TYPES_STRENGTH["high"], hand, int(bid)))

    def compare_hands(hand, other_hand) -> int:
        htype = hand[0]
        other_htype = other_hand[0]
        rank_diff = htype - other_htype
        if rank_diff != 0:
            return rank_diff

        for card, other_card in zip(hand[1], other_hand[1]):
            cstrength = card_strength[card]
            other_cstrength = card_strength[other_card]
            if cstrength != other_cstrength:
                return cstrength - other_cstrength

        return 0

    sorted_hands = sorted(hands_strength, key=cmp_to_key(compare_hands))
    # CONSOLE.print(sorted_hands)
    result = 0
    for weight, hand in enumerate(sorted_hands):
        result += (weight + 1) * hand[2]

    CONSOLE.print(f"[PART 2] Total winnings: {result}")


def main(input_file: str = ty.Argument(..., help="Input file with problem input")):
    """Main function for day 7 problem"""
    data = parse_input(input_file)
    part_one(data)
    part_two(data)


if __name__ == "__main__":
    ty.run(main)
