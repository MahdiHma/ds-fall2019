def bfs(begin, distance):
    queue = list()
    visit = [False] * n
    queue.append(begin)
    visit[begin - 1] = True
    while queue:
        v = queue.pop(0)
        for u in ver[v]:
            if not visit[u - 1]:
                visit[u - 1] = True
                queue.append(u)
                distance[u - 1] = distance[v - 1] + 1


n, m = map(int, input().split())
s, t = map(int, input().split())
s_distance = [0] * n
t_distance = [0] * n
res = [1] * n
ver = {i + 1: [] for i in range(n)}
for i in range(m):
    u, v = map(int, input().split())
    ver[u].append(v)
    ver[v].append(u)

bfs(s, s_distance)
bfs(t, t_distance)
minimum = t_distance[s - 1]
mins = {i: 0 for i in range(minimum + 1)}
for i in ver:
    distance = t_distance[i - 1] + s_distance[i - 1]

    if 0 < distance <= minimum:
        mins[t_distance[i - 1]] += 1
    else:
        ver[i] = False

for i in ver:
    distance = t_distance[i - 1]
    if not ver[i]:
        print(1, end=' ')
    elif mins[distance] == 1:
        print(3, end=' ')
    else:
        print(2, end=' ')
