import grid_util as gdu

from copy import deepcopy


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


def check_eq(g1, g2):
    for i in range(len(g1)):
        for j in range(len(g1[i])):
            if g1[i][j] != g2[i][j]:
                return False
    return True


def get_bounds(grid):
    min_i = len(grid)
    max_i = 0
    min_j = len(grid[0])
    max_j = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '#':
                if i < min_i:
                    min_i = i
                if i > max_i:
                    max_i = i
                if j < min_j:
                    min_j = j
                if j > max_j:
                    max_j = j

    count = 0
    for i in range(min_i, max_i + 1):
        for j in range(min_j, max_j + 1):
            if grid[i][j] == '.':
                count += 1

    return count


lines = readFile("d23input.txt")
width = len(lines[0])
expand = 80
grid = gdu.convert_to_grid(lines)
expanded_lines = [['.'] * (width + 2 * expand) for _ in range(expand)]
for line in grid:
    new_line = ['.'] * expand + line + ['.'] * expand
    expanded_lines.append(new_line)
expanded_lines.extend([['.'] * (width + 2 * expand) for _ in range(expand)])
grid = expanded_lines

ops = ['N', 'S', 'W', 'E']
r = 0
done = False
while not done:
    new_grid = deepcopy(grid)
    for i in range(len(new_grid)):
        for j in range(len(new_grid[i])):
            if new_grid[i][j] != '#':
                new_grid[i][j] = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '#':
                neigh = gdu.get_neighbors(grid, i, j)
                if '#' not in neigh:
                    new_grid[i][j] = '#'
                else:
                    for k in range(len(ops)):
                        op = ops[(k + r) % len(ops)]
                        if op == 'N':
                            neigh = gdu.get_neighbors(grid, i, j, custom_dirs=[5, 6, 7])
                        elif op == 'S':
                            neigh = gdu.get_neighbors(grid, i, j, custom_dirs=[1, 2, 3])
                        elif op == 'W':
                            neigh = gdu.get_neighbors(grid, i, j, custom_dirs=[3, 4, 5])
                        elif op == 'E':
                            neigh = gdu.get_neighbors(grid, i, j, custom_dirs=[7, 0, 1])
                        else:
                            neigh = None
                            print("FAIL")
                        if '#' not in neigh:
                            new_grid[i][j] = op
                            if op == 'N':
                                new_grid[i - 1][j] += 1
                            elif op == 'S':
                                new_grid[i + 1][j] += 1
                            elif op == 'W':
                                new_grid[i][j - 1] += 1
                            elif op == 'E':
                                new_grid[i][j + 1] += 1
                            break

    new_new_grid = deepcopy(grid)
    for i in range(len(new_grid)):
        for j in range(len(new_grid[i])):
            new_new_grid[i][j] = '.'

    for i in range(len(new_grid)):
        for j in range(len(new_grid[i])):
            new_i = None
            new_j = None
            if new_grid[i][j] == 'N':
                new_i = i - 1
                new_j = j
            elif new_grid[i][j] == 'S':
                new_i = i + 1
                new_j = j
            elif new_grid[i][j] == 'W':
                new_i = i
                new_j = j - 1
            elif new_grid[i][j] == 'E':
                new_i = i
                new_j = j + 1
            elif new_grid[i][j] == '#':
                new_i = i
                new_j = j
            else:
                continue

            if new_grid[new_i][new_j] == 1:
                new_new_grid[new_i][new_j] = '#'
            else:
                new_new_grid[i][j] = '#'

    done = check_eq(new_new_grid, grid)

    r += 1
    grid = new_new_grid

    if r == 10:
        print(get_bounds(grid))

print(r)
