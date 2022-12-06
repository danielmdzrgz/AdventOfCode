def main():
    file = open("input.txt", "r");
    line = file.readline().strip();

    for i in range(len(line)):
        # if len(set(line[i:i+4])) == 4:
            # return i + 4;
        
        if len(set(line[i:i+14])) == 14:
            return i + 14;

print(main());
