def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


class Node:
    def __init__(self, name, isdir, val, pa=None):
        self.name = name
        self.pa = pa
        self.isdir = isdir
        self.dirs = dict()
        self.files = dict()
        self.val = val


def set_vals(root):
    total = root.val
    if root.val == -1:
        total = 0
        for f in root.files:
            total += root.files[f].val
        for d in root.dirs:
            total += set_vals(root.dirs[d])
    root.val = total
    return total


def sum_sizes(root, thresh):
    total = 0
    if root.val <= thresh:
        total += root.val
    for d in root.dirs:
        total += sum_sizes(root.dirs[d], thresh)
    return total


def min_free_size(root, thresh):
    size = -1
    if root.val >= thresh:
        size = root.val
    else:
        return -1

    for d in root.dirs:
        new_size = min_free_size(root.dirs[d], thresh)
        if new_size != -1 and new_size < size:
            size = new_size

    return size


lines = readFile("d07input.txt")
root = Node('/', True, -1)
cur = root
for line in lines[1:]:
    ls = line.split()
    if ls[0] == '$':
        if ls[1] == "cd":
            if ls[2] == "..":
                cur = cur.pa
            else:
                cur = cur.dirs[ls[2]]
    elif ls[0] == "dir":
        newdir = Node(ls[1], True, -1, pa=cur)
        cur.dirs[ls[1]] = newdir
    else:
        newfile = Node(ls[1], True, int(ls[0]), pa=cur)
        cur.files[ls[1]] = newfile


set_vals(root)

print(sum_sizes(root, 100000))

cut = root.val - 40000000

print(min_free_size(root, cut))
