import grid_util as gdu


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


def wrap(val, lb, ub):
    return ((val - lb) % (ub - lb)) + lb


cube_bounds = {
    1: [[0, 50], [100, 150]],
    2: [[0, 50], [50, 100]],
    3: [[50, 100], [50, 100]],
    4: [[100, 150], [50, 100]],
    5: [[100, 150], [0, 50]],
    6: [[150, 200], [0, 50]]
}


def norm_coords(y, x, face):
    return y - cube_bounds[face][0][0], x - cube_bounds[face][1][0]


def reg_coords(y, x, face):
    return y + cube_bounds[face][0][0], x + cube_bounds[face][1][0]


def get_face(y, x):
    face = 0
    if y < 50:
        if 50 <= x < 100:
            face = 2
        elif x >= 100:
            face = 1
    elif 50 <= y < 100:
        face = 3
    elif 100 <= y < 150:
        if x < 50:
            face = 5
        elif 50 <= x < 100:
            face = 4
    elif 150 <= y < 200:
        face = 6
    return face


def reg_wrap(y, x, new_y, new_x, dir):
    face = get_face(y, x)
    norm_y, norm_x = norm_coords(new_y, new_x, face)
    if 0 <= norm_y < 50 and 0 <= norm_x < 50:
        return new_y, new_x, dir

    norm_y = norm_y % 50
    norm_x = norm_x % 50

    cube_neigh = {
        1: [2, 1, 2, 1],
        2: [1, 3, 1, 4],
        3: [3, 4, 3, 2],
        4: [5, 2, 5, 3],
        5: [4, 6, 4, 6],
        6: [6, 5, 6, 5]
    }

    new_face = cube_neigh[face][dir // 2]
    trans_y, trans_x = reg_coords(norm_y, norm_x, new_face)
    return trans_y, trans_x, dir


def cube_wrap(y, x, new_y, new_x, dir):
    face = get_face(y, x)
    norm_y, norm_x = norm_coords(new_y, new_x, face)
    if 0 <= norm_y < 50 and 0 <= norm_x < 50:
        return new_y, new_x, dir

    trans_x = new_x
    trans_y = new_y
    trans_dir = dir

    y2 = None
    x2 = None
    new_face = None

    if face == 1:
        if dir == 0:
            y2 = 49 - norm_y
            x2 = 49
            trans_dir = 4
            new_face = 4
        elif dir == 2:
            y2 = norm_x
            x2 = 49
            trans_dir = 4
            new_face = 3
        elif dir == 6:
            y2 = 49
            x2 = norm_x
            trans_dir = 6
            new_face = 6
    elif face == 2:
        if dir == 4:
            y2 = 49 - norm_y
            x2 = 0
            trans_dir = 0
            new_face = 5
        elif dir == 6:
            y2 = norm_x
            x2 = 0
            trans_dir = 0
            new_face = 6
    elif face == 3:
        if dir == 0:
            y2 = 49
            x2 = norm_y
            trans_dir = 6
            new_face = 1
        elif dir == 4:
            y2 = 0
            x2 = norm_y
            trans_dir = 2
            new_face = 5
    elif face == 4:
        if dir == 0:
            y2 = 49 - norm_y
            x2 = 49
            trans_dir = 4
            new_face = 1
        elif dir == 2:
            y2 = norm_x
            x2 = 49
            trans_dir = 4
            new_face = 6
    elif face == 5:
        if dir == 4:
            y2 = 49 - norm_y
            x2 = 0
            trans_dir = 0
            new_face = 2
        elif dir == 6:
            y2 = norm_x
            x2 = 0
            trans_dir = 0
            new_face = 3
    elif face == 6:
        if dir == 0:
            y2 = 49
            x2 = norm_y
            trans_dir = 6
            new_face = 4
        elif dir == 2:
            y2 = 0
            x2 = norm_x
            trans_dir = 2
            new_face = 1
        elif dir == 4:
            y2 = 0
            x2 = norm_y
            trans_dir = 2
            new_face = 2

    if y2 is not None:
        trans_y, trans_x = reg_coords(y2, x2, new_face)

    return trans_y, trans_x, trans_dir


lines = readFile("d22input.txt")
grid = []
read_dirs = False
commands = []
for line in lines:
    if len(line) == 0:
        read_dirs = True
    else:
        if read_dirs:
            commands.append(line)
        else:
            grid.append(line)


grid = gdu.convert_to_grid(grid)

com_num = ""
coms = []
for c in commands[0]:
    if not c.isnumeric():
        coms.append((int(com_num), c))
        com_num = ""
    else:
        com_num = com_num + c
if len(com_num) > 0:
    coms.append((int(com_num), 'N'))


def get_password(cube=False):
    y, x = reg_coords(0, 0, 2)
    dir = 0
    for steps, turn in coms:
        for i in range(1, steps + 1):
            new_x = x
            new_y = y
            if dir == 0:
                new_x += 1
            elif dir == 2:
                new_y += 1
            elif dir == 4:
                new_x -= 1
            elif dir == 6:
                new_y -= 1

            if cube:
                new_y, new_x, new_dir = cube_wrap(y, x, new_y, new_x, dir)
            else:
                new_y, new_x, new_dir = reg_wrap(y, x, new_y, new_x, dir)
            if grid[new_y][new_x] == '#':
                break
            else:
                y = new_y
                x = new_x
                dir = new_dir
        if turn == 'R':
            dir = (dir + 2) % 8
        elif turn == 'L':
            dir = (dir - 2) % 8

    password = (1000 * (y + 1)) + (4 * (x + 1)) + (dir // 2)
    return password


print(get_password(False))
print(get_password(True))
