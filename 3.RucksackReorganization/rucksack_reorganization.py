import string

def main():
    file = open("input.txt", "r")
    alphabet, alphabet_value, elf_trio = list(string.ascii_letters), list(range(1, 53)), [];
    alphabet_dict = dict(zip(alphabet, alphabet_value));
    priority_sum, counter = 0, 0;

    for rucksack in file:
        elf_trio.append(rucksack.strip());
        counter += 1;
        if counter == 3:
            shared_items = list(set(elf_trio[0]) & set(elf_trio[1]) & set(elf_trio[2]));
            priority_sum += alphabet_dict[shared_items[0]];
            elf_trio = [];
            counter = 0;
            
    return priority_sum;

print(main());
