import math


def binarySearch(arr, l, r, x):
    while l <= r:

        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid

        elif arr[mid] < x:
            l = mid + 1

        else:
            r = mid - 1

    else:
        return False


s = input()
str = input()
inputs = str.split(" ")
num = list()
for i in range(len(inputs)):
    num.append(int(inputs[i]))
n = len(num)
inputs = sorted(num)
a = {0: 0, 1: 0}
for i in range(n):
    search = binarySearch(inputs, 0, n, num[i])
    if math.fabs(search - i) % 2 == 1:
        a[i % 2] += 1

print(max(a[0], a[1]))
