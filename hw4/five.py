lang = dict()
inp = input()
res = 0

n = len(inp)

for i in range(n):
    for j in range(i + 1, n):
        k = i
        r = j
        while k < n and r < n and inp[k] == inp[r]:
            k += 1
            r += 1
            res += 1

    # b = True
# for k in range(min(n,l+i)):
#     if inp[i + k] != inp[j + k]:
#         b = False
#         break
# if b:
#     res += 1

# for i in range(len(inp)):
#     for j in range(i + 1):
#         if lang.get(inp[j:i + 1]):
#             res += lang[inp[j:i + 1]]
#             lang[inp[j:i + 1]] += 1
#         else:
#             lang[inp[j:i + 1]] = 1
#
print(res)
