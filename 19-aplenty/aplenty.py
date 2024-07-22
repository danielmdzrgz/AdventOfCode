"""
Advent of Code 2023
Day 19: Aplenty

Problem description: https://adventofcode.com/2023/day/19
"""

from typing import Dict, List, Tuple

from rich.console import Console
import typer as ty

CONSOLE = Console()


def parse_input(
    input_file: str,
) -> Tuple[Dict[str, Dict[str, str]], List[Dict[str, int]]]:
    """Parse input file into a the workflows and the parts information"""
    with open(input_file, "r", encoding="utf8") as f:
        data = f.read()

    data = data.split("\n\n")
    workflow_list = data[0].split("\n")
    workflows: Dict[str, Dict[str, str]] = {}
    for workflow in workflow_list:
        name = workflow.split("{")[0]
        conditions = workflow.split("{")[1][:-1].split(",")
        default = conditions.pop(-1)
        workflows[name] = {
            cond.split(":")[0]: cond.split(":")[1] for cond in conditions
        }
        workflows[name]["default"] = default

    parts_list = data[1].split("\n")
    parts = [
        {
            category.split("=")[0]: int(category.split("=")[1])
            for category in part[1:-1].split(",")
        }
        for part in parts_list
    ]
    return workflows, parts


def part_one(data: Tuple[Dict[str, Dict[str, str]], List[Dict[str, int]]]) -> None:
    """Part one of day 19 problem"""
    workflows, parts = data
    accepted_parts: List[int] = []
    for part in parts:
        current_workflow = workflows["in"]
        workflow_end = False
        while not workflow_end:
            for condition in current_workflow:
                if condition == "default":
                    if current_workflow[condition] not in "AR":
                        current_workflow = workflows[current_workflow[condition]]
                        break

                    if current_workflow[condition] == "A":
                        rate = sum(part.values())
                        accepted_parts.append(rate)

                    workflow_end = True
                    break

                if eval(condition, part.copy()):
                    if current_workflow[condition] not in "AR":
                        current_workflow = workflows[current_workflow[condition]]
                        break

                    if current_workflow[condition] == "A":
                        rate = sum(part.values())
                        accepted_parts.append(rate)

                    workflow_end = True
                    break

    CONSOLE.print(f"[PART 1] Accepted parts rating sum: {sum(accepted_parts)}")


def part_two(data: Tuple[Dict[str, Dict[str, str]], List[Dict[str, int]]]) -> None:
    """Part two of day 19 problem"""
    workflows, _ = data
    accepted_parts = check_path(
        workflows["in"],
        {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)},
        workflows,
    )
    CONSOLE.print(f"[PART 2] Accepted parts combinations: {accepted_parts}")


def check_path(current_workflow, current_parts, workflows) -> int:
    """Makes a recursive check of the workflow paths"""
    accepted_parts = 0
    for condition in current_workflow:
        condition_parts = current_parts.copy()
        dest = current_workflow[condition]
        if condition != "default":
            cat = condition[0]
            op = condition[1]
            val = int(condition[2:])

            if op == "<":
                max_val = val - 1
                if condition_parts[cat][0] > max_val:
                    return 0

                condition_parts[cat] = (condition_parts[cat][0], max_val)
                current_parts[cat] = (val, current_parts[cat][1])

            if op == ">":
                min_val = val + 1
                if condition_parts[cat][1] < min_val:
                    return 0

                condition_parts[cat] = (min_val, condition_parts[cat][1])
                current_parts[cat] = (current_parts[cat][0], val)

        if dest == "A":
            accepted_parts += (
                len(range(condition_parts["x"][0], condition_parts["x"][1] + 1))
                * len(range(condition_parts["m"][0], condition_parts["m"][1] + 1))
                * len(range(condition_parts["a"][0], condition_parts["a"][1] + 1))
                * len(range(condition_parts["s"][0], condition_parts["s"][1] + 1))
            )
            continue

        if dest == "R":
            continue

        accepted_parts += check_path(workflows[dest], condition_parts, workflows)

    return accepted_parts


def main(input_file: str = ty.Argument(..., help="Input file with problem input")):
    """Main function for day 19 problem"""
    data = parse_input(input_file)
    part_one(data)
    part_two(data)


if __name__ == "__main__":
    ty.run(main)
