def convert_to_grid(lines, convert_numeric=True):
    grid = []
    for line in lines:
        l = []
        for c in line:
            val = c
            if convert_numeric and c.isnumeric():
                try:
                    val = int(c)
                except:
                    val = float(c)
            l.append(val)
        grid.append(l)

    return grid


def serialize(grid):
    ser = ""
    for row in grid:
        for c in row:
            ser = ser + c
    return ser


def grid_project(grid, i, j, dir, step=1):
    if dir == 0:
        if j < len(grid[i]) - step:
            return i, j + step
    elif dir == 1:
        if i < len(grid) - step and j < len(grid[i]) - step:
            return i + step, j + step
    elif dir == 2:
        if i < len(grid) - step:
            return i + step, j
    elif dir == 3:
        if i < len(grid) - step and j >= step:
            return i + step, j - step
    elif dir == 4:
        if j >= step:
            return i, j - step
    elif dir == 5:
        if i >= step and j >= step:
            return i - step, j - step
    elif dir == 6:
        if i >= step:
            return i - step, j
    elif dir == 7:
        if i >= step and j < len(grid[i]) - step:
            return i - step, j + step
    return None, None


def get_region(grid, i1, j1, i2, j2, default=None):
    region = []
    for i in range(i1, i2 + 1):
        if i < 0 or i >= len(grid):
            if default is not None:
                row = [default] * (j2 - j1 + 1)
                region.append(row)
        else:
            row = []
            for j in range(j1, j2 + 1):
                if j < 0 or j >= len(grid[i]):
                    if default is not None:
                        row.append(default)
                else:
                    row.append(grid[i][j])
            region.append(row)

    return region


def get_neighbors(grid, i, j, indices=False, orth=False, custom_dirs=None, default=None):
    neigh = []
    if custom_dirs is not None:
        dirs = custom_dirs
    else:
        if orth:
            dirs = [0, 2, 4, 6]
        else:
            dirs = range(8)
    for dir in dirs:
        i2, j2 = grid_project(grid, i, j, dir)
        if i2 is not None:
            if indices:
                neigh.append((i2, j2))
            else:
                neigh.append(grid[i2][j2])
        else:
            if default is not None:
                neigh.append(default)
    return neigh


def count_val(grid, val):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == val:
                count += 1

    return count
