s = input()
t = input()
ns = len(s)
nt = len(t)
for i in range(len(s)):
    k = i
    while k < ns and k - i < nt and s[k] == t[k - i]:
        k += 1
    print(k - i, end=' ')
