from math import *

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, other):
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def dienTich(self):
        m = self.a.distance(self.b)
        n = self.b.distance(self.c)
        p = self.c.distance(self.a)
        if m + n > p and n + p > m and p + m > n:
            return '{:.2f}'.format(sqrt((m + n + p) * (m + n - p) * (m - n + p) * (-m + n + p)) / 4)
        else:
            return 'INVALID'
a = []
n = int(input())
for _ in range(n):
    a.extend(map(float, input().split()))
i = 0
for j in range(n):
    p1 = Point(a[i], a[i + 1])
    p2 = Point(a[i + 2], a[i + 3])
    p3 = Point(a[i + 4], a[i + 5])
    t = Triangle(p1, p2, p3)
    print(t.dienTich())
    i += 6