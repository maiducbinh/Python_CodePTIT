arr = []
def Try(n, s, a, b, c):
    if len(s) == n and 0 < a <= b <= c:
        print(s)
    if len(s) < n:
        Try(n, s + "A", a + 1, b, c)
        Try(n, s + "B", a, b + 1, c)
        Try(n, s + "C", a, b, c + 1)

n = int(input())
for i in range(3, n + 1):
    Try(i, "", 0, 0, 0)