def main():
    file = open("input.txt", "r");
    # ranges_contained = 0;
    ranges_overlapped = 0;

    for pair in file:
        pair = pair.strip().split(",");
        elf1_range = range(int(pair[0].split("-")[0]), int(pair[0].split("-")[1]) + 1);
        elf2_range = range(int(pair[1].split("-")[0]), int(pair[1].split("-")[1]) + 1);
        
        # Checks if the ranges overlap
        if (elf1_range[0] <= elf2_range[0] <= elf1_range[-1]) or (elf2_range[0] <= elf1_range[0] <= elf2_range[-1]):
            ranges_overlapped += 1;

        # Checks if the ranges are contained
        # if (elf1_range[0] >= elf2_range[0]) and (elf1_range[-1] <= elf2_range[-1]):
            # ranges_contained += 1;
        # elif (elf2_range[0] >= elf1_range[0]) and (elf2_range[-1] <= elf1_range[-1]):
            # ranges_contained += 1;
    
    return ranges_overlapped;
            
print(main());
