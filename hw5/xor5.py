class BIT:
    def __init__(self, n):
        self.bit = [0 for i in range(n + 1)]
        self.n = n + 1

    def add(self, i, val):
        while i < self.n:
            self.bit[i] ^= val
            i += i & -i

    def range_add(self, l, r, val):
        self.add(l, val)
        self.add(r + 1, val)

    def get_element(self, i):
        total = 0
        while i > 0:
            total ^= self.bit[i]
            i -= i & -i
        return total


# its idea came from cp-algorithms.com


n, q = tuple(map(int, input().split()))
bit = BIT(n)
for i in range(q):
    instruction = input().split()
    if instruction[0] == 1:
        val = instruction[3]
        bit.range_add(instruction[1], instruction[2], instruction[3])
    else:
        print(bit.get_element(instruction[1]))
