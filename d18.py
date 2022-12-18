def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


def get_neighbors(x, y, z):
    return [(x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1)]


def dfs(grid):
    seen = {(0, 0, 0)}
    count = 0
    q = [(0, 0, 0)]

    while len(q) > 0:
        x, y, z = q.pop()
        for x2, y2, z2 in get_neighbors(x, y, z):
            if x2 < 0 or y2 < 0 or z2 < 0 or x2 >= 50 or y2 >= 50 or z2 >= 50:
                continue

            if grid[x2][y2][z2] == 1:
                count += 1
            else:
                if (x2, y2, z2) not in seen:
                    q.append((x2, y2, z2))
                    seen.add((x2, y2, z2))

    return count


grid = [[[0] * 50 for _ in range(50)] for _2 in range(50)]
count = 0
lines = readFile("d18input.txt")
for line in lines:
    coords = [int(x) for x in line.split(',')]
    x = coords[0] + 1
    y = coords[1] + 1
    z = coords[2] + 1

    grid[x][y][z] = 1
    for x2, y2, z2 in get_neighbors(x, y, z):
        if grid[x2][y2][z2] == 1:
            count -= 1
        else:
            count += 1

print(count)
print(dfs(grid))
