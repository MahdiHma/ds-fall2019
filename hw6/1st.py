import sys

n, m = map(int, input().split())
vert = {i + 1: set() for i in range(n)}
revers = {i + 1: set() for i in range(n)}
visit = set()
sort_of_visits = list()

sys.setrecursionlimit(15000)


def ordered_dfs(ver):
    visit.add(ver)
    for u in vert[ver]:
        # print(u)
        if u not in visit:
            ordered_dfs(u)
    sort_of_visits.append(ver)


def dfs(ver, s):
    global minimum
    if ver < minimum:
        minimum = ver
    visit.add(ver)
    s.add(ver)
    for u in revers[ver]:
        if u not in visit:
            dfs(u, s)


for i in range(m):
    u, v = map(int, input().split())
    vert[u].add(v)
    revers[v].add(u)

for i in range(n):
    if i + 1 not in visit:
        ordered_dfs(i + 1)

vers = {i + 1: 0 for i in range(n)}
visit = set()
minimum = 1000000
while sort_of_visits:
    v = sort_of_visits.pop()
    if v not in visit:
        s = set()
        minimum = 10000000
        dfs(v, s)
        for i in s:
            vers[i] = minimum

for i in vers:
    print(vers[i], end=' ')
