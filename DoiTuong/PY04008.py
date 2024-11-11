class Matrix:
    def __init__(self, a, n, m):
        self.a = a
        self.n = n
        self.m = m
    def transpose(self):
        n = self.n
        m = self.m
        b = [[0] * n for i in range(m)]
        for i in range(n):
            for j in range(m):
                b[j][i] = self.a[i][j]
        return Matrix(b, m, n)
    def multiply(self, other):
        n = self.n
        m = self.m
        p = other.m
        b = [[0] * p for i in range(n)]
        for i in range(n):
            for j in range(p):
                for k in range(m):
                    b[i][j] += self.a[i][k] * other.a[k][j]
        return Matrix(b, n, p)
    
t = int(input())
b = []
while True:
    try:
        b.extend(list(map(int, input().split())))
    except:
        break
idx = 0
for _ in range(t):
    n = b[idx]
    m = b[idx + 1]
    idx += 2
    a = [[0] * m for i in range(n)]
    while len(b) - idx < n * m:
        b.extend([0])
    for i in range(n):
        for j in range(m):
            a[i][j] = b[idx + j]
        idx += m
    m1 = Matrix(a, n, m)
    m2 = m1.transpose()
    m3 = m1.multiply(m2)
    for i in range(m3.n):
        for j in range(m3.m):
            print(m3.a[i][j], end = " ")
        print()
    