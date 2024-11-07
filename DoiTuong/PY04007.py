class Matrix:
    def __init__(self, n, m, a):
        self.n = n
        self.m = m
        self.a = a
    def transpose(self):
        n = self.n
        m = self.m
        b = [[0] * self.n for i in range(self.m)]
        for i in range(n):
            for j in range(m):
                b[j][i] = self.a[i][j]
        return Matrix(self.m, self.n, b)
    def multiply(self, other):
        n = self.n
        m = self.m
        ans = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(m):
                    ans[i][j] += self.a[i][k] * other.a[k][j]
        return Matrix(n, n, ans)
    def __str__(self):
        for i in range(self.n):
            for j in range(self.m):
                print(self.a[i][j], end=' ')
            print()
for _ in range(int(input())):
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    m = Matrix(n, m, a)
    mt = m.transpose()
    result = m.multiply(mt)
    # print(result)
    for i in range(n):
            print(*result.a[i])