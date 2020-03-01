n = int(input())
arr = list(map(int, input().split()))
pasvand = [0] * (n + 1)
pishvand = [0] * (n + 1)
for i in range(n):
    pasvand[i + 1] = pasvand[i] ^ arr[i]
    pishvand[i + 1] = pishvand[i] ^ arr[n - i - 1]
maxi = 0
for i in range(n + 1):
    for j in range(n - i + 1):
        maxi = max(pasvand[i] ^ pishvand[j], maxi)

print(maxi)
