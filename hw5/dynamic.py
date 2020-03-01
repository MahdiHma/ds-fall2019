def find_set(parent, x):
    y = x
    while y != parent[y]:
        y = parent[y]
    return y


def union_set(parent, rank, x, y):
    x, y = find_set(parent, x), find_set(parent, y)
    global n
    if x == y:
        save.append(())
        # return
    else:
        save.append((x, rank[x], parent[x], y, rank[y], parent[y]))
        n -= 1
    if rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1


# def undo(parent, x, ):


n, q = tuple(map(int, input().split()))
save = list()
parent = {x + 1: x + 1 for x in range(n)}
rank = {x + 1: 0 for x in range(n)}
save = list()
b = bool()
ins = [(-1, -1) for i in range(q)]
for i in range(q):
    instruction = input().split()
    if instruction[0] == 'ADD':
        x = int(instruction[1])
        y = int(instruction[2])
        union_set(parent, rank, x, y)
        # print(x, parent[x])
        # print(y, parent[y])
        # print(int(instruct
        # ion[1]), find_set(parent, int(instruction[1])))
        # print(int(instruction[2]), find_set(parent, int(instruction[2])))

    else:
        x = save.pop()
        if x == ():
            print(n)
            continue
        parent[x[0]] = x[2]
        rank[x[0]] = x[1]
        parent[x[3]] = x[5]
        rank[x[3]] = x[4]
        n += 1
    print(n)
