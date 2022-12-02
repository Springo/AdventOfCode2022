def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


scores = {'X': 1, 'Y': 2, 'Z': 3}
results = {'X': 0, 'Y': 3, 'Z': 6}

score2 = {
    'X': {
        'A': 3,
        'B': 0,
        'C': 6
    },
    'Y': {
        'A': 6,
        'B': 3,
        'C': 0
    },
    'Z': {
        'A': 0,
        'B': 6,
        'C': 3
    }
}

score3 = {
    'X': {
        'A': 'Z',
        'B': 'X',
        'C': 'Y'
    },
    'Y': {
        'A': 'X',
        'B': 'Y',
        'C': 'Z'
    },
    'Z': {
        'A': 'Y',
        'B': 'Z',
        'C': 'X'
    }
}

lines = readFile("d02input.txt")
total = 0
for line in lines:
    plays = line.split()
    total += scores[plays[1]]
    total += score2[plays[1]][plays[0]]
print(total)

total = 0
for line in lines:
    plays = line.split()
    play2 = score3[plays[1]][plays[0]]
    total += scores[play2]
    total += results[plays[1]]
print(total)
