def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


def add_sand(grid):
    sand_x = 500
    sand_y = 0
    done = False
    while not done:
        if sand_y + 1 >= len(grid):
            return False
        if grid[sand_y + 1][sand_x] == '.':
            sand_y += 1
        elif grid[sand_y + 1][sand_x - 1] == '.':
            sand_x -= 1
            sand_y += 1
        elif grid[sand_y + 1][sand_x + 1] == '.':
            sand_x += 1
            sand_y += 1
        else:
            done = True
    grid[sand_y][sand_x] = 'O'
    return True


def add_sand_fast(grid):
    def get_val(a):
        if a == '#' or a == '.':
            return 0
        else:
            return a

    count = 1
    grid[0][500] = 1
    for y in range(1, len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '.':
                if x == 0:
                    if get_val(grid[y - 1][x]) > 0:
                        grid[y][x] = get_val(grid[y - 1][x]) + 1
                    else:
                        grid[y][x] = get_val(grid[y - 1][x + 1])
                elif x == len(grid[y]) - 1:
                    if get_val(grid[y - 1][x]) > 0:
                        grid[y][x] = get_val(grid[y - 1][x]) + 1
                    else:
                        grid[y][x] = get_val(grid[y - 1][x - 1])
                else:
                    grid[y][x] = max(get_val(grid[y - 1][x - 1]), get_val(grid[y - 1][x]), get_val(grid[y - 1][x + 1]))
                count += grid[y][x]
    return count


part1 = True
grid = [['.'] * 1000 for _ in range(400)]
lines = readFile("d14input.txt")
largest_y = 0
for line in lines:
    ls = line.split(' -> ')
    c_list = []
    for coord in ls:
        x, y = coord.split(',')
        x, y = int(x), int(y)
        if y > largest_y:
            largest_y = y
        c_list.append((x, y))

    cur_x, cur_y = c_list[0]
    for x, y in c_list[1:]:
        x1 = min(cur_x, x)
        x2 = max(cur_x, x)
        y1 = min(cur_y, y)
        y2 = max(cur_y, y)
        if x1 == x2:
            for i in range(y2 - y1 + 1):
                grid[y1 + i][x1] = '#'
        elif y1 == y2:
            for i in range(x2 - x1 + 1):
                grid[y1][x1 + i] = '#'

        cur_x = x
        cur_y = y

if part1:
    count = 0
    while add_sand(grid):
        count += 1
    print(count)
else:
    for j in range(len(grid[0])):
        grid[largest_y + 2][j] = '#'

    print(add_sand_fast(grid))
