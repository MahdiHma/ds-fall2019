from heapq import *


class Student:
    def __init__(self, score: int, index: int):
        self.score = score
        self.index = index

    def __lt__(self, other):
        global added

        x = self.score
        y = other.score
        if x + added[self.index] == y + added[other.index]:
            return self.index < other.index
        return self.score + added[self.index] < other.score + added[other.index]

    def __le__(self, other):
        global added
        x = self.score
        y = other.score
        if x + added[self.index] == y + added[other.index]:
            return self.index < other.index
        return x + added[self.index] < y + added[other.index]

    def __gt__(self, other):
        global added

        x = self.score
        y = other.score
        if x + added[self.index] == y + added[other.index]:
            return self.index > other.index
        return self.score + added[self.index] > other.score + added[other.index]

    def __ge__(self, other):
        global added
        x = self.score
        y = other.score

        if x + added[self.index] == y + added[other.index]:
            return self.index > other.index
        return x + added[self.index] > y + added[other.index]

    def __str__(self):
        return str(self.score)


n, q = tuple(map(int, input().split()))

ls = [[] for i in range(n)]
added = [0 for j in range(n)]
mins = list()
min_index = None
for i in range(q):
    instruction = list(map(int, input().split()))
    if instruction[0] is not 3:
        index = instruction[1] - 1
        x = instruction[2]
        if instruction[0] is 1:
            temp = ls[index][0] if len(ls[index]) else None
            heappush(ls[index], Student(x - added[index], index))
            if temp is not ls[index][0]:
                if temp is not None:
                    for j in range(len(mins)):
                        if mins[j] == temp:
                            mins[j] = ls[index][0]
                            heapify(mins)
                            continue
                else:
                    heappush(mins, ls[index][0])

        else:
            added[index] += x
            heapify(mins)

    else:

        if len(mins) == 0:
            print(-1)
        else:
            tmp = mins[0]
            # for j in mins:
            #     print(j, j.index, i, "DD")
            print(tmp.score + added[tmp.index])
            heappop(ls[tmp.index])

            heappop(mins)
            # for j in mins:
            #     print(j, j.index, i)

            if len(ls[tmp.index]) is not 0:
                heappush(mins, ls[tmp.index][0])
        # mins = list()
# for j in range(n):
#     if len(ls[j]):
#         heappush(mins, Student(ls[j][0].score + added[j], ls[j][0].index))
# if len(mins) == 0:
#     print(-1)
#     continue
# temp = heappop(mins)
#
# heappop(ls[temp.index])
# score = temp.score
# print(score)
# for j in mins:
# print(mins)
# min_index = None
# for j in range(n):
#     if mins[j] is not None:
#         if min_index is None:
#             min_index = j
#             # print(min_index,"gdxfg")
#         elif mins[j] + added[j] < mins[min_index] + added[min_index]:
#             # print(mins[j] + added[j], mins[min_index] + added[min_index])
#             min_index = j
#
# # print(min_index)
# if min_index is not None:
#     print(heappop(ls[min_index]) + added[min_index])
#     mins[min_index] = ls[min_index][0] if len(ls[min_index]) > 0 else None
# else:
#     print(-1)
