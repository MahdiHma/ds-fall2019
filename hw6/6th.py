def dfs(vertex):
    parent = [False] * n
    v = vertex
    while child[vertex] != len(vertices[vertex]):
        if len(vertices[v]) == 0:
            sub_leaves[v] = 1
        if len(vertices[v]) == child[v]:
            leaf = sub_leaves[v]
            v = parent[v]
            child[v] += 1
            sub_leaves[v] += leaf
        try:
            parent[vertices[v][child[v]]] = v
            v = vertices[v][child[v]]
        except:
            pass


n = int(input())
vert = list(map(int, input().split()))
vertices = {i: [] for i in range(n)}
sub_leaves = [0] * n
child = [0] * n

for i in range(n - 1):
    vertices[vert[i] - 1].append(i + 1)
dfs(0)
leaves = sub_leaves[0]
res = 0
for i in sub_leaves:
    res += i * (leaves - i)

print(res)
