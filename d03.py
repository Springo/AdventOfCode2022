def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


def get_val(letter):
    val = ord(letter)
    if val < 97:
        val = val - 65 + 26 + 1
    else:
        val = val - 97 + 1
    return val


lines = readFile("d03input.txt")
total = 0
for line in lines:
    n = len(line)
    p1 = set(line[:n // 2])
    p2 = set(line[n // 2:])
    shared = p1.intersection(p2)
    total += get_val(list(shared)[0])
print(total)

total = 0
for i in range(len(lines) // 3):
    l1 = lines[i * 3]
    l2 = lines[i * 3 + 1]
    l3 = lines[i * 3 + 2]
    a = set(l1)
    b = set(l2)
    c = set(l3)
    badge = a.intersection(b).intersection(c)
    total += get_val(list(badge)[0])
print(total)
