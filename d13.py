from functools import cmp_to_key


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


def checkpair(x1, x2):
    if type(x1) == int and type(x2) == int:
        if x1 < x2:
            return -1
        elif x1 > x2:
            return 1
        else:
            return 0
    if type(x1) == int:
        return checkpair([x1], x2)
    if type(x2) == int:
        return checkpair(x1, [x2])

    for i in range(len(x1)):
        if i >= len(x2):
            return 1
        out = checkpair(x1[i], x2[i])
        if out != 0:
            return out

    if len(x1) == len(x2):
        return 0
    return -1


lines = readFile("d13input.txt")

all_lines = []
idx = 1
i = 0
total = 0
while i < len(lines):
    x1 = eval(lines[i])
    x2 = eval(lines[i + 1])
    all_lines.append(x1)
    all_lines.append(x2)

    if checkpair(x1, x2) == -1:
        total += idx
    idx += 1
    i += 3

print(total)

a = [[2]]
b = [[6]]
all_lines.append(a)
all_lines.append(b)
all_lines = sorted(all_lines, key=cmp_to_key(checkpair))

ia = all_lines.index(a) + 1
ib = all_lines.index(b) + 1

print(ia * ib)
