# PART 1
grid = []
with open("input.txt", 'r', encoding='utf-8') as file:
    for row in file:
        string_list = list(row.strip())
        grid.append([eval(i) for i in string_list])


invisible_trees = 0
visible_trees = 400-8 # the trees on the edges (-8 removes the corner cases, prevents them from counting more than once)
for row in range(1, len(grid)-1):
    for col in range(1,98):
        tree_height = grid[row][col]
        left = all(left_trees < tree_height for left_trees in grid[row][:col])
        right = all(right_trees < tree_height for right_trees in grid[row][col+1:])
        up = all(u_trees < tree_height for u_trees in [grid[row_idx][col] for row_idx in range(row)])
        down = all(d_trees < tree_height for d_trees in [grid[row_idx][col] for row_idx in range(row+1, len(grid))])
        if any([right, left, up, down]):
            visible_trees += 1

print(visible_trees)

# PART 2
def viewing_dist(trees, reverse_iter=False):
    count = 0
    if reverse_iter:
        for i in range(len(trees)):
            count += 1
            if trees[-1-i] >= tree_height or count == len(trees):
                return count
    else:
        for i in range(len(trees)):
            count += 1
            if trees[i] >= tree_height or count == len(trees):
                return count


max_viewing_dist = 0
for row in range(1, len(grid) - 1):
    for col in range(1, 98):
        tree_height = grid[row][col]
        viewing_dist_left = viewing_dist(grid[row][:col], True)
        viewing_dist_right = viewing_dist(grid[row][col + 1:])
        viewing_dist_up = viewing_dist([grid[row_idx][col] for row_idx in range(row)], True)
        viewing_dist_down = viewing_dist([grid[row_idx][col] for row_idx in range(row + 1, len(grid))])
        total_view_dist = viewing_dist_left * viewing_dist_right * viewing_dist_up * viewing_dist_down
        if max(total_view_dist, max_viewing_dist) == total_view_dist:
            max_viewing_dist = total_view_dist

print(max_viewing_dist)
