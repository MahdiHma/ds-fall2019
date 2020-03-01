def poshte(arr, k):
    i = k + 1
    j = k - 1
    count = 0
    bool = True
    while bool:
        first = i < len(arr) and arr[i] >= arr[k]
        sec = j >= 0 and arr[j] >= arr[k]
        if first:
            i += 1
            count += 1
        if sec:
            j -= 1
            count += 1
        bool = first or sec
    return arr[k] * (count + 1)


n = int(input())
inp = list(map(int, input().split(" ")))
max = 0
for i in range(n):
    t = poshte(inp, i)
    if max < t:
        max = t
print(max)
