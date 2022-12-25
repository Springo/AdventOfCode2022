def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


def snafu_to_dec(x):
    n = 0
    for c in x:
        nc = None
        if c.isnumeric():
            nc = int(c)
        elif c == '-':
            nc = -1
        elif c == '=':
            nc = -2
        n = n * 5 + nc
    return n


def dec_to_snafu(x):
    snaf_digs = []
    n = x
    while n > 0:
        snaf_digs.append(n % 5)
        n = n // 5

    rem = 0
    snaf = ""
    for i in range(len(snaf_digs)):
        snaf_digs[i] += rem
        if snaf_digs[i] > 2:
            rem = 1
            snaf_digs[i] -= 5
        else:
            rem = 0

        if snaf_digs[i] == -2:
            c = '='
        elif snaf_digs[i] == -1:
            c = '-'
        else:
            c = str(snaf_digs[i])
        snaf = c + snaf
    if rem > 0:
        snaf_digs.append(rem)
        snaf = str(rem) + snaf

    return snaf


lines = readFile("d25input.txt")
count = 0
for line in lines:
    count += snafu_to_dec(line)

print(dec_to_snafu(count))
