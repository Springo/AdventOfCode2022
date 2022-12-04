def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


lines = readFile("d04input.txt")

count = 0
overlap = 0
for line in lines:
    s = line.split(',')
    p1 = s[0].split('-')
    p2 = s[1].split('-')
    p1 = [int(p1[0]), int(p1[1])]
    p2 = [int(p2[0]), int(p2[1])]

    if p2[0] >= p1[0] and p2[1] <= p1[1]:
        count += 1
    elif p2[0] <= p1[0] and p2[1] >= p1[1]:
        count += 1

    if max(0, min(p2[1], p1[1]) - max(p2[0], p1[0]) + 1) > 0:
        overlap += 1

print(count)
print(overlap)
