def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


def count_geodes(mins, resources, robots, bp, cache):
    if (mins, resources, robots) in cache:
        return cache[(mins, resources, robots)]

    ore, clay, obs, geo = resources
    ore_rob, clay_rob, obs_rob, geo_rob = robots
    if mins <= 0:
        return geo

    new_ore = ore + ore_rob
    new_clay = clay + clay_rob
    new_obs = obs + obs_rob
    new_geo = geo + geo_rob

    best = 0
    tried = 0

    if ore >= bp[0]:
        if ore_rob < max(bp[0], bp[1], bp[2], bp[4]):
            new_resources = (new_ore - bp[0], new_clay, new_obs, new_geo)
            new_robots = (ore_rob + 1, clay_rob, obs_rob, geo_rob)
            best = max(best, count_geodes(mins - 1, new_resources, new_robots, bp, cache))
        tried += 1

    if ore >= bp[1]:
        if clay_rob < bp[3]:
            new_resources = (new_ore - bp[1], new_clay, new_obs, new_geo)
            new_robots = (ore_rob, clay_rob + 1, obs_rob, geo_rob)
            best = max(best, count_geodes(mins - 1, new_resources, new_robots, bp, cache))
        tried += 1
    elif clay_rob == 0:
        tried += 1

    if ore >= bp[2] and clay >= bp[3]:
        if obs_rob < bp[5]:
            new_resources = (new_ore - bp[2], new_clay - bp[3], new_obs, new_geo)
            new_robots = (ore_rob, clay_rob, obs_rob + 1, geo_rob)
            best = max(best, count_geodes(mins - 1, new_resources, new_robots, bp, cache))
        tried += 1
    elif obs_rob == 0:
        tried += 1

    if ore >= bp[4] and obs >= bp[5]:
        new_resources = (new_ore - bp[4], new_clay, new_obs - bp[5], new_geo)
        new_robots = (ore_rob, clay_rob, obs_rob, geo_rob + 1)
        best = max(best, count_geodes(mins - 1, new_resources, new_robots, bp, cache))
        tried += 1
    elif geo_rob == 0:
        tried += 1

    if tried < 4:
        new_resources = (new_ore, new_clay, new_obs, new_geo)
        best = max(best, count_geodes(mins - 1, new_resources, robots, bp, cache))

    cache[(mins, resources, robots)] = best
    return best


def execute_ins(ins, resources, robots, bp):
    ore, clay, obs, geo = resources
    ore_rob, clay_rob, obs_rob, geo_rob = robots

    new_resources = None
    new_robots = None
    if ins == "wait":
        new_resources = (ore + ore_rob, clay + clay_rob, obs + obs_rob, geo + geo_rob)
        new_robots = (ore_rob, clay_rob, obs_rob, geo_rob)
    elif ins == "ore":
        new_resources = (ore + ore_rob - bp[0], clay + clay_rob, obs + obs_rob, geo + geo_rob)
        new_robots = (ore_rob + 1, clay_rob, obs_rob, geo_rob)
    elif ins == "clay":
        new_resources = (ore + ore_rob - bp[1], clay + clay_rob, obs + obs_rob, geo + geo_rob)
        new_robots = (ore_rob, clay_rob + 1, obs_rob, geo_rob)
    elif ins == "obs":
        new_resources = (ore + ore_rob - bp[2], clay + clay_rob - bp[3], obs + obs_rob, geo + geo_rob)
        new_robots = (ore_rob, clay_rob, obs_rob + 1, geo_rob)
    elif ins == "geo":
        new_resources = (ore + ore_rob - bp[4], clay + clay_rob, obs + obs_rob - bp[5], geo + geo_rob)
        new_robots = (ore_rob, clay_rob, obs_rob, geo_rob + 1)
    return new_resources, new_robots


bp_list = []
lines = readFile("d19input.txt")
for line in lines:
    ls = line.split()
    bp_list.append((int(ls[6]), int(ls[12]), int(ls[18]), int(ls[21]), int(ls[27]), int(ls[30])))


total = 0
for i in range(len(bp_list)):
    val = count_geodes(24, (0, 0, 0, 0), (1, 0, 0, 0), bp_list[i], {})
    total += (i + 1) * val

print(total)

total = 1
for i in range(0, 3):
    ins = [
        "wait",
        "wait",
        "wait",
        "wait",
        "ore",
        "wait",
        "wait",
        "ore",
        "wait",
        "clay",
        "ore",
    ]
    resources = (0, 0, 0, 0)
    robots = (1, 0, 0, 0)
    for j in ins:
        resources, robots = execute_ins(j, resources, robots, bp_list[i])

    time = 32 - len(ins)
    val = count_geodes(time, resources, robots, bp_list[i], {})
    total *= val

print(total)
