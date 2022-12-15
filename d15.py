def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


def mandist(x1, y1, x2, y2):
    return abs(y2 - y1) + abs(x2 - x1)


def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for cur in intervals:
        prev = merged[-1]
        if cur[0] <= prev[1]:
            prev[1] = max(prev[1], cur[1])
        else:
            merged.append(cur)

    return merged


def check_invalid(y_check):
    intervals = []
    for x, y in dists:
        proj = mandist(x, y, x, y_check)
        rem_dist = dists[(x, y)] - proj
        if rem_dist >= 0:
            intervals.append([x - rem_dist, x + rem_dist])

    return merge_intervals(intervals)


def cut_intervals(intervals, a, b):
    new_intervals = []
    for bar in intervals:
        x1 = bar[0]
        x2 = bar[1]
        new_x1 = max(a, x1)
        new_x2 = min(b, x2)
        if new_x2 < new_x1:
            continue
        new_intervals.append([new_x1, new_x2])
    return new_intervals


lines = readFile("d15input.txt")
sensors = dict()
for line in lines:
    ls = line.split()
    sx = int(ls[2].split('=')[1][:-1])
    sy = int(ls[3].split('=')[1][:-1])
    bx = int(ls[8].split('=')[1][:-1])
    by = int(ls[9].split('=')[1])
    sensors[(sx, sy)] = (bx, by)

dists = dict()
for x, y in sensors:
    x2, y2 = sensors[(x, y)]
    dists[(x, y)] = mandist(x, y, x2, y2)

y_check = 2000000
merged_intervals = check_invalid(y_check)

count = 0
for bar in merged_intervals:
    count += bar[1] - bar[0] + 1

collision_set = set()
for x, y in sensors:
    x2, y2 = sensors[(x, y)]
    if y2 == y_check:
        collision_set.add((x2, y2))

count -= len(collision_set)
print(count)


cut = []
for y in range(4000001):
    merged_intervals = check_invalid(y)
    cut = cut_intervals(merged_intervals, 0, 4000000)
    if len(cut) > 1:
        x_val = cut[0][1] + 1
        answer = x_val * 4000000 + y
        print(answer)
        break

