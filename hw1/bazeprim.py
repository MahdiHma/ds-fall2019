import math

inp = input().split()
n, q = int(inp[1]), int(inp[0])
divider = 10 ** 9 + 7

domain = dict()
max = 0
for i in range(n):
    inp = input().split(" ")
    key = int(inp[0])
    value = int(inp[1])
    domain[key] = value
    if value - key + 1 > max:
        max = value - key + 1
ls = {x: 0 for x in range(1, q + 1)}
res = 1
for (key, value) in sorted(domain.items()):
    for i in range(key, value + 1):
        if ls[i] is 0:
            ls[i] = max - i + key
for i in range(1, q + 1):
    if ls[i] is 0:
        ls[i] = max
    res *= ls[i]
    res %= divider
print(max, res)
