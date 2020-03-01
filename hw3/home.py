class Node(object):
    def __init__(self, value, index):
        self.value = value
        self.index = index
        self.height = 1
        self.left = None
        self.right = None
        self.child_count = 0
        # self.father = None

    def __str__(self):
        return str(self.child_count)


class AvlTree(object):
    def __init__(self):
        self.root = None

    def insert(self, rt: Node, node: Node):
        global ls
        if rt is None:
            return node
        elif node.value < rt.value:
            ls[node.index] += self.get_right_child(rt) + 1
            rt.left = self.insert(rt.left, node)
        else:
            # ls[node.index] += self.get_right_child(root) + 1
            rt.right = self.insert(rt.right, node)
        rt.child_count += 1

        rt.height = 1 + max(self.get_height(rt.right), self.get_height(rt.left))
        balance = self.get_height(rt.left) - self.get_height(rt.right) if root else 0
        if balance > 1 and node.value < rt.left.value:
            return self.rotate_right(rt)

            # Case 2 - Right Right
        if balance < -1 and node.value > rt.right.value:
            return self.rotate_left(rt)

            # Case 3 - Left Right
        if balance > 1 and node.value > rt.left.value:
            rt.left = self.rotate_left(rt.left)
            return self.rotate_right(rt)

            # Case 4 - Right Left
        if balance < -1 and node.value < rt.right.value:
            rt.right = self.rotate_right(rt.right)
            return self.rotate_left(rt)
        return rt

    # def make_parent(self, rt: Node):
    #     if rt.left:
    #         rt.left.father = rt
    #         self.make_parent(rt.left)
    #     if rt.right:
    #         rt.right.father = rt
    #         self.make_parent(rt.right)

    def get_height(self, node):
        if node:
            return node.height
        return 0

    def rotate_left(self, rt: Node):
        r = rt.right
        t = r.left
        rt.right = t
        r.left = rt
        rt.height = 1 + max(self.get_height(rt.right), self.get_height(rt.left))
        r.height = 1 + max(self.get_height(r.right), self.get_height(r.left))
        r.child_count = self.get_right_child(r) + self.get_left_child(rt) + 1 + self.get_count_all(t)
        rt.child_count = self.get_left_child(rt) + self.get_count_all(t)
        return r

    def rotate_right(self, rt: Node):
        r = rt.left
        t = r.right
        rt.left = t
        r.right = rt
        rt.height = 1 + max(self.get_height(rt.right), self.get_height(rt.left))
        r.height = 1 + max(self.get_height(r.right), self.get_height(r.left))
        r.child_count = self.get_left_child(r) + self.get_right_child(rt) + 1 + self.get_count_all(t)
        rt.child_count = self.get_right_child(rt) + self.get_count_all(t)

        return r

    @staticmethod
    def search_father_more(rt: Node, node: Node):
        count = 0
        if rt.right:
            count += AvlTree.search_father_more(rt.right, node)
        if rt.index > node.index:
            count += 1
        if rt.left:
            count += AvlTree.search_father_more(rt.left, node)
        return count

    @staticmethod
    def search_if_more(rt: Node, node: Node):
        count = 0
        father = rt
        while father.father:
            if father.value < father.father.value:
                if father.father.right:
                    count += AvlTree.search_father_more(father.father.right, node)
                if father.father.index > node.index:
                    count += 1
            father = father.father
        if rt.right:
            count += AvlTree.search_father_more(rt.right, node)

        return count

    def iterate(self, rt: Node, ls: list):
        print(rt.value, rt.child_count)
        ls[rt.index] = rt.child_count - rt.right.child_count
        if rt.left:
            # rt.left.father = rt
            self.iterate(rt.left, ls)
        if rt.right:
            # rt.right.father = rt
            self.iterate(rt.right, ls)

    def get_right_child(self, root: Node):
        if root.right:
            return root.right.child_count + 1
        return 0

    def get_left_child(self, root: Node):
        if root.left:
            return root.left.child_count + 1
        return 0

    def get_count_all(self, root: Node):
        if root:
            return root.child_count + 1
        return 0


myTree = AvlTree()
inp = list(reversed(list(map(int, input().split()))))
ls = [0] * len(inp)
root = None
for i in range(len(ls)):
    root = myTree.insert(root, Node(inp[i], i))
# myTree.root = root
# myTree.iterate(root, ls)

for i in reversed(ls):
    print(i, end=' ')
