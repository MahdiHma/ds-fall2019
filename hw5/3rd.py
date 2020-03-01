n = int(input())
arr = list(map(int, input().strip().split()))

pasvand = [0 for i in range(n)]
pishvand = [0 for j in range(n)]
max_all = 0
for i in range(n):
    pasvand[i] = arr[i] ^ pasvand[i - 1]
    pishvand[i] = arr[n - i - 1] ^ pishvand[i - 1]
    s = max(pasvand[i], pishvand[i])
    if s > max_all:
        max_all = s

for i in range(n):
    for j in range(n - i):
        s = pasvand[i] ^ pishvand[j]
        if max_all < s:
            max_all = s

print(max_all)
