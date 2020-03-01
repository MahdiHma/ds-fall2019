# class 
class Node:
    def __init__(self, value):
        self.child = dict()
        self.value = value


class Trie:
    def __init__(self):
        self.root = Node(None)

    def insert(self, x, origin):
        node = self.root
        for i in reversed(x):
            if node.child.get(i):
                node = node.child[i]
                continue
            else:
                node.child[i] = Node(i)
                node = node.child[i]
        node.origin = origin

    def search(self, x):
        node = self.root
        for i in reversed(x):
            if i == '0' and node.child.get('1'):
                node = node.child['1']
                continue
            if i == '1' and node.child.get('0'):
                node = node.child['0']
                continue
            if len(node.child) == 0:
                break
            node = node.child[i]

        try:
            return node.origin
        except:
            while len(node.child):
                if node.child.get('1'):
                    node = node.child['1']
                else:
                    node = node.child['0']
            return node.origin


n = int(input())
ls = list(map(int, input().split()))
pasvand = list()
pishvand = list()
pasvand_bin = list()
pasvand.append(ls[0])
pishvand.append(ls[-1])
pasvand_bin.append("{:b}".format(ls[0]))
trie = Trie()
for i in range(1, n):
    pasvand.append(pasvand[-1] ^ ls[i])
    pishvand.append(pishvand[-1] ^ ls[n - i - 1])

max = 0

for i in range(n):
    trie.insert("{:b}".format(pasvand[i]), pasvand[i])
    container = trie.search("{:b}".format(pasvand[n - i - 1])) ^ pasvand[n - i - 1]
    if max < int(container):
        max = int(container)

print(max)
