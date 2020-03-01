# class hamband:
#     def __init__(self):
#         self.s = set()
#
#     def find_set(self, val):
#         if val in self.s:
#             self.s.add(val)
#             return True
#         return False


n, q = tuple(map(int, input().split()))
dic = dict()
for i in range(q):
    instruction = input().split()
    if instruction[0] == 'ADD':
        for k, v in dic:
            x = int(instruction[1])
            y = int(instruction[2])
            if x in v:
                v.append(y)
            elif y in v:
                v.append(x)
            else:
                ls = list((x, y))
                print(ls)
                dic[x] = ls
