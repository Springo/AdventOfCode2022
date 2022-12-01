def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


lines = readFile("test_assembly_input.txt")


def parse_val(reg, val):
    if val.isnumeric():
        try:
            val = int(val)
            return val
        except:
            val = float(val)
            return val
    else:
        return get_val(reg, val)


def get_val(reg, key):
    if key not in reg:
        reg[key] = 0
    return reg[key]


reg = dict()

ins_list = []
for line in lines:
    args = line.split()
    parsed_args = [args[0]]
    for arg in args[1:]:
        sign = 1
        new_arg = arg
        if arg[0] == '-':
            sign = -1
            new_arg = new_arg[1:]
        if new_arg.isnumeric():
            try:
                val = int(new_arg)
                parsed_args.append(val * sign)
            except:
                val = float(new_arg)
                parsed_args.append(val * sign)
        else:
            parsed_args.append(arg)
    ins_list.append(parsed_args)



for args in ins_list:
    ins = args[0]
    v1 = args[1]
    if len(args) > 2:
        v2 = args[2]
        if isinstance(v2, str):
            v2 = get_val(reg, v2)

    if ins == "set":
        reg[v1] = v2
    elif ins == "add":
        reg[v1] = get_val(reg, v1) + v2
    elif ins == "mul":
        reg[v1] = get_val(reg, v1) * v2
    elif ins == "mod":
        reg[v1] = get_val(reg, v1) % v2
    else:
        print("OH NO!")

print(reg)
