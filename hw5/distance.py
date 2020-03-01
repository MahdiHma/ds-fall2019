from math import log2
import sys

sys.setrecursionlimit(15000)


def preprocess(arr: list, n: int):
    global lookup
    for i in range(n):
        lookup[i][0] = i

    j = 1
    while (1 << j) <= n:

        i = 0
        while i + (1 << j) - 1 < n:
            if (arr[lookup[i][j - 1]] <
                    arr[lookup[i + (1 << (j - 1))][j - 1]]):
                lookup[i][j] = lookup[i][j - 1]
            else:
                lookup[i][j] = lookup[i +
                                      (1 << (j - 1))][j - 1]

            i += 1
        j += 1


def query(arr: list, L: int, R: int) -> int:
    global lookup

    j = int(log2(R - L + 1))

    if (arr[lookup[L][j]] <=
            arr[lookup[R - (1 << j) + 1][j]]):
        return arr[lookup[L][j]]
    else:
        return arr[lookup[R - (1 << j) + 1][j]]


def dfs(v1, dis):
    global first_visits
    global visit
    global weight
    first_visits[v1] = len(weight)
    is_visited[v1] = True
    visit.append(v1)
    weight.append(dis)
    for vertices in v[v1]:
        active = vertices[0]
        if is_visited[active]:
            continue
        else:
            dfs(active, dis + vertices[1])

        visit.append(v1)
        weight.append(dis)


n, q = map(int, input().split())

visit = list()
weight = list()
first_visits = dict()
is_visited = {i + 1: False for i in range(n)}
v = {i + 1: [] for i in range(n)}
save = 0
for i in range(n - 1):
    inst = list(map(int, input().split()))
    x = inst[0]
    if i == 0:
        save = x
    y = inst[1]
    w = inst[2]
    v[x].append((y, w))
    v[y].append((x, w))

dfs(save, 0)

lookup = [[0 for i in range(20)]
          for j in range(len(weight))]
preprocess(weight, len(weight))

for j in range(q):
    x, y = map(int, input().split())
    x = first_visits[x]
    y = first_visits[y]
    l = min(x, y)
    r = max(x, y)
    s = 2 * query(weight, l, r)
    print(weight[x] + weight[y] - s)


#I USED GEEKS FOR GEEKS MINIMUM QUERY CODE