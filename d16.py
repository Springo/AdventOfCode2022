from itertools import chain, combinations
from copy import deepcopy


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


def all_pairs_sp(dist):
    keys = list(dist.keys())
    for n1 in keys:
        for n2 in keys:
            dist[n2][n2] = 0
            for n3 in keys:
                if n3 not in dist[n2]:
                    dist[n2][n3] = 1e8
                if n1 not in dist[n2]:
                    dist[n2][n1] = 1e8
                if n3 not in dist[n1]:
                    dist[n1][n3] = 1e8
                dist[n2][n3] = min(dist[n2][n3], dist[n2][n1] + dist[n1][n3])


def max_pressure_path(loc, time, open, allowed, rates, dist, state_dict):
    if (loc, time, frozenset(open)) in state_dict:
        return state_dict[(loc, time, frozenset(open))]

    best = 0
    if time > 0:
        for nex in allowed:
            if nex not in open and dist[loc][nex] + 1 <= time:
                new_open = deepcopy(open)
                new_open.add(nex)
                rate = rates[nex] * (time - dist[loc][nex] - 1)
                best = max(best, rate + max_pressure_path(nex, time - dist[loc][nex] - 1, new_open, allowed, rates, dist, state_dict))

    state_dict[(loc, time, frozenset(open))] = best
    return best


def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def iter_all_paths(valves, rates, dist):
    seen = dict()
    best = 0
    for valve_set in powerset(valves):
        other_set = valves.difference(valve_set)

        s1 = frozenset(valve_set)
        s2 = frozenset(other_set)
        if s1 in seen:
            v1 = seen[s1]
        else:
            v1 = max_pressure_path('AA', 26, {'AA'}, valve_set, rates, dist, {})
            seen[s1] = v1
        if s2 in seen:
            v2 = seen[s2]
        else:
            v2 = max_pressure_path('AA', 26, {'AA'}, other_set, rates, dist, {})
            seen[s2] = v2
        best = max(best, v1 + v2)

    return best


lines = readFile("d16input.txt")
rates = dict()
paths = dict()
dist = dict()
for line in lines:
    ls = line.split()
    valve = ls[1]
    rate = int(ls[4].split('=')[1][:-1])
    rates[valve] = rate
    paths[valve] = []
    dist[valve] = dict()
    i = 9
    while i < len(ls) - 1:
        paths[valve].append(ls[i][:-1])
        dist[valve][ls[i][:-1]] = 1
        i += 1
    paths[valve].append(ls[i])
    dist[valve][ls[i]] = 1


non_empty = set()
for valve in rates:
    if rates[valve] > 0:
        non_empty.add(valve)
non_empty.add('AA')

for i in range(len(dist)):
    for valve in non_empty:
        keys = list(dist[valve].keys())
        for ne in keys:
            if ne not in non_empty:
                for ne_ne in dist[ne]:
                    if ne_ne != valve:
                        if ne_ne in dist[valve]:
                            dist[valve][ne_ne] = min(dist[valve][ne_ne], dist[valve][ne] + dist[ne][ne_ne])
                        else:
                            dist[valve][ne_ne] = dist[valve][ne] + dist[ne][ne_ne]
                dist[valve].pop(ne, None)

keys = list(dist.keys())
for key in keys:
    if key not in non_empty:
        dist.pop(key, None)

for valve in dist:
    keys = list(dist[valve].keys())
    for key in keys:
        if dist[valve][key] >= 58:
            dist[valve].pop(key, None)

all_pairs_sp(dist)

non_empty.remove('AA')
print(max_pressure_path('AA', 30, {'AA'}, non_empty, rates, dist, {}))
print(iter_all_paths(non_empty, rates, dist))
