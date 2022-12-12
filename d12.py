import grid_util as gdu


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


def valid(cur, oth):
    x = cur
    y = oth
    if cur == 'S':
        x = 'a'
    elif cur == 'E':
        x = 'z'
    if oth == 'S':
        y = 'a'
    elif oth == 'E':
        y = 'z'
    if ord(y) - ord(x) >= -1:
        return True
    return False


def bfs(start, end_c):
    Q = [start]
    seen = dict()
    seen[start] = 0
    while len(Q) > 0:
        i, j = Q.pop(0)
        d = seen[(i, j)]
        if elev[i][j] == end_c:
            return seen[(i, j)]
        if i > 0:
            if (i - 1, j) not in seen and valid(elev[i][j], elev[i - 1][j]):
                seen[(i - 1, j)] = d + 1
                Q.append((i - 1, j))
        if i < len(elev) - 1:
            if (i + 1, j) not in seen and valid(elev[i][j], elev[i + 1][j]):
                seen[(i + 1, j)] = d + 1
                Q.append((i + 1, j))
        if j > 0:
            if (i, j - 1) not in seen and valid(elev[i][j], elev[i][j - 1]):
                seen[(i, j - 1)] = d + 1
                Q.append((i, j - 1))
        if j < len(elev[i]) - 1:
            if (i, j + 1) not in seen and valid(elev[i][j], elev[i][j + 1]):
                seen[(i, j + 1)] = d + 1
                Q.append((i, j + 1))
    return None


lines = readFile("d12input.txt")

elev = gdu.convert_to_grid(lines)
start = (-1, -1)
for i in range(len(elev)):
    for j in range(len(elev[i])):
        if elev[i][j] == 'E':
            start = (i, j)


print(bfs(start, 'S'))
print(bfs(start, 'a'))
