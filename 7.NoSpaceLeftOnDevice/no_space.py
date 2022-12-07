def main():
    file = open('input.txt', 'r');
    working_dir = [];
    sizes = {};

    for line in file:
        line = line.strip().split(" ");
        if line[0] == '$':
            if line[1] == 'cd' and line[2] != '..':
                working_dir.append(line[2]);
                sizes['/'.join(working_dir)] = 0;
            elif line[1] == 'cd' and line[2] == '..':
                working_dir.pop();
        elif line[0].isnumeric():
            working_dir_copy = working_dir.copy();
            while(len(working_dir_copy) > 0):
                sizes['/'.join(working_dir_copy)] += int(line[0]);
                working_dir_copy.pop();

    # small_dirs = [size for size in sizes.values() if size <= 100000];
    # return sum(small_dirs);

    big_dirs = [size for size in sizes.values() if size > 100000];
    big_dirs.sort();
    unused_space = 70000000 - sizes['/'];
    for size in big_dirs:
        if (unused_space + size) >= 30000000:    # If unused space reaches more or equal than 30.000.000
            return size;

print(main());
