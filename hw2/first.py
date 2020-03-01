from functools import cmp_to_key

inp = input().split()
k, n, m = int(inp[0]), int(inp[1]), int(inp[2])
li = list(map(int, input().split()))
operation = list()
ls = [[] for i in range(k)]
for i in range(n):
    inp = input().split()
    typ, index, b = int(inp[0]), int(inp[1]), int(inp[2])
    if typ == 1:
        ls[index - 1].append(b)
    else:
        operation.append((index - 1, b, 1))
for i in range(k):
    ls[i].sort(reverse=True)
    sum = li[i]
    for j in range(len(ls[i])):
        operation.append((i, sum + ls[i][j], sum))
        sum += ls[i][j]
operation.sort(key=cmp_to_key(lambda r1, r2: -r1[1] * r2[2] + r1[2] * r2[1]))
for i in range(m):
    op = operation[i]
    li[op[0]] *= op[1]
    li[op[0]] //= op[2]

result = 1
mod = 10 ** 9 + 7
for i in li:
    result *= i
    result %= mod
print(result)
