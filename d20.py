from blist import blist


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


def move_item(items, val, j):
    i = items.index((val, j))
    new_loc = (i + val) % (len(items) - 1)
    if new_loc < i:
        return items[:new_loc] + [(val, j)] + items[new_loc:i] + items[i+1:]
    elif new_loc > i:
        return items[:i] + items[i+1:new_loc + 1] + [(val, j)] + items[new_loc + 1:]
    else:
        return items


def grove_coord(raw_items, iters, encryption):
    items = []
    zero_idx = -1
    for i in range(len(raw_items)):
        items.append((raw_items[i] * encryption, i))
        if raw_items[i] == 0:
            zero_idx = i
    items = blist(items)

    for iter in range(iters):
        for i in range(len(raw_items)):
            items = move_item(items, raw_items[i] * encryption, i)

    zero_idx2 = items.index((0, zero_idx))
    x1 = items[(zero_idx2 + 1000) % len(items)]
    x2 = items[(zero_idx2 + 2000) % len(items)]
    x3 = items[(zero_idx2 + 3000) % len(items)]
    return x1[0] + x2[0] + x3[0]


lines = readFile("d20input.txt")
raw_items = []
for line in lines:
    raw_items.append(int(line))

print(grove_coord(raw_items, 1, 1))
print(grove_coord(raw_items, 10, 811589153))
