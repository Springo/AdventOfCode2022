def top_sort(adj_list):
    visited = dict()
    for key in adj_list:
        visited[key] = False

    stack = []

    for key in adj_list:
        if not visited[key]:
            _top_sort_helper(adj_list, key, visited, stack)

    return stack[::-1]


def _top_sort_helper(adj_list, v, visited, stack):
    visited[v] = True
    for neighb in adj_list[v]:
        if not visited[neighb]:
            _top_sort_helper(adj_list, neighb, visited, stack)

    stack.append(v)


def transpose(adj_list):
    new_adj_list = dict()
    for key in adj_list:
        new_adj_list[key] = []

    for key in adj_list:
        for v in adj_list[key]:
            if v not in new_adj_list:
                new_adj_list[v] = []
            new_adj_list[v].append(key)
    return new_adj_list


def scc(adj_list):
    visited = set()
    back_order = []

    def visit(u):
        if u not in visited:
            visited.add(u)
            for v in adj_list[u]:
                visit(v)
            back_order.append(u)

    for u in adj_list:
        visit(u)

    visited = set()
    adj_list_t = transpose(adj_list)

    def assign(u):
        if u not in visited:
            visited.add(u)
            component = [u]
            for v in adj_list_t[u]:
                result = assign(v)
                if result is not None:
                    component.extend(result)
            return component
        return None

    components = []
    for u in back_order[::-1]:
        comp = assign(u)
        if comp is not None:
            components.append(comp)
    return components


def bfs(adj_list, key, target):
    explored = dict()
    q = [(key, 0)]
    explored[key] = True
    while len(q) > 0:
        item, dist = q.pop(0)
        for cur in adj_list[item]:
            _, id = cur
            if id == target:
                return dist + 1

            if id not in explored:
                q.append((id, dist + 1))
                explored[id] = True
    return -1


if __name__ == "__main__":
    adj_list = dict()
    adj_list['x'] = ['y']
    adj_list['y'] = []
    adj_list['z'] = ['x', 'y']

    print(scc(adj_list))
