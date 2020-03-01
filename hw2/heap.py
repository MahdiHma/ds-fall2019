def bubble_up(arr):
    i = len(arr) - 1
    root = (i + 1) // 2 - 1

    while i > 0 and arr[i] > arr[root]:
        arr[i], arr[root] = arr[root], arr[i]
        i = root
        root = (i + 1) // 2 - 1
    return count


def bubble_down(arr):
    i = 0
    n = len(arr)
    count = 0
    while True:
        min = i
        l = 2 * i + 1  # left = 2*i + 1
        r = 2 * i + 2  # right = 2*i + 2
        # print(arr)
        if l < n and arr[min] < arr[l]:
            min = l

        if r < n and arr[min] < arr[r]:
            min = r

        if min != i:
            arr[i], arr[min] = arr[min], arr[i]
            # swap
            i = min
            count += 1
        else:
            break
    return count


n = int(input())
count = 0
heap = list()
ls = list()
sorted_list = list()
# ls = list(map(int, input().split()))
arr = list()

for i in range(n):
    x = int(input())
    y = x
    if len(arr) % 2 == 1 and len(sorted_list) is not len(arr) // 2:
        j = len(arr)
        arr[0], arr[j - 1] = arr[j - 1], arr[0]
        sorted_list.append(arr.pop(j - 1))
        bubble_down(arr)
    if x > sorted_list[0]:
        sorted_list.insert(0, x)
    elif sorted_list[0] > x > sorted_list[-1]:
        sorted_list.append(x)
        sorted_list.sort()
    else:
        # ls.append(x)
        arr.append(x)
        bubble_up(arr)

    print(sorted_list[-1])
