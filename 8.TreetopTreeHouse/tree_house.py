# def visible(grid, i, j):
#     current_tree = grid[i][j];

#     top = all(grid[x][j] < current_tree for x in range(0, i));                      # Check if the tree is visible from the top of the grid
#     bottom = all(grid[x][j] < current_tree for x in range(i + 1, len(grid)));       # Check if the tree is visible from the bottom of the grid
#     left = all(grid[i][x] < current_tree for x in range(0, j));                     # Check if the tree is visible from the left of the grid
#     right = all(grid[i][x] < current_tree for x in range(j + 1, len(grid[i])));     # Check if the tree is visible from the right of the grid

#     return top or bottom or left or right;

def scenicScore(grid, i, j):
    top, bottom, left, right, current_tree = 0, 0, 0, 0, grid[i][j];

    for x in range(i - 1, -1, -1):              # Visible trees until same height or higher tree is found in TOP direction
        top += 1;
        if current_tree <= grid[x][j]:
            break;

    for x in range(i + 1, len(grid)):           # Visible trees until same height or higher tree is found in BOTTOM direction
        bottom += 1;
        if current_tree <= grid[x][j]:
            break;

    for x in range(j - 1, -1, -1):              # Visible trees until same height or higher tree is found in LEFT direction
        left += 1;
        if current_tree <= grid[i][x]:
            break;

    for x in range(j + 1, len(grid[i])):        # Visible trees until same height or higher tree is found in RIGHT direction
        right += 1;
        if current_tree <= grid[i][x]:
            break;

    return top * bottom * left * right;    

def main():
    file = open('input.txt', 'r');
    grid = [];
    # visible_trees = 0;
    max_scenic_score = 0;

    for line in file:
        row = [int(digit) for digit in line.strip()];
        grid.append(row);

    # visible_trees += len(grid) * 4 - 4  # Edge trees are always visible
    # for i in range(1, len(grid) - 1):
    #     for j in range(1, len(grid[i]) - 1):
            # if visible(grid, i, j):
            #     visible_trees += 1

    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            current_scenic_score = scenicScore(grid, i, j);
            if current_scenic_score > max_scenic_score:
                max_scenic_score = current_scenic_score;

    return max_scenic_score;

print(main());
