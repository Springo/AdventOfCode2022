def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


part1 = False

raw_stacks = [
    "HCR",
    "BJHLSF",
    "RMDHJTQ",
    "SGRHZBJ",
    "RPFZTDCB",
    "THCG",
    "SNVZBPWL",
    "RJQGC",
    "LDTRHPFS"
]

stacks = [[*stack] for stack in raw_stacks]

lines = readFile("d05input.txt")

skip = True
for line in lines:
    if len(line) == 0:
        skip = False
        continue
    if skip:
        continue

    ls = line.split()
    s = int(ls[1])
    b1 = int(ls[3]) - 1
    b2 = int(ls[5]) - 1

    if part1:
        for i in range(s):
            if len(stacks[b1]) > 0:
                x = stacks[b1].pop()
                stacks[b2].append(x)
    else:
        new_stack = []
        for i in range(s):
            if len(stacks[b1]) > 0:
                x = stacks[b1].pop()
                new_stack.append(x)

        n = len(new_stack)
        for i in range(n):
            stacks[b2].append(new_stack.pop())


for stack in stacks:
    print(stack[-1], end="")

