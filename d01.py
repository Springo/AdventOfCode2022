def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


lines = readFile("d01input.txt")

cals = []
count = 0
for line in lines:
    if len(line) > 0:
        count += int(line)
    else:
        cals.append(count)
        count = 0

print(max(cals))
print(sum(sorted(cals)[-3:]))
