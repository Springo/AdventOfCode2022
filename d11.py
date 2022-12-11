import graph_util as gu
# functions: transpose, bfs, top_sort, scc
import grid_util as gdu
# functions: convert_to_grid, serialize, get_neighbors, count_val, grid_project


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


class Monkey:
    def __init__(self, items, op, test, t1, t2):
        self.items = items
        raw_op = op
        self.test = test
        self.t1 = t1
        self.t2 = t2

        self.op_list = raw_op.split()

    def do_op(self, val):
        if self.op_list[4] == "old":
            v2 = val
        else:
            v2 = int(self.op_list[4])
        if self.op_list[3] == "+":
            new_val = val + v2
        elif self.op_list[3] == "*":
            new_val = val * v2
        else:
            print("FAIL")
        return new_val

    def do_test(self, val):
        return val % self.test == 0


lines = readFile("d11input.txt")


def solve(part1=True):
    monkeys = []

    items = []
    op = ""
    test = -1
    t1 = -1
    t2 = -1
    for line in lines:
        args = line.split()
        if len(args) == 0:
            monkeys.append(Monkey(items, op, test, t1, t2))
            items = []
            op = ""
            test = -1
            t1 = -1
            t2 = -1

        elif args[0] == "Starting":
            for x in args[2:]:
                if x[-1] == ',':
                    items.append(int(x[:-1]))
                else:
                    items.append(int(x))
        elif args[0] == "Operation:":
            ls = line.split(": ")
            op = ls[1]
        elif args[0] == "Test:":
            test = int(args[-1])
        elif args[0] == "If":
            if args[1] == "true:":
                t1 = int(args[-1])
            elif args[1] == "false:":
                t2 = int(args[-1])

    monkeys.append(Monkey(items, op, test, t1, t2))
    worry_mod = 1
    for m in monkeys:
        worry_mod *= m.test

    inspects = [0] * len(monkeys)
    if part1:
        n_iters = 20
    else:
        n_iters = 10000
    for iter in range(n_iters):
        for j in range(len(monkeys)):
            m = monkeys[j]
            n = len(m.items)
            for i in range(n):
                x = m.items.pop(0)
                x = m.do_op(x)
                inspects[j] += 1
                if part1:
                    x = x // 3
                else:
                    x = x % worry_mod
                if m.do_test(x):
                    monkeys[m.t1].items.append(x)
                else:
                    monkeys[m.t2].items.append(x)

    inspects = sorted(inspects)
    return inspects[-1] * inspects[-2]


print(solve(True))
print(solve(False))

