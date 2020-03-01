class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.m = Dot((a.x + b.x + c.x) / 2, (a.y + b.y + c.y) / 2)

    def __lt__(self, other):
        if self.m.x < other.m.x:
            return self
        return other


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def cross(t0, t1):
    pa = t0.a
    pb = t0.b
    pc = t0.c
    p0 = t1.a
    p1 = t1.b
    p2 = t1.c
    dXa = pa.x - p2.x
    dYa = pa.y - p2.y
    dXb = pb.x - p2.x
    dYb = pb.y - p2.y
    dXc = pc.x - p2.x
    dYc = pc.y - p2.y
    dX21 = p2.x - p1.x
    dY12 = p1.y - p2.y
    D = dY12 * (p0.x - p2.x) + dX21 * (p0.y - p2.y)
    sa = dY12 * dXa + dX21 * dYa
    sb = dY12 * dXb + dX21 * dYb
    sc = dY12 * dXc + dX21 * dYc
    ta = (p2.y - p0.y) * dXa + (p0.x - p2.x) * dYa
    tb = (p2.y - p0.y) * dXb + (p0.x - p2.x) * dYb
    tc = (p2.y - p0.y) * dXc + (p0.x - p2.x) * dYc
    if D < 0:
        return ((sa >= 0 and sb >= 0 and sc >= 0) or
                (ta >= 0 and tb >= 0 and tc >= 0) or
                (sa + ta <= D and sb + tb <= D and sc + tc <= D))
    return ((sa <= 0 and sb <= 0 and sc <= 0) or
            (ta <= 0 and tb <= 0 and tc <= 0) or
            (sa + ta >= D and sb + tb >= D and sc + tc >= D))


def check_intersection(t0, t1):
    return not (cross(t0, t1) or cross(t1, t0))


def check_rect_intersection(r1, r2):
    if r1[2] < r2[0] or r2[2] < r1[0]:
        return False

    if r1[1] < r2[3] or r2[1] < r1[3]:
        return False


def aabb(ls1, ls2):
    if len(ls1 == 1) and len(ls2 == 1):
        return cross(ls1[0], ls2[0])
    else:


first_triangles = list()
second_triangles = list()

for i in range(30):
    command = input()
    while command is not "end1":
        triangles = list(map(int, command.split()))
        first_triangles.append(
            Triangle(Dot(triangles[0], triangles[1]), Dot(triangles[2], triangles[3]), Dot(triangles[4], triangles[5])))
        command = input()

    command = input()
    while command is not "end2":
        triangles = list(map(int, command.split()))
        second_triangles.append(
            Triangle(Dot(triangles[0], triangles[1]), Dot(triangles[2], triangles[3]), Dot(triangles[4], triangles[5])))
        command = input()

aabb(first_triangles.sort(key=lambda tri: tri.x <))
