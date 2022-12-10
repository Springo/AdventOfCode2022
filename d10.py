def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


def update_crt(X, cycle, crt, crt_row):
    mc = cycle % 40
    if X == mc or (mc == X + 1) or (mc == X + 2):
        pix = "#"
    else:
        pix = "."

    if len(crt_row) < 40:
        crt_row.append(pix)
        return crt_row
    else:
        crt.append(crt_row)
        return [pix]


X = 1
lines = readFile("d10input.txt")

cycle_vals = dict()

cycle = 1
cycle_vals[cycle] = X
crt_lines = []
crt_row = []
for line in lines:
    ls = line.split()
    if ls[0] == "noop":
        crt_row = update_crt(X, cycle, crt_lines, crt_row)
        cycle += 1
        cycle_vals[cycle] = X
    elif ls[0] == "addx":
        crt_row = update_crt(X, cycle, crt_lines, crt_row)
        cycle += 1
        cycle_vals[cycle] = X

        crt_row = update_crt(X, cycle, crt_lines, crt_row)
        X += int(ls[1])
        cycle += 1
        cycle_vals[cycle] = X
crt_lines.append(crt_row)

str_vals = [20, 60, 100, 140, 180, 220]
total = 0
for val in str_vals:
    total += cycle_vals[val] * val
print(total)


for line in crt_lines:
    for c in line:
        print(c, end=" ")
    print()
