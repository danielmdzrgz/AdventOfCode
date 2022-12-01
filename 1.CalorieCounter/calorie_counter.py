def main():
    calories_total = [];
    elf_calories = [];

    file = open("input.txt", "r");
    for line in file:
        if line == "\n":
            calories_total.append(sum(elf_calories));
            elf_calories = [];
            continue;
        else:
            elf_calories.append(int(line));

    file.close();
    calories_total.sort(reverse=True);
    top_3 = sum(calories_total[:3]);
    return top_3;

print(main());