n = int(input())
l = list()
total = set()
for i in range(n):
    inp = set(map(int, input().split()[1:]))
    l.append(sorted(list(inp)))
l.sort()
count = 0
n = 1
for i in range(1, len(l)):
    if l[i] == l[i - 1]:
        n += 1
    else:
        count += n * (n - 1) // 2
        n = 1

print(count + n * (n - 1) // 2)
