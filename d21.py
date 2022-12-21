import graph_util as gu


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


def bfs(adj_list, key, target):
    change_list = set()
    explored = dict()
    q = [(key, 0)]
    explored[key] = True
    change_list.add(key)
    while len(q) > 0:
        item, dist = q.pop(0)
        for cur in adj_list[item]:
            id = cur
            if id == target:
                change_list.add(id)
                return change_list

            if id not in explored:
                change_list.add(id)
                q.append((id, dist + 1))
                explored[id] = True
    return -1


adj_list = dict()
rev_adj_list = dict()
op = dict()
lines = readFile("d21input.txt")
for line in lines:
    ls = line.split()
    x = ls[0][:-1]
    if x not in adj_list:
        adj_list[x] = []
    if x not in rev_adj_list:
        rev_adj_list[x] = []
    if len(ls) == 2:
        op[x] = int(ls[1])
    elif len(ls) == 4:
        a = ls[1]
        b = ls[3]
        op[x] = ls[2]
        rev_adj_list[x].append(a)
        rev_adj_list[x].append(b)
        if a not in adj_list:
            adj_list[a] = []
        if b not in adj_list:
            adj_list[b] = []
        adj_list[a].append(x)
        adj_list[b].append(x)
    else:
        print("NO")


def must_match(node, target, end, values, change_list):
    if node == end:
        return target

    a = rev_adj_list[node][0]
    b = rev_adj_list[node][1]
    a_val = values[a]
    b_val = values[b]
    if a in change_list:
        cur_node = a
        oth = b_val
        first = True
    elif b in change_list:
        cur_node = b
        oth = a_val
        first = False
    else:
        return -1

    if op[node] == '+':
        return must_match(cur_node, target - oth, end, values, change_list)
    elif op[node] == '-':
        if first:
            return must_match(cur_node, target + oth, end, values, change_list)
        else:
            return must_match(cur_node, oth - target, end, values, change_list)
    elif op[node] == '*':
        return must_match(cur_node, target // oth, end, values, change_list)
    elif op[node] == '/':
        if first:
            return must_match(cur_node, target * oth, end, values, change_list)
        else:
            return must_match(cur_node, oth // target, end, values, change_list)
    else:
        return -1


order = gu.top_sort(adj_list)
vals = dict()
for x in order:
    vals[x] = 0
    if op[x] == '+':
        vals[x] += vals[rev_adj_list[x][0]]
        vals[x] += vals[rev_adj_list[x][1]]
    elif op[x] == '*':
        vals[x] += vals[rev_adj_list[x][0]]
        vals[x] *= vals[rev_adj_list[x][1]]
    elif op[x] == '-':
        vals[x] += vals[rev_adj_list[x][0]]
        vals[x] -= vals[rev_adj_list[x][1]]
    elif op[x] == '/':
        vals[x] += vals[rev_adj_list[x][0]]
        vals[x] = vals[x] // vals[rev_adj_list[x][1]]
    else:
        vals[x] = op[x]

print(vals["root"])

change_list = bfs(adj_list, 'humn', 'root')

op['root'] = '-'
print(must_match('root', 0, 'humn', vals, change_list))
