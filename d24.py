import grid_util as gdu

from collections import deque
from math import lcm


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


def get_timings(grid, y, x):
    n_row = len(grid) - 2
    n_col = len(grid[y]) - 2

    vert_timings = set()
    for i in range(len(grid)):
        if grid[i][x] == '^':
            vert_timings.add((i - y) % n_row)
        elif grid[i][x] == 'v':
            vert_timings.add((y - i) % n_row)

    hor_timings = set()
    for i in range(len(grid[y])):
        if grid[y][i] == '<':
            hor_timings.add((i - x) % n_col)
        elif grid[y][i] == '>':
            hor_timings.add((x - i) % n_col)

    return vert_timings, hor_timings


def bfs(start_y, start_x, end_y, end_x, t_start, t_grid):
    n_row = len(t_grid)
    n_col = len(t_grid[0])
    mod = lcm(n_row, n_col)

    q = deque([(start_y, start_x, t_start)])

    shortest = dict()
    shortest[(start_y, start_x, t_start)] = 0
    while len(q) > 0:
        y1, x1, t = q.popleft()
        prev_t = shortest[(y1, x1, t)]

        if y1 == end_y and x1 == end_x:
            return prev_t, t

        t_y = (t + 1) % n_row
        t_x = (t + 1) % n_col

        if t_y not in t_grid[y1][x1][0] and t_x not in t_grid[y1][x1][1]:
            wait_state = (y1, x1, (t + 1) % mod)
            if wait_state not in shortest:
                q.append(wait_state)
                shortest[wait_state] = prev_t + 1

        neigh = gdu.get_neighbors(t_grid, y1, x1, indices=True, orth=True)
        for i, j in neigh:
            if t_y not in t_grid[i][j][0] and t_x not in t_grid[i][j][1]:
                new_state = (i, j, (t + 1) % mod)
                if new_state not in shortest:
                    q.append(new_state)
                    shortest[new_state] = prev_t + 1

    return None, None


def get_first_z_results(start_y, start_x, end_y, end_x, t_begin, z, t_grid):
    n_row = len(t_grid)
    n_col = len(t_grid[0])
    mod = lcm(n_row, n_col)

    best = None
    best_t = None
    count = 0
    for t in range(mod):
        start_t = (t_begin + t) % mod
        if start_t not in t_grid[0][0][0] and start_t not in t_grid[0][0][1]:
            out, out_t = bfs(start_y, start_x, end_y, end_x, start_t, t_grid)
            if out is not None:
                if best is None or out + t + 2 < best:
                    best = out + t + 2
                    best_t = out_t
                    count += 1

                    if count >= z:
                        break

    return best, best_t


lines = readFile("d24input.txt")
grid = gdu.convert_to_grid(lines)

t_grid = []
for i in range(1, len(grid) - 1):
    new_line = []
    for j in range(1, len(grid[i]) - 1):
        ht, vt = get_timings(grid, i, j)
        new_line.append((ht, vt))
    t_grid.append(new_line)

n_row = len(t_grid)
n_col = len(t_grid[0])
mod = lcm(n_row, n_col)

z = 1
t1, new_t = get_first_z_results(0, 0, n_row - 1, n_col - 1, 1, z, t_grid)
print(t1)
t2, new_t = get_first_z_results(n_row - 1, n_col - 1, 0, 0, new_t + 2, z, t_grid)
t3, new_t = get_first_z_results(0, 0, n_row - 1, n_col - 1, new_t + 2, z, t_grid)
print(t1 + t2 + t3)
