def max_insert(arr):
    i = len(arr) - 1
    root = (i + 1) // 2 - 1

    while i > 0 and arr[i] > arr[root]:
        arr[i], arr[root] = arr[root], arr[i]
        i = root
        root = (i + 1) // 2 - 1


def min_insert(arr):
    i = len(arr) - 1
    root = (i + 1) // 2 - 1

    while i > 0 and arr[i] < arr[root]:
        arr[i], arr[root] = arr[root], arr[i]
        i = root
        root = (i + 1) // 2 - 1


def max_bubble_down(arr):
    i = 0
    n = len(arr)
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
        else:
            break


def min_bubble_down(arr):
    i = 0
    n = len(arr)
    while True:
        min = i
        l = 2 * i + 1  # left = 2*i + 1
        r = 2 * i + 2  # right = 2*i + 2
        # print(arr)
        if l < n and arr[min] > arr[l]:
            min = l

        if r < n and arr[min] > arr[r]:
            min = r

        if min != i:
            arr[i], arr[min] = arr[min], arr[i]
            # swap
            i = min
        else:
            break


count_r = 0
count_l = 0
min_heap = list()
max_heap = list()
median = None
n = int(input())
for i in range(n):
    x = int(input())
    if i == 0:
        median = x
    else:
        if x > median:
            min_heap.append(x)
            min_insert(min_heap)
            count_r += 1
        else:
            max_heap.append(x)
            max_insert(max_heap)
            count_l += 1
    if count_r > count_l + 1:
        temp = median
        min_heap[-1], min_heap[0] = min_heap[0], min_heap[-1]
        median = min_heap.pop(-1)
        min_bubble_down(min_heap)
        max_heap.append(temp)
        max_insert(max_heap)
        count_r -= 1
        count_l += 1

    if count_l > count_r:
        temp = median
        max_heap[-1], max_heap[0] = max_heap[0], max_heap[-1]
        median = max_heap.pop(-1)
        max_bubble_down(max_heap)
        min_heap.append(temp)
        min_insert(min_heap)
        count_r += 1
        count_l -= 1
    print(median)
