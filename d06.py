def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


def get_marker(l, n):
    count = n
    for i in range(len(l) - n + 1):
        group = l[i:i + n]
        lets = set(group)
        if len(lets) == n:
            break
        count += 1

    return count


lines = readFile("d06input.txt")
l = lines[0]

print(get_marker(l, 4))
print(get_marker(l, 14))
