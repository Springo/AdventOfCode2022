def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


def update_indices(i, j, i2, j2):
    out_i = i2
    out_j = j2
    if abs(i - i2) > 1 or abs(j - j2) > 1:
        if i - i2 > 0:
            out_i += 1
        elif i2 - i > 0:
            out_i -= 1

        if j - j2 > 0:
            out_j += 1
        elif j2 - j > 0:
            out_j -= 1
    return out_i, out_j


def track_tail(n, lines):
    idx = []
    for k in range(n):
        idx.append([0, 0])

    visited = set()
    visited.add((0, 0))

    for line in lines:
        ls = line.split()
        for k in range(int(ls[1])):
            if ls[0] == 'R':
                idx[0][1] += 1
            elif ls[0] == 'L':
                idx[0][1] -= 1
            elif ls[0] == 'U':
                idx[0][0] -= 1
            elif ls[0] == 'D':
                idx[0][0] += 1
            else:
                print("ERROR")

            for l in range(1, len(idx)):
                idx[l][0], idx[l][1] = update_indices(idx[l - 1][0], idx[l - 1][1], idx[l][0], idx[l][1])
            visited.add((idx[-1][0], idx[-1][1]))

    return len(visited)


lines = readFile("d09input.txt")

print(track_tail(2, lines))
print(track_tail(10, lines))
