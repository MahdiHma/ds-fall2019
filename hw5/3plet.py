from bisect import bisect_left


class BIT:
    def __init__(self, n):
        self.bit = [0 for i in range(n + 1)]
        self.n = n

    def update(self, i, value):
        while i <= self.n:
            self.bit[i] += value

            i += i & (-i)

    def get_sum(self, i):
        sum = 0
        while i > 0:
            sum += self.bit[i]
            i -= i & (-i)

        return sum


def convert_to_indexed_list(arr):
    srt = sorted(arr)
    for i in range(len(arr)):
        arr[i] = bisect_left(srt, arr[i]) + 1
    return arr


n = int(input())
arr = list(map(int, input().split()))
bit = BIT(n)
arr = convert_to_indexed_list(arr)
sum = 0
left = [0 for i in range(n + 1)]
right = [0 for j in range(n + 1)]
for i in range(n - 1, -1, -1):
    right[i] = bit.get_sum(arr[i] - 1)
    bit.update(arr[i], 1)

bit = BIT(n)

for i in range(n):
    left[i] = i - bit.get_sum(arr[i])
    bit.update(arr[i], 1)
    sum += left[i] * right[i]

print(sum)
