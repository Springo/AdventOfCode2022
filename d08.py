import grid_util as gdu
# functions: convert_to_grid, serialize, get_neighbors, count_val, grid_project


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


def check_visible(grid, i, j):
    val = grid[i][j]
    for d in [0, 2, 4, 6]:
        visible = True
        step = 1
        i2 = -1
        j2 = -1
        while i2 is not None and j2 is not None:
            i2, j2 = gdu.grid_project(grid, i, j, d, step=step)
            if i2 is None or j2 is None:
                break
            if grid[i2][j2] >= val:
                visible = False
            step += 1

        if visible:
            return True
    return False


def get_view_dist(grid, i, j):
    val = grid[i][j]
    score = 1
    for d in [0, 2, 4, 6]:
        step = 1
        i2 = -1
        j2 = -1
        while i2 is not None and j2 is not None:
            i2, j2 = gdu.grid_project(grid, i, j, d, step=step)
            if i2 is None or j2 is None:
                step -= 1
                break
            if grid[i2][j2] >= val:
                break
            step += 1

        score *= step

    return score


lines = readFile("d08input.txt")
grid = gdu.convert_to_grid(lines)

count = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if check_visible(grid, i, j):
            count += 1

print(count)

best = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        score = get_view_dist(grid, i, j)
        if score > best:
            best = score
print(best)
