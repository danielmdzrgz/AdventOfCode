def trimLine(line):
    i = 0;
    while i < len(line):
        if line[i] == "" and line[i+1] == "" and line[i+2] == "":
            line.pop(i);
            line.pop(i);
            line.pop(i);
        i+=1;
    
    return line;

# def moveCrates(stacks, line):
#     for i in range(0, int(line[1])):
#         temp = stacks[int(line[3]) - 1].pop();
#         stacks[int(line[5]) - 1].append(temp);
#     return stacks;

def moveCrates(stacks, line):
    aux = [];
    for i in range(0, int(line[1])):
        temp = stacks[int(line[3]) - 1].pop();
        aux.insert(0, temp);
    
    stacks[int(line[5]) - 1].extend(aux);
    return stacks;

def main():
    file = open("input.txt", "r");
    result = "";
    line = trimLine(file.readline().strip('\n').split(" "));
    stacks = [[] for i in range(len(line))];

    for i in range(len(line)):
        if line[i] != "":
            stacks[i].insert(0, line[i].strip("[]"));

    for line in file:
        if line.strip() == "" or line.strip().startswith("1"):
            continue;

        if line.strip().startswith('['):
            line = trimLine(line.strip('\n').split(" "));
            for i in range(len(line)):
                if line[i] != "":
                    stacks[i].insert(0, line[i].strip("[]"));

        else:
            stacks = moveCrates(stacks, line.strip('\n').split(" "));

    for i in range(len(stacks)):
        if stacks[i] != []:
            result += str(stacks[i][-1]);

    return result;

print(main());
