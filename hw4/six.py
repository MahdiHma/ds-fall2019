s = input()
t = input()
dic = dict()

for i in range(len(t)):
    dic[t[0:i + 1]] = True

# for k in range(5, 3 - 1, -1):a
#     print(k)

for i in range(len(s)):
    # if s[i] != t[0]:
    #     print(0, end=" ")
    #     continue
    # for j in range(len(s), i - 1, -1):
    # print(i, j)
    # if dic.get(s[i:j]):
    #     print(j - i, end=' ')
    #     break
    # print(i)
    for j in range(i, len(s)):
        # print(i, j)
        # print(s[i:j + 1])
        if not dic.get(s[i:j + 1]):
            print(j - i, end=" ")
            break
        if j == len(s) - 1:
            print(1, end=" ")
