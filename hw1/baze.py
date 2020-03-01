import math

inp = input().split()
n, q = int(inp[1]), int(inp[0])
divider = 10 ** 9 + 7

domain = list()
max = 0
for i in range(n):
    inp = input().split(" ")
    key = int(inp[0])
    value = int(inp[1])
    check = True
    for (k, v) in domain:
        if k <= key and v >= value:
            check = False
            break
    if check:
        domain.append((key, value))
    if value - key + 1 > max:
        max = value - key + 1
ls = {x: 0 for x in range(1, q + 1)}
res = 1
sorted_set = sorted(domain, key=lambda tup: tup[0])
for (key, value) in sorted_set:
    for i in range(key, value + 1):
        if ls[i] is 0:
            ls[i] = max - i + key
for i in range(1, q + 1):
    if ls[i] is 0:
        ls[i] = max
    res *= ls[i]
    res %= divider
print(max, res)
