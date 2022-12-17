def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


def collision_check(x, cur_y, shape, grid):
    for i in range(len(shape)):
        part = shape[i]
        for j in range(part[1], part[0] + 1):
            if cur_y + j >= len(grid):
                continue
            if grid[cur_y + j][x + i] == 1:
                return False
    return True


def display_floor(floor):
    for i in range(len(floor)):
        for c in floor[-(i + 1)]:
            if c == 1:
                print('#', end='')
            elif c == 0:
                print('.', end='')
        print()


lines = readFile("d17input.txt")
wind = lines[0]

shapes = [[(0, 0), (0, 0), (0, 0), (0, 0)],
          [(1, 1), (2, 0), (1, 1)],
          [(0, 0), (0, 0), (2, 0)],
          [(3, 0)],
          [(1, 0), (1, 0)]]

floor = [[1, 1, 1, 1, 1, 1, 1]]

wi = 0

p2_iters = int(1e12)
c1 = 0
c2 = 0
c3 = 0
cap = (p2_iters - 160) % (1855 - 160)
for i in range(2022):
    if i == 160:
        c1 = len(floor)
    if i == 1855:
        c2 = len(floor)
    if i == cap + 160:
        c3 = len(floor)

    top = len(floor)
    piece = shapes[i % 5]
    cur_x = 2
    cur_y = top + 3
    done = False
    while not done:
        w = wind[wi]
        if w == '>':
            if cur_x + len(piece) < 7 and collision_check(cur_x + 1, cur_y, piece, floor):
                cur_x += 1
        elif w == '<':
            if cur_x > 0 and collision_check(cur_x - 1, cur_y, piece, floor):
                cur_x -= 1
        wi = (wi + 1) % len(wind)
        if not collision_check(cur_x, cur_y - 1, piece, floor):
            done = True
        else:
            cur_y -= 1

    new_top = max([a[0] for a in piece]) + cur_y
    for j in range(len(floor) - 1, new_top):
        floor.append([0] * 7)

    for x in range(len(piece)):
        part = piece[x]
        for y in range(part[1], part[0] + 1):
            floor[cur_y + y][cur_x + x] = 1

print(len(floor) - 1)

mult = p2_iters // (1855 - 160)
print(c1 + (c2 - c1) * mult + (c3 - c1) - 1)
