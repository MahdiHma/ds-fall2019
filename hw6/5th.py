import math

try:

    from collections.abc import MutableMapping
except:
    from collections import MutableMapping
from heapq import heapify, heappush, heappop


class heapdict(MutableMapping):
    __marker = object()

    def __init__(self, *args, **kw):
        self.heap = []
        self.d = {}
        self.update(*args, **kw)

    def clear(self):
        del self.heap[:]
        self.d.clear()

    def __setitem__(self, key, value):
        if key in self.d:
            self.pop(key)
        wrapper = [value, key, len(self)]
        self.d[key] = wrapper
        self.heap.append(wrapper)
        self._decrease_key(len(self.heap) - 1)

    def _min_heapify(self, i):
        n = len(self.heap)
        h = self.heap
        while True:
            l = (i << 1) + 1
            r = (i + 1) << 1
            if l < n and h[l][0] < h[i][0]:
                low = l
            else:
                low = i
            if r < n and h[r][0] < h[low][0]:
                low = r

            if low == i:
                break

            self._swap(i, low)
            i = low

    def _decrease_key(self, i):
        while i:
            parent = (i - 1) >> 1
            if self.heap[parent][0] < self.heap[i][0]:
                break
            self._swap(i, parent)
            i = parent

    def _swap(self, i, j):
        h = self.heap
        h[i], h[j] = h[j], h[i]
        h[i][2] = i
        h[j][2] = j

    def __delitem__(self, key):
        wrapper = self.d[key]
        while wrapper[2]:
            parentpos = (wrapper[2] - 1) >> 1
            parent = self.heap[parentpos]
            self._swap(wrapper[2], parent[2])
        self.popitem()

    def __getitem__(self, key):
        return self.d[key][0]

    def __iter__(self):
        return iter(self.d)

    def popitem(self):
        wrapper = self.heap[0]
        if len(self.heap) == 1:
            self.heap.pop()
        else:
            self.heap[0] = self.heap.pop()
            self.heap[0][2] = 0
            self._min_heapify(0)
        del self.d[wrapper[1]]
        return wrapper[1], wrapper[0]

    def __len__(self):
        return len(self.d)

    def peekitem(self):
        return self.heap[0][1], self.heap[0][0]

    __all__ = ['heapdict']


# class PriorityQueue:
#     def __init__(self, n):
#         self.heap = [(i, math.inf) for i in range(2 * n)]
#         self.index = {i: i for i in range(2 * n)}
#         self.map = {i: i for i in range(2 * n)}
#
#     def edit_dis(self, key, value):
#         i = self.index[key]
#         if value == self.heap[i][1]:
#             return
#         if value > self.heap[i][1]:
#             self.heapify_down(i)
#         else:
#             self.heapify_up(i)
#
#     def heapify_up(self, i):
#         while self.heap[i][1] < self.heap[(i - 1) // 2][1]:
#             self.index[self.heap[i][0]] = (i - 1) // 2
#             self.index[self.heap[(i - 1) // 2][0]] = i
#             temp = self.heap[i]
#             self.heap[i] = self.heap[(i - 1) // 2]
#             self.heap[(i - 1) // 2] = temp
#             i = (i - 1) // 2
#
#     def heapify_down(self, i):
#         while 2 * i + 1 < len(self.heap):
#             left = self.heap[2 * i + 1][1]
#             right = None
#             try:
#                 right = self.heap[2 * i + 2][1]
#                 ind = None
#                 if left < right:
#                     ind = 2 * i + 1
#                 else:
#                     ind = 2 * i + 2
#                 if self.heap[i][1] > self.heap[ind][1]:
#                     self.index[self.heap[i][0]] = ind
#                     self.index[self.heap[ind][0]] = i
#                     temp = self.heap[i]
#                     self.heap[i] = self.heap[ind]
#                     self.heap[ind] = temp
#                     i = ind
#                 else:
#                     break
#             except:
#                 pass
#
#     def pop(self):
#         temp = self.heap[-1]
#         self.heap[-1] = self.heap[0]
#         self.heap[0] = temp
#         self.heapify_down(0)
#         return self.heap.pop()
#
#     def __len__(self):
#         return len(self.heap)
#

def dijkstra(vertices: dict, begin, end):
    dis[begin] = 0
    queue = heapdict()
    for i in range(2 * n):
        queue[i] = dis[i]
    while len(queue):
        v, distance = queue.popitem()
        for u in vertices[v]:
            if dis[u[0]] > dis[v] + u[1]:
                dis[u[0]] = dis[v] + u[1]
                queue[u[0]] = dis[u[0]]
    return dis[end]


n, m = map(int, input().split())

s, t = map(int, input().split())

s = s - 1
t = t - 1
vertices = dict()
for i in range(n):
    vertices[2 * i] = []
    vertices[2 * i + 1] = []
# dis = [math.inf] * len(vertices)
dis = {i: math.inf for i in range(2 * n)}
for i in range(m):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    # vertices[u].append((v, w))
    if w % 2 == 0:
        vertices[2 * u].append((2 * v, w))
        vertices[2 * u + 1].append((2 * v + 1, w))
    else:
        vertices[2 * u].append((2 * v + 1, w))
        vertices[2 * u + 1].append((2 * v, w))
dijkstra(vertices, 2 * s, 2 * t)
if dis[2 * t] != math.inf:
    print(dis[2 * t])
else:
    print(-1)

# I used heapdict in: https://github.com/DanielStutzbach/heapdict/blob/master/heapdict.py
